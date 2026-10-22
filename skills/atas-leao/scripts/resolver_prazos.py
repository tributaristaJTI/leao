#!/usr/bin/env python3
"""
resolver_prazos.py — atas-leao (v1.1, 2026-08-29; reconstruído a partir do contrato do SKILL.md)

Converte prazos relativos em português em datas absolutas SOMENTE quando a data
da reunião é conhecida, marca cada data como derivada, mostra a memória de
cálculo e agrega as ações por responsável. Nunca estima de cabeça: sem âncora,
o prazo fica só literal.

Uso:
  python resolver_prazos.py acoes.json --data-reuniao 2026-08-29
  python resolver_prazos.py acoes.json            # sem âncora: só agrega e devolve prazo_absoluto = null
  python resolver_prazos.py --teste               # autoteste com casos fixos

Entrada (JSON): lista de ações, cada uma com ao menos
  {"id": "A1", "texto": "...", "responsavel": "Juliane" | null, "prazo_literal": "até sexta" | null}
Saída (JSON no stdout): {"acoes": [...com prazo_absoluto, derivado, memoria_calculo...],
                         "por_responsavel": {...}, "nao_resolvidos": [...]}
Sem dependências externas (datetime e re).
"""
import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta

DIAS_SEMANA = {
    "segunda": 0, "segunda-feira": 0, "terça": 1, "terca": 1, "terça-feira": 1, "terca-feira": 1,
    "quarta": 2, "quarta-feira": 2, "quinta": 3, "quinta-feira": 3, "sexta": 4, "sexta-feira": 4,
    "sábado": 5, "sabado": 5, "domingo": 6,
}
MESES = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "marco": 3, "abril": 4, "maio": 5, "junho": 6,
    "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12,
}
NUMEROS = {
    "um": 1, "uma": 1, "dois": 2, "duas": 2, "três": 3, "tres": 3, "quatro": 4, "cinco": 5,
    "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10, "quinze": 15, "vinte": 20, "trinta": 30,
}
IRRESOLUVEIS = ("próxima reunião", "proxima reunião", "proxima reuniao", "próxima reuniao",
                "quando possível", "quando der", "assim que", "depois que", "oportunamente", "em breve")


def _n(tok: str) -> int | None:
    tok = tok.strip().lower()
    if tok.isdigit():
        return int(tok)
    return NUMEROS.get(tok)


def somar_dias_uteis(base: date, n: int) -> date:
    d = base
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:  # sem feriados: registrado na memória de cálculo
            n -= 1
    return d


def resolver(prazo_literal: str | None, ancora: date | None):
    """Devolve (data_iso | None, memoria_calculo: str)."""
    if not prazo_literal:
        return None, "sem prazo literal"
    p = prazo_literal.strip().lower()

    # 1. Expressões declaradas irresolúveis: ficam literais mesmo com âncora.
    for irr in IRRESOLUVEIS:
        if irr in p:
            return None, f"'{prazo_literal}' depende de evento sem data; fica literal"

    # 2. Datas absolutas no próprio texto não precisam de âncora.
    m = re.search(r"(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})", p)
    if m:
        d = date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        return d.isoformat(), f"data absoluta lida do texto: {m.group(0)}"
    m = re.search(r"(\d{1,2})\s+de\s+([a-zç]+)(?:\s+de\s+(\d{4}))?", p)
    if m and m.group(2) in MESES:
        ano = int(m.group(3)) if m.group(3) else (ancora.year if ancora else None)
        if ano is None:
            return None, f"'{prazo_literal}' tem dia e mês, mas sem ano nem data da reunião"
        d = date(ano, MESES[m.group(2)], int(m.group(1)))
        nota = "" if m.group(3) else " (ano assumido da data da reunião)"
        return d.isoformat(), f"dia e mês lidos do texto{nota}: {d.isoformat()}"

    # 3. Daqui em diante tudo depende da âncora.
    if ancora is None:
        return None, f"'{prazo_literal}' é relativo e não há data da reunião; fica literal"

    if "hoje" in p:
        return ancora.isoformat(), f"'hoje' = data da reunião {ancora.isoformat()}"
    if "depois de amanhã" in p or "depois de amanha" in p:
        d = ancora + timedelta(days=2)
        return d.isoformat(), f"{ancora.isoformat()} + 2 dias = {d.isoformat()}"
    if "amanhã" in p or "amanha" in p:
        d = ancora + timedelta(days=1)
        return d.isoformat(), f"{ancora.isoformat()} + 1 dia = {d.isoformat()}"

    # "em N dias", "N dias", "em N dias úteis", "N semanas", "N meses"
    m = re.search(r"(\d+|\b(?:um|uma|dois|duas|tr[eê]s|quatro|cinco|seis|sete|oito|nove|dez|quinze|vinte|trinta)\b)\s*(dias?\s+[uú]teis|dias?|semanas?|m[eê]s(?:es)?)", p)
    if m:
        n = _n(m.group(1))
        unidade = m.group(2)
        if n is not None:
            if "útil" in unidade or "uteis" in unidade or "úteis" in unidade:
                d = somar_dias_uteis(ancora, n)
                return d.isoformat(), f"{ancora.isoformat()} + {n} dias úteis (sem feriados) = {d.isoformat()}"
            if unidade.startswith("dia"):
                d = ancora + timedelta(days=n)
                return d.isoformat(), f"{ancora.isoformat()} + {n} dias = {d.isoformat()}"
            if unidade.startswith("semana"):
                d = ancora + timedelta(days=7 * n)
                return d.isoformat(), f"{ancora.isoformat()} + {n} semana(s) = {d.isoformat()}"
            if unidade.startswith("m"):
                mes = ancora.month - 1 + n
                ano = ancora.year + mes // 12
                mes = mes % 12 + 1
                dia = min(ancora.day, [31, 29 if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mes - 1])
                d = date(ano, mes, dia)
                return d.isoformat(), f"{ancora.isoformat()} + {n} mês(es) = {d.isoformat()}"

    # "próxima semana" = segunda da semana seguinte; "fim da semana" = sexta; "fim do mês" = último dia
    if "próxima semana" in p or "proxima semana" in p or "semana que vem" in p:
        d = ancora + timedelta(days=(7 - ancora.weekday()))
        return d.isoformat(), f"segunda-feira da semana seguinte a {ancora.isoformat()} = {d.isoformat()}"
    if "fim da semana" in p or "final da semana" in p:
        d = ancora + timedelta(days=(4 - ancora.weekday()) % 7)
        return d.isoformat(), f"sexta-feira da semana de {ancora.isoformat()} = {d.isoformat()}"
    if "fim do mês" in p or "final do mês" in p or "fim do mes" in p:
        prox = date(ancora.year + (ancora.month == 12), ancora.month % 12 + 1, 1)
        d = prox - timedelta(days=1)
        return d.isoformat(), f"último dia do mês de {ancora.isoformat()} = {d.isoformat()}"

    # dia da semana: "até sexta", "na quarta". Mesmo dia da semana da reunião = semana seguinte.
    for nome, idx in DIAS_SEMANA.items():
        if re.search(rf"\b{re.escape(nome)}\b", p):
            delta = (idx - ancora.weekday()) % 7
            if delta == 0:
                delta = 7
            d = ancora + timedelta(days=delta)
            return d.isoformat(), f"próxima {nome} após {ancora.isoformat()} = {d.isoformat()}"

    return None, f"'{prazo_literal}' não reconhecido; fica literal (registrar como defeito se a ação exigir data)"


