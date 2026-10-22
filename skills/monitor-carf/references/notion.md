# Notion — bases do Monitor CARF

Criadas em 30/09/2026 dentro de "Painel Leonardo" › "Monitor CARF".

```
Página "Monitor CARF"            https://app.notion.com/p/3ebdb165b4d1810bb221e3df6f48e89e
Base "Monitor CARF — Acórdãos"   https://app.notion.com/p/6293d1859ed549859bd7f98ced3b6f70
  data source (gravar e consultar)  66f1f100-a043-4d50-a139-1f36b20559ad
  visão "Fila de pauta" (quadro)     view://3ebdb165-b4d1-81d3-89a8-000c8f170f28
Base "Monitor CARF — Termos"     https://app.notion.com/p/f8d08d22404a4c0ebae820b61a6d1ba5
  data source (gravar e consultar)  9da64503-5e28-421c-8164-3ecb097d1929
```

Os nomes de ferramenta abaixo são os do conector do Notion neste ecossistema.
Se o conector expuser outro nome, usar a ferramenta equivalente.

## Base de termos (a rede)

Colunas: `Expressão` (título) · `Bloco` · `Trilha` · `Grupo` (núcleo |
registro | fronteira | regra) · `Tipo` (busca | vizinho analógico | etiqueta |
exclusão) · `Exige marcador rural` · `Ativo` · `Tese viva` · `Origem` ·
`Acertos 90d` · `Rurais pela ementa` · `date:Medido em:start` · `Obs`.

Leitura no início de toda execução (`notion-query-data-sources`, modo SQL):

```sql
SELECT "Expressão","Bloco","Trilha","Grupo","Tipo",
       "Exige marcador rural","Tese viva","Obs"
FROM "collection://9da64503-5e28-421c-8164-3ecb097d1929"
WHERE "Ativo" = '__YES__'
```

- `Tipo = busca` e `vizinho analógico` formam a rede.
- `Tipo = exclusão` são os falsos positivos e os temas fora do público.
- `Tipo = etiqueta` só marca decisão já capturada.
- Termo com `Ativo` desmarcado não existe para a execução. Quem poda é o
  Leonardo. A skill nunca desmarca nem cria termo por conta própria: sugere na
  linha "Atenção".

Gravação das contagens (`/carf calibra`): atualizar a linha do termo com
`Acertos 90d`, `Rurais pela ementa` e `date:Medido em:start`.

## Base de acórdãos (o registro e a fila)

Chaves para `notion-create-pages` com
`parent = {data_source_id: 66f1f100-a043-4d50-a139-1f36b20559ad}`:

`Acórdão` (título: número da decisão, ex. `2102-004.232`) · `Tipo` ·
`Processo` · `Seção` · `Turma` · `Relator` · `date:Sessão:start` ·
`date:Publicação:start` · `Trilha` · `Aplicação` · `Relevância` · `Resultado`
· `Votação` · `Etiquetas` (lista) · `Termo que capturou` · `Tese em uma linha`
· `Operação` · `Fatos` · `Prova que decidiu` · `Efeito tributário` · `Pauta` ·
`Ineditismo` · `Noticiado por` · `Produto relacionado` (lista) · `Link PDF` ·
`Canal` · `date:Registrado em:start` · `date:Ficha em:start` · `Série` · `Obs`.

Regras de gravação:

- Datas em `AAAA-MM-DD`. Caixa marcada é `__YES__`.
- Campos de seleção aceitam só as opções que já existem. Valor fora da lista
  cria opção nova e polui a base: não usar.
- Relevância BAIXA grava só: `Acórdão`, `Tipo`, `Processo`, `Seção`, datas,
  `Trilha`, `Relevância`, `Termo que capturou`, `Link PDF`, `Canal`,
  `date:Registrado em:start`, `Pauta = não`.
- Bloco repetitivo: uma linha para o acórdão líder, faixa de numeração em
  `Série`, etiqueta `repetitivo`.
- Proposta de súmula, súmula e pauta: título descritivo no lugar do número
  (ex. `Proposta de súmula — ITR — reserva legal`), `Tipo` correspondente,
  `Canal = Diário Oficial`.
- Até 100 linhas por chamada.

Consultas:

```sql
-- o que já foi registrado (evita repetir e triar de novo)
SELECT "Acórdão","Processo","date:Publicação:start"
FROM "collection://66f1f100-a043-4d50-a139-1f36b20559ad"
WHERE "date:Registrado em:start" >= date('now','-45 day')

-- fila de pauta
SELECT url,"Acórdão","Trilha","Relevância","Seção","Ineditismo",
       "Etiquetas","date:Publicação:start"
FROM "collection://66f1f100-a043-4d50-a139-1f36b20559ad"
WHERE "Pauta" = 'candidata'

-- regra de parada: fichas entregues em quatro semanas e o destino delas
SELECT "Pauta", COUNT(*) FROM "collection://66f1f100-a043-4d50-a139-1f36b20559ad"
WHERE "date:Ficha em:start" >= date('now','-28 day')
GROUP BY "Pauta"
```

Na execução por código, os números devolvidos pela primeira consulta vão,
um por linha, para `/tmp/carf_ja_na_base.txt`, que o `coleta --excluir` usa
para tirar da saída o que já está na base.

Antes de gravar um acórdão, conferir pelo título se ele já existe, mesmo fora
da janela de 45 dias, quando ele veio do repasse ou da fila sem data.

Atualização de linha (lente, ineditismo, `Ficha em`, status da pauta): pela
ferramenta de atualização de página do conector, usando a `url` da linha
devolvida pela consulta. Atualizar só as propriedades que mudam.

## Se o Notion não montar

Usar `references/termos-base.md` como rede, não gravar nada, entregar a ficha
na mensagem e escrever em "Atenção": "base não atualizada nesta execução". A
execução seguinte registra o que faltou, porque a janela é de 10 dias.
