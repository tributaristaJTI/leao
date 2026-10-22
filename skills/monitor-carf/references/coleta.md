# Coleta — canais, cascata e método

Ler em toda execução. As notas do índice do CARF e do SINCON foram validadas
em sessão de 03/09/2026 (com navegador) e herdadas da instrução anterior. As
notas marcadas "06/10/2026" foram medidas por execução de código numa
conversa do claude.ai, com os domínios do CARF liberados na rede da conta. O
comportamento dos canais em tarefa agendada em nuvem ainda não foi medido:
`/carf teste` é o que mede.

## 1. Cascata de canais

Tentar nesta ordem e parar no primeiro que responder. Declarar o canal usado.

| Ordem | Canal | Cobertura | Quando serve |
|---|---|---|---|
| 1a | **VER direto (código)**: `scripts/coleta_ver.py` consulta o índice de dentro do ambiente de execução de código | exaustiva | sempre que a sessão tiver execução de código e a rede dela alcançar `acordaos.economia.gov.br` |
| 1b | **VER direto (requisição)**: a ferramenta de requisição web busca os endereços fixos do texto da tarefa | exaustiva | quando 1a falhar e a ferramenta aceitar o endereço |
| 2 | **VER navegador**: a mesma consulta feita de dentro da página | exaustiva | quando houver navegador na sessão (app de desktop aberto) |
| 3 | **Jusratio**: conector de jurisprudência | por relevância, com atraso | quando 1 e 2 falharem |

1a e 1b são o mesmo canal com dois transportes. Na base, os dois gravam
`Canal = VER direto` (não criar opção nova de seleção); a mensagem final diz
qual transporte foi usado.

Como rodar o 1a: `python3 scripts/coleta_ver.py versao` diz a versão do
script; `sentinela` devolve a última publicação; `coleta --excluir
/tmp/carf_ja_na_base.txt` faz a execução padrão (10 dias); `coleta --dias 35
--excluir ...` é o repasse; `coleta --de AAAA-MM-DD --ate AAAA-MM-DD` refaz uma
janela fixa; `numero <acórdão>` localiza um acórdão; `sem-data` lista a fila
sem data de publicação; `cobertura` confere se cada família do mapa de termos
é alcançada por alguma âncora. O script tenta três vezes, com espera, antes
de declarar falha (soluço de TLS medido em 21/10/2026 não é falha de canal). Se o script encerrar com "FALHA DE CANAL", a rede da
sessão não alcança o índice: seguir para 1b sem insistir. Medido em
06/10/2026 (conversa do claude.ai): índice respondendo, 3.834 registros em 45
dias, última publicação 02/10/2026.

VER é o nome do sistema de busca de acórdãos do CARF
(`https://acordaos.economia.gov.br`). SINCON é a consulta de jurisprudência do
próprio CARF, usada aqui só como conferência cruzada, e exige navegador.

Por que a ordem: o canal 1 funciona sem ninguém por perto e devolve tudo o que
casa com os termos, e o transporte por código vem antes porque monta qualquer
consulta na hora (janela, paginação, número do acórdão), sem depender de
endereço escrito na instrução; o 2 devolve o mesmo, mas depende do computador do
Leonardo ligado; o 3 funciona sempre, mas entrega os documentos mais
relevantes de cada pergunta (cerca de 11 por consulta em teste de 30/09/2026)
e recebe as publicações depois do VER. Em 30/09/2026, dois dos três acórdãos
de referência do teste de aceite (os dos processos 11634.720048/2018-35 e
17227.721247/2021-44) não foram achados no Jusratio pelo número do processo;
o primeiro tinha sido noticiado em 24/09. Quem quer chegar antes da imprensa
depende dos canais 1 ou 2.

Falha de canal não é resultado. Se o 1a encerrar com falha de rede e o 1b
recusar o endereço (erro de permissão ou de procedência da URL), passar ao 2
sem insistir. Se só o canal 3
responder, a mensagem final diz "cobertura por relevância" e a linha
"Atenção" registra que o repasse exaustivo ficou pendente.

## 2. Índice do CARF (VER) — o que se sabe

- Endpoint: `https://acordaos.economia.gov.br/solr/acordaos2/select?wt=json`.
- Campo de busca textual: **`_texto`** (inteiro teor). Não usar `conteudo_txt`
  nem o campo padrão.
- **`ementa_s` não é pesquisável.** É recuperável, mas `ementa_s:rural`
  retorna zero. Por isso a triagem de relevância é feita depois, lendo a
  ementa recuperada.
- Data de publicação: `dt_publicacao_tdt` (`AAAA-MM-DDT00:00:00Z`). Filtro:
  `fq=dt_publicacao_tdt:[INICIO TO FIM]`. O índice aceita data relativa:
  `[NOW-10DAYS TO NOW+1DAY]`. O limite superior em `NOW+1DAY` já descarta as
  datas absurdas que existem na base (há registro com ano 2209).
