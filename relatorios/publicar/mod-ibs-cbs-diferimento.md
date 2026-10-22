# Publicar · mod-ibs-cbs-diferimento

Origem: `skills/mod-ibs-cbs-diferimento/` no repositório tributaristaJTI/leao. Versão sincronizada de referência: atualizada na conta em 2026-04-06.

## 1. SKILL.md completa e final

`````markdown
---
name: mod-ibs-cbs-diferimento
description: "Módulo de análise da reforma tributária aplicada ao agronegócio. Use SEMPRE que o usuário mencionar IBS, CBS, reforma tributária, imposto sobre bens e serviços, contribuição sobre bens e serviços, diferimento de insumos agropecuários, alíquota reduzida agro, regime específico produtor rural, transição tributária, crédito presumido reforma, cesta básica agro, ou qualquer variação de análise sobre o impacto da reforma tributária nas operações agropecuárias."
---

# Módulo IBS/CBS e Diferimento na Compra de Insumos Agropecuários

Simula a carga de IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços) sobre a operação agropecuária do cliente, com foco no diferimento na aquisição de insumos, e compara com a carga atual (ICMS e PIS/COFINS). A reforma está em regulamentação: por isso o módulo trata toda alíquota, limite, prazo e regra como parâmetro que só entra no cálculo depois de conferido na sessão.

## Escopo

- IBS e CBS aplicados ao agro, inclusive alíquotas reduzidas e créditos presumidos na cadeia
- Diferimento na aquisição de insumos agropecuários
- Regime do produtor rural pessoa física na reforma
- Período de transição e convivência de regimes
- Comparativo carga atual × carga projetada
- Exportação

## Passo 0 · Base normativa da sessão (antes de qualquer conta)

Montar a tabela de parâmetros. Cada linha é conferida no conector Jusratio ou na fonte oficial consolidada; nenhuma vem de memória, deste arquivo ou do `ref-funrural-ibs.md` (que serve só como mapa de onde procurar).

| Parâmetro | Valor | Fonte conferida | Status |
|---|---|---|---|
| Alíquota de referência de IBS e de CBS no ano analisado | | | vigente / projetado / [A CONFERIR: fonte] |
| Redução de alíquota para o produto agropecuário do cliente | | | |
| Regra de diferimento para cada categoria de insumo do cliente | | | |
| Enquadramento do produtor pessoa física (limite e efeitos) | | | |
| Crédito presumido do adquirente de produtor não contribuinte | | | |
| Tratamento da exportação | | | |
| Cronograma da transição, ano a ano, para IBS, CBS, ICMS e PIS/COFINS | | | |
| Regime atual de ICMS no estado do cliente (diferimentos, isenções) | | | |
| Regime atual de PIS/COFINS conforme o regime do cliente | | | |

Linha sem fonte conferida não bloqueia a análise: ela roda como cenário, com o parâmetro marcado [A CONFERIR: fonte], e a conclusão não se apoia nela.

## Fluxo analítico

1. **Mapear a operação.** Faturamento por produto; compras de insumos por categoria (sementes e mudas, fertilizantes e corretivos, defensivos, rações e suplementos, combustíveis e lubrificantes, máquinas e implementos); percentual exportado; regime atual (PF, PJ no lucro real ou no presumido); estados de operação. Dado que faltar entra em "Informações pendentes", sem interromper.
2. **Carga atual.** ICMS efetivo (com os diferimentos e créditos acumulados do estado) e PIS/COFINS efetivo, pelos parâmetros do Passo 0.
3. **Carga projetada.** Débitos sobre vendas internas, tratamento da exportação, créditos sobre insumos, saldo e destino do saldo credor, pelos parâmetros do Passo 0.
4. **Diferimento de insumos.** Quais insumos do cliente se enquadram, efeito no caixa (quando o imposto é pago e por quem), diferença para isenção, efeito no crédito do adquirente.
5. **Produtor pessoa física.** Enquadramento, obrigações acessórias, efeito do crédito presumido no preço que o adquirente paga, e a pergunta da operação: manter PF ou migrar para PJ.
6. **Transição.** Carga ano a ano para a operação do cliente, pelo cronograma conferido.
7. **Quadro comparativo e sensibilidade** (modelo abaixo).
8. **Recomendação.** Se a reforma melhora ou piora a operação do cliente, ações preparatórias, se há razão para reorganizar a estrutura antes da vigência plena, e o calendário de acompanhamento regulatório.

## Cálculo

Todo cálculo em Python, com os parâmetros num único dicionário que carrega valor e fonte, para que a memória de cálculo mostre de onde veio cada número:

```python
parametros = {
    "aliquota_ref_cbs": {"valor": None, "fonte": "[A CONFERIR: fonte]"},
    "aliquota_ref_ibs": {"valor": None, "fonte": "[A CONFERIR: fonte]"},
    "reducao_agro": {"valor": None, "fonte": "[A CONFERIR: fonte]"},
    # uma entrada por linha da tabela do Passo 0
}
```

Três camadas de segurança: (1) prova real, invertendo o cálculo; (2) conferência de que nenhum parâmetro usado está com `valor` vazio sem estar marcado como cenário; (3) etapas mostradas uma a uma, para o advogado conferir variável por variável. Valores finais em centavos; percentuais com quatro casas.

## Quadro comparativo

| Elemento | Carga atual | Carga projetada | Diferença |
|---|---|---|---|
| Tributos sobre vendas internas | R$ | R$ | R$ |
| Tributos sobre exportação | R$ | R$ | R$ |
| Créditos sobre insumos | R$ | R$ | R$ |
| Carga líquida | R$ | R$ | R$ |
| Carga efetiva (% da receita) | % | % | |

Sensibilidade obrigatória: alíquota de referência dois pontos acima e abaixo; exportação em 20%, 50% e 80%; com e sem diferimento de insumos; PF × PJ.

## Regras

1. Passo 0 antes de qualquer conta. Parâmetro não conferido é cenário, nunca premissa da conclusão.
2. Separar, no texto e no quadro, o que é norma vigente do que é projeção.
3. Operação em mais de um estado: considerar o efeito da tributação no destino.
4. Se a análise envolver comparação PF × PJ ou grupo econômico, articular com `mod-comparativo-pf-pj` e `mod-grupo-economico`.
5. A entrega fecha com nota metodológica: parâmetros conferidos (com fonte e data) × pendentes de conferência.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
`````

## 2. O que mudou desde a versão sincronizada

Instrução reescrita (aprovada por Leonardo em 22/10, pendente 2): novo Passo 0 monta a tabela de parâmetros conferidos no Jusratio ou na fonte oficial, com fonte e status.
Saem os números escritos de memória: o cronograma da transição ano a ano e as alíquotas do PIS/COFINS cumulativo.
Parâmetro não conferido roda como cenário e nunca sustenta a conclusão; o Python carrega valor e fonte de cada parâmetro, com três camadas de segurança.
O fluxo de nove seções vira oito passos; quadro comparativo e sensibilidade mantidos; nota metodológica obrigatória na entrega.
Description (gatilhos) idêntica; a seção "Conferência de citação" padrão fecha o arquivo.
