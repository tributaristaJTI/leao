---
name: "mod-funrural"
description: "Módulo de simulação dos regimes de apuração do Funrural. Use SEMPRE que o usuário mencionar Funrural, contribuição previdenciária rural, sub-rogação, receita bruta versus folha, SENAR, RAT rural, alíquota Funrural PF, Funrural PJ, opção anual Funrural, comercialização de produção rural, retenção na nota, ou qualquer variação de análise sobre regimes de recolhimento da contribuição previdenciária do produtor rural."
---

# Módulo Simulação Funrural

Módulo que compara os regimes de apuração do Funrural (sobre receita bruta vs sobre folha de pagamento), simula o impacto na cadeia de comercialização e avalia a melhor opção para cada perfil de produtor.

## Escopo

- Funrural PF sobre receita bruta (1,5%: 1,2% INSS + 0,1% RAT + 0,2% SENAR)
- Funrural PJ sobre receita bruta (2,05%: 1,7% INSS + 0,1% RAT + 0,25% SENAR)
- Opção pela contribuição sobre folha de pagamento (20% patronal + RAT + terceiros)
- Sub-rogação do adquirente (retenção na nota fiscal)
- Prazo e forma de opção anual
- Impacto na cadeia: venda para cooperativa, trading, indústria, exportação
- Constitucionalidade pós-STF (RE 718.874 e RE 363.852)
- Interação com a reforma tributária (transição)

## Fluxo analítico

### 1. Mapeamento da operação

Coletar:
- Receita bruta anual de comercialização da produção rural
- Número de empregados rurais
- Folha de pagamento mensal e anual (incluindo encargos)
- Tipo de produção (lavoura, pecuária, ambos)
- Canais de comercialização (cooperativa, trading, indústria, exportação direta)
- Regime atual de recolhimento (receita ou folha)

### 2. Simulação — Regime sobre Receita Bruta

Calcular em Python:

**Produtor PF:**
```
funrural_receita_pf = receita_bruta * 0.015
# Detalhamento:
inss_pf = receita_bruta * 0.012
rat_pf = receita_bruta * 0.001
senar_pf = receita_bruta * 0.002
```

**Produtor PJ (agroindústria/empresa rural):**
```
funrural_receita_pj = receita_bruta * 0.0205
# Detalhamento:
inss_pj = receita_bruta * 0.017
rat_pj = receita_bruta * 0.001
senar_pj = receita_bruta * 0.0025
```

### 3. Simulação — Regime sobre Folha de Pagamento

Calcular em Python:

```
# Contribuição patronal: 20% sobre folha
patronal = folha_anual * 0.20

# RAT (ajustar conforme grau de risco da atividade — 1%, 2% ou 3%)
# Atividade rural: geralmente grau médio (2%)
rat_folha = folha_anual * rat_percentual

# Terceiros (INCRA, SENAR, Salário-Educação, etc.)
# Calcular conforme código FPAS da atividade
terceiros = folha_anual * aliquota_terceiros

total_folha = patronal + rat_folha + terceiros
```

### 4. Análise do ponto de equilíbrio

Identificar a partir de qual relação receita/folha cada regime é mais vantajoso:

```
# Ponto de equilíbrio PF:
# Receita × 1,5% = Folha × (20% + RAT + terceiros)
# Receita / Folha = (20% + RAT + terceiros) / 1,5%
```

Se a relação receita/folha for superior ao ponto de equilíbrio, a folha é mais barata. Se inferior, a receita é mais barata.

### 5. Análise da sub-rogação

Explicar o impacto prático:
- Na venda para PJ (cooperativa, trading, indústria): o adquirente retém o Funrural na nota e recolhe. O produtor recebe o valor líquido.
- Na exportação direta: não há sub-rogação — o produtor recolhe.
- Na venda para PF: não há sub-rogação — o produtor recolhe.

Avaliar se a forma de comercialização impacta a decisão entre regimes.

### 6. Análise de sensibilidade

Rodar cenários com:
- Variação de receita (safra cheia vs safra frustrada: +30% e -30%)
- Variação de folha (contratação sazonal, mecanização)
- Cenário de expansão (mais área, mais receita, mesma equipe)
- Cenário de intensificação (mesma área, mais insumos e mão de obra)

### 7. Aspectos jurídicos relevantes

**Constitucionalidade:**
- RE 718.874 (STF, 2017): reconheceu a constitucionalidade do Funrural PF sobre receita bruta
- RE 363.852 (STF, 2010): havia declarado a inconstitucionalidade, depois superado pelo RE 718.874
- Discussão sobre a exigibilidade para períodos anteriores à Lei 10.256/2001

**Opção anual:**
- A opção pelo regime sobre folha deve ser feita na competência de janeiro de cada ano
- Irretratável para o ano-calendário inteiro
- Formalização: primeiro recolhimento em GPS sobre folha na competência de janeiro

**Controvérsias ativas:**
- Incidência sobre receitas de exportação indireta (venda para trading que exporta)
- Base de cálculo: valor bruto da nota ou valor líquido de descontos comerciais
- Funrural sobre receita de arrendamento e parceria rural

### 8. Quadro comparativo

| Elemento | Sobre Receita | Sobre Folha | Diferença |
|----------|--------------|-------------|-----------|
| Valor anual | R$ | R$ | R$ |
| Carga efetiva (% sobre receita) | % | % | |
| Forma de recolhimento | Sub-rogação / GPS | GPS | |
| Complexidade operacional | Baixa | Média | |
| Sensibilidade à safra | Alta | Baixa | |
| Risco jurídico | Baixo | Baixo | |

### 9. Recomendação

Posicionar-se indicando:
- Qual regime é mais vantajoso no cenário-base
- Em quais cenários a equação muda
- Prazo para opção (janeiro do próximo exercício)
- Providências operacionais (comunicação ao contador, ajuste de GPS)

## Regras

1. Todo cálculo em Python com prova real.
2. Incluir o detalhamento (INSS + RAT + SENAR) — não só o total.
3. A análise de sensibilidade é obrigatória.
4. Verificar a constitucionalidade e controvérsias ativas via pesquisa web antes de emitir posicionamento.
5. Se o produtor opera como PF e PJ simultaneamente, articular com o módulo Comparativo PF × PJ.

## Referência legislativa

Alíquotas, códigos FPAS, dispositivos legais e prazos são conferidos no conector Jusratio ou na fonte oficial consolidada antes de entrar no cálculo ou no texto. O arquivo `ref-funrural-ibs.md` do projeto serve só como mapa de onde procurar; não vale como fonte.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.