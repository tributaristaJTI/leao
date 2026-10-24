# Publicação · Prompt 1.3 · índice das rodadas

Gerado em 22/10/2026. Nada foi publicado. 22 skills avulsas e 1 plugin.

## Estado antes de publicar

- **Validação:** `claude plugin validate --strict` aprovado em `skills/`, em cada skill alterada e no plugin.
- **Testes:** **não rodados.** O Prompt 1.3 pressupõe "passaram na validação e nos testes", mas a suíte da `crivo-do-leao` (`claude plugin eval`) ainda não foi montada. Validar confere a estrutura, não o comportamento. Publicar antes dos testes é decisão de Leonardo.
- **Colisão:** o manifesto da conta em 22/10 tem as mesmas datas de atualização da cópia de trabalho. Nenhuma skill foi editada no chat depois da cópia, e cada cartão substitui a versão em vigor sem perder edição posterior.

## Fatos conferidos em 22/10/2026 (rodada 1)

1. **O cartão preserva `references/`.** A atualização pelo cartão troca a SKILL.md e mantém a pasta `references/` da skill em vigor. Conferido na `voz-autoral-leonardo`: depois da publicação, as quatro referências sincronizadas são idênticas às do repositório.
2. **O campo descrição do cartão sobrescreve a `description` do frontmatter** (cabeçalho da SKILL.md). O que vale como gatilho da skill é o texto digitado no cartão, não o do arquivo proposto.

Consequências para as próximas rodadas: (a) ao montar cada cartão, o campo descrição recebe exatamente a `description` do frontmatter da seção 1, desdobrada numa linha só; (b) a conferência pós-publicação compara a `description` também, porque é ali que um desvio do cartão aparece.

## Fatos conferidos em 23/10/2026 (rodada 2)

3. **O cartão só altera a SKILL.md; `references/` e `assets/` ficam como estavam.** Este fato completa o 1: arquivo de apoio alterado não sobe pelo cartão. Correção que estiver em arquivo de apoio vai para a SKILL.md, como regra de leitura do arquivo antigo.
4. **A `crivo-do-leao` está com `references/modo-social.md` na versão antiga na conta.** O critério 1 do eixo S2 ainda transcreve a lista de anti-padrões. Tratamento: frase na seção "Comandos" da SKILL.md que manda ler esse critério como remissão à seção "Proibições globais de estilo" da `voz-autoral-leonardo`; republicação na rodada 8.
5. **A `briefing-juridico` mantém `assets/template-timbrado.docx`, inerte.** A SKILL.md publicada não aponta mais para ele. Retirada, se Leonardo quiser, só pelo painel da skill.

Com isso, o repositório passa a espelhar os arquivos de apoio da conta: `crivo-do-leao/references/modo-social.md`, `monitor-carf/references/tarefa-agendada.md` e `briefing-juridico/assets/` voltaram à versão sincronizada, e as correções que estavam neles moram na SKILL.md.

## Rodadas publicadas

