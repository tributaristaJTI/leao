# Validação das skills e plugins sincronizados · Fase 1.1

Data: 22/10/2026 · Ambiente: sessão do Claude Code em nuvem (contêiner), não o Mac · Comando: `claude plugin validate <pasta> --strict` (Claude Code 2.1.308)

## Leitura em uma frase

Nenhuma skill da casa tem erro de validação. A única reprovação estrita é do plugin `box`, de terceiro, por falta de descrição no marketplace. Os avisos restantes (ícone, licença, política de privacidade, linha de instalação no README) só importam para quem publica no catálogo público de plugins, o que não é o caso.

## Desvio em relação ao plano

1. O plano supõe que `crivo-do-leao`, `destila` etc. sejam plugins `@synced`. Não são: `claude plugin list` mostra só 7 plugins sincronizados. As 36 skills da casa chegam como **skills avulsas sincronizadas** (pasta `~/.claude/skills/synced/`), e `claude plugin details crivo-do-leao@synced` responde "not found". Por isso a cópia foi feita em duas pastas: `plugins/` (os 7 plugins) e `skills/` (as 54 skills avulsas, com o manifesto em `skills/_manifest.json`).

2. Skill avulsa não tem `plugin.json`; validada sozinha, o validador acusa "No manifest found". Para validar o conteúdo, cada skill foi colocada num invólucro temporário `skills/<nome>/` (estrutura que o Claude Code carrega sem manifesto). Os arquivos copiados em `skills/` não foram alterados.

3. Skill avulsa não tem número de versão. A coluna "versão" traz a data da última atualização na conta (`updatedAt` do manifesto).

4. A Fase 0 não tinha sido executada neste ambiente. Foram criados aqui só a pasta `Leao/` com a estrutura, o `.gitignore` e o `CLAUDE.md` com o texto literal do plano. Login claude.ai e conectores não foram conferidos como no Checkpoint 0 (vários conectores de plugin falharam ao conectar nesta sessão: Notion, Gmail, Calendar e Drive do plugin, por bloqueio do proxy).

## Plugins sincronizados (7)

| Plugin | Versão | Origem | Validação estrita | Avisos |
|---|---|---|---|---|
| box | 1.0.0 | terceiro (knowledge-work-plugins) | reprovado | reprova: marketplace sem descrição; README sem linha de instalação |
| data | 1.1.0 | terceiro (knowledge-work-plugins) | aprovado | ícone; política de privacidade |
| ecossistema-do-leao | 0.1.0 | da casa (My Uploads) | aprovado | README sem linha de instalação; catálogo: licença, ícone, privacidade |
| exa | 3.4.1 | terceiro (knowledge-work-plugins) | aprovado | ícone; privacidade |
| legal | 1.1.0 | da casa (My Uploads) | aprovado | README sem linha de instalação; catálogo: ícone, privacidade |
| productivity | 1.3.1 | terceiro (knowledge-work-plugins) | aprovado | ícone; privacidade |
| zapier | 1.0.0 | terceiro (knowledge-work-plugins) | aprovado | README sem linha de instalação; catálogo: licença, privacidade |

## Skills avulsas sincronizadas (54)

Todas aprovadas na validação estrita, sem erro nem aviso de conteúdo. Os únicos apontamentos foram de catálogo público (README, LICENSE, ícone), comuns a todas por serem skills soltas.

| Skill | Atualizada em | Origem | Validação estrita |
|---|---|---|---|
| agint-aresp | 2026-08-20 | da casa | aprovada |
| apple-design | 2026-10-21 | da casa | aprovada |
| arquivo-do-leao | 2026-09-08 | da casa | aprovada |
| artigo-juridico | 2026-07-04 | da casa | aprovada |
| atas-leao | 2026-09-05 | da casa | aprovada |
| braco-direito | 2026-09-22 | da casa | aprovada |
| briefing-juridico | 2026-03-19 | da casa | aprovada |
| cerebro-pbc | 2026-07-08 | da casa | aprovada |
| coleta-inteligente | 2026-09-25 | da casa | aprovada |
| conselho-do-leao | 2026-04-13 | da casa | aprovada |
| crivo-do-leao | 2026-09-22 | da casa | aprovada |
| deck-aula-aem | 2026-09-09 | da casa | aprovada |
| destila | 2026-10-21 | da casa | aprovada |
| entregavel-cliente | 2026-04-06 | da casa | aprovada |
| faxina-do-leao | 2026-08-11 | da casa | aprovada |
| fiel-da-balanca | 2026-07-10 | da casa | aprovada |
| guardiao-de-caso | 2026-10-02 | da casa | aprovada |
| layout-aem | 2026-09-21 | da casa | aprovada |
| melhorar-prompts | 2026-10-21 | da casa | aprovada |
| mestre-de-obras | 2026-08-29 | da casa | aprovada |
| mod-comparativo-pf-pj | 2026-04-06 | da casa | aprovada |
| mod-funrural | 2026-04-06 | da casa | aprovada |
| mod-grupo-economico | 2026-04-06 | da casa | aprovada |
| mod-ibs-cbs-diferimento | 2026-04-06 | da casa | aprovada |
| mod-ir-venda-imovel | 2026-04-06 | da casa | aprovada |
| monday-caso | 2026-08-20 | da casa | aprovada |
| monitor-carf | 2026-10-21 | da casa | aprovada |
| parecer-aem | 2026-09-05 | da casa | aprovada |
| pesquisa-gcap | 2026-10-05 | da casa | aprovada |
| poda | 2026-09-22 | da casa | aprovada |
| ponto-do-leao | 2026-07-11 | da casa | aprovada |
| proposta-aem | 2026-09-05 | da casa | aprovada |
| regra-matriz | 2026-09-05 | da casa | aprovada |
| tributarista-consultivo | 2026-04-01 | da casa | aprovada |
| tributarista-contencioso | 2026-04-01 | da casa | aprovada |
| voz-autoral-leonardo | 2026-08-28 | da casa | aprovada |
| built-in-browser | 2026-09-21 | Anthropic (exemplo) | aprovada |
| canvas-design | 2026-09-14 | Anthropic (exemplo) | aprovada |
| chrome-browser | 2026-09-18 | Anthropic (exemplo) | aprovada |
| computer-use | 2026-10-08 | Anthropic (exemplo) | aprovada |
| deep-research | 2026-09-14 | Anthropic (exemplo) | aprovada |
| doc-coauthoring | 2026-09-14 | Anthropic (exemplo) | aprovada |
| docs | 2026-09-30 | Anthropic (exemplo) | aprovada |
| docx | 2026-09-30 | Anthropic | aprovada |
| google-workspace | 2026-10-14 | Anthropic (exemplo) | aprovada |
| import-memory | 2026-09-14 | Anthropic (exemplo) | aprovada |
| internal-comms | 2026-09-14 | Anthropic (exemplo) | aprovada |
| learn | 2026-09-14 | Anthropic (exemplo) | aprovada |
| morning | 2026-09-14 | Anthropic (exemplo) | aprovada |
| pdf | 2026-07-10 | Anthropic | aprovada |
| pptx | 2026-10-02 | Anthropic | aprovada |
| skill-creator | 2026-10-21 | Anthropic (exemplo) | aprovada |
| theme-factory | 2026-09-14 | Anthropic (exemplo) | aprovada |
| xlsx | 2026-09-14 | Anthropic | aprovada |

## Integridade da cópia

`diff -r` entre a origem sincronizada e a cópia em `Leao/` não acusou diferença (conferido em `plugins/legal` e `skills/crivo-do-leao`; a cópia usou `cp -a`, que preserva conteúdo e datas).

