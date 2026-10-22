---
name: "layout-aem"
description: "Identidade visual da Amaral e Melo: papel timbrado .docx (modos tribunal, cliente, interno, publicação e contrato) e tokens de marca para HTML, deck e imagem. Infraestrutura chamada por dependência, ou ao mencionar papel timbrado, marca ou layout AeM."
---

# Layout AeM — Identidade Visual e Formatação de Documentos

Skill de infraestrutura que centraliza todas as regras de formatação, assets visuais e código reutilizável para documentos .docx da Amaral e Melo Advogados — e, pelo módulo visual multi-formato, os tokens de marca para HTML/artifact, apresentações .pptx e imagens. Outras skills que geram documentos devem referenciar esta skill em vez de definir formatação localmente.

## Quando acionar

Use SEMPRE que qualquer outra skill precisar gerar um documento .docx com papel timbrado, identidade visual ou formatação padronizada do escritório — e sempre que um output visual (painel HTML, dashboard, artifact, deck .pptx, imagem institucional) precisar da marca AeM. Também acione quando o usuário mencionar "papel timbrado", "identidade do escritório", "formatar com a marca", "layout AeM", "documento timbrado", "cabeçalho do escritório", ou qualquer variação de pedido para aplicar o padrão visual da Amaral e Melo. Esta skill NÃO gera conteúdo — ela fornece as regras de formatação, os assets visuais (logo) e os templates de código para que outras skills gerem documentos padronizados. É uma skill de infraestrutura, chamada por dependência.

## Dependências

Esta skill gera documentos .docx. Antes de gerar qualquer documento, leia a skill `docx` em `/mnt/skills/public/docx/SKILL.md` para seguir as melhores práticas de criação de arquivos Word.

## Onde esta skill está no disco

O caminho varia por ambiente: `/mnt/skills/user/layout-aem/` em sessões claude.ai, ou uma pasta sincronizada em `~/.claude/skills/synced/<org>_<usuario>/layout-aem/` no Cowork. Não codificar caminho fixo: localizar uma vez e guardar em variável.

```bash
LAYOUT_AEM=$(dirname "$(find / -path '*/layout-aem/SKILL.md' 2>/dev/null | head -1)")
ls "$LAYOUT_AEM/assets" "$LAYOUT_AEM/scripts"
```

## Guia de marca completo

O arquivo `references/brand-guide.md` contém todas as especificações técnicas: cores (hex), tipografia (fontes, tamanhos, pesos por nível hierárquico), espaçamentos, margens, dados de contato das unidades, e regras de Visual Law. **Leia este arquivo antes de formatar qualquer documento.**

## Módulo visual multi-formato

Para outputs que NÃO são .docx — painel ou dashboard em HTML/artifact, apresentação .pptx, imagem/poster — leia `references/visual-tokens.md` e aplique os tokens de lá. Não defina cores, fontes ou componentes localmente.

Regras de roteamento (decisão F-07, 26/08/2026):
- Painel/dashboard → HTML nativo (artifact), com os tokens deste módulo.
- Deck institucional (sócios, clientes) → skill `pptx` nativa + tokens deste módulo. NÃO usar Gamma, Canva ou SlidesGPT como padrão.
- Gamma/Canva/SlidesGPT: apenas quando o usuário pedir a plataforma explicitamente (conteúdo descartável de marketing, brand kit do Canva).
- Imagem/poster → skill `canvas-design` com a paleta deste módulo como restrição.

## Assets disponíveis

| Arquivo | Descrição | Dimensões |
|---------|-----------|-----------|
| `assets/logo_aem.png` | Logo completa com selo 20 anos (leão + Amaral & Melo + Jurídico no Agro + selo), **fundo transparente** — arte oficial do brandbook 2025. Uso padrão em fundo claro (timbre .docx, cabeçalhos) | 2000 × 547 px (320 KB) |
| `assets/logo_aem_cor.png` | Logo horizontal cor sem selo, fundo transparente — versão limpa para composições onde o selo não cabe | 2000 × 497 px |
| `assets/logo_aem_negativo.png` | Logo horizontal negativo (texto branco, leão contornado, tagline dourada), fundo transparente — **única versão permitida sobre fundo escuro** | 2000 × 497 px |

