# Publicar · mod-comparativo-pf-pj

Origem: `skills/mod-comparativo-pf-pj/` no repositório tributaristaJTI/leao. Versão sincronizada de referência: atualizada na conta em 2026-04-06.

## 1. SKILL.md completa e final

`````markdown
---
name: mod-comparativo-pf-pj
description: "Módulo de comparação de carga tributária entre atividade rural como pessoa física e como pessoa jurídica. Use SEMPRE que o usuário mencionar comparativo PF PJ, pessoa física versus pessoa jurídica, constituir empresa rural, migrar para PJ, holding rural operacional, vantagem tributária PJ agro, regime tributário ideal para produtor rural, lucro real versus livro caixa, ou qualquer variação de análise sobre a conveniência de operar como PF ou PJ no agronegócio."
---

# Módulo Comparativo Carga Tributária PF × PJ

Módulo que simula a operação agrícola nos dois regimes (pessoa física e pessoa jurídica), comparando a carga tributária total e os custos operacionais de cada estrutura.

## Escopo

- IRPF rural (resultado via LCDPR) vs IRPJ (lucro real e lucro presumido)
- CSLL no regime PJ
- PIS/COFINS (cumulativo vs não-cumulativo; créditos presumidos na cadeia agro)
- Funrural PF vs contribuição previdenciária PJ
- Custos de manutenção da PJ (contabilidade, obrigações acessórias, escrituração)
- Impacto sucessório (transmissão de quotas vs transmissão de imóvel rural)
- Acesso a crédito rural por PJ
- Impacto na comercialização (venda direta, cooperativa, exportação)

## Fluxo analítico

### 1. Levantamento da operação atual

Coletar (ou extrair da conversa):
- Faturamento bruto anual por atividade (lavoura, pecuária, agroindústria)
- Custos e despesas dedutíveis (insumos, mão de obra, arrendamento, depreciação)
- Resultado líquido estimado da atividade rural
- Folha de pagamento (número de empregados, valor mensal)
- Patrimônio imobiliário rural (quantidade, valor, localização)
- Estrutura familiar (cônjuge, filhos, participações)

### 2. Simulação Cenário PF

Calcular em Python:

```
# IRPF Rural — Resultado via LCDPR
receita_bruta_pf = [valor]
despesas_dedutiveis_pf = [valor]
resultado_rural = receita_bruta_pf - despesas_dedutiveis_pf
# Resultado rural compõe a base de cálculo do IRPF junto com outras rendas
# Aplicar tabela progressiva do IRPF (7,5% a 27,5%)

# Funrural PF — 1,5% sobre receita bruta de comercialização
# (1,2% INSS + 0,1% RAT + 0,2% SENAR)
funrural_pf = receita_bruta_pf * 0.015

# Contribuição sindical e outras obrigações PF
```

### 3. Simulação Cenário PJ — Lucro Real

Calcular em Python:

```
# IRPJ — 15% sobre lucro real + adicional de 10% sobre o que exceder R$ 240.000/ano
# CSLL — 9% sobre o lucro real
# PIS — 1,65% não-cumulativo (com créditos)
# COFINS — 7,6% não-cumulativo (com créditos)
# Créditos presumidos na aquisição de insumos agropecuários (Lei 10.925/04)

# Contribuição previdenciária PJ:
# Opção 1: sobre folha (20% patronal + RAT + terceiros)
# Opção 2: sobre receita bruta (CPRB) — verificar se atividade agro se enquadra

