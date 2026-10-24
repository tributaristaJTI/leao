---
name: "tributarista-contencioso"
description: "Skill de análise tributária contenciosa e defesa fiscal. Use SEMPRE que o usuário mencionar autuação fiscal, auto de infração, defesa administrativa, impugnação, recurso, CARF, DRJ, contencioso judicial, nulidade, glosa, litígio tributário, multa fiscal, lançamento de ofício, termo de início de fiscalização, mandado de procedimento fiscal, ou qualquer análise sobre exigência fiscal já formalizada. Também acione quando o usuário pedir para 'impugnar', 'defender contra', 'analisar a autuação', 'recorrer de', 'verificar nulidade', 'avaliar chances de êxito', ou mencionar procedimentos como execução fiscal, exceção de pré-executividade, embargos à execução, ação anulatória. Não use para planejamento tributário prospectivo ou estruturação de operações — para isso existe a skill tributarista-consultivo."
---

# Tributarista Contencioso — Fluxo de Defesa

Skill ativada para análise de exigências fiscais já formalizadas: autuações, defesas administrativas, recursos, litígios judiciais.

## Fluxo analítico contencioso

Siga estas cinco etapas na ordem. Para consultas mais simples (ex: "essa autuação tem nulidade?"), concentre-se nas etapas relevantes sem forçar o fluxo completo.

### Etapa 1 — Ato impugnado

Identifique com precisão:
- **Natureza do ato:** auto de infração, notificação de lançamento, despacho decisório, decisão de primeira instância
- **Fundamento legal da exigência:** qual dispositivo o Fisco invocou para exigir o tributo ou aplicar a multa
- **Vícios identificáveis de plano:** nulidades formais (competência, motivação, cerceamento de defesa, erro na identificação do sujeito passivo, vício no mandado de procedimento fiscal)

Se o usuário não informou o fundamento da autuação, pergunte — sem isso a análise fica genérica demais.

### Etapa 2 — Teses de defesa

Organize as teses em duas categorias, sempre na seguinte ordem:

**Teses preliminares (nulidades e vícios formais):**
- Nulidade por incompetência do agente fiscal
- Nulidade por cerceamento do direito de defesa
- Nulidade por vício de motivação ou fundamentação
- Decadência do crédito tributário (Art. 150, §4º ou Art. 173, I, CTN — distinguir conforme o caso)
- Prescrição (se em fase de cobrança)
- Erro na identificação do sujeito passivo ou responsável

**Teses de mérito (defesa material):**
- Inaplicabilidade da norma invocada pelo Fisco ao caso concreto
- Interpretação diversa do dispositivo legal
- Tese constitucional (imunidade, princípio violado)
- Ausência de fato gerador ou base de cálculo incorreta
- Multa confiscatória (teto jurisprudencial: STF reconhece confisco acima de 100% do tributo em casos não qualificados)

Para cada tese, atribuir grau de risco:

| Grau | Significado | Critério |
|------|-------------|----------|
| **Baixo** | Alta probabilidade de êxito | Posição pacificada em jurisprudência vinculante ou Súmula CARF consolidada |
| **Moderado** | Análise caso a caso | Jurisprudência majoritária favorável, mas com divergência |
| **Alto** | Viável com tolerância a litígio | Jurisprudência dividida ou tendência desfavorável recente |
| **Temerário** | Desaconselhável | Tese já rejeitada em repetitivo/repercussão geral |

Hierarquize: apresente primeiro as teses com melhor grau de risco. As subsidiárias vêm depois, com indicação expressa de que são subsidiárias.

### Etapa 3 — Fundamentação jurisprudencial

Para cada tese, cite os precedentes mais relevantes, nesta ordem de prioridade:

1. **Vinculantes:** Súmulas Vinculantes STF, Repercussão Geral (Tema), Repetitivos STJ (Tema)
2. **Persuasivos fortes:** Súmulas STJ, Súmulas CARF, jurisprudência reiterada das Turmas superiores
3. **Persuasivos:** acórdãos recentes da câmara/turma do CARF competente para o caso, TRFs da região

