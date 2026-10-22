---
name: mod-ibs-cbs-diferimento
description: "Módulo de análise da reforma tributária aplicada ao agronegócio. Use SEMPRE que o usuário mencionar IBS, CBS, reforma tributária, imposto sobre bens e serviços, contribuição sobre bens e serviços, diferimento de insumos agropecuários, alíquota reduzida agro, regime específico produtor rural, transição tributária, crédito presumido reforma, cesta básica agro, ou qualquer variação de análise sobre o impacto da reforma tributária nas operações agropecuárias."
---

# Módulo IBS/CBS e Diferimento na Compra de Insumos Agropecuários

Módulo voltado para a reforma tributária (EC 132/2023 e legislação complementar). Simula a carga de IBS/CBS sobre operações agropecuárias, com foco no diferimento na aquisição de insumos e no comparativo entre carga atual e carga projetada.

## Escopo

- IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços) aplicados ao agro
- Diferimento na aquisição de insumos agropecuários (sementes, fertilizantes, defensivos, rações, combustível)
- Regime específico do produtor rural na reforma (PF com receita até determinado limite)
- Alíquotas reduzidas para produtos agropecuários
- Créditos presumidos na cadeia agro
- Período de transição (2026-2033) e convivência de regimes
- Comparativo carga atual (ICMS + PIS/COFINS) vs carga projetada (IBS/CBS)
- Impacto na exportação (manutenção da imunidade)

## Nota importante

**A reforma tributária está em fase de regulamentação.** As alíquotas definitivas, regras de diferimento e regime específico do produtor rural dependem de leis complementares e regulamentos que podem ser alterados. Toda análise neste módulo deve:

1. Pesquisar a legislação mais recente via web antes de calcular
2. Explicitar as premissas regulatórias adotadas
3. Sinalizar claramente o que é norma vigente e o que é projeção baseada no texto aprovado
4. Incluir cenários de sensibilidade para variações de alíquota

## Fluxo analítico

### 1. Mapeamento da operação atual

Coletar:
- Faturamento bruto anual por tipo de produto (soja, milho, gado, leite, etc.)
- Volume e valor de compras de insumos por categoria:
  - Sementes e mudas
  - Fertilizantes e corretivos
  - Defensivos agrícolas
  - Rações e suplementos (se pecuária)
  - Combustíveis e lubrificantes
  - Máquinas e implementos (investimento)
- Percentual de vendas para exportação vs mercado interno
- Regime tributário atual (PF ou PJ; se PJ, lucro real ou presumido)
- Estado de localização (para mapear ICMS atual com diferimentos estaduais)

### 2. Apuração da carga tributária atual

Calcular em Python a carga atual de:

**ICMS:**
- Verificar diferimentos estaduais aplicáveis (ex: ICMS diferido na saída de soja em GO)
- Créditos acumulados de exportação
- Carga efetiva considerando diferimentos e isenções estaduais

**PIS/COFINS:**
- Se PF: não incide (produtor PF está fora)
- Se PJ lucro real: não-cumulativo com créditos presumidos (Lei 10.925/04)
- Se PJ lucro presumido: cumulativo (0,65% + 3%)

**Carga total atual:**
```
carga_atual = icms_efetivo + pis_cofins_efetivo
carga_atual_percentual = carga_atual / receita_bruta
```

### 3. Projeção da carga com IBS/CBS

Calcular em Python com base na legislação mais recente:

```
# Alíquota de referência IBS/CBS (pesquisar valor atualizado)
# Redução para produtos agropecuários (verificar percentual de redução aprovado)
# Diferimento na aquisição de insumos (verificar regra vigente)

# Créditos de IBS/CBS sobre insumos
creditos_insumos = valor_insumos * aliquota_ibs_cbs_insumos

# Débitos de IBS/CBS sobre vendas
debitos_vendas_internas = receita_mercado_interno * aliquota_ibs_cbs_agro
debitos_exportacao = 0  # Exportação imune

# Saldo
saldo_ibs_cbs = debitos_vendas_internas - creditos_insumos

# Se saldo negativo: crédito acumulado (verificar regra de ressarcimento)
```

### 4. Análise do diferimento de insumos

Detalhar o impacto do diferimento:
- Quais insumos se enquadram no diferimento
- Impacto no fluxo de caixa (pagamento do imposto é postergado para quando?)
- Diferença entre diferimento e isenção (no diferimento, o imposto é devido, apenas pago depois)
- Impacto na tomada de créditos pelo adquirente dos produtos agropecuários

### 5. Regime específico do produtor rural PF

Avaliar:
- Limite de receita para o regime simplificado do produtor PF
- Obrigações acessórias no novo regime
- Crédito presumido concedido ao adquirente quando compra de produtor PF
- Comparação: vale mais manter PF no regime simplificado ou migrar para PJ no regime geral?

### 6. Período de transição

Mapear a transição:
- 2026-2028: CBS em fase de teste/calibragem
- 2027-2028: IBS começa a ser cobrado gradualmente
- 2029-2032: redução progressiva de ICMS e ISS com aumento correspondente de IBS
- 2033: extinção de ICMS e ISS; IBS/CBS plenos

Avaliar o impacto em cada ano da transição para a operação específica do cliente.

### 7. Quadro comparativo

| Elemento | Carga Atual | Carga Projetada (IBS/CBS) | Diferença |
|----------|-------------|---------------------------|-----------|
| Tributos sobre vendas internas | R$ | R$ | R$ |
| Tributos sobre exportação | R$ | R$ 0 (imune) | R$ |
| Créditos sobre insumos | R$ | R$ | R$ |
| Carga líquida | R$ | R$ | R$ |
| Carga efetiva (% sobre receita) | % | % | |

### 8. Análise de sensibilidade

Rodar cenários com:
- Alíquota de referência +/- 2 pontos percentuais
- Variação no percentual de exportação (20%, 50%, 80%)
- Com e sem diferimento de insumos
- PF no regime simplificado vs PJ no regime geral

### 9. Recomendação

Posicionar-se sobre:
- Se a reforma beneficia ou prejudica a operação específica do cliente
- Ações preparatórias recomendadas durante a transição
- Se há incentivo tributário para reorganizar a estrutura (PF→PJ ou vice-versa) antes da plena vigência
- Cronograma de acompanhamento regulatório

## Regras

1. **Sempre pesquisar a legislação atualizada** antes de qualquer cálculo — a reforma está em regulamentação.
2. Todo cálculo em Python com prova real.
3. Separar claramente o que é norma vigente do que é projeção.
4. A análise de sensibilidade com variação de alíquota é obrigatória.
5. Se o cliente opera em mais de um estado, considerar o impacto da transição para o princípio do destino.

## Referência legislativa

Consultar `ref-funrural-ibs.md` para dispositivos da reforma tributária e alíquotas projetadas.
