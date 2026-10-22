---
name: monday-caso
description: Registra projetos de clientes (grupos familiares) no Monday com a estrutura padrão da Amaral e Melo + Agricompany — board por fases, colunas canônicas, itens extraídos dos documentos do caso, automações de alerta e bloco na Google Agenda. Use SEMPRE que o usuário digitar /monday-caso, ou pedir para "registrar o caso no Monday", "criar o board do cliente", "lançar o projeto da família X no Monday", "abrir esse caso no Monday", ou qualquer variação de registro/atualização de projeto de cliente no Monday. NÃO use para indicadores e OKRs do escritório (governanca-leao), timesheet (ponto-do-leao) nem produção de peças jurídicas.
---

# Monday Caso — Registro padronizado de projeto de grupo familiar

## Função

Transformar um caso de planejamento sucessório/patrimonial em um board de projeto no
Monday que conta a história real do caso: o que já foi feito, o que está travado e o que
vem na semana. O board nasce dos documentos, nunca de um modelo genérico.

## Entrada

Bloco `<caso>` do usuário (todos os campos aceitos em linguagem livre):

```
FAMÍLIA / CLIENTE:            [obrigatório]
PASTA DO CASO:                [pasta conectada | "vou anexar" | vazio]
OBJETO DO PROJETO:            [default: planejamento sucessório e patrimonial]
RESPONSÁVEL(IS):              [default: o próprio usuário]
TAREFAS DA PRÓXIMA SEMANA:    [lista livre]
ALERTA:                       [dia e período/hora; ex.: segunda à tarde = 14:00]
```

Se faltar campo crítico (família, tarefas ou alerta), fazer UMA única rodada de
perguntas via AskUserQuestion. O resto segue por default e vira `[A CONFIRMAR]`.

## Auto-detecções (executar sempre, nesta ordem)

1. **Board existente** — antes de criar qualquer coisa, buscar board com o nome da
   família (tool `search`, searchType BOARDS). Se existir, entrar em **modo
   atualização**: não recriar estrutura; adicionar itens novos, atualizar situações e
   registrar as tarefas da semana no grupo de topo. Nunca duplicar board de cliente.
2. **Sem documentos** — se não houver pasta conectada nem legível, entrar em **modo
   coleta**: criar o board com a estrutura padrão, grupos vazios, e lançar apenas itens
   de coleta (checklist do que pedir ao cliente), citando a skill coleta-inteligente.
3. **Múltiplos responsáveis** — se houver mais de um nome, distribuir os itens por
   Frente (Societário, Fiscal, Contratos...) conforme indicado e notificar cada um na
   criação. Cada item tem UM responsável; nunca dois.

## Protocolo

**0. Ferramentas.** Carregar em UMA chamada de ToolSearch:
`get_user_context, search, create_board, create_column, create_group, create_items,
create_update, create_automation, change_item_column_values` (Monday) e
`list_calendars, create_event` (Google Calendar, se houver ALERTA).

**1. Ler o caso antes de registrar.** Varrer a pasta e ler o que define a estrutura:
contratos sociais e alterações, organograma, árvore genealógica, relatórios de
planejamento, memorandos fiscais, contratos de exploração, decisões. Arquivo ilegível =
reportar qual e por quê, nunca supor. Fechar com resumo de 5 linhas antes de prosseguir.

**2. Board.** Nome: `Família [SOBRENOME] — [Objeto]`. Workspace principal, usuário como
dono. Descrição: empresas com CNPJ, patrimônio em números (dos documentos), frentes de
trabalho e `CONFIDENCIAL — USO INTERNO`. Board público na conta; oferecer privado se
houver outros membros e o caso for sensível.

**3. Colunas (nesta ordem), capturando o `column_id` de CADA resposta de criação** —
não depender de get_board_info:

| Coluna | Tipo | Conteúdo |
|---|---|---|
| Situação | status | Não iniciado · Em andamento · **Aguardando terceiro** · Travado · Concluído |
| Responsável | people | dono único |
| Prazo | date | data-limite |
| Prioridade | status | Crítica · Alta · Média · Baixa |
| Frente | dropdown | Societário · Fiscal/Cadastral · Contratos · Sucessão · Governança |
| Lembrete | date | data COM hora (alimenta a automação) |
| Observações | long_text | uma linha; análise vai no Update |
| Última atualização | last_updated | detecta item parado |

"Aguardando terceiro" é obrigatório: cartório, junta, fisco e contador são metade da
vida de um caso desses, e sem esse status tudo parado vira falso "Travado".

**4. Grupos por fase, de cima para baixo** (topo = mais ativo, onde itens novos caem):
`🎯 Foco da Semana ([datas])` · `⚖️ Sucessão e Governança` · `🏛️ Societário —
Alterações e Registro` · `💰 Fiscal e Cadastral` · `📄 Contratos de Exploração` ·
`✅ Concluído`. Excluir (ou esvaziar e avisar) os grupos default do board.

**5. Itens em LOTE** (`create_items`, até 20 por chamada, `createLabelsIfMissing:
true` na primeira leva). Cada item: verbo no infinitivo + objeto específico do caso
("Corrigir a matrícula 8.560 no contrato social", nunca "Revisar contratos"). Registrar
também as etapas VENCIDAS no grupo Concluído — o board conta a história. Concluído só
com comprovação documental. Divergência entre documentos vira item próprio, prioridade
alta, com as duas versões citadas.

**6. Contexto nos Updates, nunca no nome.** Para cada tarefa da semana e pendência
crítica: objetivo, problema concreto (cláusula, matrícula, processo, dispositivo — só
com certeza; na dúvida, "conferir"), pontos a verificar, onde está a prova. Tarefas
interdependentes declaram isso nos dois Updates.

**7. Tarefas da semana** no grupo de topo: prazo na sexta da semana indicada,
prioridade Alta, responsável definido, Lembrete na data e hora do ALERTA.

**8. Automações (3), sempre com hora explícita e fuso America/Sao_Paulo** — a
automação de data SEM hora devolve pedido de esclarecimento e desperdiça uma rodada:
- Lembrete chegou → notificar responsável na hora do alerta;
- Prazo chegou → notificar às 09:00;
- Situação virou Travado → notificar imediatamente.

**9. Agenda (se houver ALERTA).** UM bloco de 1h na agenda principal, no dia/hora do
alerta, com as tarefas e os links dos itens na descrição, pop-up 15 min antes,
disponibilidade ocupado. Avisar: evento estático; a integração nativa Monday↔Agenda, se
ativada depois, duplicaria — apagar o manual antes.

**10. Fechamento.** Relatório em uma tela: link do board · itens por grupo · automações
ativas · lista `[A CONFIRMAR]`. Em seguida, registrar a sessão via ponto-do-leao
(disparo automático, sem perguntar), cliente = slug da família.

## Regras invioláveis

Não inventar dado, data, CNPJ, matrícula, processo ou dispositivo legal. Informação
faltante = `[A CONFIRMAR — o quê]`, nunca estimativa. Nada de Concluído sem documento.
Conteúdo sigiloso: nada sai do board, dos Updates e da agenda do usuário. Em modo
atualização, jamais apagar item existente — só mudar situação e comentar.