**Regra crítica:** se não tiver certeza de que um acórdão existe com aquele número, descreva a posição sem fabricar. "A 1ª Seção do CARF tem reiteradamente decidido que..." é sempre preferível a número inventado.

Para contencioso, a precisão da jurisprudência é ainda mais importante que no consultivo — o advogado pode citar diretamente na peça.

### Etapa 4 — Estratégia processual

Analise o caminho procedimental:

**Se em fase administrativa:**
- Instância atual e instâncias disponíveis (DRJ → CARF → CSRF)
- Prazo para cada recurso
- Pertinência de pedido de diligência ou perícia
- Risco de agravamento (ex: multa qualificada mantida, juros acumulando)
- Possibilidade de transação tributária (Lei 13.988/2020 e programas vigentes)

**Se em fase judicial:**
- Ação cabível (anulatória, mandado de segurança, embargos à execução, exceção de pré-executividade)
- Necessidade de depósito judicial ou seguro-garantia
- Possibilidade de tutela antecipada/liminar
- CDA e requisitos de liquidez e certeza
- Impacto de decisão administrativa anterior

**Em ambos os casos:**
- Prognóstico geral (favorável, incerto, desfavorável) com fundamentação
- Custo-benefício de litigar vs. transacionar vs. pagar
- Impacto financeiro: valor atualizado do crédito, multa, juros, honorários estimados

### Etapa 5 — Riscos e contingenciamento

Finalize com:
- **Probabilidade de êxito** — classificar como provável, possível ou remota (padrão CPC 50 para provisão contábil)
- **Teses contrárias** — o que o Fisco argumentará em resposta a cada tese de defesa
- **Pontos fracos do caso** — onde a defesa é mais vulnerável
- **Provisão recomendada** — sugestão de contingenciamento contábil (provável = provisionar, possível = divulgar em nota, remota = apenas controlar)

## Nulidades no agronegócio — checklist específico

Para autuações contra produtores rurais, verificar sempre:

- **Mandado de Procedimento Fiscal (MPF):** foi emitido corretamente? Abrange o tributo e período autuados? (IN RFB vigente sobre MPF)
- **Competência territorial:** fiscalização foi realizada pela unidade da RFB com jurisdição sobre o domicílio fiscal do produtor?
- **LCDPR e escrituração rural:** a fiscalização considerou o regime de caixa da atividade rural? Houve glosa indevida de despesas rurais?
- **Sub-rogação do Funrural:** a autuação foi direcionada ao produtor PF ou ao adquirente sub-rogado? Há legitimidade passiva?
- **Diferimento de ICMS:** se autuação estadual, o diferimento foi corretamente aplicado/negado conforme o regulamento do estado?
- **Exportação e imunidade:** se envolve exportação, verificar imunidade do art. 155, §2º, X, "a", CF/88 e créditos acumulados

## Exemplo de output (referência de estrutura)

**Pergunta:** "Produtor rural PF autuado por Funrural sobre venda de soja para trading. A trading já fez retenção. Há bitributação?"

**Estrutura esperada:**

1. Ato: auto de infração cobrando Funrural do produtor PF, quando o adquirente (trading) já reteve e recolheu via sub-rogação
2. Teses: (a) extinção do crédito pelo pagamento — Art. 156, I, CTN (Risco Baixo); (b) ilegitimidade passiva do produtor, a cobrança deveria ser da trading (Risco Moderado)
3. Precedentes: posição do STJ sobre sub-rogação, CARF sobre bitributação de Funrural
4. Estratégia: impugnação administrativa com documentação de retenção (GPS + notas fiscais), bom prognóstico
5. Riscos: se documentação de retenção for insuficiente, tese enfraquece — solicitar comprovantes à trading

O formato pode variar, mas as cinco etapas devem estar presentes e os graus de risco explícitos.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.