---
name: deck-aula-aem
description: "Apresentações didáticas no padrão visual e pedagógico AeM — decks .pptx com identidade da marca, uma ideia por slide, ilustrações vetoriais e QA visual obrigatório."
---

# Deck-Aula AeM — apresentações didáticas no padrão da casa

Transforma conteúdo verificado em aula visual que converte o complexo em simples: identidade AeM, uma ideia por slide, ilustrações vetoriais e verificação visual antes de entregar.

## Dependências

Ler antes de gerar: `layout-aem` (tokens de marca — seções 1, 2, 4 e 6 do `references/visual-tokens.md`; assets de logo) e a skill `pptx` nativa (gotchas do pptxgenjs e scripts de QA). Se houver gráfico de dados, ler também `dataviz`. NUNCA usar Gamma, Canva ou SlidesGPT salvo pedido expresso.

## Etapa 0 — público e registro (pergunta única se não estiver claro)

Dois registros mudam tudo; identificar antes de escrever:

- **Técnico** (alunos IBET/AGET, advogados, contadores): dispositivos legais citados em chips discretos no slide; matrizes e quadros comparativos completos; provocações dogmáticas nas notas.
- **Porteira** (produtores rurais, cliente leigo): ZERO juridiquês no corpo — artigos só nas notas de apresentador; eleger UMA metáfora-mestra que carregue os conceitos duros da aula inteira (ex.: o "vale" para crédito/compensação/ressarcimento; "o crédito viaja com o grão" para transferência) e sustentá-la do primeiro ao último slide; personagens concretos (Produtor A / Produtor B) com números redondos.

Extensão default: módulo 6–8 slides • aula executiva 10–12 • palestra completa 20+. Uma ideia por slide, sem exceção.

## Arquitetura pedagógica (o arco)

1. **Capa** com timbre — fundo navy + logo negativa para plateia externa; fundo claro + logo completa para módulo interno/acadêmico. Título como frase-nome, subtítulo com a promessa da aula.
2. **Pergunta de abertura** que bifurca o público (com enquete de mãos na nota).
3. **O problema** tornado visível (gráfico ou número-herói: "quanto isso custa por ano").
4. **O mecanismo**, um passo por slide (fluxos com setas rotuladas; contas em blocos com o item-chave destacado em verde).
5. **Síntese comparativa** — matriz 2×2 ou "os N caminhos" com barras de tempo/valor.
6. **Calendário** com UM marco em destaque dourado (a urgência real).
7. **Checklist acionável** de fechamento (5 itens, verbo no imperativo) + assinatura.

Títulos são afirmações ("O vale volta no acerto da própria venda"), nunca rótulos ("Créditos"). Eyebrow em caixa alta dourada nomeia o bloco. **Notas de apresentador em TODOS os slides**: fala sugerida no tom do Leonardo, interações de plateia e as ressalvas honestas (ex.: "alíquota ilustrativa — a de referência ainda será fixada"; pendências normativas declaradas). Números: poucos, grandes, coerentes entre slides, sempre com a base declarada quando ilustrativos.

## Sistema visual (tokens fixos)

- Fundo `#FBFAF7` (paper) • cards `#FFFFFF` com borda `#E4E0D5` • chips `#F5F3EC` • texto `#22303F`/`#5C6B7A` • títulos e números-herói navy `#1D3D69` em Georgia bold • acento dourado `#B88657` (eyebrows, numeração de bloco, marco de destaque) • funcionais: verde `#1E8E4E` (dinheiro/ok), laranja `#C56A1A` (atenção), vermelho `#B03A2E` (problema) — sempre com ícone ou rótulo, nunca cor sozinha.
- Corpo em Arial 11–14pt; títulos Georgia 27–32pt (folga de ~10% na caixa — fonte de métrica imprecisa no QA); nunca Times New Roman.
- Capa: logo + regra dourada horizontal (timbre). Slides internos: logo_aem_cor pequena no rodapé direito + numeração + título curto à esquerda. Sem barras decorativas, sem sublinhado de título, sem emoji.
- Tabelas: cabeçalho navy com texto branco, linhas alternadas `#F5F5F5`.

## Elementos ilustrativos (pipeline)

- **Ícones**: react-icons (FontAwesome) rasterizados com sharp em PNG 512px transparente, aplicados dentro de círculos coloridos (navy/gold/card2) — nunca emoji, nunca clipart. Gerar por script (renderToStaticMarkup → sharp → png) nas cores da paleta.
- **Fluxos**: nós como círculos/retângulos arredondados (produtor=navy, cooperativa=gold, neutro=card2 com borda), setas com ponta de triângulo e RÓTULO em cima ("entrega a 0%", "seu vale vai junto"); badge colorido sobre a seta para o elemento em discussão.
- **Gráficos**: série única navy, ponta arredondada, rótulo direto com o valor, sem legenda nem eixo carregado (regras da dataviz). Comparações de tempo/valor como barras horizontais com rótulo textual.
- **Número-herói**: card2 com valor em Georgia 28–40pt navy ou verde + linha de contexto pequena.
- **Contas**: linhas empilhadas (item + valor à direita), item-chave com fundo `#E6F4EB` e borda verde.
- **Timeline**: linha horizontal com marcos alternando acima/abaixo; o marco crítico em card dourado.

## Produção e QA (obrigatório, nesta ordem)

1. Gerar com **pptxgenjs**, `LAYOUT_WIDE` (13,33×7,5), cores sem `#`, `isTextBox:true` em todo texto, margens ≥ 0,6".
2. `validate.py` da skill pptx — corrigir no gerador, nunca no XML.
3. Renderizar TODAS as lâminas (soffice → pdf → pdftoppm) e OLHAR uma a uma: overflow de texto, colisões, contraste, coerência dos números entre slides, ausência de juridiquês no corpo (registro porteira). Corrigir e re-renderizar até limpar.
4. Entregar o .pptx; registrar a sessão via ponto-do-leao (regra das userPreferences).

Variante: quando o pedido for aula interativa para revisitar/compartilhar (não projetar), a mesma arquitetura vira artifact HTML com fluxograma progressivo — tokens e arco idênticos, um passo por clique.

## O que esta skill NÃO faz

Não pesquisa nem verifica conteúdo normativo (corpus do project e skills de análise fazem isso antes); não emite parecer nem documento de decisão; não cria posts ou material de marca (marca-raro); não substitui o crivo-do-leao quando o material for para uso externo sensível.