# Custos operacionais PJ:
# Contabilidade mensal estimada
# Obrigações acessórias (SPED, ECD, ECF, EFD-Contribuições)
# Certidões, alvarás, taxas
```

### 4. Simulação Cenário PJ — Lucro Presumido

Calcular em Python:

```
# Base presumida para atividade rural:
# Venda de mercadorias (soja, milho, gado): 8% da receita bruta
# Prestação de serviços (se houver): 32% da receita bruta
# IRPJ: 15% sobre base presumida + adicional 10%
# CSLL: 9% sobre base presumida (12% ou 32% conforme atividade)
# PIS: 0,65% cumulativo (sem créditos)
# COFINS: 3% cumulativo (sem créditos)
```

### 5. Quadro comparativo consolidado

Montar tabela com:

| Tributo/Custo | PF (LCDPR) | PJ Lucro Real | PJ Lucro Presumido |
|---------------|-----------|---------------|---------------------|
| IRPF/IRPJ | | | |
| CSLL | — | | |
| PIS | — | | |
| COFINS | — | | |
| Funrural / Previdenciária | | | |
| Custos operacionais | | | |
| **Carga total** | | | |
| **Carga efetiva (% sobre receita)** | | | |

### 6. Análise de variáveis não tributárias

Além da carga tributária pura, avaliar:

**Vantagens da PJ:**
- Limitação de responsabilidade patrimonial
- Acesso a linhas de crédito rural para PJ (em alguns casos, condições melhores)
- Facilidade na entrada de sócios e investidores
- Planejamento sucessório via transmissão de quotas (ITCMD sobre valor contábil vs valor de mercado)
- Possibilidade de distribuição de lucros isenta

**Desvantagens da PJ:**
- Custo fixo de manutenção (contabilidade, obrigações acessórias)
- Impossibilidade de usar o resultado negativo (prejuízo) da atividade rural para compensar outras rendas PF
- Tributação na saída (integralização de imóveis pode gerar ganho de capital)
- Complexidade na gestão de múltiplos CNPJs
- ITBI na transferência de imóveis para a PJ

### 7. Análise de sensibilidade

Rodar os cenários com variações de:
- Faturamento (+20% e -20%)
- Margem de lucro (+10 p.p. e -10 p.p.)
- Cenário de safra cheia vs safra frustrada

Isso mostra em qual faixa de faturamento/margem cada regime é mais vantajoso.

### 8. Recomendação

Posicionar-se com clareza:
- Qual regime é mais vantajoso no cenário-base
- A partir de qual faturamento/margem a equação muda
- Custo de transição (ITBI, contabilidade, reorganização contratual)
- Cronograma de implementação recomendado
- Riscos de cada caminho

## Premissas que devem ser explicitadas

Toda simulação deve listar as premissas adotadas:
- Alíquotas vigentes na data da análise
- Presunção de que os custos informados são dedutíveis
- Cotação da soja utilizada para tradução (se aplicável)
- Se houve consideração de créditos presumidos de PIS/COFINS
- Se houve consideração de incentivos estaduais (ICMS diferido, etc.)

## Regras

1. Todo cálculo em Python com três camadas de segurança.
2. Nunca comparar apenas a alíquota nominal — comparar a carga efetiva total.
3. Incluir custos operacionais da PJ na comparação (contabilidade, obrigações acessórias).
4. A análise de sensibilidade é obrigatória — um cenário único é insuficiente.
5. Se o caso envolver grupo econômico, articular com o módulo de Grupo Econômico.

## Referência legislativa

Tabelas de IRPF e IRPJ, alíquotas de Funrural e contribuições previdenciárias, dispositivos e prazos são conferidos no conector Jusratio ou na fonte oficial consolidada antes de entrar no cálculo ou no texto. Os arquivos `ref-ir-rural.md` e `ref-funrural-ibs.md` do projeto servem só como mapa de onde procurar; não valem como fonte.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
`````

## 2. O que mudou desde a versão sincronizada

A seção "Referência legislativa" deixa de mandar ler o(s) arquivo(s) `ref-*.md` do projeto como fonte: agora manda conferir no Jusratio ou na fonte oficial consolidada, e os arquivos ficam só como mapa de onde procurar (decisão 1).
Arquivos-mapa: `ref-ir-rural.md` e `ref-funrural-ibs.md`.
Nova seção final "Conferência de citação", com texto idêntico nas 22 skills que citam norma ou julgado (laudo de 03/10, decisão 3).
O que não for conferido fica fora ou marcado [A CONFERIR: fonte].
Regras de cálculo e fluxo intocados.
