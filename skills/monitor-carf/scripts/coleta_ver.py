#!/usr/bin/env python3
"""Coleta no indice de acordaos do CARF (VER) por execucao de codigo. v0.2 (2026-10-21)

Uso:
  python3 coleta_ver.py versao
  python3 coleta_ver.py sentinela
  python3 coleta_ver.py coleta [--dias 10 | --de AAAA-MM-DD --ate AAAA-MM-DD]
                               [--excluir ARQ] [--saida /tmp/carf_coleta.json]
  python3 coleta_ver.py numero 2401-012.623
  python3 coleta_ver.py sem-data [--linhas 40]
  python3 coleta_ver.py cobertura [--termos ARQ] [--dias 90]
  python3 coleta_ver.py urls [--dias 10]

v0.2: (1) paginacao completa por cursor, sem o teto de 60 por rede: o CARF
publica em lote (256 acordaos da rede rural em 10/09/2026) e o teto cortava o
lote e o repasse; (2) --excluir: arquivo com os numeros ja registrados na base
do Notion, que saem da saida antes de o modelo ler; (3) blocos repetitivos
colapsados em uma linha; (4) ancoras da trilha 13 (agroindustria e
cooperativas) e marcadores "cerealista" e "in natura"; (5) subcomando
cobertura: toda familia do mapa de termos precisa de ancora que a capture.

Fonte unica das ancoras das duas redes. Os enderecos fixos do texto da tarefa
agendada saem de `urls`; se uma ancora mudar aqui, regerar e colar la.
So le. Nao grava nada fora do arquivo de saida.
"""
import argparse, json, os, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request

VERSAO = "0.2"
BASE = "https://acordaos.economia.gov.br/solr/acordaos2/select"
PDF = "https://acordaos.economia.gov.br/acordaos2/pdfs/processados/"
FL = ("id,numero_decisao_s,numero_processo_s,turma_s,secao_s,dt_sessao_tdt,"
      "dt_publicacao_tdt,nome_relator_s,ementa_s,decisao_txt,"
      "nome_arquivo_pdf_s,arquivo_indexado_s")
PAGINA = 200      # documentos por pagina do cursor
TRAVA = 2000      # seguranca por rede; passou disso, a saida avisa
URL_LINHAS = 100  # linhas dos enderecos fixos (transporte 1b, sem cursor)
ORDEM = "dt_publicacao_tdt desc,id asc"  # id e a chave unica: cursor estavel

# O indice ignora acento e trata plural (medido em 06/10 e 21/10/2026): uma
# grafia por ancora basta. Tupla = segmentos que tem de ocorrer juntos (AND).
REDE_RURAL = [
    "atividade rural", "produtor rural", "imóvel rural", "propriedade rural",
    "funrural", "senar", "produção rural", "arrendamento rural",
    "parceria rural", "parceria agrícola", "parceria pecuária",
    "imposto sobre a propriedade territorial rural",
    "imposto territorial rural", "valor da terra nua", "agroindústria",
    "segurado especial",
    # trilha 13 (v0.2): "agroindustria" nao casa "agroindustrial"
    "agroindustrial", "cerealista", "cooperativa agropecuária",
    ("crédito presumido", "in natura"),
]
REDE_PATRIMONIAL = [
    "integralização de capital", "integralização de bem imóvel",
    "conferência de bens", "holding", "alienação fiduciária",
    "consolidação da propriedade", "adjudicação", "arrematação",
    "dação em pagamento", "adiantamento de legítima",
    "antecipação da legítima", "usufruto", "devolução de capital",
    "redução de capital", "propósito negocial",
    "distribuição disfarçada de lucros", "equiparação a pessoa jurídica",
]
# Marcadores rurais conferidos NA EMENTA, palavra inteira
# (references/triagem-e-lente.md, secao 2). Pre-triagem: quem decide e a leitura.
MARCADORES = [
    r"rural", r"rurais", r"terra nua", r"pecuári[ao]s?", r"agropecuári[ao]s?",
    r"agrícolas?", r"agroindústrias?", r"agroindustria(?:l|is)", r"lavouras?",
    r"safras?", r"glebas?", r"ITR", r"funrural", r"senar",
    r"cerealistas?", r"in natura",
]
RE_MARC = re.compile(r"(?<![\wÀ-ÿ])(" + "|".join(MARCADORES) + r")(?![\wÀ-ÿ])", re.I)
RE_NUM = re.compile(r"\d{4}-\d{3}\.\d{3}")


