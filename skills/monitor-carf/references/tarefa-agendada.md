# Tarefa agendada, calendário e teste de aceite

## 1. A tarefa

Uma tarefa só, em dias úteis, no lugar das três antigas. Sugestão de
configuração: nome "Monitor CARF — pauta do dia"; de segunda a sexta, cedo;
modelo Sonnet (coleta e triagem não pedem modelo maior, e o custo fixo de
abrir a sessão se paga cinco vezes por semana).

O texto abaixo vai inteiro no campo de instruções da tarefa. Os endereços
estão no texto da tarefa, e não só aqui, porque a ferramenta de requisição
pode aceitar apenas endereço escrito pelo usuário. Os três usam data relativa
do próprio índice (`NOW-10DAYS`), então não precisam ser reescritos a cada dia.

```text
Rode a skill monitor-carf no modo agendado: /carf agendado

Regras desta execução:

1. Não pergunte nada. O que exigiria pergunta vai para o campo Obs da base ou para a linha "Atenção" da mensagem final.

2. Calendário: segunda-feira inclui /carf repasse; quarta-feira inclui /carf antecipa; sexta-feira inclui /carf serie; primeiro dia útil do mês inclui /carf sem-data.

3. Canal. Primeiro tente a consulta direta por execução de código, na pasta da skill monitor-carf. Rode `python3 scripts/coleta_ver.py versao`. Se responder 0.2 ou mais: faça a consulta da base do Passo 2 da skill e grave os números já registrados, um por linha, em /tmp/carf_ja_na_base.txt; rode `python3 scripts/coleta_ver.py sentinela` e, se responder, `python3 scripts/coleta_ver.py coleta --excluir /tmp/carf_ja_na_base.txt` (na segunda-feira, também `coleta --dias 35 --excluir /tmp/carf_ja_na_base.txt`, que é o repasse). Se o subcomando versao não existir (pacote antigo), rode `sentinela` e `coleta` como antes. Se o script encerrar com FALHA DE CANAL, ou a sessão não tiver execução de código, use a ferramenta de requisição web com os endereços abaixo, que eu autorizo, exatamente como estão escritos; se o resultado trouxer numFound maior que o número de linhas devolvidas, diga na linha "Atenção" que a coleta por esse transporte foi parcial. Se ela recusar, não insista: siga a cascata de canais da skill (navegador, depois Jusratio). Diga na mensagem final qual canal e qual transporte usou.

Sentinela (última data de publicação):
https://acordaos.economia.gov.br/solr/acordaos2/select?wt=json&rows=1&q=*:*&fq=dt_publicacao_tdt:%5BNOW-45DAYS%20TO%20NOW%2B1DAY%5D&sort=dt_publicacao_tdt%20desc&fl=numero_decisao_s,dt_publicacao_tdt

Rede rural, últimos 10 dias:
https://acordaos.economia.gov.br/solr/acordaos2/select?wt=json&rows=100&q=%28_texto:%22atividade%20rural%22%20OR%20_texto:%22produtor%20rural%22%20OR%20_texto:%22im%C3%B3vel%20rural%22%20OR%20_texto:%22propriedade%20rural%22%20OR%20_texto:funrural%20OR%20_texto:senar%20OR%20_texto:%22produ%C3%A7%C3%A3o%20rural%22%20OR%20_texto:%22arrendamento%20rural%22%20OR%20_texto:%22parceria%20rural%22%20OR%20_texto:%22parceria%20agr%C3%ADcola%22%20OR%20_texto:%22parceria%20pecu%C3%A1ria%22%20OR%20_texto:%22imposto%20sobre%20a%20propriedade%20territorial%20rural%22%20OR%20_texto:%22imposto%20territorial%20rural%22%20OR%20_texto:%22valor%20da%20terra%20nua%22%20OR%20_texto:agroind%C3%BAstria%20OR%20_texto:%22segurado%20especial%22%20OR%20_texto:agroindustrial%20OR%20_texto:cerealista%20OR%20_texto:%22cooperativa%20agropecu%C3%A1ria%22%20OR%20%28_texto:%22cr%C3%A9dito%20presumido%22%20AND%20_texto:%22in%20natura%22%29%29&fq=dt_publicacao_tdt:%5BNOW-10DAYS%20TO%20NOW%2B1DAY%5D&sort=dt_publicacao_tdt%20desc&fl=numero_decisao_s,numero_processo_s,turma_s,secao_s,dt_sessao_tdt,dt_publicacao_tdt,nome_relator_s,ementa_s,nome_arquivo_pdf_s

Rede patrimonial, últimos 10 dias:
https://acordaos.economia.gov.br/solr/acordaos2/select?wt=json&rows=100&q=%28_texto:%22integraliza%C3%A7%C3%A3o%20de%20capital%22%20OR%20_texto:%22integraliza%C3%A7%C3%A3o%20de%20bem%20im%C3%B3vel%22%20OR%20_texto:%22confer%C3%AAncia%20de%20bens%22%20OR%20_texto:holding%20OR%20_texto:%22aliena%C3%A7%C3%A3o%20fiduci%C3%A1ria%22%20OR%20_texto:%22consolida%C3%A7%C3%A3o%20da%20propriedade%22%20OR%20_texto:adjudica%C3%A7%C3%A3o%20OR%20_texto:arremata%C3%A7%C3%A3o%20OR%20_texto:%22da%C3%A7%C3%A3o%20em%20pagamento%22%20OR%20_texto:%22adiantamento%20de%20leg%C3%ADtima%22%20OR%20_texto:%22antecipa%C3%A7%C3%A3o%20da%20leg%C3%ADtima%22%20OR%20_texto:usufruto%20OR%20_texto:%22devolu%C3%A7%C3%A3o%20de%20capital%22%20OR%20_texto:%22redu%C3%A7%C3%A3o%20de%20capital%22%20OR%20_texto:%22prop%C3%B3sito%20negocial%22%20OR%20_texto:%22distribui%C3%A7%C3%A3o%20disfar%C3%A7ada%20de%20lucros%22%20OR%20_texto:%22equipara%C3%A7%C3%A3o%20a%20pessoa%20jur%C3%ADdica%22%29&fq=dt_publicacao_tdt:%5BNOW-10DAYS%20TO%20NOW%2B1DAY%5D&sort=dt_publicacao_tdt%20desc&fl=numero_decisao_s,numero_processo_s,turma_s,secao_s,dt_sessao_tdt,dt_publicacao_tdt,nome_relator_s,ementa_s,nome_arquivo_pdf_s

Página de busca: https://acordaos.economia.gov.br
Consulta de jurisprudência do CARF: https://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf

4. Entrega: a mensagem final no formato da skill, com o canal usado, a contagem e no máximo uma ficha de pauta. Sem texto de post.
```

