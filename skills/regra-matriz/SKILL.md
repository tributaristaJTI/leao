---
name: "regra-matriz"
description: "Skill de decomposição de normas tributárias pela Regra-Matriz de Incidência Tributária (RMIT) e pelo Percurso Gerativo de Sentido (S1→S4) de Paulo de Barros Carvalho. Use SEMPRE que o usuário pedir para 'decompor', 'analisar pela regra-matriz', 'montar a RMIT', 'qual a regra-matriz de', 'quais os critérios de incidência', 'analisar o fato gerador', 'decomposição normativa', ou qualquer variação de análise estrutural de norma tributária usando o método PBC. Também acione quando o usuário mencionar 'S1', 'S2', 'S3', 'S4', 'percurso gerativo de sentido', 'planos interpretativos', ou pedir para 'interpretar o artigo X pela RMIT'. Acione tanto para análise de dispositivos legais isolados ('decomponha o art. 138 da LC 214') quanto para operações concretas ('monte a regra-matriz da venda de soja por produtor PF para trading exportadora'). Não use para análises tributárias genéricas que não exijam decomposição estrutural — para isso existem as skills tributarista-consultivo e tributarista-contencioso."
---

# Regra-Matriz de Incidência Tributária — Método Interpretativo Completo

Skill de análise estrutural de normas tributárias combinando a **Regra-Matriz de Incidência Tributária (RMIT)** com o **Percurso Gerativo de Sentido (S1→S4)**, ambos desenvolvidos por Paulo de Barros Carvalho. O método transforma texto legal em norma jurídica construída, decomposta e testada sistematicamente.

## Fundamento teórico

A RMIT não é um mero esquema classificatório — é um instrumento epistemológico que exige percurso interpretativo prévio. A norma não está "no" texto; ela é *construída a partir dele* pelo intérprete. O percurso gerativo de sentido (S1→S4) é o caminho obrigatório dessa construção. A RMIT (montada no plano S3) só tem rigor se precedida pela coleta literal (S1) e pela decomposição semântica (S2), e só tem validade se testada sistemicamente (S4).

Referência doutrinária central: CARVALHO, Paulo de Barros. *Curso de Direito Tributário*. São Paulo: Saraiva (diversas edições); *Direito Tributário, Linguagem e Método*. São Paulo: Noeses; *Regra-Matriz de Incidência Tributária: Da Teoria à Prática*. São Paulo: Noeses, 2021. Complementar: CARVALHO, Aurora Tomazini de. *Curso de Teoria Geral do Direito: o constructivismo lógico-semântico*. São Paulo: Noeses.

---

## Passo zero — Detecção de input e calibragem de contexto

### Tipo de input

Ao receber o pedido, identifique se o input é:

**(A) Dispositivo legal** — o usuário pede para decompor um artigo, parágrafo ou conjunto de dispositivos específicos. Exemplo: "Decomponha o art. 5º, §1º da LC 214/2025."
- Neste caso, o percurso começa em S1 com a transcrição literal dos enunciados.

**(B) Operação concreta** — o usuário descreve uma situação fática e pede a regra-matriz aplicável. Exemplo: "Produtor PF vende soja para cooperativa em Goiás — monte a RMIT."
- Neste caso, o percurso começa pela identificação dos dispositivos que incidem sobre a operação (um S1 reverso: da operação ao texto), e depois segue normalmente S1→S4.

Se o input for ambíguo, pergunte: "Você quer que eu decomponha um dispositivo específico ou que eu monte a regra-matriz de uma operação concreta?"

### Contexto de uso

Antes de iniciar a análise, pergunte uma única vez:

> **Qual o contexto de uso desta análise?**
> (a) **Parecer / análise interna** — output técnico denso, com citações completas e fundamentação para uso profissional.
> (b) **Material didático** — output com explicação de cada etapa do método, linguagem acessível para alunos ou público não-especializado (IBET, AGET, Sindicato Rural).

A resposta calibra o tom, a profundidade explicativa e o nível de citação em todo o output.

---

## Percurso analítico: S1 → S2 → S3 → S4 → Alertas

O output SEMPRE apresenta explicitamente os quatro planos como seções, nesta ordem. Cada plano é uma seção com cabeçalho próprio.

---

### S1 — Plano da Literalidade Textual

**O que é:** Coleta dos enunciados prescritivos relevantes no plano da expressão — o texto bruto da lei.

**O que fazer:**

