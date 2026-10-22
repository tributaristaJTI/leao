# Validação das skills e plugins · Fase 1.1 (refeita pelo plano v1.3)

Data: 22/10/2026 · Ambiente: sessão do Claude Code em nuvem (contêiner), não o Mac · Claude Code 2.1.308

## Comandos

- `claude plugin validate skills --strict` · aprovado, sem erro nem aviso.
- `claude plugin validate plugins/ecossistema-do-leao --strict` · aprovado, sem erro nem aviso de manifesto.
- Conferência adicional da sessão anterior: cada skill validada isoladamente num invólucro `skills/<nome>/`; as 54 passaram.

## Cópia

54 pastas com SKILL.md copiadas de `~/.claude/skills/synced/<id-da-conta>/` para `skills/`, 19 delas com `references/`. `plugins/ecossistema-do-leao/` copiado de `~/.claude/plugins/synced/<id-da-conta>/`. `diff -r` entre origem e cópia: nenhuma diferença. O `manifest.json` da origem foi guardado em `relatorios/skills-manifest.json`, fora de `skills/`, para não misturar com as pastas de skill. Os 6 plugins de terceiros copiados na primeira rodada (box, data, exa, legal, productivity, zapier) saíram da pasta de trabalho, como pede o v1.3; ficam no histórico do git (commit 87d65a1).

## Tabela

| Nome | Origem | Atualizada em | Resultado | Avisos |
|---|---|---|---|---|
| ecossistema-do-leao | plugin da casa (v0.1.0) | | aprovado | só de catálogo público: README sem linha de instalação; sem LICENSE, ícone e política de privacidade |
| agint-aresp | skill da casa | 2026-08-20 | aprovado | nenhum |
| apple-design | skill da casa | 2026-10-21 | aprovado | nenhum |
| arquivo-do-leao | skill da casa | 2026-09-08 | aprovado | nenhum |
| artigo-juridico | skill da casa | 2026-07-04 | aprovado | nenhum |
| atas-leao | skill da casa | 2026-09-05 | aprovado | nenhum |
| braco-direito | skill da casa | 2026-09-22 | aprovado | nenhum |
| briefing-juridico | skill da casa | 2026-03-19 | aprovado | nenhum |
| cerebro-pbc | skill da casa | 2026-07-08 | aprovado | nenhum |
| coleta-inteligente | skill da casa | 2026-09-25 | aprovado | nenhum |
| conselho-do-leao | skill da casa | 2026-04-13 | aprovado | nenhum |
| crivo-do-leao | skill da casa | 2026-09-22 | aprovado | nenhum |
| deck-aula-aem | skill da casa | 2026-09-09 | aprovado | nenhum |
| destila | skill da casa | 2026-10-21 | aprovado | nenhum |
| entregavel-cliente | skill da casa | 2026-04-06 | aprovado | nenhum |
| faxina-do-leao | skill da casa | 2026-08-11 | aprovado | nenhum |
| fiel-da-balanca | skill da casa | 2026-07-10 | aprovado | nenhum |
| guardiao-de-caso | skill da casa | 2026-10-02 | aprovado | nenhum |
| layout-aem | skill da casa | 2026-09-21 | aprovado | nenhum |
| melhorar-prompts | skill da casa | 2026-10-21 | aprovado | nenhum |
| mestre-de-obras | skill da casa | 2026-08-29 | aprovado | nenhum |
| mod-comparativo-pf-pj | skill da casa | 2026-04-06 | aprovado | nenhum |
| mod-funrural | skill da casa | 2026-04-06 | aprovado | nenhum |
| mod-grupo-economico | skill da casa | 2026-04-06 | aprovado | nenhum |
| mod-ibs-cbs-diferimento | skill da casa | 2026-04-06 | aprovado | nenhum |
| mod-ir-venda-imovel | skill da casa | 2026-04-06 | aprovado | nenhum |
| monday-caso | skill da casa | 2026-08-20 | aprovado | nenhum |
| monitor-carf | skill da casa | 2026-10-21 | aprovado | nenhum |
| parecer-aem | skill da casa | 2026-09-05 | aprovado | nenhum |
| pesquisa-gcap | skill da casa | 2026-10-05 | aprovado | nenhum |
| poda | skill da casa | 2026-09-22 | aprovado | nenhum |
| ponto-do-leao | skill da casa | 2026-07-11 | aprovado | nenhum |
| proposta-aem | skill da casa | 2026-09-05 | aprovado | nenhum |
| regra-matriz | skill da casa | 2026-09-05 | aprovado | nenhum |
| tributarista-consultivo | skill da casa | 2026-04-01 | aprovado | nenhum |
| tributarista-contencioso | skill da casa | 2026-04-01 | aprovado | nenhum |
| voz-autoral-leonardo | skill da casa | 2026-08-28 | aprovado | nenhum |
| built-in-browser | skill Anthropic (exemplo) | 2026-09-21 | aprovado | nenhum |
| canvas-design | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| chrome-browser | skill Anthropic (exemplo) | 2026-09-18 | aprovado | nenhum |
| computer-use | skill Anthropic (exemplo) | 2026-10-08 | aprovado | nenhum |
| deep-research | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| doc-coauthoring | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| docs | skill Anthropic (exemplo) | 2026-09-30 | aprovado | nenhum |
| docx | skill Anthropic | 2026-09-30 | aprovado | nenhum |
| google-workspace | skill Anthropic (exemplo) | 2026-10-14 | aprovado | nenhum |
| import-memory | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| internal-comms | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| learn | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| morning | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| pdf | skill Anthropic | 2026-07-10 | aprovado | nenhum |
| pptx | skill Anthropic | 2026-10-02 | aprovado | nenhum |
| skill-creator | skill Anthropic (exemplo) | 2026-10-21 | aprovado | nenhum |
| theme-factory | skill Anthropic (exemplo) | 2026-09-14 | aprovado | nenhum |
| xlsx | skill Anthropic | 2026-09-14 | aprovado | nenhum |