def consulta(params):
    """Tres tentativas (urllib, depois curl) com espera de 3 e 8 s: soluco de
    TLS e comum (medido em 21/10/2026) e nao e falha de canal."""
    url = BASE + "?" + urllib.parse.urlencode(params)
    dados, erro = None, ""
    for espera in (0, 3, 8):
        if espera:
            time.sleep(espera)
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                dados = json.loads(r.read().decode("utf-8"))
                break
        except Exception as e1:  # proxy da sessao pode exigir o curl
            p = subprocess.run(["curl", "-s", "-m", "90", url],
                               capture_output=True, text=True)
            if p.returncode == 0 and p.stdout.strip().startswith("{"):
                dados = json.loads(p.stdout)
                break
            erro = f"{type(e1).__name__}: {e1}; curl rc={p.returncode}"
    if dados is None:
        raise SystemExit(
            "FALHA DE CANAL: o indice nao respondeu por execucao de codigo apos tres "
            f"tentativas ({erro}). Seguir a cascata de references/coleta.md.")
    if "error" in dados:
        raise SystemExit(f"ERRO DO INDICE: {dados['error'].get('msg')}")
    return dados


def termo(a):
    return f'_texto:"{a}"' if " " in a else f"_texto:{a}"


def q_rede(ancoras):
    partes = []
    for a in ancoras:
        if isinstance(a, tuple):
            partes.append("(" + " AND ".join(termo(x) for x in a) + ")")
        else:
            partes.append(termo(a))
    return "(" + " OR ".join(partes) + ")"


TODAS = f"({q_rede(REDE_RURAL)} OR {q_rede(REDE_PATRIMONIAL)})"


def janela(dias=None, de=None, ate=None):
    if de or ate:
        ini = f"{de}T00:00:00Z" if de else "*"
        fim = f"{ate}T23:59:59Z" if ate else "NOW+1DAY"
        return f"dt_publicacao_tdt:[{ini} TO {fim}]"
    return f"dt_publicacao_tdt:[NOW-{dias}DAYS TO NOW+1DAY]"


def total(q, fq=None):
    p = {"wt": "json", "rows": 0, "q": q}
    if fq:
        p["fq"] = fq
    return consulta(p)["response"]["numFound"]


def tudo(q, fq, fl=FL, trava=TRAVA):
    """Pagina por cursor ate o fim do resultado (ou a trava)."""
    docs, cursor, n = [], "*", 0
    while True:
        r = consulta({"wt": "json", "q": q, "fq": fq, "fl": fl, "rows": PAGINA,
                      "sort": ORDEM, "cursorMark": cursor})
        n = r["response"]["numFound"]
        docs.extend(r["response"]["docs"])
        prox = r.get("nextCursorMark")
        if not prox or prox == cursor or len(docs) >= min(n, trava):
            return docs[:trava], n
        cursor = prox


def titulos(ementa):
    out = []
    for ln in re.split(r"[\r\n]+", ementa or ""):
        ln = ln.strip()
        if len(ln) > 12 and ln == ln.upper() and re.search(r"[A-ZÀ-Ý]", ln):
            out.append(ln)
    return out


def resumo(d, rede):
    em = d.get("ementa_s") or ""
    marc = sorted({m.group(1).lower() for m in RE_MARC.finditer(em)})
    arq = d.get("nome_arquivo_pdf_s") or ""
    ind = d.get("arquivo_indexado_s")
    return {
        "acordao": d.get("numero_decisao_s"),
        "processo": d.get("numero_processo_s"),
        "secao": d.get("secao_s"), "turma": d.get("turma_s"),
        "relator": d.get("nome_relator_s"),
        "sessao": (d.get("dt_sessao_tdt") or "")[:10],
        "publicacao": (d.get("dt_publicacao_tdt") or "")[:10],
        "rede": rede,
        "marcadores_na_ementa": marc,
        "titulos": titulos(em),
        "ementa": em, "dispositivo": d.get("decisao_txt"),
        "inteiro_teor_no_indice": ind == "S",
        "link_pdf": PDF + arq if arq else None,
        "link_pdf_responde": ind == "S",
        "sem_ementa": not em.strip(),
    }


