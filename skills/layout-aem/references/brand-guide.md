# Brand Guide — Amaral e Melo Advogados

Especificações técnicas canônicas de identidade visual e formatação. Este arquivo é a fonte única de verdade para cores, fontes, espaçamentos e dados institucionais. Todas as skills que geram documentos devem consultar este arquivo.

---

## 1. Paleta de Cores

### Cores primárias

| Nome | Hex | Uso |
|------|-----|-----|
| Azul Marinho | #1D3D69 | Títulos, cabeçalhos de tabela, elementos de destaque institucional |
| Dourado | #B88657 | Separadores, linhas decorativas, detalhes de marca |

### Cores funcionais (caixas de destaque)

| Tipo | Fundo | Borda esquerda | Uso |
|------|-------|----------------|-----|
| Alerta | #FFF9E6 | #E67E22 (laranja) | Pontos de atenção, riscos moderados, cuidados |
| Risco/Perigo | #FFF0F0 | #C0392B (vermelho) | Cenários sem planejamento, riscos altos, alertas críticos |
| Economia/Positivo | #F0FFF0 | #27AE60 (verde) | Cenários com planejamento, resultados favoráveis, economia |
| Recomendação | #F0F5FF | #1D3D69 (azul marinho) | Recomendação do escritório, conclusões, posicionamentos |
| Informativo | #F0F5FF | #B88657 (dourado) | Informações complementares, notas explicativas |

### Cores de suporte

| Nome | Hex | Uso |
|------|-----|-----|
| Texto corpo | #333333 | Texto principal do documento |
| Texto secundário | #666666 | Rodapés, notas, legendas |
| Texto pendente | #999999 | Campos "[A CONFIRMAR]", marcações de lacuna |
| Fundo alternado tabela | #F5F5F5 | Linhas pares de tabelas |
| Borda tabela | #CCCCCC | Bordas de células |
| Branco cabeçalho tabela | #FFFFFF | Texto sobre fundo azul marinho |

---

## 2. Tipografia

### Fontes institucionais

| Contexto | Fonte | Fallback |
|----------|-------|----------|
| Títulos e destaques | Georgia | Times New Roman |
| Corpo de texto | Arial | Calibri |

### Hierarquia tipográfica por modo

#### Modo Tribunal

| Elemento | Fonte | Tamanho | Peso | Cor |
|----------|-------|---------|------|-----|
| Heading 1 | Georgia | 14pt (28 half-pt) | Bold | #1D3D69 |
| Heading 2 | Georgia | 13pt (26 half-pt) | Bold | #1D3D69 |
| Heading 3 | Arial | 13pt (26 half-pt) | Bold | #1D3D69 |
| Corpo | Arial | 12pt (24 half-pt) | Regular | #333333 |
| Rodapé | Arial | 7pt (14 half-pt) | Regular | #666666 |

#### Modo Cliente

| Elemento | Fonte | Tamanho | Peso | Cor |
|----------|-------|---------|------|-----|
| Heading 1 | Georgia | 15pt (30 half-pt) | Bold | #1D3D69 |
| Heading 2 | Georgia | 14pt (28 half-pt) | Bold | #1D3D69 |
| Heading 3 | Arial | 14pt (28 half-pt) | Bold | #1D3D69 |
| Corpo | Arial | 13pt (26 half-pt) | Regular | #333333 |
| Rodapé | Arial | 7pt (14 half-pt) | Regular | #666666 |

#### Modo Interno

| Elemento | Fonte | Tamanho | Peso | Cor |
|----------|-------|---------|------|-----|
| Heading 1 | Arial | 13pt (26 half-pt) | Bold | #1D3D69 |
| Heading 2 | Arial | 12pt (24 half-pt) | Bold | #1D3D69 |
| Heading 3 | Arial | 12pt (24 half-pt) | Bold | #333333 |
| Corpo | Arial | 11pt (22 half-pt) | Regular | #333333 |
| Rodapé | Arial | 7pt (14 half-pt) | Regular | #999999 |