As âncoras têm fonte única em `scripts/coleta_ver.py`; os dois endereços de
rede acima foram gerados por `python3 scripts/coleta_ver.py urls` em
21/10/2026, na v0.2 (uma grafia por âncora, porque o índice ignora acento e
trata plural; âncoras da trilha 13 incluídas; até 100 linhas por endereço,
porque este transporte não pagina). Se uma âncora mudar no script,
regerar e colar de novo no texto da tarefa. Eles cobrem só as âncoras de cada
rede; a base de termos do Notion continua sendo a referência para a triagem.

A tarefa criada com o texto da v0 continua funcionando: os endereços antigos
são equivalentes. O que ela não faz é tentar a execução de código primeiro;
para isso, trocar o texto da tarefa por este.

## 2. Calendário

| Dia | Além da execução padrão |
|---|---|
| Segunda | `/carf repasse` (35 dias) |
| Quarta | `/carf antecipa` (propostas de súmula, súmulas, pautas) |
| Sexta | `/carf serie` e a contagem da regra de parada |
| Primeiro dia útil do mês | `/carf sem-data` |

O repasse e a fila sem data rendem mais com navegador. Se cair em dia sem
navegador, a execução avisa, e o Leonardo pode rodar `/carf repasse` à mão
com o computador aberto.

## 3. Teste de aceite (`/carf teste`)

Rodar uma vez sob demanda antes de ligar a tarefa, e de novo depois de
06/10/2026, quando as tarefas passam a rodar na nuvem.

**Parte A — canais.** Tentar os quatro e devolver uma tabela: canal, respondeu
ou não, erro literal se houve, data de publicação mais recente vista.