| Rodada | Skills | Conferência |
|---|---|---|
| 1 | mod-ibs-cbs-diferimento, braco-direito, voz-autoral-leonardo | 22/10: corpo idêntico; frontmatter igual descontadas aspas no `name`, dobra da `description` e quebra de linha final. A dobra do repositório inseria um espaço em "científico- dissertativo"; a versão publicada está correta, e o repositório foi alinhado a ela. |
| 2 | destila, briefing-juridico, crivo-do-leao | 23/10: as três SKILL.md batem (mesmos critérios da rodada 1). Arquivos de apoio da conta inalterados (fatos 3 a 5). A `crivo-do-leao` volta na rodada 8 com a frase de remissão. |
| 3 | mod-ir-venda-imovel, mod-funrural, mod-comparativo-pf-pj | 24/10: as três SKILL.md batem (mesmos critérios); arquivos de apoio inalterados; repositório alinhado ao cabeçalho publicado. |
| 4 | mod-grupo-economico, cerebro-pbc, regra-matriz | 24/10: as três SKILL.md batem (mesmos critérios); a `cerebro-pbc` sincronizou às 13:50 UTC, depois das outras duas; arquivos de apoio inalterados; repositório alinhado ao cabeçalho publicado. |
| 5 | fiel-da-balanca, monitor-carf, artigo-juridico | 2026-10-24: corpo após o frontmatter e `description` idênticos nas três; arquivos de apoio inalterados (o `tarefa-agendada.md` da `monitor-carf` segue na versão da conta, como previsto); repositório alinhado ao cabeçalho publicado. |
| 6 | entregavel-cliente, guardiao-de-caso, agint-aresp | 2026-10-24: corpo após o frontmatter e `description` idênticos nas três; arquivos de apoio inalterados; repositório alinhado ao cabeçalho publicado. |
| 7 | parecer-aem, pesquisa-gcap, tributarista-consultivo | 2026-10-24: corpo após o frontmatter e `description` idênticos nas três; arquivos de apoio inalterados (inclusive `assets/`, `references/` e `scripts/` da `parecer-aem`); repositório alinhado ao cabeçalho publicado. |

## Rodadas (até três cartões por rodada, das mudanças de maior efeito para as menores)

| Rodada | Arquivos em `relatorios/publicar/` | Por que nesta ordem |
|---|---|---|
| 1 | `mod-ibs-cbs-diferimento.md`, `braco-direito.md`, `voz-autoral-leonardo.md` | Reescrita, troca de destinatário e fonte única de estilo |
| 2 | `destila.md`, `briefing-juridico.md`, `crivo-do-leao.md` | Etapa nova, migração de layout, remissão no Modo Social |
| 3 | `mod-ir-venda-imovel.md`, `mod-funrural.md`, `mod-comparativo-pf-pj.md` | Módulos de cálculo: fonte conferida |
| 4 | `mod-grupo-economico.md`, `cerebro-pbc.md`, `regra-matriz.md` | Módulo restante; nome de modelo; marcadores |
| 5 | `fiel-da-balanca.md`, `monitor-carf.md`, `artigo-juridico.md` | Marcador; parágrafo padrão e leitura do modelo da tarefa agendada na SKILL.md (o arquivo de apoio fica como está na conta); parágrafo padrão |
| 6 | `entregavel-cliente.md`, `guardiao-de-caso.md`, `agint-aresp.md` | Só o parágrafo padrão |
| 7 | `parecer-aem.md`, `pesquisa-gcap.md`, `tributarista-consultivo.md` | Só o parágrafo padrão |
| 8 | `tributarista-contencioso.md`, `crivo-do-leao.md` | Parágrafo padrão; republicação da crivo com a frase de remissão do modo social |
| à parte | `_plugin-ecossistema-do-leao.md` | Plugin: novo envio pela tela de plugins, sem cartão |

Arquivos de apoio: pelos fatos 1 e 3, o cartão não toca `references/` nem `assets/`. Toda correção destinada a arquivo de apoio entra na SKILL.md como regra de leitura (feito na `crivo-do-leao` e na `monitor-carf`). Os arquivos de publicação levam só a SKILL.md.

## Passo 0 nos módulos (aberto em 24/10; não executar)

**Status:** planejado. Rodada própria, depois da 8, só com aprovação de Leonardo.

**O quê:** `mod-ir-venda-imovel`, `mod-funrural`, `mod-comparativo-pf-pj` e `mod-grupo-economico` ganham o Passo 0, a tabela de parâmetros com fonte e status, no modelo da `mod-ibs-cbs-diferimento` publicada na rodada 1. Assim, o corpo da skill deixa de entregar alíquota pronta. Cada alíquota, faixa, limite e prazo passa a ser parâmetro conferido no Jusratio ou na fonte oficial consolidada; o que não for conferido roda como cenário marcado [A CONFERIR: fonte].