- Campos a recuperar (`fl`): `numero_decisao_s, numero_processo_s, turma_s,
  secao_s, dt_sessao_tdt, dt_publicacao_tdt, nome_relator_s, ementa_s,
  nome_arquivo_pdf_s`. Evitar `conteudo_txt` em massa.
- Inteiro teor: `https://acordaos.economia.gov.br/acordaos2/pdfs/processados/{nome_arquivo_pdf_s}`,
  só para registro com `arquivo_indexado_s = S`. O endereço
  `/solr/acordaos2/browse?id=...` devolve a página de busca, e não o
  documento (06/10/2026): não usar como rota de inteiro teor.
- **Acentuação (corrigido em 06/10/2026):** `_texto` ignora acento. "imovel
  rural" e "imóvel rural" devolvem o mesmo total (21.132 na base inteira), e o
  mesmo vale para parceria agrícola, alienação fiduciária, produção rural e
  simulação em 90 dias. Uma grafia por expressão basta; a nota anterior
  (10/06 e 03/09), que mandava consultar as duas, está vencida. Os endereços
  antigos com as duas grafias continuam certos, só mais longos.
- **Variante curta do ITR (corrigido em 06/10/2026):** `_texto:"imposto
  territorial rural"` não é variante morta. Em 90 dias devolveu 6 acórdãos,
  3 deles sem a forma longa "Imposto sobre a Propriedade Territorial Rural".
  As duas formas ficam na rede rural.
- **`arquivo_indexado_s` (corrigido em 06/10/2026):** o campo diz se o
  inteiro teor já entrou no índice, e é isso que governa duas coisas.
  Com "S", `_texto` alcança relatório e voto e o PDF responde no endereço de
  inteiro teor (10 de 10 amostras). Com "N", `_texto` só alcança ementa e
  dispositivo (a frase "é o relatório" aparece em 872 de 902 registros "S" e
  em nenhum dos 2.931 "N") e o PDF devolve erro 404 (10 de 10 amostras).
  Em 06/10/2026 tudo o que foi publicado depois de 10/09 estava em "N": o
  inteiro teor entra em lotes, semanas depois da publicação. Consequências:
  (a) na janela de 10 dias a busca é, na prática, busca por ementa, e a
  menção rural só no corpo não aparece; (b) acórdão cujo termo só está no
  corpo fica invisível até virar "S", e quem o pesca é o repasse; (c) o link
  de inteiro teor gravado na base não abre enquanto o registro for "N".
- O sinal de registro sem texto nenhum continua sendo não responder a
  `_texto:recurso` (166 de 3.834 em 45 dias, todos "N", metade deles sem
  ementa). `ementa_s:[* TO *]` funciona como filtro de "tem ementa".
- Os títulos em CAIXA ALTA dentro de `ementa_s` são o resumo temático mais
  denso. Extrair as linhas com mais de 12 caracteres que sejam iguais à
  própria versão em maiúsculas.
- Há um segundo manipulador, `/solr/acordaos2/browse` com `&wt=json`, que
  busca o inteiro teor sem nome de campo. Nele, juntar muitas frases com OR
  zera o resultado: uma frase por consulta, deduplicando depois. Usar só se o
  `/select` com `_texto:` falhar.
- **Blocos repetitivos:** é comum a turma julgar dezenas de acórdãos idênticos
  na mesma sessão. Agrupar por turma, data de sessão e primeiro título em
  caixa alta; registrar o acórdão líder, a faixa de numeração no campo `Série`
  e a etiqueta `repetitivo`.

### Expressões dos termos

Na base de termos, cada expressão é uma ou mais frases separadas por ` + `.
Cada segmento é uma frase exata; todos os segmentos têm de ocorrer no mesmo
acórdão. `permuta + torna` vira `_texto:"permuta" AND _texto:"torna"`.

Para a coleta diária não é preciso uma consulta por termo. Duas consultas
amplas (rede rural e rede patrimonial, com as âncoras unidas por OR) trazem os
candidatos da janela; o termo que capturou cada um é identificado depois, no
texto da ementa, e gravado no campo `Termo que capturou`. Consulta termo a
termo é coisa do `/carf calibra`.

As âncoras das duas redes têm fonte única em `scripts/coleta_ver.py`. Os
endereços fixos dessas duas consultas e da sentinela, usados pelo transporte
1b, saem de `python3 scripts/coleta_ver.py urls`, estão em
`references/tarefa-agendada.md` e são repetidos no texto da tarefa, porque a
ferramenta de requisição pode aceitar só endereço que veio escrito na
instrução do usuário. Âncora alterada no script pede endereço regerado. Se ela aceitar endereço montado na hora, montar as
variações necessárias (janela de 35 dias, paginação com `start=`, consulta por
número de acórdão).