#### Modo Publicação

| Elemento | Fonte | Tamanho | Peso | Cor |
|----------|-------|---------|------|-----|
| Heading 1 | Georgia | 16pt (32 half-pt) | Bold | #1D3D69 |
| Heading 2 | Georgia | 14pt (28 half-pt) | Bold | #1D3D69 |
| Heading 3 | Georgia | 13pt (26 half-pt) | Bold | #1D3D69 |
| Corpo | Georgia | 12pt (24 half-pt) | Regular | #333333 |

---

## 3. Layout de Página

### Tamanho

Sempre A4: 210 × 297 mm (11906 × 16838 DXA). Nunca A3. Nunca US Letter.

### Margens por modo (em DXA, 1cm ≈ 567 DXA)

| Modo | Topo | Inferior | Esquerda | Direita | Largura útil |
|------|------|----------|----------|---------|-------------|
| Tribunal | 1418 (2,5cm) | 1418 | 1701 (3cm) | 1134 (2cm) | 9071 |
| Cliente | 1134 (2cm) | 1134 | 1134 | 1134 | 9638 |
| Interno | 1134 | 1134 | 1134 | 1134 | 9638 |
| Publicação | 1418 | 1418 | 1418 | 1418 | 9070 |

### Entrelinhamento por modo (em twips, base = 240 twips para 1.0)

| Modo | Fator | Valor em twips |
|------|-------|----------------|
| Tribunal | 1.5 | 360 |
| Cliente | 1.3 | 312 |
| Interno | 1.2 | 288 |
| Publicação | 1.5 | 360 |

### Espaçamento entre parágrafos

| Modo | Espaço after (twips) | Recuo primeira linha (DXA) |
|------|---------------------|---------------------------|
| Tribunal | 0 | 720 (~1,27cm) |
| Cliente | 160 (8pt) | 0 |
| Interno | 120 (6pt) | 0 |
| Publicação | 200 (10pt) | 0 |

---

## 4. Cabeçalho e Rodapé

### Cabeçalho