def ler_excluir(caminho):
    if not caminho:
        return set()
    if not os.path.exists(caminho):
        raise SystemExit(f"ARQUIVO DE EXCLUSAO NAO ENCONTRADO: {caminho}")
    return set(RE_NUM.findall(open(caminho, encoding="utf-8").read()))


def cmd_versao(_):
    print(VERSAO)


def cmd_sentinela(_):
    r = consulta({"wt": "json", "rows": 1, "q": "*:*", "fq": janela(45),
                  "sort": "dt_publicacao_tdt desc",
                  "fl": "numero_decisao_s,dt_publicacao_tdt"})
    d = r["response"]["docs"]
    print(json.dumps({"canal": "VER direto (execucao de codigo)", "versao": VERSAO,
                      "registros_45d": r["response"]["numFound"],
                      "ultima_publicacao": d[0]["dt_publicacao_tdt"][:10] if d else None},
                     ensure_ascii=False))


def linha(it, tam=70):
    rep = ""
    if it.get("bloco"):
        b = it["bloco"]
        rep = f" [bloco de {len(b)}: {b[0]} a {b[-1]}]"
    return " | ".join([
        str(it["acordao"]), it["publicacao"], it["rede"],
        ",".join(it["marcadores_na_ementa"]) or ("SEM EMENTA" if it["sem_ementa"] else "-"),
        "S" if it["inteiro_teor_no_indice"] else "N",
        ((it["titulos"] or ["(sem titulo)"])[0][:tam]) + rep])


