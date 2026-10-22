/**
 * Gerador de Parecer Jurídico — Amaral e Melo Advogados
 * 
 * Uso: node generate_parecer.js <input.json> <output.docx>
 * 
 * O input.json deve conter:
 * Para parecer: { tipo, tema, data, ementa, consulta, fundamentacao, conclusao }
 * Para briefing: { tipo, tema, data, contexto, analise, recomendacao }
 * Textos podem conter \n para separar parágrafos.
 */

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Header, Footer, ImageRun,
  AlignmentType, BorderStyle, TabStopType, PageNumber
} = require('docx');

// === IDENTIDADE VISUAL AMARAL E MELO ===
const CORES = {
  AZUL_MARINHO: '1D3D69',
  DOURADO: 'B88657',
  PRETO: '000000',
  CINZA_CLARO: '666666',
  CINZA_MEDIO: '999999'
};

const FONTES = {
  PRINCIPAL: 'Georgia',
  SECUNDARIA: 'Arial'
};

// Margens em DXA (1440 DXA = 1 inch = 2.54cm)
const MARGENS = {
  top: 1800,     // Espaço extra para acomodar logo no cabeçalho
  bottom: 1600,  // Espaço extra para rodapé com contatos
  left: 1701,    // 3cm
  right: 1134    // 2cm
};

// A4 (padrão brasileiro)
const PAGE_WIDTH = 11906;
const PAGE_HEIGHT = 16838;
const CONTENT_WIDTH = PAGE_WIDTH - MARGENS.left - MARGENS.right;

// Caminho da logo relativo ao script
const LOGO_PATH = path.join(__dirname, '..', 'assets', 'logo_aem.png');

// === HELPERS ===

/** Converte texto com \n em array de Paragraphs formatados para corpo */
function textToBodyParagraphs(text, extraRunOpts = {}) {
  return text.split('\n').filter(p => p.trim() !== '').map(p =>
    new Paragraph({
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: 360, after: 120 },
      indent: { firstLine: 720 },
      children: [
        new TextRun({
          text: p.trim(),
          font: FONTES.PRINCIPAL,
          size: 24,
          color: CORES.PRETO,
          ...extraRunOpts
        })
      ]
    })
  );
}

/** Título de seção (ex: "I. EMENTA") */
function sectionTitle(text) {
  return new Paragraph({
    spacing: { before: 360, after: 200 },
    children: [
      new TextRun({ text, font: FONTES.PRINCIPAL, size: 26, bold: true, color: CORES.AZUL_MARINHO })
    ]
  });
}

/** Linha dourada decorativa */
function goldenLine() {
  return new Paragraph({
    spacing: { before: 60, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: CORES.DOURADO, space: 1 } },
    children: []
  });
}

// === CABEÇALHO COM LOGO ===
function buildHeader() {
  let logoBuffer = null;
  try {
    if (fs.existsSync(LOGO_PATH)) {
      logoBuffer = fs.readFileSync(LOGO_PATH);
      console.log('Logo carregada com sucesso.');
    }
  } catch (e) {
    console.warn(`Aviso: logo não encontrada em ${LOGO_PATH}. Usando cabeçalho textual.`);
  }

  if (logoBuffer) {
    // Logo original: 690x210px. Renderizar com ~3.3cm de altura (~95px) mantendo proporção
    // docx-js ImageRun transformation usa pixels na prática
    const targetHeight = 95;
    const targetWidth = Math.round(targetHeight * (690 / 210));

    return new Header({
      children: [
        new Paragraph({
          spacing: { after: 80 },
          border: {
            bottom: { style: BorderStyle.SINGLE, size: 4, color: CORES.DOURADO, space: 6 }
          },
          children: [
            new ImageRun({
              data: logoBuffer,
              transformation: { width: targetWidth, height: targetHeight },
              type: 'png'
            })
          ]
        })
      ]
    });
  }

  // Fallback: cabeçalho textual caso a logo não esteja disponível
  return new Header({
    children: [
      new Paragraph({
        spacing: { after: 80 },
        border: {
          bottom: { style: BorderStyle.SINGLE, size: 4, color: CORES.DOURADO, space: 6 }
        },
        children: [
          new TextRun({ text: 'AMARAL & MELO', font: FONTES.SECUNDARIA, size: 22, color: CORES.AZUL_MARINHO, bold: true }),
          new TextRun({ text: '  |  ', font: FONTES.SECUNDARIA, size: 18, color: CORES.CINZA_MEDIO }),
          new TextRun({ text: 'Jur\u00eddico no Agro', font: FONTES.SECUNDARIA, size: 18, color: CORES.AZUL_MARINHO, italics: true })
        ]
      })
    ]
  });
}