**Escopo levantado em 24/10** (linhas do corpo com percentual ou valor monetário fixo):

| Módulo | Linhas | Exemplos do que vira parâmetro |
|---|---|---|
| mod-ir-venda-imovel | 12 | faixas e alíquotas do ganho de capital, percentual de redução por ano de aquisição, alíquota da atividade rural |
| mod-funrural | 9 | composição do Funrural PF e PJ (INSS, RAT, SENAR), contribuição sobre a folha, graus de RAT |
| mod-comparativo-pf-pj | 15 | tabela do IRPF, Funrural, IRPJ e adicional, CSLL, PIS/COFINS |
| mod-grupo-economico | 0 | nenhuma alíquota fixa no corpo; o Passo 0 reúne os parâmetros que o módulo herda dos outros três e as alíquotas de ITCMD do estado envolvido |

**Marcador de dispositivo não conferido (entra na rodada 9):** uniformizar em [A CONFERIR: fonte] o marcador da `cerebro-pbc` (S1, "⚠️ verificar contra texto oficial") e da `regra-matriz` (regra geral 1, "⚠️ Verificar contra texto oficial."), que ainda convivem com [A CONFERIR: fonte] nas mesmas skills. Escaparam da varredura do pendente 5, que procurou as formas "[verificar]" e "citado de memória".

**agint-aresp no mesmo lote (rodada 9):** o corpo traz dispositivos e prazos escritos: arts. 1.021, 1.003 (§ 5º) e 219 do CPC; art. 39 da Lei 8.038/1990; Súmulas 182, 281, 315 e 316. Na mesma conferência de 24/10 apareceram ainda o art. 258 do RISTJ, o art. 798 do CPP, o art. 1.035-A do CPC, a Lei 15.484/2026 e a Súmula 7. A seção "Conteúdo volátil" está datada de 19/08/2026 e o gatilho de revisão era setembro/2026, já vencido. Tratamento: os prazos e dispositivos do corpo viram parâmetros do Passo 0, com fonte e status; o "Conteúdo volátil" é reverificado no Jusratio e na fonte oficial, e ganha nova data e novo gatilho. A agint-aresp não é módulo de cálculo, então o Passo 0 dela confere o rito e os prazos, e não alíquotas.

**Candidatas a uniformização de rótulo "mapa, não fonte" (rodada 9):** citação escrita no corpo passa a ter o mesmo rótulo dos módulos (decisão 1 do laudo): indica onde conferir, e não vale como fonte.
- `pesquisa-gcap`: dispositivos escritos no Questionário canônico, Q1 a Q9 (linhas 37 a 45 da versão de 24/10).
- `parecer-aem`: o exemplo de interação cita CF, art. 195, e Lei 10.833/2003 como fundamentação (linha 98 da versão de 24/10).

**Como fazer quando aprovado:** reescrever por proposta ao lado da atual, como na decisão 9 do laudo; Leonardo aprova; arquivos de publicação novos; rodada 9 de cartões. A `description` de cada módulo fica igual.

## Prompt para o chat do Claude (uma rodada por vez)

Com o repositório tributaristaJTI/leao conectado à conversa:

```
Leia relatorios/publicar/<arquivo 1>, <arquivo 2> e <arquivo 3>. Para cada um, proponha a skill como atualização da skill existente de mesmo nome, com a SKILL.md completa da seção 1. Mostre o resumo da seção 2 junto do cartão. No campo descrição de cada cartão, use exatamente a description do frontmatter da seção 1, em uma linha só, porque esse campo sobrescreve a do arquivo.
```

## Depois de cada rodada

Na sessão seguinte do Code, a cópia em `~/.claude/skills/synced/*/<nome>/` traz a versão nova. Conferir com `diff` contra `skills/<nome>/SKILL.md`; batendo, commit "publicada v<n>: <nome>".
