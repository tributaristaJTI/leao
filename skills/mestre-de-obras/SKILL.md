---
name: mestre-de-obras
description: "Planejador de projetos de cliente (Amaral e Melo + Agricompany). Lê ata, briefing ou extração da atas-leao e monta o plano de trabalho em dois níveis: macro (antes da proposta: fases, escopos candidatos, complexidade, esforço, gatilhos) e execução (após o aceite: tarefas, perfil de executor, delegabilidade, dependências, prazos relativos), sempre com lacunas nomeadas, e entrega o bloco caso pronto para a monday-caso. Use SEMPRE que o usuário digitar /plano, /plano macro ou /plano execucao, ou pedir 'monta o plano de trabalho', 'plano de ação do caso', 'fases do projeto', 'o que dá pra delegar', 'quem faz o quê', 'dimensiona esse caso', 'complexidade do projeto', 'escopo do projeto', ou qualquer planejamento da execução de projeto de cliente (tributário, societário, sucessório, transação de fazenda, consultoria Agricompany). NÃO use para registrar no Monday (monday-caso), precificar (proposta-aem), extrair ata (atas-leao) nem produzir análise jurídica. O mestre-de-obras planeja o trabalho; não o executa."
---

# Mestre de Obras — plano de trabalho de projeto de cliente

## 1. Função e posição na cadeia

Transformar a leitura de um atendimento em plano de trabalho padronizado, no lugar do desenho caso a caso. A skill ocupa o meio de uma cadeia cujas pontas já existem:

```
leitura (ata via /ata da atas-leao | /comercial ou /operacional da briefing-juridico | extração pronta)
   → /plano macro  ........ dimensiona: fases, escopos candidatos, complexidade, esforço, gatilhos, lacunas
   → proposta-aem  ........ precifica sobre o macro, ou vende o Diagnóstico quando houver gatilho
   → aceite do cliente (opção escolhida = trilha contratada)
   → /plano execucao ...... expande só o escopo vendido em tarefas, perfis, delegação e prazos relativos
   → /monday-caso  ........ registra o board a partir do bloco <caso> que este plano entrega
```

Duas informações, dois donos: o **desenho** do projeto mora no `plano.md`; o **status de execução** mora no Monday. A skill nunca escreve status no plano nem desenho no Monday.

## 2. Entrada aceita

1. **Extração pronta da `atas-leao`** (decisões, ações com dono e prazo, pendências, riscos, defeitos da ata). Entrada preferida.
2. **Briefing da `briefing-juridico`**: `/comercial` (Briefing Comercial) para o nível macro; `/operacional` (Ficha Técnica) para o nível execução.
3. **Ata ou notas brutas**: a skill não extrai. Ela diz ao usuário "invocar `/ata` com este texto" e consome a extração quando ela voltar. Nunca chamada silenciosa entre skills (precedente A-06).

Para `/plano execucao` a entrada exige, além do plano v0, a **opção aceita pelo cliente** (trilha contratada). Sem ela, a skill para e pergunta só isso.

## 3. Os dois níveis

**v0, macro (pré-proposta).** Fases numeradas com entregável e critério de conclusão; dependências entre fases e com terceiros; perfis envolvidos por fase; faixa de esforço total e por fase; gatilhos de complexidade; escopos candidatos (opções A e B, cada uma como subconjunto de fases, no formato que a `proposta-aem` usa para escopo em opções); lacunas nomeadas. Sem tarefas, sem donos nominais, sem datas. É o insumo do Passo 1 (Leitura do Caso) da `proposta-aem`: complexidade, esforço, gatilhos e fases.

**v1, execução (pós-aceite).** Só o escopo vendido. Cada fase expandida em tarefas com perfil, delegabilidade, skill executora quando houver, dependência, prazo relativo a marco e prioridade; tarefas da primeira semana; bloco `<caso>` para a `monday-caso`. Mesmo arquivo, mesma pasta: o v0 fica preservado na seção de histórico do `plano.md`.

## 4. Protocolo `/plano macro`

0. **Pré-leitura.** Ler `references/plano-esquema.md` (esquema fixo) e `references/lacunas.md` (regra de lacuna). Identificar a **entidade dona** do projeto: AeM, Agricompany ou conjunto. Se a entrada não permitir decidir, é lacuna, não inferência.
1. **Ler a entrada** e fixar em cinco linhas: cliente, objeto, o que o cliente disse que quer, o que a leitura jurídica ou de gestão disse que precisa, e o que ninguém disse ainda.
2. **Escolher o fluxo** em `references/fluxos/`: `transacao-fazenda.md`, `sucessorio-patrimonial.md`, ou `_sem-fluxo.md` quando nenhum encaixar. Fluxo aponta para as skills donas do conteúdo; não copia método de nenhuma.
3. **Montar as fases** pelo esquema comum (id, nome, entregável, critério de conclusão, entradas, dependências, perfis, esforço, executor, frente Monday). Dependência sempre tipada: fase anterior, documento do cliente, decisão do cliente, decisão de sócio, terceiro (cartório, junta, banco, fisco, contador externo).
4. **Gatilhos de complexidade.** Aplicar os três gatilhos do Passo 2 da `proposta-aem` por remissão, sem reescrevê-los: protocolo da reforma (IBS/CBS), risco de planejamento abusivo, múltiplas entidades. Gatilho disparado faz o Diagnóstico pago ser a Fase 1 do plano, e as fases seguintes ficam condicionadas ao resultado dele.
5. **Perfis e esforço.** Perfis de `references/perfis.md`, por papel, nunca por nome. Esforço em faixa (P, M, G, GG), por fase e total; faixas provisórias, ver esquema.
6. **Escopos candidatos.** Opção A (mínimo que resolve a dor declarada) e Opção B (resolve a causa-raiz, normalmente com a Agricompany na raia de gestão ou governança). Cada opção lista as fases que inclui. Complexidade final no vocabulário do `/comercial` (baixa, média, alta).
7. **Lacunas.** Tudo o que a entrada não disse e o plano precisa: listar no formato de `references/lacunas.md`, com quem resolve e o que bloqueia. Nunca preencher.
8. **Gravar** `plano.md` v0 na pasta do caso (seção 7) e **entregar o handoff** à `proposta-aem`: complexidade, esforço total, gatilhos disparados, opções A e B com suas fases. A skill não precifica.

