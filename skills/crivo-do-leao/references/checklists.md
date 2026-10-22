# Checklists de Verificação — Crivo do Leão

Este arquivo contém os checklists específicos para cada tipo de documento coberto na v1. O SKILL.md referencia este arquivo na Etapa 3.

---

## Checklist 1 — Parecer Jurídico

Aplicar todas as verificações abaixo, na ordem. Cada item que gerar suspeita vira um achado no laudo.

### 1.1 Legislação citada

Para cada dispositivo legal mencionado no parecer (artigo, inciso, parágrafo, alínea de qualquer lei, decreto, instrução normativa, portaria, resolução, convênio, ou norma constitucional):

- O diploma legal existe? (ex: "Lei 14.XXX/2024" — essa lei foi promulgada?)
- O artigo citado existe dentro desse diploma? (ex: "art. 47 da Lei 9.393/96" — a lei tem 47 artigos?)
- O conteúdo atribuído ao dispositivo corresponde ao que ele realmente diz? (ex: o texto afirma que "o art. 12 da Lei X prevê isenção de..." — o art. 12 trata mesmo de isenção?)
- A redação citada é a vigente? O dispositivo foi alterado por lei posterior? Foi revogado?
- Incisos e parágrafos estão numerados corretamente? (ex: §3º existe? Inciso IV existe?)

Atenção especial para: Emendas Constitucionais recentes (EC 132/2023), Leis Complementares da reforma tributária (LC 214/2025, LC 227/2026), e legislação infralegal (IN RFB, Decretos estaduais) — são as fontes mais propensas a erro por desatualização ou confusão de numeração.

### 1.2 Jurisprudência citada

Para cada precedente mencionado (acórdão, decisão, recurso, repercussão geral, repetitivo, súmula):

- O número do processo/recurso existe? (ex: RE 574.706/PR — esse RE existe no STF?)
- O tribunal está correto? (ex: não atribuir ao STJ uma decisão que é do STF, ou vice-versa)
- A ementa ou tese atribuída corresponde ao que o julgado efetivamente decidiu?
- O Tema de Repercussão Geral ou Repetitivo está correto? (ex: Tema 69 do STF trata do que o texto afirma?)
- A data de julgamento está correta ou pelo menos compatível?
- Súmulas: o número e o tribunal estão corretos? O enunciado corresponde?

Particularidade CARF: acórdãos do CARF têm indexação web precária. Se a busca não retornar resultados, classificar como amarelo com nota: "Acórdão CARF não localizado em bases públicas — verificar diretamente no sistema e-processo/CARF."

### 1.3 Referências doutrinárias

Para cada citação de doutrina (livros, artigos acadêmicos, teses):

- O autor existe e é da área citada?
- A obra existe? O título está correto?
- A edição ou ano mencionados são compatíveis?

Esta verificação tem menor criticidade que legislação e jurisprudência, mas erros aqui comprometem a credibilidade do parecer.

### 1.4 Consistência lógica

Analisar a cadeia argumentativa do parecer como um todo:

- A conclusão decorre logicamente da fundamentação? Ou há um salto argumentativo — a fundamentação desenvolve a tese A mas a conclusão afirma B?
- Há contradições internas? (ex: um parágrafo afirma que a operação é isenta, outro parágrafo calcula o tributo devido sobre a mesma operação)
- As premissas fáticas estão consistentes ao longo do texto? (ex: o texto menciona "produtor pessoa física" na consulta mas analisa regime de pessoa jurídica na fundamentação)
- O posicionamento é claro? Ou o parecer oscila entre posições sem se comprometer?

### 1.5 Conformidade com posições do escritório

Verificar, quando identificável, se o parecer contradiz posições consolidadas da Amaral e Melo:

- Sobre Funrural: o escritório tem posição sobre constitucionalidade pós-RE 718.874?
- Sobre IRPF rural: há orientações específicas sobre livro caixa, depreciação, diferimento?
- Sobre reforma tributária: as posições sobre IBS/CBS e diferimento estão alinhadas com o que o escritório defende publicamente?

Esta verificação depende do conhecimento contextual disponível. Se não houver informação suficiente para avaliar, pular este item e registrar: "Conformidade com posições do escritório: não verificável nesta sessão."

---

## Checklist 2 — Análise Tributária

Inclui todas as verificações do Checklist 1 (1.1 a 1.5) com as seguintes adições:

### 2.1 Alíquotas e faixas

Para cada alíquota, percentual ou faixa de tributação mencionada:

- O percentual está correto para o tributo e regime citados? (ex: alíquota de Funrural PF é 1,5% ou 1,2%? Depende do período — verificar)
- A base de cálculo indicada é a correta? (ex: receita bruta, valor da operação, lucro líquido)
- Se houver faixas progressivas (IRPF), as faixas e alíquotas estão atualizadas para o ano-calendário correto?
- Contribuições adicionais (SENAR, RAT, SAT) estão com percentuais corretos?

### 2.2 Coerência numérica

Para cálculos apresentados no texto (não necessariamente em tabela):