1. Transcrever literalmente os dispositivos centrais aplicáveis (artigo, parágrafos, incisos, alíneas).
2. Identificar e transcrever dispositivos conectados por remissão (o art. X que remete ao art. Y — ambos devem estar aqui).
3. Identificar definições legais relevantes em outros pontos do mesmo diploma ou em legislação complementar (ex: definição de "fornecimento" no art. 4º da LC 214/2025, definição de "produtor rural" nos arts. 164-165).
4. Quando o input for operação concreta (tipo B), listar primeiro quais dispositivos incidem sobre a operação, com justificativa breve, e então transcrever.

**Fontes primárias para coleta de S1:**
- EC 132/2023 (normas constitucionais)
- LC 214/2025 (IBS/CBS/IS — lei geral)
- LC 227/2026 (CG-IBS, processos, ITCMD, alterações da LC 214)
- Decreto nº 12.955/2026 — RCBS (regulamento CBS: Livro I = normas comuns IBS/CBS, 620 artigos + 5 anexos)
- Resolução CGIBS nº 6/2026 (regulamento IBS: espelha Livro I do RCBS + Livro II com normas IBS-específicas)
- LC 224/2025 (incentivos fiscais, impacto na cadeia de insumos agro)
- Legislação estadual (CTE-GO, RCTE-GO quando aplicável a ICMS)

**Regra:** Pesquisar no project knowledge (LC 214/2025 e RCBS) antes de transcrever. Se o dispositivo não puder ser confirmado no texto primário disponível, sinalizar expressamente com o marcador "[A CONFERIR: fonte]".

**Formato para contexto parecer:** Transcrição direta com citação completa (art. X, §Y, inciso Z, da LC 214/2025).
**Formato para contexto didático:** Transcrição com destaque visual dos termos-chave que serão decompostos em S2.

---

### S2 — Plano das Significações

**O que é:** Atribuição de conteúdo semântico aos termos-chave dos enunciados coletados em S1. Aqui o intérprete constrói o sentido — a norma começa a emergir.

**O que fazer:**

1. Identificar os termos juridicamente relevantes nos enunciados de S1 (verbos nucleares, sujeitos, complementos, condicionantes).
2. Para cada termo-chave, atribuir significação técnica com base em:
   - Definição legal expressa (quando existir no próprio diploma)
   - Conceito doutrinário consolidado (PBC, Aurora Tomazini, Roque Carrazza)
   - Conceito setorial específico (ex: "produtor rural" no direito tributário do agro tem contorno próprio)
3. **Sinalizar polissemia ou ambiguidade** — quando o mesmo termo admite mais de uma significação plausível, mapear as alternativas. Isso é crítico: muitas controvérsias tributárias nascem em S2, não em S3.
4. **Distinguir conceitos de direito privado absorvidos pelo direito tributário** de conceitos autônomos criados pela legislação tributária (art. 109 e 110 do CTN).

**Exemplo de decomposição S2:**
- "fornecer" (art. 4º, LC 214/2025) → verbo nuclear que abrange bens corpóreos e incorpóreos, serviços, direitos — conceito mais amplo que "venda" ou "prestação de serviço" isoladamente
- "operação onerosa" → exige contraprestação; exclui doações e operações gratuitas (salvo equiparações legais)
- "produtor rural pessoa física" (arts. 164-165, LC 214/2025) → sujeito com regime específico; a qualificação depende de thresholds de receita e número de propriedades

**Formato para contexto parecer:** Glossário analítico com fundamentação legal/doutrinária por termo.
**Formato para contexto didático:** Decomposição explicativa com exemplos do agro para ilustrar cada conceito ("quando o produtor vende soja, o 'fornecimento' é a tradição do bem corpóreo mediante preço").

---

### S3 — Plano das Significações Normativas Articuladas (RMIT)

**O que é:** Organização das significações construídas em S2 na estrutura lógica do juízo hipotético condicional: SE [antecedente] → ENTÃO [consequente]. É aqui que se monta a Regra-Matriz de Incidência Tributária propriamente dita.

**O que fazer:**

Montar a RMIT nos cinco critérios, usando as significações de S2:

#### ANTECEDENTE (Hipótese de incidência)

**Critério material** — O núcleo da hipótese: verbo + complemento.
- Identificar a conduta tributável descrita na norma.
- Formular como ação: "fornecer bens mediante contraprestação", "importar bens do exterior", "fornecer operação onerosa com bem imóvel".
- Importante: o critério material confirma ou infirma a base de cálculo (teste de Paulo de Barros — se houver descompasso entre critério material e base de cálculo, há vício na norma).