// === RODAPÉ COM CONTATOS DAS DUAS UNIDADES ===
function buildFooter() {
  // Tab stop para alinhar a coluna da direita (Unidade Rio Verde)
  const rightColTab = Math.round(CONTENT_WIDTH / 2) + 200;
  const tabStops = [{ type: TabStopType.LEFT, position: rightColTab }];
  const smallFont = { font: FONTES.SECUNDARIA, size: 13, color: CORES.CINZA_CLARO };
  const labelFont = { font: FONTES.SECUNDARIA, size: 14, bold: true, color: CORES.AZUL_MARINHO };

  return new Footer({
    children: [
      // Linha dourada no topo do rodapé
      new Paragraph({
        spacing: { after: 60 },
        border: { top: { style: BorderStyle.SINGLE, size: 3, color: CORES.DOURADO, space: 4 } },
        children: []
      }),
      // Nomes das unidades
      new Paragraph({
        spacing: { after: 0 }, tabStops,
        children: [
          new TextRun({ text: 'Unidade Jata\u00ed', ...labelFont }),
          new TextRun({ text: '\t', ...smallFont }),
          new TextRun({ text: 'Unidade Rio Verde', ...labelFont })
        ]
      }),
      // Endereços
      new Paragraph({
        spacing: { after: 0 }, tabStops,
        children: [
          new TextRun({ text: 'Rua Minas Gerais, 1409 - Samuel Graham', ...smallFont }),
          new TextRun({ text: '\t', ...smallFont }),
          new TextRun({ text: 'Av. Presidente Vargas, 266 - Le Monde, sala 601', ...smallFont })
        ]
      }),
      // Cidade/CEP
      new Paragraph({
        spacing: { after: 0 }, tabStops,
        children: [
          new TextRun({ text: 'Jata\u00ed-GO, CEP 75.804-062', ...smallFont }),
          new TextRun({ text: '\t', ...smallFont }),
          new TextRun({ text: 'Jardim Marconal, Rio Verde-GO, CEP 75.901-551', ...smallFont })
        ]
      }),
      // Telefone e email
      new Paragraph({
        spacing: { after: 0 }, tabStops,
        children: [
          new TextRun({ text: '(64) 99606-5724 | contato@amaralemelo.adv.br', ...smallFont }),
          new TextRun({ text: '\t', ...smallFont }),
          new TextRun({ text: '(64) 99903-1847 | rioverde@amaralemelo.adv.br', ...smallFont })
        ]
      }),
      // Número da página centralizado
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 80 },
        children: [
          new TextRun({ text: 'P\u00e1gina ', font: FONTES.SECUNDARIA, size: 13, color: CORES.CINZA_MEDIO }),
          new TextRun({ children: [PageNumber.CURRENT], font: FONTES.SECUNDARIA, size: 13, color: CORES.CINZA_MEDIO })
        ]
      })
    ]
  });
}

// === GERAÇÃO DO CORPO DO PARECER ===
function generateParecer(data) {
  const children = [];

  // Título principal centralizado
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 400, after: 100 },
    children: [
      new TextRun({
        text: data.tipo === 'briefing' ? 'BRIEFING JUR\u00cdDICO' : 'PARECER JUR\u00cdDICO',
        font: FONTES.PRINCIPAL, size: 32, bold: true, color: CORES.AZUL_MARINHO
      })
    ]
  }));

  // Subtítulo com o tema
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 100 },
    children: [
      new TextRun({
        text: data.tema,
        font: FONTES.PRINCIPAL, size: 24, italics: true, color: CORES.AZUL_MARINHO
      })
    ]
  }));

  children.push(goldenLine());

  // Corpo: varia conforme o tipo de peça
  if (data.tipo === 'briefing') {
    if (data.contexto) { children.push(sectionTitle('CONTEXTO')); children.push(...textToBodyParagraphs(data.contexto)); }
    if (data.analise) { children.push(sectionTitle('AN\u00c1LISE')); children.push(...textToBodyParagraphs(data.analise)); }
    if (data.recomendacao) { children.push(sectionTitle('RECOMENDA\u00c7\u00c3O')); children.push(...textToBodyParagraphs(data.recomendacao)); }
  } else {
    children.push(sectionTitle('I. EMENTA'));
    children.push(...textToBodyParagraphs(data.ementa, { italics: true }));
    children.push(sectionTitle('II. DA CONSULTA'));
    children.push(...textToBodyParagraphs(data.consulta));
    children.push(sectionTitle('III. DA FUNDAMENTA\u00c7\u00c3O'));
    children.push(...textToBodyParagraphs(data.fundamentacao));
    children.push(sectionTitle('IV. DA CONCLUS\u00c3O'));
    children.push(...textToBodyParagraphs(data.conclusao));
  }

  children.push(goldenLine());

  // Fechamento: local, data e assinatura
  children.push(new Paragraph({
    alignment: AlignmentType.RIGHT, spacing: { before: 200 },
    children: [new TextRun({ text: `Rio Verde/GO, ${data.data}`, font: FONTES.PRINCIPAL, size: 24, color: CORES.PRETO })]
  }));
  children.push(new Paragraph({
    alignment: AlignmentType.RIGHT, spacing: { before: 200, after: 100 },
    children: [new TextRun({ text: 'AMARAL & MELO ADVOGADOS', font: FONTES.PRINCIPAL, size: 24, bold: true, color: CORES.AZUL_MARINHO })]
  }));
  children.push(new Paragraph({
    alignment: AlignmentType.RIGHT,
    children: [new TextRun({ text: 'Jur\u00eddico no Agro', font: FONTES.PRINCIPAL, size: 20, italics: true, color: CORES.CINZA_CLARO })]
  }));

  // Monta o documento final com cabeçalho, rodapé e conteúdo
  return new Document({
    styles: {
      default: { document: { run: { font: FONTES.PRINCIPAL, size: 24 } } }
    },
    sections: [{
      properties: {
        page: {
          size: { width: PAGE_WIDTH, height: PAGE_HEIGHT },
          margin: MARGENS
        }
      },
      headers: { default: buildHeader() },
      footers: { default: buildFooter() },
      children
    }]
  });
}

// === MAIN ===
async function main() {
  const inputPath = process.argv[2];
  const outputPath = process.argv[3];

  if (!inputPath || !outputPath) {
    console.error('Uso: node generate_parecer.js <input.json> <output.docx>');
    process.exit(1);
  }

  const data = JSON.parse(fs.readFileSync(inputPath, 'utf-8'));
  const doc = generateParecer(data);
  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(outputPath, buffer);
  console.log(`Parecer gerado com sucesso: ${outputPath}`);
}

main().catch(err => {
  console.error('Erro ao gerar parecer:', err);
  process.exit(1);
});