- As contas fecham? Se o texto diz "receita de R$ 1.000.000 × 1,5% = R$ 15.000", a multiplicação está correta?
- Proporções e percentuais comparativos são consistentes? (ex: "economia de 32%" — os números apresentados realmente geram 32%?)
- Se houver cenários comparativos, os mesmos parâmetros foram usados em todos os cenários? (mesma receita base, mesmo período, mesmas premissas)
- Somas, diferenças e totais conferem com os valores parciais apresentados?

Nota: o Crivo aponta inconsistências aparentes, não refaz os cálculos. Se suspeitar de erro numérico, classificar como amarelo com ação recomendada "Refazer cálculo com Python ou planilha."

### 2.3 Vigência e transição

Para cada norma citada na análise:

- A norma está em vigor na data de referência da análise?
- Se a análise trata de planejamento futuro, as normas de transição da reforma tributária (EC 132/2023, LC 214/2025) foram consideradas?
- Há norma revogadora ou alteradora que o texto não mencionou?
- Regulamentos estaduais e decretos: estão vigentes? (Atenção especial para RICMS de GO, MT, MG, BA — estados frequentes na base de clientes)

---

## Checklist 3 — Contrato

> Fonte única do núcleo contratual: a skill `poda` lê as seções 3.1 a 3.3 como camada intocável antes de propor cortes e roda este checklist sobre a versão podada. Alteração aqui repercute lá.

Inclui as verificações 1.1 (legislação) e 2.3 (vigência) com as seguintes adições específicas:

### 3.1 Cláusulas essenciais por tipo contratual

Verificar se o contrato contém as cláusulas mínimas exigidas para o tipo contratual identificado. Os tipos mais frequentes na prática do escritório:

**Contrato de parceria rural (Estatuto da Terra + Lei 4.504/64, Decreto 59.566/66):**
- Qualificação completa das partes (incluindo CPF/CNPJ, estado civil, regime de bens)
- Identificação do imóvel (matrícula, localização, área)
- Prazo e condições de renovação
- Percentual de participação nos frutos
- Obrigações de cada parte (insumos, maquinário, mão de obra)
- Cláusula sobre benfeitorias
- Cláusula ambiental (responsabilidade por área de reserva legal e APP)
- Foro competente

**Contrato de arrendamento rural:**
- Mesmos itens acima, substituindo percentual de participação por valor do arrendamento
- Forma e periodicidade do pagamento
- Índice de reajuste (atenção: proibição de reajuste vinculado a produtos — art. 18, parágrafo único, Decreto 59.566/66)
- Direito de preferência do arrendatário

**Contrato de compra e venda de imóvel rural:**
- Descrição completa do imóvel (matrícula, CCIR, ITR, CAR, georreferenciamento)
- Preço e condições de pagamento
- Cláusula sobre VTN e benfeitorias (separação para fins de GCap)
- Anuência do cônjuge (se aplicável)
- Certidões negativas exigidas
- Cláusula de evicção
- Prazo para escrituração e registro

**Reestruturação societária:**
- Motivos da operação
- Laudos de avaliação
- Tratamento de passivos e contingências
- Cláusulas de não-concorrência e não-aliciamento (se aplicável)
- Regime de responsabilidade tributária (CTN arts. 132-133)

Se o contrato for de tipo não listado, verificar apenas as cláusulas universais: qualificação das partes, objeto, obrigações, prazo, preço/remuneração, rescisão, foro.

### 3.2 Consistência interna

Verificar se o contrato é internamente consistente:

- Definições usadas na primeira menção são mantidas ao longo do texto? (ex: se define "PARCEIRO-OUTORGANTE" na qualificação, esse mesmo termo é usado nas cláusulas?)
- Cláusulas não se contradizem? (ex: cláusula 5 diz que o prazo é de 3 anos, cláusula 12 menciona obrigações "durante os 5 anos do contrato")
- Referências cruzadas entre cláusulas estão corretas? (ex: "conforme cláusula 7.2" — a cláusula 7.2 existe e trata do que foi mencionado?)
- Valores, percentuais e prazos são consistentes em todas as menções?
- Anexos mencionados existem? (ex: "conforme Anexo III" — o contrato tem Anexo III?)

### 3.3 Adequação de foro e legislação aplicável

- O foro eleito é competente para o tipo de contrato? (contratos rurais: foro do imóvel, não da sede da empresa)
- A legislação aplicável indicada é a correta? (ex: contrato de parceria rural deve referenciar Estatuto da Terra, não apenas Código Civil)
- Há conflito entre a legislação mencionada e o conteúdo das cláusulas?

---

## Verificações comuns (aplicáveis a qualquer tipo)

Quando o documento não se encaixar nos três perfis acima, ou como camada adicional, aplicar:

- Todas as referências legislativas mencionadas existem e dizem o que o texto afirma (verificação 1.1 simplificada)
- Dados numéricos e estatísticas têm fonte verificável
- Não há contradições internas no texto
- Nomes próprios (de leis, tribunais, órgãos, pessoas) estão grafados corretamente
