# Pauta — do acórdão à ficha

## 1. Filtro RARO

Uma decisão só entra na fila (`Pauta = candidata`) se passar em pelo menos
dois dos cinco testes:

1. **Contraria o senso comum do produtor.** A conclusão é diferente do que o
   produtor, o contador ou o vizinho dão como certo.
2. **Tem cena.** O relatório traz fatos contáveis em três linhas: quem fez o
   quê, quando, por quanto, e como o fisco descobriu.
3. **É inédita, ou tem ângulo próprio disponível.** Ninguém noticiou; ou
   noticiaram a ementa e sobra o que só o Leonardo faz: a conta aplicada a
   uma fazenda, a discordância fundamentada, a leitura do voto vencido.
4. **Conecta com produto ou tese viva.** Leva a uma conversa que o escritório
   ou a Agricompany sabem conduzir.
5. **Integra padrão.** É a terceira ou mais no trimestre na mesma direção, e
   a base permite dizer isso com número.

Entram direto, sem contagem: decisão da Câmara Superior em tema do núcleo,
súmula aprovada ou proposta de súmula em tema do núcleo, e caso direto de
alienação fiduciária.

Não entra, por melhor que pareça: relevância BAIXA, exclusão ativa, decisão
cuja lente não pôde ser preenchida com o texto do acórdão.

## 2. Ordem da fila

1. tese viva; 2. Câmara Superior e súmula; 3. relevância ALTA; 4. inédita
antes de já noticiada; 5. publicação mais recente.

Os acórdãos chegam em lotes. A fila guarda as candidatas e cada execução
entrega a primeira, de modo que um lote com seis boas decisões rende seis
dias de pauta. Candidata com mais de 30 dias sem ser escolhida vira
`descartada` com `Obs = venceu na fila`.

## 3. Teste de ineditismo

Antes de montar a ficha, buscar na web pelo número do acórdão e pelo número
do processo (duas buscas, no máximo).

- Nada encontrado: `Ineditismo = inédito`.
- Encontrado: `já noticiado`, com o veículo e a data em `Noticiado por`. A
  ficha passa a exigir o ângulo próprio, escrito em uma linha.
- Busca indisponível: `não verificado`. Dizer isso na ficha.

Página de resumo automático por acórdão conta como "já noticiado", mas pesa
pouco: anotar "resumo automático" em vez do nome do site.

## 4. A ficha

Uma por execução. Tudo o que está nela tem de estar no acórdão, com a página
ou o trecho de onde saiu.

```
PAUTA DO DIA — <trilha>
Acórdão <número> · <turma e seção> · sessão DD/MM/AAAA · publicado DD/MM/AAAA
Resultado: <contribuinte | Fazenda | parcial> · <unanimidade | maioria | voto de qualidade>
Aplicação: <direta | analógica potencial: o caso é de <setor>; alcança o produtor porque ...>

Cena: <três linhas com os fatos do relatório, sem nome do contribuinte>
O que o produtor não espera: <uma ou duas linhas>
Prova que decidiu: <uma linha>
Voto vencido: <uma linha, ou "não houve">
A quem atinge: <perfil de produtor ou de família>
Produto relacionado: <da lista da base>
Ineditismo: <inédito | já noticiado por ... em DD/MM | não verificado>
Ângulo próprio possível: <uma linha; obrigatória se já noticiado>

Lastro: <link do inteiro teor> · cena: p. X · prova: p. Y · voto vencido: p. Z
Cuidados: <o que conferir antes de publicar>
```

Regras da ficha:

- Não traz título de post, gancho, frase de efeito nem rascunho de texto.
- Não traz nome de contribuinte. Região e porte podem aparecer se o acórdão
  os disser.
- Dispositivo legal só como o acórdão cita, e a linha `Cuidados` manda
  conferir na fonte oficial.
- Em imposto de renda da atividade rural, se a decisão falar em prejuízo, a
  ficha diz que é prejuízo fiscal (apropriação das despesas de investimento
  no ano em que feitas), e não perda financeira.
- Resultado desfavorável ao contribuinte é pauta tão boa quanto o favorável.
  Não torcer o resultado para agradar.
- Decisão de turma ordinária não é "entendimento do CARF". Dizer o órgão.

Depois de entregar a ficha, gravar na linha da base os campos da lente, o
ineditismo e o produto relacionado. O status continua `candidata` até o
Leonardo dizer o contrário.

## 5. Status e regra de parada

O Leonardo muda o status no Notion ou pelo comando
`/carf pauta <acórdão> escolhida | publicada | descartada`.

Regra de parada, ratificada em 30/09/2026: a cada sexta, contar as fichas
entregues nas últimas quatro semanas e quantas estão como `escolhida` ou
`publicada`. Se a proporção for menor que um terço depois de quatro semanas
completas, a mensagem de sexta recomenda baixar a cadência para três
execuções por semana. A skill recomenda; quem muda a tarefa é o Leonardo.

## 6. Série semanal (sextas)

Um número que só a base própria permite, com denominador e período. Exemplos
de pergunta: quantas parcerias requalificadas no trimestre e em quantas a
multa qualificada foi mantida; placar contribuinte e Fazenda por trilha;
quantas decisões de valor da terra nua caíram por falta de laudo.

Regras:
- dizer sempre "na base do monitor, de DD/MM a DD/MM, N decisões", nunca "no
  CARF";
- dizer o canal predominante do período: se a coleta foi por relevância, o
  número é amostra, não contagem;
- com menos de cinco decisões no recorte, não há série: dizer isso.

## 7. Antecipação (quartas)

O CARF publica antes de decidir. Três fontes, buscadas na web e no Diário
Oficial da União:

1. **Proposta de súmula.** Portaria que convoca turma da Câmara Superior ou o
   Pleno para votar enunciado, com o texto proposto e os acórdãos
   precedentes. Registrar com `Tipo = proposta de súmula`, a data da reunião
   em `Sessão` e `Canal = Diário Oficial`.
2. **Súmula aprovada.** `Tipo = súmula aprovada`.
3. **Pauta da Câmara Superior.** As pautas trazem número do processo e nome do
   recorrente, sem o tema. Cruzar os números de processo com a base; nome de
   parte com marcador rural é indício fraco: registrar com `Tipo = pauta` e
   `Obs = tema a confirmar`.

Texto de enunciado só é transcrito da fonte oficial (Diário Oficial ou
página do CARF), com o link. Se a única fonte for notícia, registrar o tema,
o link e `Obs = texto a conferir na fonte oficial`, sem transcrever.

Proposta ou súmula em tema do núcleo entra direto na fila. É o conteúdo de
maior valor: o Leonardo comenta antes da decisão, ou no dia dela.

## 8. Ficha preliminar

Quando o relatório não pôde ser lido (ponte do navegador fora, Jusratio sem
aprovação, ou acórdão fresco cujo PDF ainda não responde no VER, que é a
regra nas primeiras semanas depois da publicação: ver `coleta.md`, seção 2),
a ficha sai **preliminar**: o campo Cena diz "relatório não lido",
Prova que decidiu fica vazio, e o resto vem só da ementa e do `decisao_txt`
com a marca "segundo a ementa" ou "segundo o dispositivo". Regras:

- não preencher `Ficha em` na base, para não contar na regra de parada;
- a linha continua `candidata`, e a `Obs` registra que o relatório não foi lido;
- a próxima execução lê o relatório da candidata antes de montar a ficha
  completa, e só então grava `Ficha em`;
- a mensagem de entrega abre com a palavra PRELIMINAR no título da pauta.
