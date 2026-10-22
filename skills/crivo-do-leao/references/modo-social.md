# Modo Social — Crivo do Leão

Modo adicional do Crivo para conteúdo de marca curto: post (LinkedIn/Instagram), carrossel, roteiro de vídeo, legenda, texto institucional, texto de site, material produzido pela assessoria. **Não é eixo novo** — é uma bateria substituta: quando o modo social é acionado, os 6 eixos da bateria padrão (peça jurídica) NÃO se aplicam; aplicam-se apenas os três eixos abaixo.

## Gatilho

- Comando explícito: `/crivo social`
- Detecção automática: quando o input for claramente peça de comunicação pública (post, roteiro, legenda, texto de site/institucional)
- **Em dúvida entre peça jurídica e peça de marca, perguntar ao usuário — nunca assumir.**

## Eixo S1 — Técnico-jurídico (semáforo)

Regra mecânica: **toda afirmação normativa da peça é listada com veredito individual. Nenhuma passa sem cor.**

- 🔴 afirmação de direito falsa; dispositivo inexistente; tese que o escritório não sustenta; promessa de resultado (violação do Provimento 205/2021 da OAB — publicidade advocatícia)
- 🟡 afirmação verdadeira mas sem qualificação necessária (regra com exceção relevante omitida); generalização que induz o leitor a autoaplicação errada
- 🟢 conteúdo juridicamente conferível, ou opinativo declarado como tal

Verificação de dispositivos e precedentes segue o roteamento de motores da bateria padrão (Jusratio / web search), incluindo a Etapa 0 (verificação degradada).

## Eixo S2 — Voz e anti-padrões (checklist mecânico)

Fontes de critério (lista fechada — não inventar critérios novos):

1. Proibições globais de estilo: a lista completa, com exemplos e testes, está na skill `voz-autoral-leonardo`, seção "Proibições globais de estilo" (ler como referência de critério, **não executar** a skill).
2. Critérios de voz da skill `marca-raro` (DNA de marca) — ler como referência de critério, **não executar** a skill.

Saída: lista de ocorrências com **localização exata (frase transcrita)** — nunca juízo genérico de "tom inadequado".

O eixo não reescreve. Aponta e devolve.

## Eixo S3 — Posicionamento RARO

Pergunta única e binária por peça: **esta peça cria/reforça categoria própria, ou compete dentro de categoria existente** (preço, volume, "mais um tributarista do agro")?

- 🟡/🔴 quando a peça: usa argumento de autoridade genérico substituível por qualquer concorrente; posiciona o escritório como fornecedor de serviço em vez de dono de categoria; contradiz posicionamento já publicado
- **Cadeia causal obrigatória:** o veredito de posicionamento vem acompanhado da frase da peça que o sustenta — nunca asserido em abstrato.

## Interface e contrato

**Input:** texto da peça (colado ou arquivo).

**Output:** relatório em três blocos (S1, S2, S3). Cada achado com transcrição + cor + fundamento. Fechamento com veredito agregado:

- **Apto**
- **Apto com ressalvas**
- **Devolver à assessoria**

Quando o veredito for "devolver à assessoria", o relatório sai com a lista de correções **em linguagem que a agência entende — sem juridiquês, item por item — pronta para colar no e-mail de devolução**. Isso ataca o custo real: a mesa do advogado deixa de traduzir o erro.

Invariante preservado: **o modo não corrige nem reescreve.** Aponta, fundamenta e devolve.

## Fora de escopo do modo

- Produção de conteúdo → `marca-raro`
- Revisão de peça jurídica → bateria padrão dos 6 eixos (checklists.md)
- Decisão sobre linha editorial → do usuário ou do `conselho-do-leao`

## Dependências

Nenhuma nova. Lê `marca-raro` como referência de critério, não a executa. Não toca no A-06 (7º eixo de calibragem do crivo) — são trilhas independentes dentro do crivo.