**Critério espacial** — Onde o fato deve ocorrer para que a norma incida.
- No IBS/CBS, atenção especial: o princípio do destino (art. 11, LC 214/2025) desloca o critério espacial da origem para o local de entrega/consumo.
- Identificar regras especiais de localização por tipo de operação (bens corpóreos, serviços, operações digitais, imóveis).

**Critério temporal** — Quando se considera ocorrido o fato jurídico tributário.
- Momento em que nasce a obrigação tributária.
- Atenção a diferimentos (art. 138, LC 214/2025 para insumos agro) — o diferimento desloca o critério temporal, não o elimina.

#### CONSEQUENTE (Prescrição)

**Critério subjetivo** — Quem são os sujeitos da relação jurídica tributária.
- **Sujeito ativo:** quem tem direito ao crédito tributário (União para CBS; estados/municípios para IBS via CG-IBS).
- **Sujeito passivo:** contribuinte (quem realiza o fato gerador) e responsável tributário (terceiro obrigado por lei — ex: sub-rogação no split payment).
- No agro: distinguir produtor PF contribuinte regular vs. produtor PF não-contribuinte com crédito presumido ao adquirente.

**Critério quantitativo** — Quanto é devido.
- **Base de cálculo:** valor da operação (receita bruta, valor da importação, valor do imóvel). Confirmar coerência com critério material.
- **Alíquota:** padrão, reduzida (60% ou 100%), ou zero. Especificar se a redução é vinculada ao produto/operação (objetiva) ou ao sujeito (subjetiva) — no IBS/CBS, a redução é objetiva (vinculada ao produto/operação, não à identidade do contribuinte).

**Formato de apresentação — sempre usar esta estrutura:**

```
REGRA-MATRIZ DE INCIDÊNCIA — [TRIBUTO] — [OPERAÇÃO]

ANTECEDENTE (SE)
├── Critério material: [verbo + complemento]
├── Critério espacial: [local de incidência + fundamento]
└── Critério temporal: [momento do fato gerador + fundamento]

CONSEQUENTE (ENTÃO)
├── Critério subjetivo
│   ├── Sujeito ativo: [quem]
│   └── Sujeito passivo: [contribuinte / responsável]
└── Critério quantitativo
    ├── Base de cálculo: [grandeza + fundamento]
    └── Alíquota: [percentual + fundamento + tipo de redução se aplicável]
```

**Formato para contexto didático:** Além do quadro acima, incluir uma explicação narrativa de cada critério com exemplo concreto da operação analisada.

**Quando a operação gerar mais de uma RMIT** (exemplo: arrendamento com pagamento in natura gera a RMIT da locação imobiliária + a RMIT da dação em pagamento da commodity), montar cada uma separadamente e identificar a autonomia dos fatos geradores.

---

### S4 — Plano da Sistematização

**O que é:** Teste da norma construída (S3) contra o sistema jurídico. Vínculos de coordenação e subordinação com outras normas — hierarquia constitucional, normas de isenção/imunidade que mutilam a RMIT, regimes especiais que a modificam, antinomias.

**O que fazer:**

1. **Teste constitucional** — A RMIT construída respeita os limites constitucionais?
   - Competência tributária (art. 156-A CF para IBS; art. 195, V CF para CBS)
   - Princípios: legalidade, anterioridade, irretroatividade, não-confisco, capacidade contributiva, neutralidade
   - Imunidades aplicáveis (exportação, entidades imunes, cesta básica)

2. **Normas de mutilação** — Identificar normas que parcialmente retiram eficácia da RMIT:
   - Isenções (zero-rating no Anexo XV)
   - Reduções de alíquota (Anexo IX — 60% para insumos agro)
   - Imunidades (exportações — art. 51, §2º, I)
   - Não-incidências qualificadas
   - Regimes de diferimento (art. 138 — posterga o critério temporal sem eliminar a RMIT)

3. **Regime especial/diferenciado** — A operação se enquadra em regime que modifica a RMIT padrão?
   - Produtor rural PF: arts. 164-170 LC 214 / arts. 238-249 RCBS
   - Operações imobiliárias: arts. 251-270 LC 214 / arts. 360-390 RCBS
   - Cooperativas: regime próprio para ato cooperativo
   - Simples Nacional / MEI: exclusão do IBS/CBS

4. **Antinomias e lacunas** — Há conflito entre a RMIT construída e outra norma do sistema? Há lacuna normativa?

