# Boletim diário por e-mail — contrato

Pedido pelo Leonardo em 02/10/2026 e ratificado em 06/10/2026 como substituto
do relatório por tema da tarefa antiga `monitoramento-carf-agro`. É uma
segunda leitura da base de acórdãos, e não um segundo coletor: quem coleta e
classifica é esta skill; o boletim só lê o que ela gravou.

Esta skill não envia e-mail. O envio é de uma automação externa (cenário no
Make, aprovado em 02/10/2026) que lê o Notion e manda pelo Gmail. Este arquivo
fixa o que a automação deve ler e como deve montar a mensagem, para que a
base e o boletim não se afastem.

## O que entra

- Fonte: base "Monitor CARF — Acórdãos" (data source em `notion.md`).
- Linhas com `Registrado em` igual ao dia do envio. O envio roda depois do
  horário da tarefa agendada.
- Dia sem linha nova: não envia nada.

## Formato

```
Assunto: Monitor CARF — AAAA-MM-DD — N novos (ALTA a)

RELEVÂNCIA ALTA
<Acórdão> · <Trilha> · <Resultado> · <Tese em uma linha>
  registro: <endereço da linha no Notion> · inteiro teor: <Link PDF>

POR TRILHA
<nome da trilha> (m)
  <Acórdão> · <Tese em uma linha> · <endereço da linha no Notion>
  ...

Relevância baixa: b registros (só na base).
```

Regras:

- Ordem das trilhas: a da tabela de `triagem-e-lente.md`. Trilha sem linha no
  dia não aparece.
- Decisão ALTA aparece no bloco de cima e não se repete na trilha.
- Bloco repetitivo: uma linha, com a faixa do campo `Série`.
- Relevância BAIXA entra só como contagem.
- O endereço de consulta é o da linha no Notion, que sempre abre. O `Link
  PDF` vai junto, mas não abre nas primeiras semanas depois da publicação
  (ver `coleta.md`, seção 2).
- Sem nome de contribuinte (a base não o guarda).
- O boletim informa; não substitui a ficha de pauta nem traz texto pronto.

## Destinatário

Só o Leonardo. Incluir outra pessoa é decisão dele: enquanto vai só para ele,
a base é ferramenta pessoal; com terceiros, passa a ser ativo compartilhado.

## Estado em 06/10/2026

Contrato escrito. A existência e o estado do cenário no Make não foram
conferidos na sessão que escreveu este arquivo.