## 5. Protocolo `/plano execucao`

0. Ler o `plano.md` v0 e a opção aceita. Fases fora da opção aceita ficam listadas em "fora de escopo" e não geram tarefa.
1. **Expandir cada fase em tarefas**: verbo no infinitivo com objeto específico do caso ("Formalizar o arrendamento da Fazenda Boa Vista entre o patriarca e a Agro Guimarães Ltda.", nunca "Regularizar contratos"). Cada tarefa: id, fase, perfil, delegável (S ou N, com o motivo quando N), skill ou comando executor quando houver, dependência (outra tarefa ou terceiro), prazo relativo a marco (D+n após o aceite, após o recebimento do documento X, após o registro na junta), prioridade (Crítica, Alta, Média, Baixa).
2. **Nunca data absoluta sem âncora.** Data só quando o marco tem data conhecida, e marcada como derivada (regra herdada da `atas-leao`).
3. **Tarefas da primeira semana**: as que não dependem de nada externo, em ordem.
4. **Gravar** `plano.md` v1 no mesmo arquivo (cabeçalho atualizado, v0 preservado no histórico).
5. **Emitir o bloco `<caso>`** da `monday-caso` já preenchido: família ou cliente; pasta do caso; objeto; responsáveis (deixar o campo em perfil quando não houver pessoa nomeada; a `monday-caso` exige dono único por item); tarefas da próxima semana; alerta. Acrescentar a lista de grupos por fase do fluxo, para que a `monday-caso` não use os grupos fixos do sucessório quando o fluxo for outro (delta registrado em `deltas-fora-da-skill.md`).
6. **Fechamento**: relatório em uma tela (fases, número de tarefas por fase e por perfil, delegáveis, lacunas abertas) e registro da sessão via `ponto-do-leao`, disparo automático, cliente = slug do caso.

## 6. Precipitação: como os fluxos crescem

Plano montado com `_sem-fluxo.md` sai marcado no cabeçalho com "fluxo: sem-fluxo; família candidata: [nome]" e gera uma linha no arquivo `candidatos-a-fluxo.md` da pasta canônica (seção 7): data, cliente (slug), família candidata, fases usadas. Quando um segundo caso da mesma família aparecer, a skill aponta a coincidência e propõe a promoção a fluxo-padrão; a promoção é ratificação do Leonardo e vira arquivo novo em `references/fluxos/` na versão seguinte da skill. A skill não promove sozinha.

## 7. Onde grava

- **`plano.md`**: na pasta do dossiê do cliente (Guardião de caso, ao lado de `_estado.md` e `_ledger.md`) quando ela existir; senão, em `Ecossistema do Leão/Mestre de Obras/planos/` (ID `12tWxyYfRPMfLmOAuMS_RfRBel9xyVTdK`), um arquivo por caso, nome `[slug-do-caso] — plano.md`. Sempre `.md` com conversão desabilitada; localizar pasta por ID, nunca por nome.
- **`candidatos-a-fluxo.md`**: `Ecossistema do Leão/Mestre de Obras/` (ID `1D6ZlG0nR3m_oZO6-Nbnq9eFISzsvQfnl`). Como a integração do Drive não edita conteúdo, a atualização é arquivo novo com a versão anterior renomeada para `_historico/` (ID `1KiC3q07bmrU5ntBezeyjziug3eanrKGy`).

## 8. Regras invioláveis

1. **Lacuna se nomeia, não se preenche.** Sem dono, sem prazo, sem dado: marcar, nunca supor.
2. **Não precificar, não reabrir análise, não registrar no Monday.** Cada uma tem dona.
3. **Fluxo aponta, não copia.** O método de cada fase mora na skill dona (`porteira-fechada`, `mod-grupo-economico`, `tributarista-consultivo`, `coleta-inteligente`); o plano referencia o comando.
4. **Escopo do v1 é o escopo vendido.** Fase que o cliente não comprou não vira tarefa.
5. **Entidade dona declarada** em todo plano; "conjunto" exige a raia de cada casa explícita por fase.
6. **Perfil, não pessoa.** A atribuição nominal é da `monday-caso`, no registro.
7. **Uma fonte por informação**: desenho no `plano.md`, status no Monday, tese no acervo (via `destila`), preço na proposta.