### Pelo navegador

Abrir `https://acordaos.economia.gov.br` e consultar o índice de dentro da
página (requisição ao mesmo domínio). Notas da sessão de 03/09/2026:

- A saída da ferramenta de script corta em cerca de mil caracteres. Guardar o
  resultado em variável da página e imprimir em lotes de 1 a 3 acórdãos.
- Não pedir que a página devolva `form.action` nem cadeias de consulta: a
  extensão bloqueia saída que contenha dado de cookie.
- (Nota de 03/09/2026, vencida em 06/10/2026.) O ambiente de execução de
  código passou a alcançar `acordaos.economia.gov.br` e `carf.fazenda.gov.br`
  depois que os domínios foram liberados na rede da conta. O navegador deixa
  de ser o caminho normal e fica como reserva do canal 1.
- **Duas pontes de navegador, só uma roda script (medido em 30/09/2026).** A
  extensão claude-in-chrome executou a consulta ao índice (status 200). A
  ponte Control Chrome abriu páginas e listou abas, mas falhou ao executar
  script ("Google Chrome is not running"). Usar a extensão claude-in-chrome e
  abrir aba própria no domínio do VER; fechar a aba ao terminar.
- **A extensão bloqueia saída com cadeia de consulta** ("[BLOCKED: Cookie/query
  string data]"). Nunca imprimir HTML bruto de página nem URL com `?`. Para
  texto de página, converter com DOMParser e trocar por "[link]" tudo o que
  contenha `?`, `=` ou `&` antes de imprimir.
- **As pontes caem no meio da sessão** (duas chamadas seguidas expiraram em 4
  minutos, após cerca de uma hora de uso). Ordem de trabalho que sobrevive a
  isso: coletar, triar, REGISTRAR NO NOTION e só depois ler inteiro teor.
  Guardar os resultados em variável da página (`window.__x`) continua
  funcionando enquanto a aba existir.
- **Campos recuperáveis do índice** (`fl=*`): `ementa_s`, `decisao_txt`,
  `numero_processo_s`, `nome_relator_s`, `turma_s`, `secao_s`, datas e
  `nome_arquivo_pdf_s`. O `decisao_txt` é o dispositivo: traz o resultado, a
  votação (unanimidade, maioria, voto de qualidade) e a composição da sessão.
  Ler o `decisao_txt` de toda decisão ALTA, porque ele dá `Resultado` e
  `Votação` sem abrir o PDF. Não existe campo recuperável com o inteiro teor.
- **Relatório e voto:** para registro "S", baixar o PDF do endereço de
  inteiro teor por execução de código e ler. Para registro "N" (o acórdão
  fresco, que é o que interessa à pauta), ainda sem método validado. A rota de página do
  documento foi bloqueada pela extensão. Tentar o Jusratio pelo número que
  termina o nome do arquivo (arquivo `..._7414749.pdf` vira
  `carf-acordao-7414749`); em 30/09/2026 as duas chamadas voltaram com "No
  approval received". Sem relatório, a ficha sai preliminar (ver `pauta.md`).

## 3. SINCON — conferência cruzada

`https://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf`

- Busca na ementa (mais preciso que o inteiro teor) e recebe a publicação de
  2 a 4 dias antes do VER.
- Em 06/10/2026 a página respondeu por execução de código (status 200). O
  preenchimento do formulário e a obtenção do PDF por esse transporte não
  foram testados; as notas abaixo são do navegador. É a rota candidata para o
  inteiro teor do acórdão "N" (decisão de 01/10/2026 de portar o método
  "SINCON primeiro"), pendente de validação isolada.
- Formulário `consultaJurisprudenciaForm`. Campos: `dataInicialInputDate` e
  `dataFinalInputDate` (formato MM/AAAA), rádios `campo_pesquisa1` (1 =
  Processo, 3 = Acórdão) e `campo_pesquisa3` (1 = Ementa, 2 = Decisão, 3 =
  Ementa e Decisão), `valor_pesquisa1` / `valor_pesquisa3`, botão
  `botaoPesquisarCarf`.
- O rótulo diz "Mês/Ano do Acórdão", mas o filtro é por data de publicação.
- O resultado vem em blocos de texto ("Acórdão:", "Número do Processo:",
  "Data de Publicação:", "Contribuinte:", "Relator(a):", "Ementa:",
  "Decisão:"), em ordem decrescente de publicação.
- O formulário some na página de resultados. Para nova busca, voltar ao
  endereço, ou trabalhar num iframe do mesmo domínio posicionado fora da tela
  com dimensões reais (iframe com `display:none` não gera texto).