Fonte canônica das artes: brandbook Amaral & Melo 2025 e pasta `MKT/Logos` do Drive (RGB/PNG). Nunca recriar, esticar ou recolorir o logo; nunca usar a versão cor sobre fundo escuro.

### Cópia reduzida para embutir no .docx

O asset original tem 320 KB e faz cada documento pesar cerca de 340 KB. No cabeçalho o logo é renderizado com 227 × 62 px, então uma cópia de 680 px de largura, quantizada em 128 cores, é visualmente idêntica e tem 19 KB (documentos finais ficam em torno de 45 KB). Gerar a cópia no início da sessão, a partir do asset oficial, e apontar `logoPath` para ela:

```bash
python3 - <<'EOF'
from PIL import Image
import os
src = os.environ.get('LAYOUT_AEM', '.') + '/assets/logo_aem.png'
im = Image.open(src).convert('RGBA')
w, h = im.size
nw = 680; nh = round(h * nw / w)
im.resize((nw, nh), Image.LANCZOS).quantize(colors=128, method=Image.Quantize.FASTOCTREE).save('logo_aem_680.png', optimize=True)
EOF
```

O redimensionamento é só para embutir: o asset oficial não muda e continua sendo a fonte para HTML, deck e imagem.

## Modos de calibração

A skill define cinco modos de formatação, cada um otimizado para um destinatário e contexto de leitura. O modo deve ser escolhido pela skill chamadora com base no tipo de documento. Em todos os modos o cabeçalho leva o logo (62 px de altura) e a linha dourada, o que ocupa cerca de 1600 twips: por isso a margem superior é de 2000 twips (3,5 cm) com distância do cabeçalho de 400 twips, e a margem inferior é de 1900 twips (3,35 cm) quando o rodapé traz os endereços das unidades (quatro linhas) ou 1500 twips (2,65 cm) quando traz só a tarja "confidencial" ou a numeração. Valores testados em Word e LibreOffice em 21/09/2026.