def cmd_coleta(a):
    fq = janela(a.dias, a.de, a.ate)
    excl = ler_excluir(a.excluir)
    vistos, itens, atencao, por_rede = {}, [], [], {}
    for nome, anc in (("rural", REDE_RURAL), ("patrimonial", REDE_PATRIMONIAL)):
        docs, n = tudo(q_rede(anc), fq)
        por_rede[nome] = n
        if n > len(docs):
            atencao.append(f"rede {nome}: {n} candidatos, trava de {TRAVA} atingida; "
                           f"reduzir a janela ou repetir com --de/--ate")
        for d in docs:
            k = d.get("numero_decisao_s") or d.get("nome_arquivo_pdf_s") or d.get("id")
            if k in vistos:
                vistos[k]["rede"] = "rural+patrimonial"
                continue
            it = resumo(d, nome)
            vistos[k] = it
            itens.append(it)
    ja = [it for it in itens if it["acordao"] in excl]
    novos = [it for it in itens if it["acordao"] not in excl]
    # blocos repetitivos: turma + sessao + primeiro titulo em caixa alta
    grupos = {}
    for it in novos:
        g = (it["turma"], it["sessao"], (it["titulos"] or [""])[0])
        grupos.setdefault(g, []).append(it)
    lideres = []
    for g, membros in grupos.items():
        membros.sort(key=lambda x: x["acordao"] or "")
        lider = membros[0]
        if len(membros) > 1 and g[2]:
            lider["bloco"] = [m["acordao"] for m in membros]
            for m in membros[1:]:
                m["bloco_lider"] = lider["acordao"]
            lideres.append(lider)
        else:
            for m in membros:
                m["bloco"] = None
                lideres.append(m)
    lideres.sort(key=lambda x: (x["publicacao"], x["acordao"] or ""), reverse=True)
    def so_corpo(x):  # rede patrimonial cuja ancora nao aparece na ementa (citacao, nao tema)
        em = sem_acento(x["ementa"])
        return x["rede"] == "patrimonial" and em and not any(sem_acento(a) in em for a in REDE_PATRIMONIAL)
    sem_marc = [x for x in lideres if x["rede"] == "rural" and not x["marcadores_na_ementa"] and not x["sem_ementa"]]
    corpo = [x for x in lideres if so_corpo(x)]
    principais = [x for x in lideres if x not in sem_marc and x not in corpo]
    tot = total("*:*", fq)
    com_texto = total("_texto:recurso", fq)
    com_teor = total("arquivo_indexado_s:S", fq)
    medida = {
        "janela": fq, "registros_na_janela": tot,
        "sem_texto_pesquisavel": tot - com_texto,
        "com_inteiro_teor_no_indice": com_teor,
        "so_ementa_e_dispositivo": com_texto - com_teor,
        "capturados_por_rede": por_rede,
    }
    contagem = {"capturados": len(itens), "ja_na_base": len(ja), "novos": len(novos),
                "linhas_apos_colapso": len(lideres), "para_triagem": len(principais),
                "sem_marcador_rural_na_ementa": len(sem_marc),
                "patrimonial_ancora_so_no_corpo": len(corpo)}
    if a.excluir is None:
        atencao.append("sem --excluir: a saida inclui o que ja esta na base; "
                       "conferir no Notion antes de registrar")
    json.dump({"canal": "VER direto (execucao de codigo)", "versao": VERSAO,
               "medida": medida, "contagem": contagem, "atencao": atencao,
               "ja_na_base": sorted(x["acordao"] for x in ja if x["acordao"]),
               "candidatos": novos},
              open(a.saida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"canal: VER direto (execucao de codigo) | coleta_ver {VERSAO} | {fq}")
    print("medida:", json.dumps(medida, ensure_ascii=False))
    print("contagem:", json.dumps(contagem, ensure_ascii=False))
    for e in atencao:
        print("ATENCAO:", e)
    print(f"saida completa (so os novos, com ementa e dispositivo): {a.saida}")
    print("\nNOVOS PARA TRIAGEM — acordao | publ. | rede | marcador na ementa | teor | primeiro titulo")
    for it in principais:
        print(linha(it))
    if sem_marc:
        print(f"\nSEM MARCADOR RURAL NA EMENTA (so rede rural; descarte provavel pela regra "
              f"[R], conferir se houver duvida) — {len(sem_marc)} linhas")
        for it in sem_marc:
            print(linha(it, 50))
    if corpo:
        print(f"\nPATRIMONIAL COM A ANCORA SO NO CORPO (citacao, nao tema; descarte provavel "
              f"pela trava de ruido) — {len(corpo)} linhas")
        for it in corpo:
            print(linha(it, 40))


def cmd_numero(a):
    r = consulta({"wt": "json", "rows": 5, "q": f'numero_decisao_s:"{a.acordao}"', "fl": FL})
    docs = [resumo(d, "consulta") for d in r["response"]["docs"]]
    print(json.dumps(docs, ensure_ascii=False, indent=1))


def cmd_sem_data(a):
    r = consulta({"wt": "json", "rows": a.linhas, "q": q_rede(REDE_RURAL),
                  "fq": "-dt_publicacao_tdt:[* TO *]",
                  "fl": "numero_decisao_s,numero_processo_s,dt_sessao_tdt,nome_arquivo_pdf_s,secao_s"})
    docs = r["response"]["docs"]

    def num(d):
        m = re.search(r"_(\d+)\.pdf", d.get("nome_arquivo_pdf_s") or "")
        return int(m.group(1)) if m else 0
    docs.sort(key=num, reverse=True)
    print("sem data de publicacao na rede rural:", r["response"]["numFound"],
          "(amostra nao ordenada pelo indice; confirmar data real antes de registrar)")
    for d in docs:
        print(d.get("numero_decisao_s"), "|", d.get("numero_processo_s"), "|",
              (d.get("dt_sessao_tdt") or "")[:10], "|", num(d))


# ---------- cobertura: toda familia do mapa precisa de ancora que a capture ----------

def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(c))


def ler_termos_base(caminho):
    """Le references/termos-base.md: familias '**NN Titulo — trilha X [R]**'
    seguidas de expressoes separadas por ' · ' e segmentos por ' + '.
    Para antes de '## Regras transversais' (etiquetas e exclusoes nao sao busca)."""
    fams, atual, texto = [], None, []
    for ln in open(caminho, encoding="utf-8").read().splitlines():
        if ln.startswith("## Regras transversais"):
            break
        m = re.match(r"\*\*(\d{2}) (.+?)\*\*\s*$", ln.strip())
        if m:
            if atual:
                fams.append((atual, " ".join(texto)))
            atual, texto = f"{m.group(1)} {m.group(2)}", []
            continue
        if atual and not ln.startswith("#"):
            texto.append(ln.strip())
    if atual:
        fams.append((atual, " ".join(texto)))
    out = []
    for fam, t in fams:
        t = re.sub(r"\([^)]*\)", " ", t)              # notas entre parenteses
        t = re.sub(r"\[[RA]\]", " ", t)
        t = re.sub(r"Caso direto:|Vizinhos\s*:", " ", t)
        exprs = [e.strip(" .;") for e in t.split("·")]
        exprs = [e for e in exprs if e and len(e) > 2]
        out.append((fam, [[s.strip() for s in e.split(" + ") if s.strip()] for e in exprs]))
    return out


