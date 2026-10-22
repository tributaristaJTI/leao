# Matriz de precificação — Amaral e Melo Advogados

**Versão:** v1.0-formulário — 2026-08-29 (reconstruído a partir do contrato do SKILL.md; o original de 22/06 não foi instalado com a skill). **Estado: NÃO PREENCHIDO.** Enquanto o bloco de parâmetros da seção 8 tiver `null`, o `scripts/proposta.py` devolve "MATRIZ NÃO PREENCHIDA" e a proposta não é precificada. Isso substitui a improvisação silenciosa que rodou de junho a agosto.

Quem preenche: Leonardo. Onde: neste arquivo (cópia canônica no Drive, pasta `Mestre de Obras/` até a reinstalação; depois, dentro do pacote da skill). Os números aqui são regra comercial do escritório, não dado do modelo.

## 1. Trilhas (produto que a proposta vende)

| Trilha | O que entrega | Camada da Garra | Quando |
|---|---|---|---|
| `diagnostico` | dimensiona exposição e classifica a trilha seguinte; produto pago | oportunidade | qualquer gatilho do Passo 2 (reforma, planejamento abusivo, múltiplas entidades) |
| `parecer` | estratégia: cenários, tese, recomendação | oportunidade | caso preventivo com decisão a tomar |
| `operacao` | execução: reestruturação, transação, protocolo, contratos | oportunidade ou relacionamento | após parecer ou com veículo já decidido |
| `defesa` | contencioso administrativo ou judicial | crise | exigência já formalizada |

## 2. Complexidade (vocabulário único: `/comercial` §6 e `plano.md` v0)

| Nível | Critério de enquadramento | Faixa de esforço do plano |
|---|---|---|
| baixa | uma entidade, tema pacificado, sem gatilho | P ou M |
| média | duas entidades ou tema com divergência, um gatilho | M ou G |
| alta | múltiplas entidades, reforma ou planejamento abusivo, dois ou mais gatilhos | G ou GG |

## 3. Faixas de honorário por trilha × complexidade (A PREENCHER)

Base de cálculo por trilha: `defesa` e `operacao` em percentual do valor em jogo (com piso e teto em R$); `parecer` e `diagnostico` em R$ fixo por faixa.

| Trilha | Baixa | Média | Alta | Piso R$ | Teto R$ |
|---|---|---|---|---|---|
| defesa (% do valor em jogo, honorário fixo) | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] |
| defesa (% de êxito sobre economia ou redução) | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | — | [A PREENCHER] |
| operacao (% do valor em jogo) | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] |
| parecer (R$) | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | — | — |
| diagnostico (R$) | [A PREENCHER] | [A PREENCHER] | [A PREENCHER] | — | — |

## 4. Modelos de honorário

| Modelo | Quando recomendar | Parâmetros |
|---|---|---|
| `fixo` | parecer, diagnóstico, operação de escopo fechado | faixa da seção 3 |
| `fixo_mais_exito` | defesa com economia mensurável | fixo reduzido + % de êxito (seção 3) |
| `exito` | defesa em que o cliente não tem caixa e a tese é forte | só % de êxito; piso de entrada [A PREENCHER] |
| `mensalidade` | contratos recorrentes (camada relacionamento) | R$/mês por porte [A PREENCHER] |
| `por_fase` | operação longa (plano de execução com marcos) | parcela por fase concluída, conforme `plano.md` v1 |

## 5. Escada de crédito (cada degrau credita no seguinte)

| De → para | Percentual do honorário anterior creditado | Validade do crédito |
|---|---|---|
| diagnostico → parecer | [A PREENCHER] % | [A PREENCHER] dias após a entrega |
| parecer → operacao | [A PREENCHER] % | [A PREENCHER] dias após a entrega |
| diagnostico → operacao (pulando o parecer) | [A PREENCHER] % | [A PREENCHER] dias |

Regra do SKILL.md preservada: o crédito é estrutura de honorário, não "promoção" (Provimento 205).

## 6. Calendário de colheita (janelas de caixa do produtor)

| Cultura | Janela de caixa | Observação |
|---|---|---|
| soja | [A PREENCHER: ex. fevereiro a abril] | |
| milho safrinha | [A PREENCHER: ex. julho a setembro] | |
| pecuária | [A PREENCHER] | |
| sem sazonalidade (PJ, agroindústria) | parcelas mensais | |

Regra: a primeira parcela nunca fica fora de janela sem acordo expresso; a entrada (sinal) é [A PREENCHER] % do fixo.

## 7. Regras de piso e de escalação

- Honorário abaixo do piso da OAB-GO: não propor; ver a tabela vigente da Seccional [A PREENCHER: referência e data].
- Proposta acima de R$ [A PREENCHER] ou com êxito acima de [A PREENCHER] %: ratificação de dois sócios.
- Modo neutro (transação de fazenda com dois contratantes): honorário dividido [A PREENCHER: proporção] e limite do art. 22 do CED na carta.

## 8. Parâmetros lidos pelo `scripts/proposta.py`

Preencher os `null`. Percentuais em fração (0.05 = 5 %). Meses em números (1 = janeiro).

```json
{
  "versao": "1.0-formulario",
  "preenchida_em": null,
  "faixas": {
    "defesa":      {"pct_fixo": {"baixa": null, "media": null, "alta": null}, "pct_exito": {"baixa": null, "media": null, "alta": null}, "piso": null, "teto_fixo": null, "teto_exito": null},
    "operacao":    {"pct": {"baixa": null, "media": null, "alta": null}, "piso": null, "teto": null},
    "parecer":     {"fixo": {"baixa": null, "media": null, "alta": null}},
    "diagnostico": {"fixo": {"baixa": null, "media": null, "alta": null}}
  },
  "modelos": {"exito_piso_entrada": null, "mensalidade": {"pequeno": null, "medio": null, "grande": null}, "sinal_pct": null},
  "escada_credito": {"diagnostico_parecer": {"pct": null, "validade_dias": null}, "parecer_operacao": {"pct": null, "validade_dias": null}, "diagnostico_operacao": {"pct": null, "validade_dias": null}},
  "calendario_colheita": {"soja": {"inicio": null, "fim": null}, "milho_safrinha": {"inicio": null, "fim": null}, "pecuaria": {"inicio": null, "fim": null}},
  "escalacao": {"valor_dois_socios": null, "exito_dois_socios": null}
}
```