### Modo Tribunal
Peças judiciais, impugnações, recursos, petições. Destinatário: magistrado/servidor.
- A4, margens 3cm (esquerda), 2cm (direita), 3,5cm (topo, cabeçalho com logo), 3,35cm (inferior, rodapé com endereços)
- Corpo: Arial 12pt, justificado com hifenização
- Títulos: Georgia Bold 14pt, azul marinho (#1D3D69)
- Entrelinhamento: 1.5 (equivalente a 18pt para corpo 12pt)
- Intensidade visual: moderada (tabelas e fluxogramas sim, QR codes não)
- Cabeçalho com logo, rodapé com endereços + numeração de página

### Modo Cliente
Pareceres, entregáveis, relatórios para produtor rural. Destinatário: cliente leigo.
- A4, margens laterais 2cm, topo 3,5cm, inferior 3,35cm
- Corpo: Arial 13pt, justificado
- Títulos: Georgia Bold 15pt, azul marinho (#1D3D69)
- Entrelinhamento: 1.3 (equivalente a ~17pt para corpo 13pt)
- Espaço entre parágrafos: 8pt (sem recuo de primeira linha)
- Caixas de destaque coloridas, tabelas comparativas, linguagem simples
- Otimizado para leitura em celular (parágrafos curtos, coluna única)
- Cabeçalho com logo, rodapé com endereços + numeração de página

### Modo Interno
Briefings, fichas técnicas, guias de uso de minuta, documentos de trabalho. Destinatário: equipe do escritório.
- A4, margens laterais 2cm, topo 3,5cm, inferior 2,65cm
- Corpo: Arial 11pt, justificado
- Títulos: Arial Bold 13pt, azul marinho (#1D3D69)
- Entrelinhamento: 1.2
- Formato compacto, uso livre de tabelas e códigos de cor
- Cabeçalho com logo, rodapé com "CONFIDENCIAL — USO INTERNO" + numeração

### Modo Publicação
Artigos, conteúdo para portais jurídicos e agro. Destinatário: público leitor.
- A4, margens laterais 2,5cm, topo 3,5cm, inferior 2,65cm
- Corpo: Georgia 12pt, justificado
- Títulos: Georgia Bold 16pt, azul marinho (#1D3D69)
- Entrelinhamento: 1.5
- Parágrafos com espaço entre eles (10pt), sem recuo
- Cabeçalho com logo, sem rodapé com endereços (apenas numeração)

### Modo Contrato
Minutas, contratos, aditivos, termos e anexos contratuais. Destinatário: partes, testemunhas, cartório e, em juízo, o magistrado. Incluído em 21/09/2026 (minuta padrão de parceria rural v2.0).
- A4, margens laterais 2,5cm, topo 3,5cm, inferior 3,35cm
- Corpo: Arial 11pt, justificado
- Títulos: Georgia Bold 14pt (título do instrumento, centralizado), 12pt (cláusulas), 11pt (subtítulos), azul marinho (#1D3D69)
- Entrelinhamento: 1.2; espaço entre parágrafos 6pt; sem recuo
- Tabelas em 9pt (quadro-resumo, demonstrativos), linhas que não quebram entre páginas
- Campos variáveis escritos entre colchetes e destacados com sombreamento amarelo claro (`FFF2A8`) no run, nunca com `highlight`
- Bloco de assinaturas indivisível: fecho, data e linhas de assinatura com `keepNext`
- Quebra de página só antes dos anexos que precisam começar em página nova (quadro-resumo); os demais anexos seguem no fluxo
- Cabeçalho com logo, rodapé com endereços + numeração de página

## Como gerar o documento .docx

Use o script JavaScript abaixo como base. Ele demonstra a geração completa de um .docx com cabeçalho (logo), rodapé (endereços + numeração), estilos tipográficos e estrutura de página.

### Passo 1 — Instalar dependências

```bash
npm install -g docx
```

### Passo 2 — Estrutura base do documento

O código abaixo é o esqueleto reutilizável. Substitua `[CONTEÚDO]` pelo conteúdo gerado pela skill chamadora.

```javascript
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, ImageRun, Header, Footer,
        AlignmentType, HeadingLevel, BorderStyle, PageNumber, TabStopType,
        PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo,
        PositionalTabLeader, Table, TableRow, TableCell, WidthType,
        ShadingType, LevelFormat, LineRuleType, PageBreak } = require('docx');

// ═══════════════════════════════════════════════════════════════
// CONFIGURAÇÃO DO MODO — ajustar conforme o tipo de documento
// ═══════════════════════════════════════════════════════════════
const MODO = 'cliente'; // 'tribunal' | 'cliente' | 'interno' | 'publicacao' | 'contrato'

// Margens em DXA/twips (1cm = 567). Topo 2000 em todos os modos: o cabeçalho com logo
// ocupa ~1600 twips e margem menor faz o corpo colidir com o logo (Word e LibreOffice
// reagem de forma diferente). Inferior 1900 com rodapé de endereços, 1500 sem ele.
const CONFIG = {
  tribunal: {
    margemTopo: 2000,
    margemInferior: 1900,
    margemEsquerda: 1701, // 3cm
    margemDireita: 1134,  // 2cm
    corpoFonte: 'Arial', corpoTamanho: 24, // half-points: 24 = 12pt
    tituloFonte: 'Georgia', tituloTamanho: 28, // 14pt
    entrelinhamento: 360, // 1.5 × 240 = 360 (twips)
    espacoEntreParas: 0,
    recuoPrimeiraLinha: 720, // ~1,27cm
    rodapeTexto: 'enderecos',
    tabelaFonte: 20, // 10pt
  },
  cliente: {
    margemTopo: 2000,
    margemInferior: 1900,
    margemEsquerda: 1134,
    margemDireita: 1134,
    corpoFonte: 'Arial', corpoTamanho: 26, // 13pt
    tituloFonte: 'Georgia', tituloTamanho: 30, // 15pt
    entrelinhamento: 312, // 1.3 × 240
    espacoEntreParas: 160, // 8pt em twips
    recuoPrimeiraLinha: 0,
    rodapeTexto: 'enderecos',
    tabelaFonte: 22, // 11pt
  },
  interno: {
    margemTopo: 2000,
    margemInferior: 1500,
    margemEsquerda: 1134,
    margemDireita: 1134,
    corpoFonte: 'Arial', corpoTamanho: 22, // 11pt
    tituloFonte: 'Arial', tituloTamanho: 26, // 13pt
    entrelinhamento: 288, // 1.2 × 240
    espacoEntreParas: 120,
    recuoPrimeiraLinha: 0,
    rodapeTexto: 'confidencial',
    tabelaFonte: 18, // 9pt
  },
  publicacao: {
    margemTopo: 2000,
    margemInferior: 1500,
    margemEsquerda: 1418,
    margemDireita: 1418,
    corpoFonte: 'Georgia', corpoTamanho: 24, // 12pt
    tituloFonte: 'Georgia', tituloTamanho: 32, // 16pt
    entrelinhamento: 360,
    espacoEntreParas: 200, // 10pt
    recuoPrimeiraLinha: 0,
    rodapeTexto: 'simples',
    tabelaFonte: 20,
  },
  contrato: {
    margemTopo: 2000,
    margemInferior: 1900,
    margemEsquerda: 1418, // 2,5cm
    margemDireita: 1418,
    corpoFonte: 'Arial', corpoTamanho: 22, // 11pt
    tituloFonte: 'Georgia', tituloTamanho: 28, // 14pt (H2 = 12pt, H3 = 11pt)
    entrelinhamento: 288, // 1.2
    espacoEntreParas: 120, // 6pt
    recuoPrimeiraLinha: 0,
    rodapeTexto: 'enderecos',
    tabelaFonte: 18, // 9pt
  },
};

const cfg = CONFIG[MODO];

// ═══════════════════════════════════════════════════════════════
// CORES DA MARCA
// ═══════════════════════════════════════════════════════════════
const AZUL_MARINHO = '1D3D69';
const DOURADO = 'B88657';
const CINZA_CLARO = 'F5F5F5';
const CINZA_BORDA = 'CCCCCC';
const CAMPO_FUNDO = 'FFF2A8'; // sombreamento dos campos variáveis [campo]

// ═══════════════════════════════════════════════════════════════
// LOGO
// ═══════════════════════════════════════════════════════════════
// Apontar para a cópia reduzida (680 px, 128 cores) gerada a partir de assets/logo_aem.png.
// Nunca prosseguir sem o logo: é regra inviolável.
const logoPath = process.env.LOGO_AEM || (__dirname + '/logo_aem_680.png');
if (!fs.existsSync(logoPath)) { console.error('Logo AeM não encontrada: ' + logoPath); process.exit(1); }
const logoBuffer = fs.readFileSync(logoPath);
// Proporção da arte 2000:547. No header, renderizar com 227 × 62 px (~6cm de largura).

// ═══════════════════════════════════════════════════════════════
// CABEÇALHO
// ═══════════════════════════════════════════════════════════════
function criarCabecalho() {
  return new Header({
    children: [
      new Paragraph({
        // Entrelinha explícita e proporcional: sem lineRule, o LibreOffice aplica o entrelinha
        // padrão do documento como altura fixa e corta o logo. Testado em 21/09/2026.
        spacing: { line: 240, lineRule: LineRuleType.AUTO, after: 0 },
        children: [
          new ImageRun({
            data: logoBuffer,
            transformation: { width: 227, height: 62 }, // px para renderização (proporção 2000:547)
            type: 'png',
          }),
        ],
      }),
      // Linha separadora dourada abaixo da logo
      new Paragraph({
        border: {
          bottom: { style: BorderStyle.SINGLE, size: 6, color: DOURADO, space: 1 },
        },
        spacing: { after: 200 },
      }),
    ],
  });
}

// ═══════════════════════════════════════════════════════════════
// RODAPÉ
// ═══════════════════════════════════════════════════════════════
function criarRodape() {
  const filhos = [];

  // Linha separadora dourada acima do rodapé
  filhos.push(
    new Paragraph({
      border: {
        bottom: { style: BorderStyle.SINGLE, size: 4, color: DOURADO, space: 1 },
      },
      spacing: { after: 100 },
    })
  );

  if (cfg.rodapeTexto === 'enderecos') {
    // Unidade Jataí (lado esquerdo) | Unidade Rio Verde (lado direito)
    // Usando tab stops para duas colunas
    const rodapeFonte = { font: 'Arial', size: 14, color: '666666' }; // 7pt
    const rodapeNegrito = { ...rodapeFonte, bold: true, color: AZUL_MARINHO, size: 16 }; // 8pt

    filhos.push(
      new Paragraph({
        tabStops: [{ type: TabStopType.LEFT, position: 5200 }],
        spacing: { after: 20 },
        children: [
          new TextRun({ ...rodapeNegrito, text: 'Unidade Jataí' }),
          new TextRun({ ...rodapeFonte, text: '\t' }),
          new TextRun({ ...rodapeNegrito, text: 'Unidade Rio Verde' }),
        ],
      }),
      new Paragraph({
        tabStops: [{ type: TabStopType.LEFT, position: 5200 }],
        spacing: { after: 20 },
        children: [
          new TextRun({ ...rodapeFonte, text: 'Rua Minas Gerais, 1409 - Samuel Graham' }),
          new TextRun({ ...rodapeFonte, text: '\t' }),
          new TextRun({ ...rodapeFonte, text: 'Av. Presidente Vargas, 266 - Centro Empresarial Le Monde' }),
        ],
      }),
      new Paragraph({
        tabStops: [{ type: TabStopType.LEFT, position: 5200 }],
        spacing: { after: 20 },
        children: [
          new TextRun({ ...rodapeFonte, text: 'Jataí-GO, CEP 75.804-062' }),
          new TextRun({ ...rodapeFonte, text: '\t' }),
          new TextRun({ ...rodapeFonte, text: 'sala 601 - Jardim Marconal, Rio Verde-GO, CEP 75.901-551' }),
        ],
      }),
      new Paragraph({
        tabStops: [{ type: TabStopType.LEFT, position: 5200 }],
        spacing: { after: 20 },
        children: [
          new TextRun({ ...rodapeFonte, text: '☎ (64) 99606-5724 | contato@amaralemelo.adv.br' }),
          new TextRun({ ...rodapeFonte, text: '\t' }),
          new TextRun({ ...rodapeFonte, text: '☎ (64) 99903-1847 | rioverde@amaralemelo.adv.br' }),
        ],
      })
    );
  } else if (cfg.rodapeTexto === 'confidencial') {
    filhos.push(
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({
            text: 'CONFIDENCIAL — USO INTERNO — AMARAL E MELO ADVOGADOS',
            font: 'Arial', size: 14, color: '999999', italics: true,
          }),
        ],
      })
    );
  }

  // Numeração de página (sempre presente, alinhada à direita)
  filhos.push(
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      spacing: { before: 60 },
      children: [
        new TextRun({ font: 'Arial', size: 16, color: AZUL_MARINHO, bold: true,
          children: [PageNumber.CURRENT] }),
      ],
    })
  );

  return new Footer({ children: filhos });
}

// ═══════════════════════════════════════════════════════════════
// ESTILOS DO DOCUMENTO
// ═══════════════════════════════════════════════════════════════
function criarEstilos() {
  return {
    default: {
      document: {
        run: { font: cfg.corpoFonte, size: cfg.corpoTamanho, color: '333333' },
        paragraph: {
          spacing: {
            line: cfg.entrelinhamento,
            lineRule: LineRuleType.AUTO, // sempre explícito (ver cabeçalho)
            after: cfg.espacoEntreParas,
          },
          indent: cfg.recuoPrimeiraLinha > 0
            ? { firstLine: cfg.recuoPrimeiraLinha }
            : undefined,
        },
      },
    },
    paragraphStyles: [
      {
        id: 'Heading1', name: 'Heading 1',
        basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: cfg.tituloTamanho, bold: true, font: cfg.tituloFonte, color: AZUL_MARINHO },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0, keepNext: true },
      },
      {
        id: 'Heading2', name: 'Heading 2',
        basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: cfg.tituloTamanho - 2, bold: true, font: cfg.tituloFonte, color: AZUL_MARINHO },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 1, keepNext: true },
      },
      {
        id: 'Heading3', name: 'Heading 3',
        basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: cfg.corpoTamanho + 2, bold: true, font: cfg.corpoFonte, color: AZUL_MARINHO },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2, keepNext: true },
      },
    ],
  };
}

// ═══════════════════════════════════════════════════════════════
// HELPERS PARA CONTEÚDO
// ═══════════════════════════════════════════════════════════════

// Separador de seção (linha dourada fina)
function separadorSecao() {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: DOURADO, space: 4 } },
    spacing: { before: 120, after: 200 },
  });
}

// Campo variável de minuta: texto entre colchetes com sombreamento amarelo no run.
// Nunca usar `highlight` no TextRun: o docx-js emite w:highlightCs e o validador rejeita.
function campo(nome, base) {
  return new TextRun({ ...(base || {}), text: '[' + nome + ']', shading: { type: ShadingType.CLEAR, fill: CAMPO_FUNDO } });
}

// Caixa de destaque (borda esquerda colorida + fundo)
function caixaDestaque(tipo, textos) {
  const temas = {
    alerta:       { fundo: 'FFF9E6', borda: 'E67E22' },
    risco:        { fundo: 'FFF0F0', borda: 'C0392B' },
    economia:     { fundo: 'F0FFF0', borda: '27AE60' },
    recomendacao: { fundo: 'F0F5FF', borda: AZUL_MARINHO },
    info:         { fundo: 'F0F5FF', borda: DOURADO },
  };
  const tema = temas[tipo] || temas.info;
  const borda = { style: BorderStyle.SINGLE, size: 1, color: tema.borda };
  const bordaEsquerda = { style: BorderStyle.SINGLE, size: 18, color: tema.borda, space: 8 };
  // Nota: docx-js reordena borders internamente. Usar scripts/fix_borders.py após geração.
  return textos.map((texto, i) => {
    const borders = { top: borda, left: bordaEsquerda, bottom: borda, right: borda };
    return new Paragraph({
      border: borders,
      shading: { fill: tema.fundo, type: ShadingType.CLEAR },
      spacing: { before: i === 0 ? 120 : 40, after: i === textos.length - 1 ? 120 : 40 },
      indent: { left: 200, right: 200 },
      children: Array.isArray(texto) ? texto : [new TextRun(texto)],
    });
  });
}

// Tabela padrão AeM (cabeçalho azul marinho, linhas alternadas).
// `larguras` (opcional): percentuais por coluna, ex.: [30, 70]; sem ele, colunas iguais.
// Linhas com cantSplit para não quebrar entre páginas (quadro-resumo, demonstrativos).
function tabelaAeM(cabecalhos, linhas, larguraTotal, larguras) {
  const larg = larguraTotal || larguraUtil;
  const pct = larguras && larguras.length === cabecalhos.length ? larguras : cabecalhos.map(() => 100 / cabecalhos.length);
  const ws = pct.map(p => Math.floor(larg * p / 100));
  const bordaTabela = { style: BorderStyle.SINGLE, size: 1, color: CINZA_BORDA };
  const bordas = { top: bordaTabela, bottom: bordaTabela, left: bordaTabela, right: bordaTabela };
  const margem = { top: 60, bottom: 60, left: 100, right: 100 };

  const headerRow = new TableRow({
    tableHeader: true,
    cantSplit: true,
    children: cabecalhos.map((h, i) =>
      new TableCell({
        borders: bordas,
        width: { size: ws[i], type: WidthType.DXA },
        shading: { fill: AZUL_MARINHO, type: ShadingType.CLEAR },
        margins: margem,
        children: [new Paragraph({
          children: [new TextRun({ text: h, bold: true, color: 'FFFFFF', font: 'Arial', size: cfg.tabelaFonte })],
        })],
      })
    ),
  });

  const dataRows = linhas.map((linha, idx) =>
    new TableRow({
      cantSplit: true,
      children: linha.map((celula, i) =>
        new TableCell({
          borders: bordas,
          width: { size: ws[i], type: WidthType.DXA },
          shading: idx % 2 === 0
            ? { fill: CINZA_CLARO, type: ShadingType.CLEAR }
            : undefined,
          margins: margem,
          children: [new Paragraph({
            children: Array.isArray(celula) ? celula : [new TextRun({
              text: celula, font: 'Arial', size: cfg.tabelaFonte,
            })],
          })],
        })
      ),
    })
  );

  return new Table({
    width: { size: larg, type: WidthType.DXA },
    columnWidths: ws,
    rows: [headerRow, ...dataRows],
  });
}

// Bloco de assinaturas indivisível (modo contrato): fecho, local/data e linhas de assinatura
// com keepNext, para nunca deixar assinatura sozinha em página nova.
function blocoAssinaturas(fecho, localData, assinantes) {
  const paras = [
    new Paragraph({ keepNext: true, spacing: { before: 240 }, children: [new TextRun(fecho)] }),
    new Paragraph({ keepNext: true, children: [new TextRun(localData)] }),
  ];
  assinantes.forEach((a, i) => {
    paras.push(new Paragraph({ keepNext: i < assinantes.length - 1, spacing: { before: 360 }, children: [new TextRun('_'.repeat(45))] }));
    paras.push(new Paragraph({ keepNext: i < assinantes.length - 1, children: [new TextRun({ text: a, bold: true })] }));
  });
  return paras;
}

// ═══════════════════════════════════════════════════════════════
// MONTAGEM DO DOCUMENTO
// ═══════════════════════════════════════════════════════════════

// Calcular largura útil para tabelas (largura da página - margens)
const larguraPagina = 11906; // A4 em DXA
const larguraUtil = larguraPagina - cfg.margemEsquerda - cfg.margemDireita;

const doc = new Document({
  styles: criarEstilos(),
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: {
          top: cfg.margemTopo,
          bottom: cfg.margemInferior,
          left: cfg.margemEsquerda,
          right: cfg.margemDireita,
          header: 400, // distância do cabeçalho à borda
          footer: 400,
        },
      },
    },
    headers: { default: criarCabecalho() },
    footers: { default: criarRodape() },
    children: [
      // ═══ [CONTEÚDO] — substituir pelo conteúdo da skill chamadora ═══
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun('Título do Documento')],
      }),
      new Paragraph({
        children: [new TextRun('Conteúdo do documento aqui.')],
      }),
      // ═══ [FIM DO CONTEÚDO] ═══
    ],
  }],
});

// ═══════════════════════════════════════════════════════════════
// GERAR E SALVAR
// ═══════════════════════════════════════════════════════════════
const outputPath = '/mnt/user-data/outputs/documento_aem.docx';
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log('Documento gerado:', outputPath);
});
```

### Passo 3 — Corrigir, validar e inspecionar

O docx-js reordena borders de parágrafo para `top, bottom, left, right`, mas o schema OpenXML exige `top, left, bottom, right`. Se o documento usar caixas de destaque (`caixaDestaque`), aplicar o fix. A rota portátil (funciona em qualquer ambiente com `unzip`/`zip`):

```bash
rm -rf u_doc && mkdir u_doc && (cd u_doc && unzip -q ../documento_aem.docx)
python3 "$LAYOUT_AEM/scripts/fix_borders.py" u_doc/word/document.xml
(cd u_doc && zip -qXr -9 ../documento_aem.docx .)
python3 /mnt/skills/public/docx/scripts/office/validate.py documento_aem.docx
```

Onde a skill `docx` oferecer `scripts/office/unpack.py` e `pack.py`, eles substituem o `unzip`/`zip` (`pack.py unpacked/ saida.docx --original entrada.docx`). Nem todo ambiente os traz: conferir com `ls /mnt/skills/public/docx/scripts/office/`.

Se o documento não usa caixas de destaque, a validação direta funciona:

```bash
python3 /mnt/skills/public/docx/scripts/office/validate.py documento_aem.docx
```

Validar não basta: converter em PDF e olhar página a página antes de entregar. É o único jeito de pegar logo cortado, tabela partida, assinatura sozinha em página nova ou campo com colchete quebrado.

```bash
soffice --headless --convert-to pdf --outdir . documento_aem.docx
pdftoppm -r 60 -png documento_aem.pdf pag   # gera pag-1.png, pag-2.png ... para leitura
```

### Armadilhas conhecidas (registradas em 21/09/2026)

1. **Logo cortado no LibreOffice.** O entrelinha padrão do documento (`w:line="288"` ou `360`) sem `lineRule` é aplicado ao parágrafo do logo como altura fixa e corta a imagem. Sempre `lineRule: LineRuleType.AUTO` nos estilos padrão e `spacing: { line: 240, lineRule: AUTO }` no parágrafo do logo. O Word não mostra o defeito; o cliente que abre no LibreOffice ou no celular mostra.
2. **`highlight` no TextRun.** Gera `w:highlightCs`, que o validador rejeita. Para destacar campo variável, usar `shading` no run (`campo()` acima).
3. **Linha de tabela partida entre páginas.** `cantSplit: true` em toda `TableRow` (já no helper `tabelaAeM`).
4. **Assinatura órfã.** Fecho, data e assinaturas com `keepNext` (helper `blocoAssinaturas`); títulos também com `keepNext` para não ficarem sozinhos no fim da página.
5. **Documento de 340 KB.** É o logo original embutido; usar a cópia reduzida de 680 px (seção Assets).
6. **Quebra de página antes de cada anexo.** Só antes do anexo que precisa começar em página nova; o resto segue no fluxo, senão sobram páginas com três linhas.
7. **Fix de borders com `zip` no lugar de `pack.py`.** Reempacotar de dentro da pasta descompactada (`cd u_doc && zip -qXr -9 ../saida.docx .`), senão o `[Content_Types].xml` fica fora da raiz e o Word recusa o arquivo.

## Como outras skills devem referenciar esta skill

No topo do SKILL.md da skill chamadora, incluir:

```markdown
## Dependências

Para formatação do documento, leia a skill `layout-aem` (localizar o SKILL.md com
`find / -path '*/layout-aem/SKILL.md' 2>/dev/null | head -1`; em sessões claude.ai fica em
`/mnt/skills/user/layout-aem/SKILL.md`) antes de gerar o .docx.
Use o código-base, assets e regras de formatação de lá.
Não defina cores, fontes ou margens localmente.
```

A skill chamadora deve:
1. Ler este SKILL.md para obter o código-base
2. Ler `references/brand-guide.md` para especificações detalhadas
3. Escolher o MODO adequado ao tipo de documento (minutas e contratos: `contrato`)
4. Gerar a cópia reduzida do logo e apontar `logoPath` para ela
5. Usar os helpers (`caixaDestaque`, `tabelaAeM`, `separadorSecao`, `campo`, `blocoAssinaturas`) conforme necessário
6. Substituir a seção `[CONTEÚDO]` pelo conteúdo específico
7. Corrigir borders (se houver caixas), validar, converter em PDF e inspecionar página a página

## Regras invioláveis

1. **Nunca gerar documento AeM sem logo no cabeçalho.** Se o asset não for encontrado, sinalizar erro — não prosseguir sem identidade visual.
2. **Nunca usar Times New Roman.** A tipografia do escritório é Georgia (títulos/destaque) e Arial (corpo).
3. **Nunca usar cores fora da paleta.** Azul Marinho (#1D3D69), Dourado (#B88657), e os tons funcionais definidos no brand-guide.
4. **Sempre A4.** Nunca A3, nunca Letter.
5. **Sempre validar o .docx gerado** com o script de validação da skill docx **e inspecionar o PDF página a página** antes de entregar.
6. **Dados de contato canônicos** estão no `references/brand-guide.md`. Se mudarem, atualizar APENAS lá.

## Histórico

- 2026-08-26 (F-07): módulo visual multi-formato e regras de roteamento.
- 2026-09-21: modo `contrato`; margens superior/inferior recalibradas para o cabeçalho com logo; `lineRule` explícito (logo cortado no LibreOffice); cópia reduzida do logo; `campo()` com sombreamento no lugar de `highlight`; `cantSplit`, `keepNext` e `blocoAssinaturas`; `tabelaAeM` com larguras por coluna; rota portátil de fix de borders; inspeção em PDF obrigatória; caminho da skill localizado por `find`. Origem: minuta padrão de parceria rural v2.0.