0. VER direto (código): `python3 scripts/coleta_ver.py sentinela`. Se
   encerrar com FALHA DE CANAL, copiar a mensagem de erro inteira.
1. VER direto (requisição): buscar o endereço da sentinela.
2. VER navegador: dizer se há navegador na sessão; se houver, abrir a página
   de busca e repetir a sentinela de dentro dela.
3. Jusratio: uma busca no tribunal CARF por "funrural" com data inicial de 120
   dias atrás; informar a publicação mais recente devolvida.

**Parte B — três acórdãos de referência.** O comando tem de achar sozinho, e
dizer por qual canal e por qual termo:

| Acórdão | Por que está na lista |
|---|---|
| 2102-004.232 | Funrural com sub-rogação. Publicado em 29/05/2026 segundo o SINCON e sem data no VER: foi o caso que expôs a falha de cobertura em 03/09/2026. |
| 2401-012.623 | Ganho de capital em imóvel rural, valor da terra nua e benfeitorias. Analisado pelo Leonardo em 14/08/2026. |
| 1201-007.725 | Holding patrimonial e venda de imóvel, 1ª Seção, sem marcador rural. Noticiado por site especializado em 24/09/2026, antes de qualquer alerta do monitor. |

Acórdão não achado não reprova a skill: mostra qual canal ou qual termo
precisa de ajuste. Registrar o resultado na mensagem, sem gravar linha de
teste na base.

**Parte C — Notion.** Ler a base de termos e informar quantos estão ativos
(em 30/09/2026 eram 123 expressões de busca ativas, mais 5 etiquetas e 5
exclusões). Não gravar nada.

## 4. Depois do teste

- Canal 1 respondeu, por código ou por requisição: a tarefa roda sozinha, de
  qualquer lugar.
- Só o canal 2 respondeu: a tarefa depende do aplicativo de desktop aberto no
  horário. Ajustar o horário para quando o computador costuma estar ligado.
- Só o canal 3 respondeu: a tarefa roda, com cobertura por relevância e
  atraso. O repasse de segunda passa a ser manual, com navegador.

Em seguida, rodar `/carf calibra` uma vez (com canal exaustivo) para medir os
termos e podar o que retorna zero ou só ruído.

## 5. Resultado da primeira execução manual (30/09/2026)

- **Canal 1 (VER direto):** recusado pela ferramenta de requisição, três vezes,
  com "This URL was not in any prior search or fetch result". Na conversa, o
  endereço da sentinela estava só em arquivo escrito pelo assistente, o que não
  conta como endereço fornecido pelo usuário. O teste valendo exige colar o
  endereço da sentinela numa mensagem do chat, ou a primeira execução da
  tarefa agendada, em que o endereço vem no texto escrito pelo usuário.
- **Canal 2 (VER navegador):** funcionou pela extensão claude-in-chrome. Índice
  com 3.338 acórdãos publicados nos últimos 45 dias; publicação mais recente
  25/09/2026. Rede rural: 43 acórdãos; rede patrimonial: 6; 48 únicos; 13
  grupos registrados (44 acórdãos).
- **Parte B:** o 1201-007.725 foi achado sozinho (publicado em 23/09/2026,
  antes da notícia de 24/09). Os outros dois acórdãos de referência ficam fora
  da janela de 10 dias e não foram testados.
- **Canal 3 (Jusratio):** busca respondeu; leitura de documento falhou duas
  vezes por falta de aprovação.

## 6. Medição de 06/10/2026 (conversa do claude.ai, project Arquiteto)

- **VER direto (código):** respondeu. Sentinela: 3.834 registros em 45 dias,
  última publicação 02/10/2026. Coleta de 10 dias: 505 registros na janela, 35
  sem texto pesquisável, nenhum com inteiro teor no índice; 23 candidatos
  únicos nas duas redes.
- **SINCON:** a página respondeu por execução de código; formulário não
  testado.
- **Não medido:** se a sessão agendada em nuvem tem a mesma rede. É a
  pergunta que a Parte A do teste responde na primeira execução agendada. Se
  o 1a falhar lá e o 1b também, a tarefa depende do aplicativo de desktop
  aberto (item 4 acima).
