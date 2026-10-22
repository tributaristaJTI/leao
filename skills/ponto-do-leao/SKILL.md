---
name: ponto-do-leao
description: Skill de registro de atividades e relatório diário de produtividade (timesheet pessoal) do Ecossistema do Leão. Use SEMPRE que o usuário digitar /ponto (registrar a sessão atual) ou /espelho (relatório do dia), ou mencionar "bate o ponto", "registra essa sessão", "espelho do dia", "relatório do meu dia", "onde gastei meu tempo", "como foi meu dia de trabalho", "o que eu fiz hoje aqui". Também acione automaticamente ao concluir entrega produzida por skill de produção, conforme regra das userPreferences. Cada sessão vira um arquivo .md imutável na pasta Ponto do Google Drive; o /espelho varre o dia e consolida em quatro blocos, na ordem, eixo (estratégico/tático/operacional), finalidade (posicionamento, comercial, aprendizado, artigos, jurídico, gestão), casos/clientes e temas. NÃO use para metas e OKRs (governanca-leao), nem para arquivar teses no acervo (destila), nem para estruturar atas de reunião (atas-leao).
---

# Ponto do Leão

## Função

Registrar sessões de trabalho nas três superfícies (claude.ai, Cowork, Code) e devolver, via /espelho, o retrato do dia: eixo de atuação, finalidade, casos e temas. Timesheet e produtividade pessoal. Duas entradas: registro manual (/ponto) e disparo automático pós-entrega (regra das userPreferences). Uma saída: /espelho.

## Fonte canônica

Pasta-âncora no Google Drive — **ID fixo**: `11255Kg3hNU4IBzwdtkUSrmuDSd06XcFC`
(caminho legível: `Ecossistema do Leão/Ponto/`, dono leonardo@amaralemelo.adv.br)

**Regra de ouro: navegar sempre por ID (`parentId`), nunca por nome.** A busca por nome no Drive é não confiável (latência de indexação e cobertura parcial) e há pastas homônimas no Meu Drive. Gravação (/ponto) e leitura (/espelho) partem do MESMO ID-âncora — é isso que garante que o que se grava é o que se lê.

Resolução da pasta do mês (idêntica para gravar e ler):
1. A partir do ID-âncora, localizar a subpasta do ano: `parentId = '11255Kg3hNU4IBzwdtkUSrmuDSd06XcFC' and mimeType = 'application/vnd.google-apps.folder' and title = 'AAAA'`. Se não existir, criar com esse parentId.
2. A partir do ID do ano, localizar/criar a subpasta do mês `MM` (dois dígitos) do mesmo modo.
3. Gravar e ler os registros com `parentId = <ID do mês>`.

- Um arquivo por registro. Nome: `AAAA-MM-DD-hhmm-slug.md` (slug em kebab-case, 2 a 4 palavras).
- Substituir SEMPRE `AAAA` e `MM` pelos valores reais (ex.: `2026`, `07`). Nunca criar pasta com o nome literal do placeholder (`AAAA`, `MM`, com ou sem barra).
- Gravar SEMPRE com `disableConversionToGoogleType=true` e `contentMimeType='text/markdown'`; sem isso o Drive converte o .md em Google Doc.
- Se a pasta do ano ou do mês não existir, criar antes de gravar (sempre por parentId a partir do ID-âncora).
- Registro é imutável: nunca editar arquivo existente. Correção = novo arquivo com o campo `corrige:` apontando o id original; no /espelho, o registro corretor substitui o corrigido.

## Template do registro

```markdown
---
id: AAAA-MM-DD-hhmm-slug
data: AAAA-MM-DD
hora: "hh:mm"
superficie: claude.ai | cowork | code
project: nome-do-project | nenhum
skills: [lista das skills acionadas] | []
eixo: estrategico | tatico | operacional
finalidade: posicionamento | comercial | aprendizado | artigos | juridico | gestao
cliente: slug-do-cliente | interno
temas: [lista de temas]
entrega: descrição curta do que foi produzido | nenhuma
tier: modelo usado na sessão (ex.: fable-5, opus, sonnet)
tempo: P | M | G | GG
---
Resumo da sessão em uma linha.
```

Regras dos campos:

- **tempo**: P (<15min) | M (15–45) | G (45–90) | GG (>90). Inferir pela extensão e densidade da sessão; o usuário corrige se discordar.
- **cliente**: slug curto e consistente — o mesmo caso usa sempre o mesmo slug. Trabalho interno (escritório, Agricompany, ecossistema, estudo) = `interno`.
- **eixo e finalidade**: aplicar o mapa de defaults abaixo; o usuário sobrescreve no ato quando a sessão fugir do padrão.
- Campo não inferível e não informado = `n/i`. Nunca inventar valor.
- Uma sessão com múltiplas entregas = UM registro, com as entregas listadas no campo `entrega`.

## Mapa de defaults (eixo × finalidade por skill acionada)

