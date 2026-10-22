# Tokens Visuais AeM — multi-formato (v1 · 26/08/2026)

Fonte única para HTML/artifact, .pptx e imagem. O brand-guide.md
continua sendo a fonte para .docx; divergência entre os dois se
resolve a favor do brand-guide e vira correção aqui.

## 1. Paleta (tema claro / tema escuro)

| Token | Claro | Escuro | Uso |
|---|---|---|---|
| paper (fundo) | #FBFAF7 | #0F1726 | fundo da página |
| card | #FFFFFF | #17223A | cartões, superfícies |
| card-2 | #F5F3EC | #1C2840 | chips, superfícies secundárias |
| ink | #22303F | #E7EAF1 | texto principal |
| ink-2 | #5C6B7A | #A2AEC2 | texto secundário |
| ink-3 | #8A96A3 | #7A87A0 | legendas, meta |
| navy (títulos) | #1D3D69 | #A9BFDF | títulos, números de destaque |
| gold (acento) | #B88657 | #C99C6E | regras, eyebrows, destaque pontual |
| steel | #6E86AE | #8FA7C9 | apoio; cor de barra no escuro |
| line | #E4E0D5 | #2A3650 | bordas |
| barra (fill) | #1D3D69 | #8FA7C9 | gráficos de série única |

Funcionais (status — sempre ponto colorido + texto, nunca cor sozinha):

| Status | Claro | Escuro |
|---|---|---|
| ok / executado | #1E8E4E | #4CC38A |
| atenção / aberto | #C56A1A | #E8934A |
| risco / quebrado | #B03A2E | #E06C5E |
| neutro / candidato | #7A8794 | #93A0B4 |

(Os funcionais do brand-guide — #27AE60, #E67E22, #C0392B — são a
referência de família; os valores acima são os mesmos matizes
ajustados para contraste AA sobre paper/card de cada tema.)

## 2. Tipografia

- Títulos, números de destaque (KPI), nomes de seção: **Georgia**
  (fallback Times New Roman) — a serifa é a voz institucional.
- Corpo, UI, labels, tabelas: **Arial** (fallback Helvetica).
- Labels em caixa alta: letter-spacing .08–.14em, 10–11px.
- Números alinhados: `font-variant-numeric: tabular-nums`.
- Nunca Times New Roman como escolha; nunca fontes de Google Fonts —
  as fontes institucionais são de sistema.

## 3. HTML/artifact — regras de construção

1. Estrutura token-first: paleta clara completa em `:root`;
   escuro redefine SÓ os tokens em
   `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) }`
   e de novo em `:root[data-theme="dark"]`. Nenhuma cor definida
   fora de token. `body` sempre com background explícito.
2. Timbre: logo no topo + regra dourada 2px abaixo do cabeçalho.
   Rodapé institucional: regra dourada + "CONFIDENCIAL — USO
   INTERNO — AMARAL E MELO ADVOGADOS" (interno) ou endereços
   das unidades (cliente).
3. Gráficos: seguir a skill `dataviz` (obrigatória antes de
   qualquer gráfico). Distribuições em barra = série única
   (navy no claro, steel no escuro), ponta arredondada 4px,
   rótulo direto com o valor. NUNCA usar navy/gold/steel como
   paleta categórica multi-série — reprova no validador da
   dataviz (chroma baixo, faixa de luminosidade); para
   multi-série real, usar a paleta da dataviz e rodar o
   validador.
4. Interatividade sóbria: tabs, busca com filtro, tooltip em
   hover. Foco visível (outline gold). prefers-reduced-motion
   respeitado.
5. Painel que o usuário vai revisitar/compartilhar → publicar
   como artifact; visualização pontual → arquivo na conversa.

## 4. Deck .pptx — regras

1. Gerar pela skill `pptx` nativa (Anthropic). Não usar Gamma,
   Canva ou SlidesGPT salvo pedido explícito do usuário.
2. Paleta e fontes da seção 1–2. Slide de título com timbre
   (logo + regra dourada); slides internos com logo pequeno
   no rodapé.
3. Uma ideia por slide (userPreferences). Tabelas: cabeçalho
   navy com texto branco, linhas alternadas #F5F5F5.
4. Rodapé de deck interno: "Confidencial — Uso Interno".

## 5. Imagem/poster — regras

Skill `canvas-design` com a paleta da seção 1 como restrição
dura. Logo conforme a seção 6: versão cor em área clara,
versão negativa em área escura.

## 6. Logo — assets oficiais (transparentes)

Artes oficiais do brandbook 2025, todas com fundo transparente:
- `assets/logo_aem.png` (2000×547) — logo completa COM selo
  20 anos. Padrão para timbre em fundo claro (docx, HTML claro,
  slide de título).
- `assets/logo_aem_cor.png` (2000×497) — horizontal cor SEM
  selo, para composições compactas em fundo claro.
- `assets/logo_aem_negativo.png` (2000×497) — texto branco,
  tagline dourada. ÚNICA versão permitida sobre fundo escuro
  (dark mode do HTML, slides escuros).

Regras:
- Tema claro → logo_aem.png direto, sem mix-blend-mode nem chip.
- Tema escuro → logo_aem_negativo.png direto. Nunca a versão
  cor sobre fundo escuro; nunca inverter/recolorir via CSS.
- Em HTML token-first: duas <img> (claro/escuro) alternadas por
  token de display definido nos blocos de tema.
- Nunca esticar (manter proporção), nunca recriar o desenho.
Fonte das artes: pasta `MKT/Logos/RGB/PNG` no Drive
(Padrão e SELO 20 ANOS) e brandbook 2025.

## 7. Validação antes de entregar

- Gráfico novo → rodar o validador da dataviz com surface do tema.
- Contraste AA (brand-guide §7) nos dois temas.
- HTML → renderizar e OLHAR (claro e escuro) antes de publicar.

## 8. Referência de implementação

Painel-piloto que validou este módulo: artifact "Mapa do Arquiteto"
(https://claude.ai/code/artifact/a819f78f-0f68-44fe-9a55-35e4955585a2),
publicado em 26/08/2026 — timbre, KPI strip, tabs, busca, chips com
sinalização, pills de status, barras de série única e tabelas, nos
dois temas.
