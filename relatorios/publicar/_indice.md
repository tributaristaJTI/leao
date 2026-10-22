# Publicação · Prompt 1.3 · índice das rodadas

Gerado em 22/10/2026. Nada foi publicado. 22 skills avulsas e 1 plugin.

## Estado antes de publicar

- **Validação:** `claude plugin validate --strict` aprovado em `skills/`, em cada skill alterada e no plugin.
- **Testes:** **não rodados.** O Prompt 1.3 pressupõe "passaram na validação e nos testes", mas a suíte da `crivo-do-leao` (`claude plugin eval`) ainda não foi montada. Validar confere a estrutura, não o comportamento. Publicar antes dos testes é decisão de Leonardo.
- **Colisão:** o manifesto da conta em 22/10 tem as mesmas datas de atualização da cópia de trabalho. Nenhuma skill foi editada no chat depois da cópia, e cada cartão substitui a versão em vigor sem perder edição posterior.

## Rodadas (até três cartões por rodada, das mudanças de maior efeito para as menores)

| Rodada | Arquivos em `relatorios/publicar/` | Por que nesta ordem |
|---|---|---|
| 1 | `mod-ibs-cbs-diferimento.md`, `braco-direito.md`, `voz-autoral-leonardo.md` | Reescrita, troca de destinatário e fonte única de estilo |
| 2 | `destila.md`, `briefing-juridico.md`, `crivo-do-leao.md` | Etapa nova, migração de layout, remissão no Modo Social |
| 3 | `mod-ir-venda-imovel.md`, `mod-funrural.md`, `mod-comparativo-pf-pj.md` | Módulos de cálculo: fonte conferida |
| 4 | `mod-grupo-economico.md`, `cerebro-pbc.md`, `regra-matriz.md` | Módulo restante; nome de modelo; marcadores |
| 5 | `fiel-da-balanca.md`, `monitor-carf.md`, `artigo-juridico.md` | Marcador; referência; parágrafo padrão |
| 6 | `entregavel-cliente.md`, `guardiao-de-caso.md`, `agint-aresp.md` | Só o parágrafo padrão |
| 7 | `parecer-aem.md`, `pesquisa-gcap.md`, `tributarista-consultivo.md` | Só o parágrafo padrão |
| 8 | `tributarista-contencioso.md` | Só o parágrafo padrão |
| à parte | `_plugin-ecossistema-do-leao.md` | Plugin: novo envio pela tela de plugins, sem cartão |

`crivo-do-leao`, `monitor-carf` e `briefing-juridico` mudam também fora da SKILL.md (um arquivo de apoio alterado nas duas primeiras, um retirado na terceira). Se o cartão só aceitar a SKILL.md, essas três ficam publicadas pela metade [A CONFERIR na rodada 2].

## Prompt para o chat do Claude (uma rodada por vez)

Com o repositório tributaristaJTI/leao conectado à conversa:

```
Leia relatorios/publicar/<arquivo 1>, <arquivo 2> e <arquivo 3>. Para cada um, proponha a skill como atualização da skill existente de mesmo nome, com a SKILL.md completa da seção 1 (e os arquivos de apoio, quando houver). Mostre o resumo da seção 2 junto do cartão.
```

## Depois de cada rodada

Na sessão seguinte do Code, a cópia em `~/.claude/skills/synced/*/<nome>/` traz a versão nova. Conferir com `diff` contra `skills/<nome>/SKILL.md`; batendo, commit "publicada v<n>: <nome>".