| Skill acionada | Eixo | Finalidade |
|---|---|---|
| parecer-aem | operacional | juridico |
| briefing-juridico — /comercial | tatico | comercial |
| briefing-juridico — /operacional | operacional | juridico |
| proposta-aem | tatico | comercial |
| entregavel-cliente | operacional | juridico |
| tributarista-consultivo | tatico | juridico |
| tributarista-contencioso | operacional | juridico |
| regra-matriz | operacional | juridico |
| coleta-inteligente | operacional | juridico |
| mod-funrural, mod-ir-venda-imovel, mod-comparativo-pf-pj, mod-grupo-economico, mod-ibs-cbs-diferimento | operacional | juridico |
| braco-direito | operacional | juridico |
| legal:contract-review, legal:nda-triage, legal:canned-responses, legal:compliance | operacional | juridico |
| legal:legal-risk-assessment | tatico | juridico |
| legal:meeting-briefing | tatico | juridico (reunião de sócios → gestao) |
| crivo-do-leao | operacional | herda a finalidade do texto revisado |
| destila | operacional | herda a finalidade do conteúdo (default gestao) |
| atas-leao | operacional | gestao |
| conselho-do-leao | estrategico | gestao |
| governanca-leao | estrategico | gestao |
| cerebro-pbc | tatico | aprendizado |
| artigo-juridico | operacional | artigos |
| voz-autoral-leonardo (acionada sozinha) | operacional | artigos |
| marca-raro | operacional | posicionamento |

Skills de infraestrutura chamadas por dependência (layout-aem e equivalentes) não geram registro próprio.

Múltiplas skills na mesma sessão: prevalece o default da skill da entrega principal; as demais entram na lista `skills`.

## Defaults para sessão sem skill (registro manual)

| Contexto da sessão | Eixo | Finalidade |
|---|---|---|
| Decisão de sócios, estrutura societária, governança AeM/Agricompany | estrategico | gestao |
| Posicionamento e marca (sem acionar marca-raro) | estrategico | posicionamento |
| Produto, precificação, expansão comercial | estrategico | comercial |
| Governança do ecossistema Claude (project Arquiteto) | estrategico | gestao |
| Estudo, leitura guiada, exploração de tema | tatico | aprendizado |
| Livro em produção (project Livro) | operacional | artigos |
| Consulta pontual ≥15min | operacional | conforme o tema |

## Protocolo /ponto (registro manual)

1. Inferir do contexto da conversa: superfície, project, skills acionadas, eixo, finalidade, cliente, temas, entrega, tier, faixa de tempo.
2. Aplicar o mapa de defaults ao que faltar.
3. Se restar campo crítico não inferível (eixo, finalidade ou cliente), perguntar em UMA única mensagem, no máximo 3 perguntas. Os demais campos vão como `n/i`.
4. Montar o .md conforme o template e gravar na pasta do mês **resolvida por ID** (ver Fonte canônica), com `disableConversionToGoogleType=true` e `contentMimeType='text/markdown'`.
5. Confirmar em uma linha: `Ponto registrado: <id> — <eixo>/<finalidade>, <tempo>.` Sem prosa adicional.

## Disparo automático (pós-entrega)

Gatilho: conclusão de entrega produzida por skill de produção, conforme a regra das userPreferences.

1. Montar o registro só com inferência e defaults. Não perguntar nada.
2. Gravar e confirmar em uma linha ao final da resposta da entrega.
3. O registro nunca atrasa nem interrompe a entrega principal. Se a gravação falhar, reportar em uma linha e seguir — o usuário decide se refaz via /ponto.

## Protocolo /espelho (relatório do dia)

1. Data-alvo: default hoje. Aceitar `/espelho ontem` e `/espelho AAAA-MM-DD`.
2. Resolver a pasta do mês **por ID** (ver Fonte canônica) e buscar os registros com `parentId = <ID do mês> and title contains '<data-alvo no formato AAAA-MM-DD>'`. Nunca por busca de nome global. Ler todos.
3. Ponderar cada registro pelo valor central da faixa de tempo: P=10 | M=30 | G=70 | GG=120 minutos.
4. Consolidar em quatro blocos, nesta ordem:
   - **Eixo** — distribuição percentual ponderada entre estratégico, tático e operacional + veredito em uma frase (a resposta direta a "atuei mais estratégica, tática ou operacionalmente?").
   - **Finalidade** — distribuição percentual ponderada entre as seis finalidades.
   - **Casos e clientes** — cada cliente/caso tocado no dia, com o que foi feito em cada um (a partir dos resumos de uma linha).
   - **Temas** — agregado dos temas do dia.
5. Rodapé: número de sessões, tempo total estimado e, no máximo, UMA observação de desequilíbrio quando substantiva (ex.: nenhuma sessão estratégica na semana). Constatar, não moralizar.
6. Dia sem registros: dizer isso em uma linha e listar os últimos 5 registros existentes na pasta.

## Regras mecânicas

- Corte de ruído: sessão de consulta pura com menos de 15 minutos não registra. Exceção: /ponto explícito sempre registra.
- O registro carrega metadados e resumo de uma linha; nunca conteúdo do trabalho (tese, trecho de parecer, cláusula). Conhecimento consultável é papel do destila.
- Nome de cliente no slug: o mínimo para identificar o caso; nada de dados sensíveis.
- Nunca inventar dado. `n/i` é resposta válida.

## O que esta skill NÃO faz

Não mede OKRs nem indicadores do escritório (governanca-leao). Não arquiva conhecimento no acervo (destila). Não estrutura atas (atas-leao). Não fatura honorários: se o timesheet um dia virar insumo de cobrança, a evolução é refinar as faixas para minutos em v2, não improvisar sobre P/M/G/GG.