def ler_termos_arquivo(caminho):
    """Exportacao da base viva do Notion: uma linha por termo, 'Bloco<TAB>Expressao'
    ou 'Bloco | Expressao'. Linhas de exclusao ou etiqueta devem ficar fora."""
    fams = {}
    for ln in open(caminho, encoding="utf-8"):
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        partes = re.split(r"\t|\s\|\s", ln, maxsplit=1)
        if len(partes) != 2:
            continue
        fams.setdefault(partes[0].strip(), []).append(
            [s.strip() for s in partes[1].split(" + ") if s.strip()])
    return list(fams.items())


def cmd_cobertura(a):
    fq = janela(a.dias)
    if a.termos:
        fams = ler_termos_arquivo(a.termos)
        fonte = a.termos
    else:
        fonte = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "termos-base.md")
        fams = ler_termos_base(fonte)
    print(f"cobertura | coleta_ver {VERSAO} | {fq} | termos: {fonte}")
    print("familia | expressao | no texto | fora das ancoras | fora, com o termo na ementa | fora, com marcador rural na ementa")
    escapes = {}
    for fam, exprs in fams:
        for segs in exprs:
            q = " AND ".join(termo(s) for s in segs)
            tot = total(f"({q})", fq)
            fora = total(f"({q}) AND NOT {TODAS}", fq) if tot else 0
            na_em = marc = 0
            if fora:
                docs, _ = tudo(f"({q}) AND NOT {TODAS}", fq, fl="id,ementa_s", trava=100)
                for d in docs:
                    em = d.get("ementa_s") or ""
                    if all(sem_acento(s) in sem_acento(em) for s in segs):
                        na_em += 1
                    if RE_MARC.search(em):
                        marc += 1
            if na_em:
                escapes.setdefault(fam, []).append((" + ".join(segs), na_em))
            print(f"{fam[:28]} | {' + '.join(segs)[:55]} | {tot} | {fora} | {na_em} | {marc}")
    print("\nFAMILIAS COM ESCAPE (o termo aparece na ementa e nenhuma ancora capturou):")
    if not escapes:
        print("nenhuma")
    for fam, lst in escapes.items():
        print(f"- {fam}: " + "; ".join(f"{e} ({k})" for e, k in lst))
    print("Escape com termo na ementa pede ancora nova ou decisao expressa de deixar fora; "
          "ruido (termo so no corpo) nao pede nada.")


def cmd_urls(a):
    for nome, anc in (("Rede rural", REDE_RURAL), ("Rede patrimonial", REDE_PATRIMONIAL)):
        p = urllib.parse.urlencode({"wt": "json", "rows": URL_LINHAS, "q": q_rede(anc),
                                    "fq": janela(a.dias), "sort": "dt_publicacao_tdt desc",
                                    "fl": FL.replace("id,", "").replace(",decisao_txt", "").replace(",arquivo_indexado_s", "")},
                                   quote_via=urllib.parse.quote, safe=":,")
        print(f"{nome}, últimos {a.dias} dias (até {URL_LINHAS} linhas; se numFound passar disso, a coleta por este transporte é parcial):\n{BASE}?{p}\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("versao").set_defaults(f=cmd_versao)
    sp.add_parser("sentinela").set_defaults(f=cmd_sentinela)
    c = sp.add_parser("coleta")
    c.add_argument("--dias", type=int, default=10)
    c.add_argument("--de"); c.add_argument("--ate")
    c.add_argument("--excluir", help="arquivo com os numeros de acordao ja registrados na base")
    c.add_argument("--saida", default="/tmp/carf_coleta.json"); c.set_defaults(f=cmd_coleta)
    n = sp.add_parser("numero"); n.add_argument("acordao"); n.set_defaults(f=cmd_numero)
    s = sp.add_parser("sem-data"); s.add_argument("--linhas", type=int, default=40); s.set_defaults(f=cmd_sem_data)
    cb = sp.add_parser("cobertura"); cb.add_argument("--termos"); cb.add_argument("--dias", type=int, default=90)
    cb.set_defaults(f=cmd_cobertura)
    u = sp.add_parser("urls"); u.add_argument("--dias", type=int, default=10); u.set_defaults(f=cmd_urls)
    a = ap.parse_args(); a.f(a)
