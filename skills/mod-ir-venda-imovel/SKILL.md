---
name: mod-ir-venda-imovel
description: "Módulo de apuração de IR sobre ganho de capital na alienação de imóveis rurais por pessoa física. Use SEMPRE que o usuário mencionar venda de fazenda, alienação de imóvel rural, ganho de capital rural, GCap, VTN, DIAT, fatores de redução, custo de aquisição de imóvel rural, benfeitorias em imóvel rural, ou qualquer variação de apuração de imposto na venda de terra. Também acione para consultas sobre isenções (pequeno valor, único imóvel, reinvestimento em 180 dias), regime do VTN vs contratual, ou retificação de DITR para otimizar VTN."
---

# Módulo IR na Venda de Imóvel Rural

Módulo especializado na apuração de Imposto de Renda sobre Ganho de Capital (IR-GCap) na alienação de imóveis rurais por pessoa física. Substitui e amplia o antigo agente IR-GCap.

## Escopo

- Ganho de capital PF na alienação de imóveis rurais
- Regime do VTN (Art. 19 da Lei 9.393/96) vs regime contratual
- Tratamento de benfeitorias (deduzidas e não deduzidas no LCDPR)
- Fatores de redução FR1 e FR2 (Lei 11.196/2005)
- Reduções para imóveis adquiridos antes de 1988 (Lei 7.713/88)
- Isenções legais (pequeno valor, único imóvel, reinvestimento em 180 dias)
- Alíquotas progressivas (15% a 22,5% — Lei 8.981/95)
- Imóveis adquiridos antes de 01/01/1997 (regime híbrido)
- Imóveis em condomínio ou composse
- Retificação de DITR para otimização do VTN

## Fluxo analítico

### 1. Enquadramento do regime

Determinar qual regime se aplica ao caso:

| Data de aquisição | Regime | Fundamento |
|-------------------|--------|------------|
| Até 31/12/1996 | Híbrido (VTN para terra nua + valor contratual para benfeitorias) | Art. 19, parágrafo único, Lei 9.393/96 |
| A partir de 01/01/1997 | VTN integral (terra nua E benfeitorias pelo VTN) | Art. 19, caput, Lei 9.393/96 |

**Atenção especial:** imóveis adquiridos em 1996 (sem VTN declarado e sem possibilidade de correção monetária — "limbo legal"). Alertar o advogado e recomendar estratégia defensiva.

### 2. Apuração do custo de aquisição

```
Custo de aquisição = VTN na data da aquisição (conforme DIAT)
(+) Benfeitorias NÃO deduzidas no LCDPR (com documentação)
(=) Custo total de aquisição
```

**Regras de benfeitorias:**
- Benfeitorias deduzidas no LCDPR como despesa da atividade rural: NÃO entram no custo de aquisição (já foram abatidas do IR)
- Benfeitorias não deduzidas com notas fiscais: entram no custo
- Benfeitorias sem documentação: não podem ser computadas — alertar o advogado sobre o risco
- Benfeitorias deduzidas no LCDPR serão tributadas como receita da atividade rural (até 27,5%) quando da alienação — calcular esse impacto separadamente

### 3. Apuração do valor de alienação

- No regime VTN: usar o VTN constante da DIAT do ano da alienação (ou do ano anterior, se a alienação ocorrer antes da entrega da DITR do exercício)
- No regime contratual: usar o valor efetivo da transação

### 4. Cálculo do ganho de capital

```
Ganho bruto = Valor de alienação - Custo total de aquisição
```

### 5. Aplicação dos fatores de redução

**FR1 (Lei 11.196/2005, Art. 40, I):**
```
FR1 = 1 / (1,0060 ^ n1)
n1 = número de meses entre a data de aquisição e novembro/2005
```

**FR2 (Lei 11.196/2005, Art. 40, II):**
```
FR2 = 1 / (1,0035 ^ n2)
n2 = número de meses entre dezembro/2005 e a data de alienação
```

**Reduções adicionais para imóveis adquiridos até 1988:**
Aplicar percentual de redução conforme tabela do Art. 18 da Lei 7.713/88 (5% por ano de aquisição, de 1969 a 1988).

```
Ganho de capital tributável = Ganho bruto × FR1 × FR2 × (1 - percentual Lei 7.713)
```

### 6. Cálculo do IR devido

Aplicar alíquotas progressivas sobre o ganho de capital tributável:

| Faixa do ganho de capital | Alíquota |
|---------------------------|----------|
| Até R$ 5.000.000,00 | 15% |
| De R$ 5.000.000,01 a R$ 10.000.000,00 | 17,5% |
| De R$ 10.000.000,01 a R$ 30.000.000,00 | 20% |
| Acima de R$ 30.000.000,00 | 22,5% |

### 7. Verificação de isenções

Antes de apresentar o resultado, verificar se o caso se enquadra em alguma isenção:

- **Pequeno valor:** alienação por valor igual ou inferior a R$ 35.000,00 no mês (verificar se é por bem ou por conjunto)
- **Único imóvel:** alienação de único imóvel por valor igual ou inferior a R$ 440.000,00, desde que não tenha realizado outra alienação nos últimos 5 anos
- **Reinvestimento residencial:** aplicação do produto da venda na aquisição de imóvel residencial em 180 dias (atenção: discutível para imóvel RURAL — alertar sobre a controvérsia)

### 8. Cenários obrigatórios

Toda análise deve apresentar no mínimo dois cenários comparativos:

**Cenário VTN:** usando valores de terra nua do DIAT (aquisição e alienação)
**Cenário Contratual:** usando valores efetivos do contrato de compra e venda

Se aplicável, incluir cenários adicionais:
- Com e sem benfeitorias documentadas
- Com retificação de DITR (quando o VTN declarado estiver defasado)
- Com segregação de áreas (quando parte do imóvel tiver data de aquisição diferente)

### 9. Alertas automáticos

Em TODA análise, verificar e reportar:

**Crítico (exige ação imediata):**
- Imóvel adquirido em 1996 (limbo legal)
- Ausência total de DIAT nos anos de aquisição E alienação
- Benfeitorias > 50% do valor de venda sem documentação
- Prazo decadencial < 6 meses
- Autuação fiscal em curso

**Atenção (exige cuidado):**
- VTN declarado < 70% do valor SIPT (risco de arbitramento)
- Inconsistência entre valor no IRPF e na DITR
- Benfeitorias com documentação parcial
- Laudos de avaliação sem conformidade com NBR 14653-3

**Oportunidade (potencial de economia):**
- Economia pelo VTN > R$ 100.000
- Fatores de redução aplicáveis (imóvel anterior a 1988)
- Benfeitorias não deduzidas significativas com documentação
- Possibilidade de retificação de DITR para otimizar VTN de aquisição

## Regras de cálculo

1. Todo cálculo em Python. Jamais inline.
2. Variáveis em português com nomes descritivos.
3. Prova real obrigatória: inverter o cálculo e conferir.
4. Mostrar cada etapa separadamente — o advogado precisa conferir variável por variável.
5. Arredondar valores finais para centavos (2 casas decimais). Manter precisão máxima nos fatores de redução (4 casas).

## Referência legislativa

Alíquotas, fatores de redução, dispositivos legais e prazos são conferidos no conector Jusratio ou na fonte oficial consolidada antes de entrar no cálculo ou no texto. O arquivo `ref-ir-rural.md` do projeto serve só como mapa de onde procurar (quais tabelas, alíquotas e dispositivos conferir); não vale como fonte.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
