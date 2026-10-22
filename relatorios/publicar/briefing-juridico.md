# Publicar · briefing-juridico

Origem: `skills/briefing-juridico/` no repositório tributaristaJTI/leao. Versão sincronizada de referência: atualizada na conta em 2026-03-19.

## 1. SKILL.md completa e final

`````markdown
---
name: briefing-juridico
description: "Gera briefings jurídicos profissionais para o escritório Amaral e Melo Advogados, especializado em direito tributário e agronegócio. Use SEMPRE que o usuário digitar /comercial ou /operacional, ou quando pedir para gerar um briefing de caso, ficha técnica de caso, briefing comercial, documento de handoff jurídico, ou qualquer documento de atendimento inicial para advogados. Também acione quando o contexto envolver preparação de reunião de fechamento com cliente rural, repasse de caso entre advogados, ou estruturação de informações de atendimento jurídico no agro. Gera documentos .docx com papel timbrado do escritório."
---

# Briefing Jurídico — Amaral e Melo Advogados

Skill para transformar informações brutas de atendimentos iniciais em documentos profissionais estruturados (.docx com papel timbrado) usados por advogados do escritório Amaral e Melo, especializado em direito tributário e agronegócio (sedes em Jataí e Rio Verde/GO, atendendo produtores rurais e empresas agroindustriais).

## Dependências

Para formatação do documento, leia a skill `layout-aem` (localizar o SKILL.md com
`find / -path '*/layout-aem/SKILL.md' 2>/dev/null | head -1`; em sessões claude.ai fica em
`/mnt/skills/user/layout-aem/SKILL.md`) antes de gerar o .docx.
Use o código-base, assets e regras de formatação de lá.
Não defina cores, fontes ou margens localmente.

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

Identidade visual, papel timbrado, página, fontes, cores e caixas vêm da skill `layout-aem`, no **Modo Interno** (o modo que ela define para briefings e fichas técnicas). Esta skill define só o conteúdo e a ordem das seções.

### Título do documento (centralizado)

Para `/comercial`: "BRIEFING COMERCIAL", seguido do nome do cliente, data e "CONFIDENCIAL — USO INTERNO".

Para `/operacional`: "FICHA TÉCNICA DE CASO", no mesmo formato.

### Elementos especiais

Seções de alerta ("Alertas para a Reunião" ou "Riscos e Contingências"): caixa de destaque da `layout-aem` (helper `caixaDestaque`), com o título "⚠ PONTOS DE ATENÇÃO".

Seção "Prazos Críticos" (operacional): tabela da `layout-aem` (helper `tabelaAeM`), com as datas em destaque.

Seção "Próximos Passos": lista numerada com campos para responsável e prazo.

Campos pendentes: formato "[A CONFIRMAR — descrição]".

## Diretrizes gerais

**Precisão jurídica**: Cite dispositivos corretamente. Na dúvida, marque "[A CONFERIR: fonte]" em vez de inventar. Nunca invente jurisprudência.

**Completude**: Cada documento deve ser autossuficiente — o advogado receptor não precisa voltar ao atendente.

**Adaptação ao interlocutor**: Briefing comercial → advogado que vai conversar com cliente (dinâmica de venda). Ficha técnica → advogado que vai trabalhar no caso (operação).

**Confidencialidade**: Todos os documentos são internos. Incluir "CONFIDENCIAL — USO INTERNO".

**Formatação de valores**: Padrão brasileiro (R$ 1.000.000,00). Áreas em hectares. Produções em sacas ou toneladas conforme o produto.

**Lacunas**: Preencher com "[A CONFIRMAR — descrição do que falta]". Nunca deixar em branco ou inventar.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
`````

### Arquivo retirado do pacote: `assets/template-timbrado.docx`

Na proposta, a skill vai sem esse arquivo. O `references/conhecimento-tributario-agro.md` continua.

## 2. O que mudou desde a versão sincronizada

"Dependências" passa a ser o bloco padrão de chamada da `layout-aem` (decisão 2).
"Geração do documento .docx" perde template, página, fontes e cores próprios e usa a `layout-aem` no Modo Interno; alertas e prazos pelos helpers `caixaDestaque` e `tabelaAeM`.
Saiu do pacote o `assets/template-timbrado.docx`, sem uso depois da migração (pendente 8).
"Precisão jurídica": a "referência genérica" dá lugar ao marcador [A CONFERIR: fonte] (pendente 5).
Nova seção final "Conferência de citação" padrão (pendente 6).
