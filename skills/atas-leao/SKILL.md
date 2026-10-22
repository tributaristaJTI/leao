---
name: atas-leao
description: Skill de leitura e estruturação de atas de reunião do escritório Amaral e Melo Advogados e da Agricompany. Use SEMPRE que o usuário digitar /ata, ou mencionar "ler a ata", "resumir a reunião", "extrair os próximos passos", "o que ficou em aberto", "ações da reunião", "ata de sócios", "ata do comitê", "transcrição da reunião", ou pedir para transformar uma ata, transcrição ou notas de reunião em resumo estruturado com decisões, próximos passos e pendências. A skill extrai com fidelidade e NOMEIA as lacunas (decisão sem dono, ação sem prazo) — nunca preenche o que a ata não disse. NÃO use para preparar a reunião antes dela acontecer (isso é a legal:meeting-briefing). NÃO use para revisar texto jurídico (crivo-do-leao) nem para arquivar no acervo (destila) — esses são passos a jusante que esta skill aciona, não substitui.
---

# Skill de Leitura de Atas — Amaral e Melo Advogados

Você lê atas, transcrições e notas de reunião e produz uma extração estruturada em PT-BR: decisões, próximos passos (ações), pendências e riscos — mais um bloco de **defeitos da ata**, que é o produto mais valioso desta skill.

## Princípio inegociável

**A skill nunca preenche lacuna — ela nomeia a lacuna.**

Extraia com fidelidade ao que foi dito. Toda inferência que você fizer é redirecionada de "preencher o buraco" para "apontar o buraco". Você JAMAIS cria um responsável ou um prazo que não estava na ata. Se uma ação não tem dono, você não inventa um — você a marca como defeito. Se um prazo foi dito como "até a próxima reunião", você não chuta uma data — você registra o prazo literal e só resolve para data absoluta se a data da reunião for conhecida, via Python, marcado como derivado.

Isso é o que mantém a ata confiável. Um resumo que inventa estrutura é pior que nenhum resumo.

## Fluxo

### Passo 1 — Identificar a fonte e o tipo

Leia o arquivo da ata (em `/mnt/user-data/uploads` no Cowork, ou o conteúdo colado no chat). Antes de extrair, classifique o **tipo de fonte**, porque isso calibra quanto você infere:

- **Ata formal** (já estruturada, com pauta e deliberações) → extração próxima do literal, inferência mínima.
- **Notas informais** (tópicos soltos, taquigrafia) → inferência moderada.
- **Transcrição bruta** (gravação transcrita, divagação, fala sobreposta) → inferência pesada: você precisa identificar quem disse o quê e o que de fato virou decisão no meio da conversa. Aqui o gradiente de confiança trabalha mais.

Registre também os metadados disponíveis: data da reunião (crítica para resolver prazos), participantes, tipo de reunião (sócios/Coração do Leão, cliente, comitê, Agricompany, contencioso).

### Passo 2 — Extrair pelas quatro categorias

Consulte `references/extracao.md` para a taxonomia completa, os marcadores de detecção em português e o gradiente de confiança. As quatro categorias são, resumidamente:

- **Decisão** — resolução tomada, settled. Pode *gerar* ações.
- **Ação / próximo passo** — tarefa derivada, com dono e prazo. O item crítico para o loop com a meeting-briefing.
- **Pendência** — questão levantada e NÃO resolvida. Sem dono porque ninguém decidiu — categoricamente diferente de ação órfã.
- **Risco / alerta** — preocupação sinalizada, sem virar decisão nem tarefa.

Cada item carrega `trecho_origem` (o span da ata que o sustenta) e `tipo_captura` (`explícito` | `inferido`). Inferido sempre visível, sempre rastreável. Esse é o anti-alucinação processual — não a frase "não invente", que dá falsa segurança, mas o span verificável ao lado de cada item.

### Passo 3 — Resolver prazos e agregar (Python)

Rode `scripts/resolver_prazos.py` para:
- Converter prazos relativos em datas absolutas — SÓ quando a data da reunião é conhecida. Marcado como derivado. Sem data da reunião, o prazo fica apenas literal.
- Agregar ações por responsável (visão "o que cada um saiu devendo").

Cálculo determinístico em Python, com a memória de cálculo visível. Nunca estime data de cabeça.

### Passo 4 — Computar o bloco de defeitos

O bloco "Defeitos da ata" NÃO é uma categoria extraída — é uma **visão computada** sobre o que foi extraído. Reúne:

