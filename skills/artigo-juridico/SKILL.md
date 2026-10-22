---
name: artigo-juridico
description: >
  Produz artigos jurídicos assinados por Leonardo Amaral do começo ao fim: fixa a tese, monta o
  esqueleto argumentativo do registro certo, reúne a fundamentação, redige seção a seção e formata
  em .docx. Use SEMPRE que o usuário pedir para "escrever/redigir/produzir/montar um artigo", "um
  paper", "um capítulo", "um texto para o ConJur/JOTA/IBET", ou trabalhar no livro em produção.
  Orquestra a skill voz-autoral-leonardo (para o tom) e a skill regra-matriz (para a decomposição
  normativa nos registros densos). NÃO confundir com a voz-autoral-leonardo sozinha, que cuida só
  do tom e serve para revisar a voz de um texto pronto; NÃO confundir com marca-raro, que é post e
  comunicação de marca. Esta skill é a produção completa do artigo, da tese ao arquivo.
---

# Artigo Jurídico — Produção (Leonardo Amaral)

Esta skill produz o artigo inteiro. Ela é dona de três coisas: a **arquitetura argumentativa** (a sequência de movimentos do raciocínio por registro), o **workflow de produção** (da tese ao .docx) e a **orquestração** das skills que fazem o resto. O tom não é daqui: é da `voz-autoral-leonardo`. A decomposição normativa não é daqui: é da `regra-matriz`. Não reimplemente nenhum dos dois; chame-os.

## Quando esta skill vale (e quando não)

Vale para **produzir uma peça autoral de fôlego, do zero ou reestruturando-a**: artigo, paper, capítulo, texto para publicação.

Não confunda:
- **`voz-autoral-leonardo` sozinha** cuida só do tom, e serve para *revisar a voz* de um texto pronto. Produzir o artigo (estrutura, fundamentação, redação, formatação) é aqui.
- **`marca-raro`** é comunicação de marca: post, WhatsApp, texto institucional. Peça autoral assinada e argumentativa é aqui.

## Workflow de produção

Siga na ordem. Cada passo tem um resultado verificável.

1. **Fixar a tese.** Antes de qualquer estrutura, defina em uma frase a posição que o artigo vai sustentar e o que precisa provar. Sem tese clara, não há artigo.
2. **Selecionar o registro** pela peça e pelo veículo, e ler o esqueleto correspondente (tabela abaixo).
3. **Montar o outline e submeter ao Leonardo para ratificar.** Liste os movimentos do esqueleto, cada um preenchido com o argumento daquela seção. Não redija a peça inteira antes do aval: propor, ratificar, construir.
4. **Reunir a fundamentação.** Legislação com artigo, inciso e parágrafo precisos; doutrina; jurisprudência (STF, STJ, CARF, TJs). **Nunca inventar dispositivo:** se não confirmar a existência e a redação, não cite.
5. **Redigir seção a seção** seguindo o esqueleto do registro e **vestindo o texto com a voz: chame a `voz-autoral-leonardo`** no registro escolhido. A estrutura vem do esqueleto; o tom vem da voz.
6. **Nos registros densos** (técnico-aplicado e científico-dissertativo), **chame a `regra-matriz`** para a decomposição normativa (montar a RMIT do tributo, aplicar o percurso S1→S4) e traga o resultado para a prosa. Não reimplemente a decomposição.
7. **Conferir as citações.** Cada dispositivo citado existe e está com a redação certa? Cada nota fecha? Dispositivo não confirmado sai.
8. **Formatar em .docx.** Publicação externa (ConJur, JOTA, periódico) recebe documento limpo, **sem timbre** do escritório. Peça interna ou institucional usa o timbre quando aplicável (skill `layout-aem`).
9. **Acionar o `crivo-do-leao`** para a verificação final de voz e estrutura antes do uso.

## Seleção de registro

| A peça é… | Registro | Leia o esqueleto |
|---|---|---|
| Artigo curto para o produtor, site ou blog | Divulgação | `references/esqueleto-divulgacao.md` |
| Opinião para veículo jurídico (ConJur, JOTA, Migalhas) | Opinião publicada | `references/esqueleto-opiniao-publicada.md` |
| Artigo ou capítulo técnico aplicado, ou o **livro em produção** | Técnico-aplicado | `references/esqueleto-tecnico-aplicado.md` |
| Artigo científico, paper, dissertação, texto para o IBET | Científico-dissertativo | `references/esqueleto-cientifico-dissertativo.md` |

O registro que a produção escolhe aqui é o **mesmo** que a `voz-autoral-leonardo` usa para o tom. Escolha uma vez e passe adiante.

## Orquestração

- **`voz-autoral-leonardo`** — veste o esqueleto com o tom do registro. **Sempre.** É a camada de voz, e sem ela o texto sai correto mas sem dono.
- **`regra-matriz`** — faz a decomposição normativa (RMIT, percurso S1→S4) nos registros técnico-aplicado e científico. Chamada quando o argumento exige montar a norma de incidência.
- **`crivo-do-leao`** — confere voz e estrutura ao final. Esta skill produz; o crivo verifica.

## Recursos

- `references/esqueleto-divulgacao.md` — arquitetura argumentativa do artigo de divulgação
- `references/esqueleto-opiniao-publicada.md` — arquitetura argumentativa do artigo de opinião publicada
- `references/esqueleto-tecnico-aplicado.md` — arquitetura argumentativa do artigo técnico-aplicado (o livro em produção)
- `references/esqueleto-cientifico-dissertativo.md` — arquitetura argumentativa do artigo científico/dissertação