- A paginação trava com frequência a partir da quinta ou sexta página. Em
  janela longa, consultar acórdão por acórdão pelo número.
- Uma busca leva de 8 a 12 segundos. Disparar, guardar o resultado na página e
  consultar depois; não encadear duas buscas na mesma chamada.

Uso: na execução com navegador, buscar "rural" na ementa do mês corrente e
comparar com o que o VER trouxe. Acórdão que só o SINCON tem entra na base
com `Canal = SINCON` e a observação de que o VER ainda não o indexou.

## 4. Jusratio

- Restringir a busca ao tribunal CARF e pedir o modo de triagem (só
  identificação, citação e ementa curta).
- O filtro de data é pela data de julgamento. A data de publicação vem dentro
  da citação ("DJe DD/MM/AAAA"). Como o acórdão é publicado semanas depois de
  julgado, usar data inicial de 120 dias atrás e filtrar a publicação depois.
- Uma pergunta por trilha, formulada como problema jurídico (é o canal em que
  a busca por problema funciona). Uma pergunta ampla rende mais que várias
  decompostas.
- O identificador do documento termina no mesmo número do arquivo do VER, e o
  link de inteiro teor aponta para o VER quando o acórdão é recente.
- Serve também, em qualquer execução, para a varredura analógica da trilha de
  alienação fiduciária e para localizar um acórdão pelo número do processo.

## 5. Repasse (segundas)

O texto integral entra no índice do VER com semanas de atraso: em julho de
2026, 7% dos registros do mês ainda não respondiam à busca textual no fim de
agosto. Em 06/10/2026 o inteiro teor mais recente no índice era de publicação
de 10/09 (26 dias); se esse atraso passar de 35 dias, o repasse deixa de
alcançar o acórdão cujo termo só está no corpo. Informar na mensagem de
segunda a data da publicação "S" mais recente; atraso acima de 30 dias vai
para a linha "Atenção" com a sugestão de alongar o repasse. O repasse repete a coleta com janela de 35 dias e registra só o que
não está na base, marcando `Obs = recuperado no repasse` (`coleta --dias 35
--excluir /tmp/carf_ja_na_base.txt`, com a consulta da base cobrindo 45
dias). O índice recebe o inteiro teor em lote semanal, aos sábados (campo
`dt_index_tdt`; medido em 21/10/2026: 03, 10 e 17/10), por isso o repasse cai
na segunda.

Medir e informar o passivo de indexação da janela: total de registros contra
os que respondem a `_texto:recurso`. A diferença continua invisível e será
pescada nos repasses seguintes.

Se o repasse cair no canal 3, dizer que ele ficou parcial e que o repasse
exaustivo depende de uma execução com navegador.

## 6. Fila sem data de publicação (mensal)

Em 03/09/2026 o VER tinha 49.684 registros sem `dt_publicacao_tdt`, dos quais
5.570 mencionavam termos rurais. Nenhum deles entra em janela alguma. O caso
que expôs a falha foi o acórdão 2102-004.232 (Funrural com sub-rogação),
publicado em 29/05/2026 segundo o SINCON e sem data no VER.

1. Consultar os termos da rede com `fq=-dt_publicacao_tdt:[* TO *]`.
2. Ordenar pelo número do arquivo (`_(\d+)\.pdf` em `nome_arquivo_pdf_s`), que
   cresce com a data de processamento: janeiro/2026 perto de 7.330.000,
   maio/2026 perto de 7.367.000, agosto/2026 perto de 7.404.000, publicações
   de 10/09/2026 perto de 7.410.000. Trabalhar do número mais alto para baixo.
3. Número alto significa processamento recente, não publicação recente: a
   fila é dominada por acervo histórico sendo digitalizado, e a data de
   sessão desses registros costuma estar corrompida. Confirmar a data real
   (no SINCON, pelo número do acórdão, ou no Jusratio, pelo processo) antes
   de registrar.
4. Registrar só o que tiver publicação real nos últimos 12 meses e tema
   monitorado, com `Obs = recuperado da fila sem data`.

## 7. Limites de cada execução

- Sem teto de captura (v0.2): o script pagina por cursor até o total, com
  trava de segurança de 2.000 por rede e aviso na linha "Atenção" se for
  atingida. O teto de 60 da v0.1 cortava o lote do CARF (256 acórdãos da
  rede rural em 10/09/2026) e o próprio repasse, que em 21/10/2026 só
  enxergava até 09/10. O que controla o custo agora é a exclusão do que já
  está na base e o colapso dos blocos repetitivos, não o corte.
- Leitura de inteiro teor: só do acórdão que vai virar ficha, e dos de
  relevância ALTA quando a ementa não bastar para preencher a lente.
