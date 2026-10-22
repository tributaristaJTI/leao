#!/usr/bin/env python3
"""
proposta.py — proposta-aem (v1.0, 2026-08-29; reconstruído a partir do contrato do SKILL.md)

Devolve FAIXA, MODELO RECOMENDADO e CENÁRIOS. Nunca um preço único: o número é
julgamento do advogado (Passo 4). Todos os parâmetros vêm do bloco JSON da seção 8
de references/matriz_precificacao.md; enquanto houver `null` relevante, o script
para com "MATRIZ NÃO PREENCHIDA" (regra mecânica no lugar da improvisação).

Funções de trilha:   trilha_defesa, trilha_operacao, trilha_parecer, trilha_diagnostico
Cenários:            calendario_colheita, fixo_vs_exito, escada_credito
Autoverificação:     por inversão (recalcula a entrada a partir da saída e compara).

Uso:
  python proposta.py --trilha operacao --valor 1500000 --complexidade alta
  python proposta.py --trilha defesa --valor 800000 --complexidade media --economia 350000
  python proposta.py --trilha diagnostico --complexidade alta --escada
  python proposta.py --trilha operacao --valor 1500000 --complexidade alta --cultura soja --data-aceite 2026-09-08
  python proposta.py --teste       # roda com uma matriz DEMO (não usar em proposta)
"""
import argparse
import json
import os
import re
import sys
from datetime import date, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
MATRIZ_PATH = os.path.join(AQUI, "..", "references", "matriz_precificacao.md")
COMPLEXIDADES = ("baixa", "media", "alta")


class MatrizNaoPreenchida(Exception):
    pass