- **Decisões órfãs** — decisão com `requer_acao = true` e `responsavel_execucao = null`. Decidiu-se que algo deve ser feito, mas não quem faz. (Decisão declaratória/autoexecutável — "aprovamos a ata anterior" — tem `requer_acao = false` e legitimamente não precisa de dono; NÃO é defeito.)
- **Ações sem prazo.**
- **Ações com responsável ambíguo** — "alguém", "a equipe", "o pessoal do contencioso".
- **Pendências sem encaminhamento** — questão aberta que ninguém ficou de levar adiante.
- **Referente ambíguo / nome não confirmado** — nome próprio, entidade ou valor deixado contraditório ou corrompido pela fonte, quando esse referente vai dentro de cláusula, prazo ou cálculo. Ver `references/extracao.md` para os gatilhos. A skill aponta o conflito; não escolhe o referente correto.

Isto é meta-comentário sobre a incompletude da reunião, não conteúdo inventado. É o que um resumo comum não entrega.

### Passo 5 — Render e arquivamento (a jusante)

Esta skill produz a extração estruturada. O que vem depois é downstream e reaproveita o que já existe:

- **Render** — se o usuário quiser o `.docx` de ata-resumo para circular, use `layout-aem` no modo Interno. Não embuta formatação aqui.
- **Arquivamento** — se o usuário quiser preservar as decisões/pendências no acervo, acione `destila` (split durável/volátil, grava nota canônica no Drive). É o que popula o corpus para a confrontação longitudinal da v2.

Não execute render nem arquivamento automaticamente. Ofereça; o usuário decide.

## Eixos de tipagem da ação (os dois, não um)

A ação carrega **dois eixos ortogonais**, porque servem a propósitos diferentes:

1. **Eixo de captura** (próprio desta skill, o que a *leitura* exige): `tipo_captura` = explícito | inferido, mais `confianca` = alta | média | baixa. Mede quão confiável é a captura.
2. **Eixo de ator** (herdado da meeting-briefing, o que o *loop* exige para casar): `tipo_ator` = equipe_juridica | cliente | externo | reuniao_followup. Mede quem executa.

Não escolha entre os eixos. Some os dois. O primeiro é o que distingue uma ação sólida de uma candidata; o segundo é o que permite a v2 confrontar a ação desta ata contra a ação registrada no briefing pré-reunião.

## Vocabulário de status e o mapa de equivalência

O status da ação, em PT-BR: `aberto` | `em_andamento` | `concluído`.

A `legal:meeting-briefing` usa o template em inglês (`Open`, prioridade `H/M/L`). Para o matching na v2, o mapa de equivalência é:

| Ata (PT-BR) | meeting-briefing (template) |
|---|---|
| aberto | Open |
| em_andamento | (sem equivalente direto — In Progress) |
| concluído | (sem equivalente direto — Done/Closed) |

O anglicismo da briefing é dívida técnica dela, não padrão a propagar. Esta skill nasce em PT-BR; o mapa faz a ponte sem contaminar. (Recomendação registrada: ao evoluir a briefing, migrá-la para PT-BR e o mapa vira identidade.)

## Fronteira que mais gera erro: pendência vs. ação órfã

A confusão mais comum, e a que destrói o valor da extração:

- **Pendência**: ninguém resolveu a questão. Não tem dono porque não houve decisão. Ex.: "ficou em aberto se vamos PJ ou mantemos PF."
- **Ação órfã**: a tarefa *deveria* ter executor e não tem. Houve direção, faltou atribuir. Ex.: "ficou definido que precisamos protocolar a transação — [mas ninguém assumiu]."

A meeting-briefing colapsa as duas em "issue sem owner". Esta skill as separa — e é exatamente aí que ela entrega o que a briefing não dá.

## Onde roda

Cowork (lê o arquivo, escreve em disco, grava no Drive via destila). Em chat funciona, mas só entrega download e perde o gancho do acervo.

## Limite da v1 (o que NÃO fazer agora)

NÃO faça confrontação com o histórico — "essa pendência já estava aberta na reunião passada?", "essa decisão contradiz o que ratificamos em março?". Isso é um read-hook de leitura do acervo, idêntico ao que está hoje bloqueado na injeção do parecer-aem, esperando validação do `/destila` com outputs reais. A v1 extrai e arquiva limpo; a confrontação longitudinal é v2, destravada junto com o read-hook do parecer. Construir a leitura-de-volta antes de validar o `/destila` repete o bloqueio que já existe.
