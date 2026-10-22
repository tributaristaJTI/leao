# Limites por destino

Origem: Inventário do Ecossistema (Camada 4) e Diário de Fricção do project Arquiteto, estado de 2026-10-21. Em divergência, vale o Inventário vivo no Drive; esta cópia é atualizada quando o Arquiteto registrar limite novo.

## Regras comuns a todo destino
- Arquivo e pasta do Google Drive são referenciados por ID, nunca só por nome (a busca por nome falha em arquivo recente).
- Nenhum executor apaga arquivo. Mover e renomear, sim.
- Arquivo gravado no Drive segue a regra de residência: documento vai para `Arquivo AeM/` (ou `_Entrada/` sem subpasta), tese vai ao Acervo, estado de project vai à pasta do project. Saída dentro de aplicativo (Monday, Notion, Make) fica no aplicativo.

## Conversa nova do Claude (claude.ai)
- Não enxerga esta conversa: contexto, decisões e definições precisam estar no prompt.
- Anexo não viaja: o prompt diz quais arquivos anexar ou dá o ID do Drive.
- Skill aciona por comando ou descrição: quando uma skill específica deve ser usada, nomeá-la.

## Tarefa agendada (sessão em nuvem)
- Só conta com conectores em nuvem (Drive, Notion, Monday, Gmail, Calendar, Zapier e afins). Sem Chrome, sem ponte com o Mac, sem painel interativo.
- Não pode perguntar nada: o prompt é autossuficiente e traz decisão padrão para cada dúvida previsível ("na dúvida, mover para `_revisar/` e relatar").
- Saída em arquivo no Drive, pasta indicada por ID, ou no aplicativo de destino.
- Pesquisa na internet por busca web, não por navegador.

### Régua de custo (também usada pelo /auditoria custo do Arquiteto)
Cada execução paga o contexto inteiro a cada chamada de ferramenta; modelo, tamanho da conversa e conectores são fatores de consumo declarados na documentação da Anthropic. O prompt de tarefa agendada cumpre, nesta ordem:
- (a) Frequência: não rodar quando não há chance de novidade; se a janela de consulta cobre o intervalo (ex.: consulta de 10 dias), dias úteis bastam, e a execução de segunda amplia a janela para cobrir o fim de semana.
- (b) Saída antecipada: checagem barata de novidade (listagem só com metadados, sentinela) antes de qualquer leitura pesada; sem novidade, relatório de três linhas e encerrar.
- (c) Coleta determinística: quando houver script ou consulta estruturada, a coleta e o filtro ficam no código e só o delta entra no contexto; registrar o que já foi visto para não reprocessar nem repetir.
- (d) Conectores: a tarefa herda os conectores da conversa em que nasceu, e a atualização não os altera; criar a tarefa a partir de conversa com acesso restrito ao que ela usa.
- (e) Modelo: o menor que sustenta o julgamento exigido, com o motivo escrito; troca só por pedido expresso do Leonardo.
- (f) Chamadas: agrupar consultas, ler em paralelo, nenhuma rodada para descobrir ferramenta que a sessão não tem; no máximo duas tentativas por URL.
- (g) Emissão: nada emitido duas vezes; arquivo publicado é editado por trecho, não reescrito inteiro; registro só-acréscimo não é reemitido inteiro.
- (h) Valor: entrega com destino lido por alguém (pasta por ID, aplicativo, aviso); sem leitor, a tarefa é candidata a desligar.

## Cowork
- Alcança arquivos locais do Mac e o espelho do Drive.
- Mudança de estado em lote segue três fases no próprio prompt: mapear, propor e pausar, executar só depois da ratificação.
- Sessão longa: o prompt diz qual arquivo de estado ler na abertura e qual gravar no fechamento.

## Claude Code e subagente
- Janela isolada: recebe só o prompt. Passar caminhos, o critério de pronto e o formato do que deve ser devolvido.
- Subagente devolve resultado a quem o chamou, não ao usuário: pedir saída curta e estruturada.

## Agente OpenAI (Codex, ChatGPT)
- Diretório de trabalho fora do `Arquivo AeM/` (por exemplo `~/Documents/Codex`); só o arquivo final é copiado para a `_Entrada/`.
- Marca de origem no nome do arquivo: `_codex` para o Codex, `_gpt` para o ChatGPT.
- Não conhece as skills nem as convenções do ecossistema: o que importar delas vai escrito no prompt.

## Pessoa da equipe
- Glosar sigla, código interno e nome de skill na primeira ocorrência.
- Dizer dono, prazo, formato da devolução e a quem perguntar em caso de dúvida.