# ---------------------------------------------------------------- matriz
def carregar_matriz(path: str = MATRIZ_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    m = re.search(r"```json\s*(\{.*?\})\s*```", txt, flags=re.S)
    if not m:
        raise MatrizNaoPreenchida("bloco ```json``` não encontrado em matriz_precificacao.md")
    return json.loads(m.group(1))


def _exigir(matriz: dict, *caminho):
    """Lê um valor da matriz; null → MatrizNaoPreenchida com o caminho do campo."""
    v = matriz
    for k in caminho:
        v = v.get(k) if isinstance(v, dict) else None
        if v is None:
            raise MatrizNaoPreenchida("MATRIZ NÃO PREENCHIDA: " + ".".join(caminho))
    return v


def _faixa_pct(valor: float, pct: float, piso, teto) -> tuple[float, float, dict]:
    """Faixa em torno de pct × valor (±20 %), respeitando piso e teto. Devolve (min, max, memória)."""
    centro = valor * pct
    lo, hi = centro * 0.8, centro * 1.2
    if piso is not None:
        lo, hi = max(lo, piso), max(hi, piso)
    if teto is not None:
        lo, hi = min(lo, teto), min(hi, teto)
    mem = {"centro": round(centro, 2), "regra": "centro = valor × pct; faixa = centro ± 20 %; piso e teto aplicados"}
    return round(lo, 2), round(hi, 2), mem


def _inverter(valor: float, faixa_min: float, faixa_max: float, pct: float, piso, teto) -> bool:
    """Autoverificação: reconstitui pct a partir do centro da faixa quando piso/teto não cortaram."""
    centro = (faixa_min / 0.8 + faixa_max / 1.2) / 2
    cortado = (piso is not None and faixa_min <= piso + 1e-6) or (teto is not None and faixa_max >= teto - 1e-6)
    if cortado:
        return True
    return abs(centro / valor - pct) < 1e-6


# ---------------------------------------------------------------- trilhas
def trilha_defesa(matriz: dict, valor_em_jogo: float, complexidade: str, economia_esperada: float | None = None) -> dict:
    pf = _exigir(matriz, "faixas", "defesa", "pct_fixo", complexidade)
    pe = _exigir(matriz, "faixas", "defesa", "pct_exito", complexidade)
    piso = matriz["faixas"]["defesa"].get("piso")
    teto_fixo = matriz["faixas"]["defesa"].get("teto_fixo")
    lo, hi, mem = _faixa_pct(valor_em_jogo, pf, piso, teto_fixo)
    assert _inverter(valor_em_jogo, lo, hi, pf, piso, teto_fixo), "autoverificação falhou (defesa)"
    base_exito = economia_esperada if economia_esperada is not None else valor_em_jogo
    return {
        "trilha": "defesa", "complexidade": complexidade, "valor_em_jogo": valor_em_jogo,
        "faixa_fixo": [lo, hi], "pct_exito": pe, "base_exito": base_exito,
        "exito_estimado": round(base_exito * pe, 2),
        "modelo_recomendado": "fixo_mais_exito" if economia_esperada else "fixo",
        "memoria": mem,
    }


def trilha_operacao(matriz: dict, valor_em_jogo: float, complexidade: str) -> dict:
    p = _exigir(matriz, "faixas", "operacao", "pct", complexidade)
    piso, teto = matriz["faixas"]["operacao"].get("piso"), matriz["faixas"]["operacao"].get("teto")
    lo, hi, mem = _faixa_pct(valor_em_jogo, p, piso, teto)
    assert _inverter(valor_em_jogo, lo, hi, p, piso, teto), "autoverificação falhou (operacao)"
    return {"trilha": "operacao", "complexidade": complexidade, "valor_em_jogo": valor_em_jogo,
            "faixa_fixo": [lo, hi], "modelo_recomendado": "fixo" if complexidade != "alta" else "por_fase", "memoria": mem}


def _trilha_fixa(matriz: dict, nome: str, complexidade: str) -> dict:
    v = _exigir(matriz, "faixas", nome, "fixo", complexidade)
    lo, hi = round(v * 0.85, 2), round(v * 1.15, 2)
    assert abs((lo / 0.85 + hi / 1.15) / 2 - v) < 1e-6, f"autoverificação falhou ({nome})"
    return {"trilha": nome, "complexidade": complexidade, "faixa_fixo": [lo, hi], "modelo_recomendado": "fixo",
            "memoria": {"centro": v, "regra": "faixa = valor da matriz ± 15 %"}}


def trilha_parecer(matriz: dict, complexidade: str) -> dict:
    return _trilha_fixa(matriz, "parecer", complexidade)


def trilha_diagnostico(matriz: dict, complexidade: str) -> dict:
    return _trilha_fixa(matriz, "diagnostico", complexidade)


# ---------------------------------------------------------------- cenários
def calendario_colheita(matriz: dict, total: float, data_aceite: date, cultura: str, sinal_pct: float | None = None, n_parcelas: int = 3) -> dict:
    """Sinal no aceite; saldo em parcelas iguais dentro da janela de caixa da cultura."""
    if cultura == "sem_sazonalidade":
        parcela = round(total / n_parcelas, 2)
        parcelas = [{"n": i + 1, "mes": (data_aceite.month + i - 1) % 12 + 1, "valor": parcela} for i in range(n_parcelas)]
        return {"cenario": "calendario_colheita", "cultura": cultura, "sinal": 0.0, "parcelas": parcelas, "soma": round(parcela * n_parcelas, 2)}
    ini = _exigir(matriz, "calendario_colheita", cultura, "inicio")
    fim = _exigir(matriz, "calendario_colheita", cultura, "fim")
    sp = sinal_pct if sinal_pct is not None else _exigir(matriz, "modelos", "sinal_pct")
    sinal = round(total * sp, 2)
    saldo = total - sinal
    meses = []
    m = ini
    while True:
        meses.append(m)
        if m == fim:
            break
        m = m % 12 + 1
    n = min(n_parcelas, len(meses))
    parcela = round(saldo / n, 2)
    parcelas = [{"n": i + 1, "mes": meses[i], "valor": parcela} for i in range(n)]
    soma = round(sinal + parcela * n, 2)
    assert abs(soma - total) < 0.05 * n + 0.01, "autoverificação falhou (soma das parcelas)"
    return {"cenario": "calendario_colheita", "cultura": cultura, "sinal": sinal, "parcelas": parcelas, "soma": soma,
            "memoria": f"sinal = {sp:.0%} no aceite; saldo em {n} parcela(s) nos meses {meses[:n]} (janela {ini}-{fim})"}


def fixo_vs_exito(matriz: dict, valor_em_jogo: float, complexidade: str, economia_esperada: float, prob_exito: float = 0.5) -> dict:
    """Compara fixo puro, fixo+êxito e êxito puro pelo valor esperado; a decisão é do advogado."""
    d = trilha_defesa(matriz, valor_em_jogo, complexidade, economia_esperada)
    fixo_centro = d["memoria"]["centro"]
    exito = d["exito_estimado"]
    piso_entrada = matriz["modelos"].get("exito_piso_entrada")
    cenarios = {
        "fixo": {"cliente_paga_sempre": fixo_centro, "valor_esperado_escritorio": fixo_centro},
        "fixo_mais_exito": {"fixo_reduzido": round(fixo_centro * 0.6, 2), "exito_se_ganhar": exito,
                            "valor_esperado_escritorio": round(fixo_centro * 0.6 + exito * prob_exito, 2)},
        "exito": {"entrada": piso_entrada, "exito_se_ganhar": exito,
                  "valor_esperado_escritorio": round((piso_entrada or 0) + exito * prob_exito, 2)},
    }
    return {"cenario": "fixo_vs_exito", "prob_exito_assumida": prob_exito, "cenarios": cenarios,
            "nota": "prob_exito é premissa declarada do advogado (grau de risco da tese), não saída do script"}


def escada_credito(matriz: dict, complexidade: str, valor_em_jogo: float | None = None) -> dict:
    diag = trilha_diagnostico(matriz, complexidade)["memoria"]["centro"]
    par = trilha_parecer(matriz, complexidade)["memoria"]["centro"]
    e_dp = _exigir(matriz, "escada_credito", "diagnostico_parecer", "pct")
    e_po = _exigir(matriz, "escada_credito", "parecer_operacao", "pct")
    linhas = [{"degrau": "diagnostico", "bruto": diag, "credito": 0.0, "liquido": diag}]
    cred_p = round(diag * e_dp, 2)
    linhas.append({"degrau": "parecer", "bruto": par, "credito": cred_p, "liquido": round(par - cred_p, 2)})
    if valor_em_jogo:
        op = trilha_operacao(matriz, valor_em_jogo, complexidade)["memoria"]["centro"]
        cred_o = round(par * e_po, 2)
        linhas.append({"degrau": "operacao", "bruto": op, "credito": cred_o, "liquido": round(op - cred_o, 2)})
    total_bruto = round(sum(l["bruto"] for l in linhas), 2)
    total_liq = round(sum(l["liquido"] for l in linhas), 2)
    assert abs(total_bruto - total_liq - sum(l["credito"] for l in linhas)) < 0.01, "autoverificação falhou (escada)"
    return {"cenario": "escada_credito", "degraus": linhas, "total_bruto": total_bruto, "total_liquido": total_liq,
            "validade": {"diagnostico_parecer_dias": matriz["escada_credito"]["diagnostico_parecer"].get("validade_dias"),
                         "parecer_operacao_dias": matriz["escada_credito"]["parecer_operacao"].get("validade_dias")}}


# ---------------------------------------------------------------- demo (nunca em proposta real)
MATRIZ_DEMO = {
    "versao": "DEMO", "preenchida_em": "nunca",
    "faixas": {"defesa": {"pct_fixo": {"baixa": 0.03, "media": 0.05, "alta": 0.08}, "pct_exito": {"baixa": 0.10, "media": 0.15, "alta": 0.20}, "piso": 15000, "teto_fixo": 400000, "teto_exito": None},
               "operacao": {"pct": {"baixa": 0.02, "media": 0.03, "alta": 0.05}, "piso": 20000, "teto": 500000},
               "parecer": {"fixo": {"baixa": 12000, "media": 25000, "alta": 45000}},
               "diagnostico": {"fixo": {"baixa": 8000, "media": 15000, "alta": 25000}}},
    "modelos": {"exito_piso_entrada": 10000, "mensalidade": {"pequeno": 3000, "medio": 6000, "grande": 12000}, "sinal_pct": 0.3},
    "escada_credito": {"diagnostico_parecer": {"pct": 0.5, "validade_dias": 90}, "parecer_operacao": {"pct": 0.3, "validade_dias": 180}, "diagnostico_operacao": {"pct": 0.3, "validade_dias": 180}},
    "calendario_colheita": {"soja": {"inicio": 2, "fim": 4}, "milho_safrinha": {"inicio": 7, "fim": 9}, "pecuaria": {"inicio": 1, "fim": 12}},
    "escalacao": {"valor_dois_socios": 300000, "exito_dois_socios": 0.25},
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Faixa, modelo e cenários de honorário (nunca preço único).")
    ap.add_argument("--trilha", choices=["defesa", "operacao", "parecer", "diagnostico"])
    ap.add_argument("--valor", type=float, help="valor econômico em jogo (R$)")
    ap.add_argument("--complexidade", choices=COMPLEXIDADES, default="media")
    ap.add_argument("--economia", type=float, help="economia ou redução esperada (R$), base do êxito")
    ap.add_argument("--prob-exito", type=float, default=0.5)
    ap.add_argument("--cultura", choices=["soja", "milho_safrinha", "pecuaria", "sem_sazonalidade"])
    ap.add_argument("--data-aceite", help="AAAA-MM-DD")
    ap.add_argument("--escada", action="store_true", help="inclui o cenário de escada de crédito")
    ap.add_argument("--matriz", default=MATRIZ_PATH)
    ap.add_argument("--teste", action="store_true", help="roda com a matriz DEMO; saída marcada, não usar em proposta")
    a = ap.parse_args()

    try:
        matriz = MATRIZ_DEMO if a.teste else carregar_matriz(a.matriz)
        if a.teste:
            a.trilha, a.valor, a.complexidade, a.economia, a.cultura, a.data_aceite, a.escada = "defesa", 800000.0, "media", 350000.0, "soja", "2026-09-08", True
        if not a.trilha:
            ap.error("--trilha é obrigatória (ou --teste)")
        saida = {"aviso": "DEMO: matriz fictícia, não usar em proposta" if a.teste else None, "matriz_versao": matriz.get("versao")}
        if a.trilha == "defesa":
            if a.valor is None:
                ap.error("--valor é obrigatório para defesa")
            saida["trilha"] = trilha_defesa(matriz, a.valor, a.complexidade, a.economia)
            if a.economia:
                saida["fixo_vs_exito"] = fixo_vs_exito(matriz, a.valor, a.complexidade, a.economia, a.prob_exito)
        elif a.trilha == "operacao":
            if a.valor is None:
                ap.error("--valor é obrigatório para operacao")
            saida["trilha"] = trilha_operacao(matriz, a.valor, a.complexidade)
        elif a.trilha == "parecer":
            saida["trilha"] = trilha_parecer(matriz, a.complexidade)
        else:
            saida["trilha"] = trilha_diagnostico(matriz, a.complexidade)
        if a.escada:
            saida["escada_credito"] = escada_credito(matriz, a.complexidade, a.valor)
        if a.cultura and a.data_aceite:
            total = sum(saida["trilha"]["faixa_fixo"]) / 2
            saida["calendario_colheita"] = calendario_colheita(matriz, total, datetime.strptime(a.data_aceite, "%Y-%m-%d").date(), a.cultura)
        esc = matriz.get("escalacao", {})
        centro = saida["trilha"].get("memoria", {}).get("centro")
        if esc.get("valor_dois_socios") and centro and centro > esc["valor_dois_socios"]:
            saida["escalacao"] = "acima do limite: ratificação de dois sócios"
        print(json.dumps(saida, ensure_ascii=False, indent=2))
        return 0
    except MatrizNaoPreenchida as e:
        print(str(e), file=sys.stderr)
        print("A proposta não é precificada com a matriz incompleta. Preencher references/matriz_precificacao.md (seção 8).", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