def processar(acoes: list, ancora: date | None) -> dict:
    saida, nao_resolvidos = [], []
    por_resp: dict = {}
    for a in acoes:
        iso, memoria = resolver(a.get("prazo_literal"), ancora)
        item = dict(a)
        item["prazo_absoluto"] = iso
        item["derivado"] = iso is not None and not re.search(r"\d{1,2}[/.-]\d{1,2}[/.-]\d{4}", (a.get("prazo_literal") or ""))
        item["memoria_calculo"] = memoria
        saida.append(item)
        if a.get("prazo_literal") and iso is None:
            nao_resolvidos.append({"id": a.get("id"), "prazo_literal": a.get("prazo_literal"), "motivo": memoria})
        chave = a.get("responsavel") or "[SEM RESPONSÁVEL]"
        por_resp.setdefault(chave, []).append({"id": a.get("id"), "texto": a.get("texto"), "prazo_absoluto": iso, "prazo_literal": a.get("prazo_literal")})
    for lista in por_resp.values():
        lista.sort(key=lambda x: (x["prazo_absoluto"] is None, x["prazo_absoluto"] or ""))
    return {"data_reuniao": ancora.isoformat() if ancora else None, "acoes": saida, "por_responsavel": por_resp, "nao_resolvidos": nao_resolvidos}


def _teste() -> int:
    anc = date(2026, 8, 29)  # sábado
    casos = [
        ("até sexta", "2026-09-04"), ("em 15 dias", "2026-09-13"), ("10 dias úteis", "2026-09-11"),
        ("próxima semana", "2026-08-31"), ("fim do mês", "2026-08-31"), ("15 de setembro", "2026-09-15"),
        ("08/09/2026", "2026-09-08"), ("duas semanas", "2026-09-12"), ("até a próxima reunião", None),
        ("amanhã", "2026-08-30"), ("em um mês", "2026-09-29"),
    ]
    falhas = 0
    for lit, esperado in casos:
        got, mem = resolver(lit, anc)
        ok = got == esperado
        falhas += (not ok)
        print(f"{'OK ' if ok else 'ERRO'} {lit!r:28} -> {got}  [{mem}]")
    # sem âncora, relativo fica literal
    got, _ = resolver("em 15 dias", None)
    ok = got is None
    falhas += (not ok)
    print(f"{'OK ' if ok else 'ERRO'} sem âncora: 'em 15 dias' -> {got}")
    print("falhas:", falhas)
    return 1 if falhas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Resolve prazos relativos de atas com âncora explícita.")
    ap.add_argument("arquivo", nargs="?", help="JSON com a lista de ações")
    ap.add_argument("--data-reuniao", help="Âncora ISO (AAAA-MM-DD). Sem ela, prazos relativos ficam literais.")
    ap.add_argument("--teste", action="store_true")
    args = ap.parse_args()
    if args.teste:
        return _teste()
    if not args.arquivo:
        ap.error("informe o arquivo JSON ou --teste")
    with open(args.arquivo, encoding="utf-8") as f:
        dados = json.load(f)
    acoes = dados["acoes"] if isinstance(dados, dict) and "acoes" in dados else dados
    ancora = datetime.strptime(args.data_reuniao, "%Y-%m-%d").date() if args.data_reuniao else None
    print(json.dumps(processar(acoes, ancora), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