- Logo (`assets/logo_aem.png`, com selo 20 anos, fundo transparente) alinhada à esquerda
- Dimensões de renderização: 227 × 62 px (≈ 6cm de largura)
- Sobre fundo escuro, usar exclusivamente `assets/logo_aem_negativo.png`
- Abaixo da logo: linha separadora horizontal dourada (#B88657), 6pt de espessura, com 200 twips de espaço after

### Rodapé — Modo "enderecos" (tribunal, cliente)

Linha separadora dourada (4pt) seguida de duas colunas com tab stops:

**Coluna esquerda — Unidade Jataí:**
- Rua Minas Gerais, 1409 - Samuel Graham
- Jataí-GO, CEP 75.804-062
- ☎ (64) 99606-5724
- ✉ contato@amaralemelo.adv.br

**Coluna direita — Unidade Rio Verde:**
- Av. Presidente Vargas, 266 - Centro Empresarial Le Monde
- sala 601 - Jardim Marconal, Rio Verde-GO, CEP 75.901-551
- ☎ (64) 99903-1847
- ✉ rioverde@amaralemelo.adv.br

Fonte: Arial 7pt, cor #666666. Nomes das unidades em Arial Bold 8pt, cor #1D3D69.

### Rodapé — Modo "confidencial" (interno)

"CONFIDENCIAL — USO INTERNO — AMARAL E MELO ADVOGADOS" centralizado, Arial 7pt itálico, cor #999999.

### Rodapé — Modo "simples" (publicação)

Apenas numeração de página, sem endereços.

### Numeração de página (todos os modos)

Alinhada à direita, Arial Bold 8pt, cor #1D3D69.

---

## 5. Elementos Visual Law

### Princípios gerais

- Intensidade visual moderada é o ponto ótimo para tribunais (dados empíricos AeM)
- Fluxogramas: ~95% de aprovação judicial — usar com confiança
- QR codes: 39,2% de rejeição judicial — evitar em peças para tribunal
- Tabelas comparativas: alta aprovação, usar amplamente
- Ícones e ilustrações: aceitos quando funcionais, não decorativos
- Referência normativa: Recomendação CNJ nº 144/2023 (linguagem simples + elementos visuais)

### Caixas de destaque

Usar a função `caixaDestaque(tipo, textos)` do código-base. Cinco tipos disponíveis: alerta, risco, economia, recomendacao, info.

Regras:
- Borda esquerda grossa (18pt de size no BorderStyle)
- Fundo suave (cores claras da paleta funcional)
- Padding interno: indent left/right 200 DXA
- Máximo 2 caixas de destaque por página (evitar poluição visual)

### Tabelas

Usar a função `tabelaAeM(cabecalhos, linhas, largura)` do código-base.

Regras:
- Cabeçalho: fundo azul marinho (#1D3D69), texto branco, bold
- Linhas alternadas: cinza claro (#F5F5F5) e branco
- Bordas: cinza (#CCCCCC), 1pt
- Padding de célula: top/bottom 60 twips, left/right 100 twips
- Máximo 4-5 colunas em documentos para cliente (legibilidade em celular)
- Máximo 3 colunas se o documento será lido primariamente em celular

### Separadores de seção

Linha dourada fina (3pt) com espaçamento before 120 / after 200 twips. Usar entre seções principais, não entre subseções.

---

## 6. Formatação de Valores e Convenções

- Valores monetários: padrão brasileiro (R$ 1.000.000,00)
- Áreas: hectares (ha)
- Produções: sacas (sc) ou toneladas (t) conforme o produto
- Dispositivos legais: Art. X, §Y, inciso Z, da Lei nº AAAA/BBBB
- Campos pendentes: "[A CONFIRMAR — descrição]" em itálico, cor #999999
- Datas: formato brasileiro (DD/MM/AAAA)
- Confidencialidade: incluir "CONFIDENCIAL" quando documento for uso restrito

---

## 7. Otimização para Leitura em Celular

Regras aplicáveis ao Modo Cliente e qualquer documento que o produtor rural receberá por WhatsApp:

- Layout coluna única (nunca múltiplas colunas)
- Parágrafos curtos: 3-4 frases no máximo
- Espaço entre parágrafos em vez de recuo de primeira linha
- Tabelas: máximo 3 colunas; se precisar de mais, dividir em duas tabelas
- Headings claros e descritivos (o cliente escaneia antes de ler)
- Contraste mínimo WCAG AA: ratio 4.5:1 para texto normal, 3:1 para texto grande
- A paleta AeM atende esses ratios: #333333 sobre branco = 12.6:1; #1D3D69 sobre branco = 9.8:1

---

## 8. Dados Institucionais

### Razão social
Amaral e Melo Advogados

### Tagline
Jurídico no Agro

### Selo comemorativo atual
20 Anos (incluído na logo)

### Unidades

| | Jataí | Rio Verde |
|-|-------|-----------|
| Endereço | Rua Minas Gerais, 1409 - Samuel Graham | Av. Presidente Vargas, 266 - Centro Empresarial Le Monde, sala 601 - Jardim Marconal |
| CEP | 75.804-062 | 75.901-551 |
| Telefone | (64) 99606-5724 | (64) 99903-1847 |
| E-mail | contato@amaralemelo.adv.br | rioverde@amaralemelo.adv.br |

### Sites
- amaralemelo.adv.br (principal)
- amaralemelo.com (redirecionamento)

---

*Última atualização: Agosto 2026 (assets de logo oficiais transparentes, renderização 227×62)*
*Fonte única de verdade para formatação de documentos da Amaral e Melo Advogados.*