5. **Controvérsias doutrinárias** — Onde há divergência interpretativa, mapear as correntes e indicar a posição mais defensável com fundamentação. Formato:
   - **Corrente A** (autor/fonte): [posição] — fundamento
   - **Corrente B** (autor/fonte): [posição] — fundamento
   - **Posição mais defensável:** [qual e por quê]
   - **Posição LA (Leonardo Amaral):** [quando houver posição consolidada — referenciar sempre]

**Formato para contexto parecer:** Análise densa com citações específicas de princípios, dispositivos constitucionais e legais, precedentes quando existentes.
**Formato para contexto didático:** Análise com provocações ("o que acontece se o produtor ultrapassar o limite de receita no meio do ano-calendário?") para estimular reflexão.

---

### Alertas Operacionais (pós-S4)

**O que é:** Camada complementar à RMIT ortodoxa. Ativada quando a análise revelar questões que o modelo clássico PBC não captura mas que têm impacto prático direto.

**Quando emitir alertas:**

Os alertas NÃO são obrigatórios em toda análise. Só devem ser emitidos quando a decomposição S1→S4 revelar pelo menos uma das seguintes situações:

- **Mecanismo de recolhimento** — split payment, retenção na fonte, ou regime especial de apuração que altera a dinâmica da obrigação tributária
- **Transição de regimes** — operação durante período de convivência (2026-2032) sujeita simultaneamente ao sistema antigo e ao novo
- **Creditamento e cadeia** — ruptura na cadeia de créditos, crédito presumido com calibragem pendente, risco de crédito irrecuperável
- **Obrigações acessórias** — documentação fiscal específica não coberta pela RMIT (modelo de nota fiscal, escrituração)
- **Regulamentação pendente** — critério da RMIT que depende de norma infralegal ainda não publicada
- **Impacto financeiro não-tributário** — diferimento ou regime especial com efeito relevante de fluxo de caixa que a análise normativa não captura

**Formato:**

```
⚠️ ALERTAS OPERACIONAIS

[Número]. [Título do alerta]
Descrição concisa. Fundamento legal quando aplicável. Recomendação prática.
```

---

## Regras gerais

1. **Pesquisar antes de afirmar.** Usar o project knowledge (LC 214/2025 e RCBS) para verificar dispositivos antes de citá-los. Quando não for possível confirmar, sinalizar com "⚠️ Verificar contra texto oficial."

2. **Não inventar dispositivos.** Se não souber o número exato do artigo/parágrafo, dizer que não sabe. Marcar "[A CONFERIR: fonte]" é infinitamente melhor que citar errado.

3. **Distinguir certeza de interpretação.** Em cada critério da RMIT, explicitar se o preenchimento decorre de (a) texto legal expresso, (b) interpretação doutrinária consolidada, ou (c) interpretação do analista sobre ponto controverso.

4. **Referenciar posições consolidadas do usuário (Posição LA).** Ao encontrar um ponto sobre o qual o knowledge base contém posição consolidada de Leonardo Amaral, referenciar como "Posição LA" em S4, mantendo neutralidade analítica — apresentar correntes e indicar a posição mais defensável, que pode ou não coincidir com a Posição LA.

5. **Cada RMIT é autônoma.** Se a operação gera múltiplos fatos geradores (ex: arrendamento com renda in natura), montar uma RMIT para cada. Não fundir.

6. **Self-review obrigatório.** Ao finalizar a decomposição completa (S1→S4 + alertas), revisar internamente: (a) os artigos citados estão corretos? (b) há coerência entre critério material e base de cálculo? (c) as remissões de S1 estão completas? (d) S4 identifica as normas de mutilação relevantes?

---

## Posições consolidadas (Posição LA) — Referência

Para mapear posições consolidadas de Leonardo Amaral sobre temas recorrentes, consultar, em IBS/CBS, o arquivo de estado `posicoes-la-ibs-cbs.md` do project Especialista Reforma Tributária (knowledge do project; casa canônica no Drive, pasta ID `1naGorhPKOPi3zR14aIo6TNEGPsRaRo98`) e, nas demais matérias, o Acervo AeM alimentado pela `destila` (Drive, ID `1V4xYyffyXXT7lSY2i51tVd7l1P5xIGIh`). Esta skill não carrega cópia própria das posições: fonte única (A-12, 2026-08-29). Estas posições devem ser referenciadas em S4 quando o tema cruzar com a análise, mas não substituem o percurso analítico.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.