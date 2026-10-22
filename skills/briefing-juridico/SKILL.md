---
name: briefing-juridico
description: "Gera briefings jurídicos profissionais para o escritório Amaral e Melo Advogados, especializado em direito tributário e agronegócio. Use SEMPRE que o usuário digitar /comercial ou /operacional, ou quando pedir para gerar um briefing de caso, ficha técnica de caso, briefing comercial, documento de handoff jurídico, ou qualquer documento de atendimento inicial para advogados. Também acione quando o contexto envolver preparação de reunião de fechamento com cliente rural, repasse de caso entre advogados, ou estruturação de informações de atendimento jurídico no agro. Gera documentos .docx com papel timbrado do escritório."
---

# Briefing Jurídico — Amaral e Melo Advogados

Skill para transformar informações brutas de atendimentos iniciais em documentos profissionais estruturados (.docx com papel timbrado) usados por advogados do escritório Amaral e Melo, especializado em direito tributário e agronegócio (sedes em Jataí e Rio Verde/GO, atendendo produtores rurais e empresas agroindustriais).

## Dependências

Esta skill gera documentos .docx. Antes de gerar qualquer documento, leia a skill `docx` em `/mnt/skills/public/docx/SKILL.md` para seguir as melhores práticas de criação de arquivos Word.

## Conhecimento de domínio

Para enriquecer análises jurídicas com temas recorrentes do agronegócio (Funrural, ICMS, ITR, CPR, Reforma Tributária, contratos agrários), leia o arquivo `references/conhecimento-tributario-agro.md` dentro do diretório desta skill.

## Comandos e fluxos

A skill possui dois modos de operação:

### Comando `/comercial` → Briefing Comercial de Caso

Documento que prepara o advogado para a reunião de fechamento de contrato com o cliente. O advogado que receber este documento NÃO participou do atendimento inicial — ele precisa de todas as informações para conduzir a reunião com segurança e confiança.

**Estrutura obrigatória do documento:**

1. **Dados do Cliente** — Nome/razão social, atividade rural/agroindustrial, porte estimado (área em hectares, faturamento se disponível), localização, contato.
2. **Situação Apresentada** — Narrativa clara do problema na linguagem do cliente. Preserve a "dor" real, não juridifique demais.
3. **Diagnóstico Preliminar** — Enquadramento jurídico: questão tributária ou agrária, tributos/obrigações envolvidos, cenário normativo.
4. **Tese Jurídica Viável** — Principal linha de atuação com fundamentação legal (dispositivos-chave, jurisprudência favorável, posição doutrinária).
5. **Argumentos de Valor** — Por que contratar o escritório: urgência, riscos de inação, benefício econômico potencial, diferencial técnico.
6. **Complexidade e Estimativa** — Classificação (baixa/média/alta), tipo de atuação (consultiva/administrativa/judicial), estimativa de prazo e faixa de honorários.
7. **Alertas para a Reunião** — Objeções prováveis, concorrência de escritórios, expectativas a gerenciar, informações a confirmar.

**Tom:** Estratégico e orientado a conversão. Armar o advogado para vender o serviço com competência técnica. Clareza e objetividade, sem linguagem excessivamente acadêmica.

### Comando `/operacional` → Ficha Técnica de Caso

Documento de handoff operacional para o advogado responsável técnico. Garante que ele inicie o trabalho sem refazer a análise inicial.

**Estrutura obrigatória do documento:**

1. **Identificação** — Cliente (nome/razão social, CNPJ/CPF, inscrição estadual/produtor rural), representante/contato, data do atendimento, advogado atendente.
2. **Fatos Relevantes** — Narrativa factual detalhada e cronológica. Apenas fatos, sem opinião jurídica.
3. **Documentação** — Documentos já recebidos (listar) e documentos pendentes/necessários (com justificativa de cada um).
4. **Enquadramento Jurídico** — Questões de direito, institutos aplicáveis, regime tributário, legislação incidente (federal/estadual/municipal).
5. **Teses e Estratégia** — Teses principal e subsidiárias, fundamentação legal e jurisprudencial, posição dos tribunais (pacífica/majoritária/divergente).
6. **Riscos e Contingências** — Riscos processuais/fiscais, teses contrárias do fisco/adversário, pontos fracos do caso.
7. **Prazos Críticos** — Prescrição, decadência, prazos administrativos/contratuais, vencimentos de tributos, obrigações acessórias.
8. **Próximos Passos** — Ações sequenciadas com responsável sugerido e prazo recomendado.

