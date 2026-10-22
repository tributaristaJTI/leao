# Registro para o Arquiteto

Esta skill nasceu em conversa avulsa do claude.ai em 30/09/2026, fora de
sessão do project Arquiteto. O que segue é o delta a incorporar ao Inventário
e ao Diário de Fricção na próxima sessão de governança. Nada aqui foi gravado
na pasta `Ecossistema do Leão/`.

## O que foi criado

- **Skill `monitor-carf` v0** (comando `/carf`). Dimensão sugerida: Clube do
  Leão, pilar Inteligência Preditiva. Finalidade: pauta de conteúdo RARO a
  partir das decisões do CARF, com base consultável.
- **Notion**, dentro de "Painel Leonardo":
  - página "Monitor CARF" — `3ebdb165-b4d1-810b-b221-e3df6f48e89e`
  - base "Monitor CARF — Acórdãos" — data source
    `66f1f100-a043-4d50-a139-1f36b20559ad` (com a visão "Fila de pauta")
  - base "Monitor CARF — Termos" — data source
    `9da64503-5e28-421c-8164-3ecb097d1929`, semeada com 135 linhas (123
    expressões de busca ativas, 5 etiquetas, 5 exclusões, 2 cortes)
- **Texto da tarefa agendada** em `references/tarefa-agendada.md`. A tarefa em
  si é criada pelo Leonardo.

## O que ela substitui

- `monitoramento-carf-agro` (versão de 03/09/2026) e
  `inteligencia-sucessoria-agro` (versão de 07/07/2026). As instruções
  originais continuam no Drive em dois lugares: no backup "Computadores ›
  Meu Mac › Documents › Claude › Scheduled" e em
  `Arquiteto/importados-openai-2026-09/Scheduled`.
- Uma terceira entrada que o Leonardo vê como "CARF monitoramento +
  diagnóstico ITR": instrução não localizada em arquivo. Copiar da tela antes
  de pausar.
- Pausar as antigas só depois do teste de aceite.

## Decisões ratificadas pelo Leonardo em 30/09/2026

1. Skill com comando próprio e tarefa agendada que só a chama.
2. Uma coleta, oito trilhas (as seis do texto de escopo que ele trouxe, mais
   ITR e contribuições do produtor).
3. Canal em cascata, declarado em cada entrega.
4. Registro no Notion, sem instrução que se reescreve.
5. Entrega em forma de ficha de pauta, no máximo uma por dia útil; sem texto
   pronto.
6. Leitura do inteiro teor do candidato.
7. Teste de ineditismo.
8. Camada de antecipação (propostas de súmula e pautas).
9. Série semanal da base.
10. Cadência em dias úteis, com regra de parada: menos de um terço das fichas
    virando conteúdo em quatro semanas baixa para três por semana.
11. Captura por palavra, leitura por problema; alienação fiduciária como
    trilha própria, com adjudicação, arrematação e entrega de bens ao credor
    como aplicação analógica potencial; trava de ruído.

## Pendências

- Rodar `/carf teste` antes e depois de 06/10/2026 (mudança das tarefas para
  a nuvem nos planos Pro e Max). O comportamento dos canais em nuvem não foi
  medido; a v0.1 sai do resultado.
- Rodar `/carf calibra` e podar os termos com as contagens.
- Decidir se execução agendada registra ponto (a skill assume que não).
- Abrir a frente no Diário de Fricção e registrar a skill na Camada 1, as
  bases na Camada 4 e a tarefa na lista de tarefas agendadas.

## Sinalizações para a próxima auditoria

- **Sobreposição com o Radar Agro.** A descrição da skill `radar-agro` inclui
  "decisões do CARF" no digest diário. Com o monitor no ar, o radar deveria
  apontar para a base em vez de varrer o CARF por conta própria.
- **Origem das pastas `Scheduled`, `Projects` e `Artifacts`** que caíram na
  `_Entrada` na noite de 08/09/2026. A triagem de 10/09 as atribuiu ao lado
  OpenAI, mas o conteúdo indica as pastas de trabalho do aplicativo do Claude
  (`~/Documents/Claude/`): os `SKILL.md` chamam `update_scheduled_task`, e
  `Projects` tem uma pasta com o nome de um project do Claude. Conferir no
  Mac se `~/Documents/Claude/Scheduled/` ficou vazia; se ficou, é a causa de
  o Leonardo não ter encontrado o arquivo de descrição das tarefas.
- **Base "Monitor CARF — Acórdãos" e matriz de ganho de capital rural.** A
  base pode servir de rotina de atualização da matriz; decidir se a matriz lê
  daqui.

## v0.1 — 06/10/2026 (sessão do project Arquiteto, claude.ai)

Origem: o Leonardo trouxe o texto da tarefa antiga `monitoramento-carf-agro`
(marca d'água de 27/08/2026) para análise. A leitura contra esta skill e a
medição no índice geraram quatro correções, ratificadas em bloco.

- **Canal:** consulta direta por execução de código (`scripts/coleta_ver.py`)
  passa a ser a primeira tentativa. A requisição web fica como segundo
  transporte do mesmo canal.
- **Notas técnicas corrigidas** em `coleta.md`: o índice ignora acento; a
  forma curta "imposto territorial rural" não é variante morta;
  `arquivo_indexado_s` indica inteiro teor no índice e PDF disponível, e os
  registros recentes só são pesquisáveis por ementa e dispositivo.
- **Relevância:** ITR com invasão, esbulho ou ocupação entra na lista de ALTA
  (`triagem-e-lente.md`), como estava na tarefa antiga.
- **Mensagem final:** linha nova "Ponto cego", com os registros da janela sem
  texto pesquisável.
- **Boletim:** contrato em `boletim.md`.

O delta do Inventário e do Diário de Fricção foi gravado em
`Arquiteto/delta-estado-2026-10-06-monitor-carf.md`, que absorve também as
pendências de registro listadas acima neste arquivo.

Pendências da v0.1: `/carf teste` em execução agendada (rede da sessão em
nuvem); rota de inteiro teor para acórdão fresco (SINCON por execução de
código, a validar isolada); inclusão de `imposto territorial rural` na base
de termos pelo Leonardo; conferência do cenário do boletim no Make.