**Tom:** Técnico e completo. Ferramenta de trabalho — priorizar precisão e organização. Terminologia jurídica adequada, dispositivos legais no formato padrão (Art. X, §Y, da Lei nº AAAA/BBBB).

## Modos de entrada

### Com texto (Notas Livres)

Quando o usuário colar texto após o comando (notas de reunião, transcrição, bullet points), extrair e organizar todas as informações no formato do documento solicitado.

Se informações críticas estiverem ausentes, gerar o documento completo com o que há e incluir ao final uma seção **"INFORMAÇÕES PENDENTES"** listando o que falta e por que é necessário. Nunca interromper a geração para perguntar — o usuário pode não ter as respostas naquele momento.

### Sem texto (Anamnese Guiada)

Quando o usuário enviar apenas o comando sem texto, iniciar questionário interativo em grupos de 3-4 questões.

Para `/comercial`, priorizar: identificação do cliente e atividade rural → problema/dor → urgência e contexto → expectativa e orçamento percebido.

Para `/operacional`, priorizar: identificação completa (dados cadastrais) → fatos cronológicos → documentos recebidos/mencionados → histórico de atuação anterior.

Após reunir informações suficientes, gerar o documento. Se o usuário indicar que não tem mais informações, gerar com o que há e sinalizar lacunas.

## Geração do documento .docx

### Template do escritório

O template do papel timbrado está em `assets/template-timbrado.docx` dentro do diretório desta skill. Use-o SEMPRE como base para os documentos gerados. O fluxo é: copiar o template para o diretório de trabalho → descompactar (é um ZIP) → substituir o conteúdo do `word/document.xml` com o briefing formatado em WordprocessingML → reempacotar o ZIP como .docx. Isso preserva o cabeçalho com logo "Amaral & Melo — Jurídico no Agro" (selo 20 anos), rodapé com endereços das unidades Jataí e Rio Verde, estilos, fontes e numeração de página.

Se por algum motivo o template não for encontrado, gere o .docx do zero seguindo as instruções da skill `docx`, aplicando a formatação abaixo.

### Configurações de página (quando usando template)

Não alterar: A4 (11906 × 16838 twips), margens topo=2127, direita=720, inferior=1418, esquerda=720. Largura útil para conteúdo: ~10466 twips.

### Formatação do conteúdo

Fonte Arial em todo o documento. Títulos de seção: Arial Bold 12pt, cor azul escuro (#1B3A5C), com linha dourada (#C4972A) abaixo como separador. Corpo: Arial Regular 11pt, preto, justificado. Tabelas: largura total (~10466 DXA), coluna de rótulos com fundo cinza (#F0F0F0), bordas cinza claro (#CCCCCC). Campos pendentes: itálico, cor cinza (#999999), formato "[A CONFIRMAR — descrição]".

### Título do documento (centralizado)

Para `/comercial`: "BRIEFING COMERCIAL" em Arial Bold 14pt azul escuro, seguido do nome do cliente, data e "CONFIDENCIAL — USO INTERNO".

Para `/operacional`: "FICHA TÉCNICA DE CASO" no mesmo formato.

### Elementos especiais

Seções de alerta ("Alertas para a Reunião" ou "Riscos e Contingências"): caixa com fundo amarelo claro (#FFF9E6), borda esquerda grossa laranja (#E67E22), título "⚠ PONTOS DE ATENÇÃO" em laranja.

Seção "Prazos Críticos" (operacional): tabela formatada com datas em destaque.

Seção "Próximos Passos": lista numerada com campos para responsável e prazo.

## Diretrizes gerais

**Precisão jurídica**: Cite dispositivos corretamente. Na dúvida, use referência genérica ("conforme legislação aplicável") em vez de inventar. Nunca invente jurisprudência.

**Completude**: Cada documento deve ser autossuficiente — o advogado receptor não precisa voltar ao atendente.

**Adaptação ao interlocutor**: Briefing comercial → advogado que vai conversar com cliente (dinâmica de venda). Ficha técnica → advogado que vai trabalhar no caso (operação).

**Confidencialidade**: Todos os documentos são internos. Incluir "CONFIDENCIAL — USO INTERNO".

**Formatação de valores**: Padrão brasileiro (R$ 1.000.000,00). Áreas em hectares. Produções em sacas ou toneladas conforme o produto.

**Lacunas**: Preencher com "[A CONFIRMAR — descrição do que falta]" em itálico cinza. Nunca deixar em branco ou inventar.
