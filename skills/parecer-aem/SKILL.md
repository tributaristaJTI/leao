---
name: parecer-aem
description: "Skill para emissão de pareceres jurídicos e briefings da Amaral e Melo Advogados. Use SEMPRE que o usuário mencionar 'parecer', 'opinião legal', 'briefing jurídico', 'consulta tributária', 'análise jurídica', 'nota técnica', ou pedir para analisar a legalidade/constitucionalidade de alguma questão tributária ou do agronegócio. Também acione quando o usuário pedir para 'emitir parecer sobre', 'analisar juridicamente', 'fundamentar posição sobre', ou qualquer variação de pedido de produção de peça consultiva. Mesmo que o pedido seja informal (ex: 'me ajuda a montar aquele parecer sobre ICMS'), esta skill deve ser acionada. Não use para petições, contratos, artigos de opinião ou apresentações — apenas para peças consultivas (pareceres e briefings)."
---

# Parecer Jurídico — Amaral e Melo Advogados

Skill para produção de pareceres tributários e briefings jurídicos com estrutura padronizada, tom calibrado e output em .docx com identidade visual do escritório.

## Quando usar

Esta skill cobre toda peça de natureza consultiva: pareceres completos, briefings executivos, notas técnicas e opiniões legais. O output padrão é um arquivo `.docx` formatado com a identidade Visual Law da Amaral e Melo.

## Fluxo de trabalho

Ao receber um pedido de parecer ou briefing, siga estes passos na ordem:

### 1. Coletar informações essenciais

Antes de redigir, confirme com o usuário (se não estiver claro no pedido):

- **Tema central**: qual a questão jurídica? (ex: "incidência de FUNDEINFRA sobre exportações de soja")
- **Caso concreto**: há um cliente ou situação específica? Se sim, quais os fatos relevantes?
- **Tipo de peça**: parecer completo (4 seções) ou briefing executivo (versão resumida)?
- **Arquivos de referência**: o usuário quer que você leia algum documento local (contrato, planilha, parecer anterior)?

Se o pedido já contém essas informações, pule direto para a redação. Não faça perguntas desnecessárias.

### 2. Ler arquivos de referência (se houver)

Se o usuário apontar para arquivos locais:

- Leia contratos, planilhas LCDPR, ou outros documentos mencionados
- Se houver pareceres anteriores na pasta de referência, use-os como modelo de tom e profundidade
- Extraia dados relevantes para incorporar na fundamentação

### 3. Redigir seguindo a estrutura fixa

Leia o arquivo `references/estrutura_parecer.md` para a estrutura detalhada. Em resumo, todo parecer segue quatro seções obrigatórias:

1. **EMENTA** — Resumo da conclusão em 2-3 linhas
2. **DA CONSULTA** — Descrição do problema e dos fatos
3. **DA FUNDAMENTAÇÃO** — Análise com legislação, jurisprudência e doutrina
4. **DA CONCLUSÃO** — Resposta objetiva à consulta

Para briefings executivos, a estrutura é comprimida: ementa + análise resumida + recomendação, em no máximo 2 páginas.

### 4. Aplicar o tom, estilo e princípios de calibragem

Leia `references/estilo_leonardo.md` para as diretrizes completas. Este arquivo contém quatro princípios de calibragem que devem ser aplicados a todo parecer:

- **Advocacia orientada à decisão:** a conclusão e a recomendação prática já aparecem na ementa. O leitor sabe a resposta antes de ler a fundamentação.
- **Engenharia de clareza:** aplicar o teste de fricção (sem releitura forçada, sem ambiguidade, sem sobrecarga conceitual). Máximo de 2 referências legislativas por parágrafo.
- **Persuasão por contraste:** na conclusão, sempre incluir o cenário de inação — o que acontece se o cliente não seguir a recomendação, quantificado em reais quando possível.
- **Compressão:** eliminar prolixidade, vocabulário proibido (destarte, outrossim, mister, etc.), parágrafos de no máximo 8 linhas.

Além disso: tom técnico mas acessível, referências legislativas precisas, posicionamento claro quando houver divergência doutrinária, e tradução para linguagem do agro na ementa/conclusão/briefings.

Antes de gerar o .docx, aplicar o checklist final que está no fim do arquivo `estilo_leonardo.md`.

### 5. Gerar o .docx formatado

Use a skill `docx` (docx-js via Node.js) para gerar o arquivo Word. Siga estas especificações de Visual Law:

**Identidade visual Amaral e Melo:**
- Fonte principal: Georgia (corpo do texto, 12pt)
- Fonte secundária: Arial (cabeçalhos e rodapé, conforme indicado)
- Cor primária (títulos de seção): Azul Marinho `#1D3D69`
- Cor de destaque (linhas decorativas, destaques): Dourado `#B88657`
- Margens: 3cm esquerda, 2cm direita, 2,5cm superior e inferior
- Espaçamento entre linhas: 1.5
- Alinhamento do corpo: justificado
- Numeração de páginas: rodapé, centralizada

**Estrutura do documento:**
- Cabeçalho: nome do escritório em Arial 10pt, Azul Marinho, com linha dourada abaixo
- Título "PARECER JURÍDICO" centralizado, Georgia 16pt Bold, Azul Marinho
- Subtítulo com o tema, Georgia 12pt Italic, Azul Marinho
- Seções numeradas com título em Georgia 13pt Bold, Azul Marinho
- Corpo em Georgia 12pt, cor preta
- Notas de rodapé para referências legislativas quando extensas
- Rodapé: "Amaral e Melo Advogados — Direito Tributário & Agronegócio" + número da página

### 6. Validar e entregar

Após gerar o .docx:
- Valide com `python /mnt/skills/public/docx/scripts/office/validate.py <arquivo.docx>` (script da skill pública `docx`; caminho corrigido em 2026-08-29)
- Se a validação falhar, corrija e re-gere
- Apresente o arquivo ao usuário com um resumo de 2-3 linhas do que foi produzido

## Exemplo de interação

**Usuário:** "Emita um parecer sobre a incidência de PIS/COFINS na venda de soja por pessoa física."

**Skill executa:**
1. Tema claro, caso genérico → pula coleta de informações
2. Sem arquivos de referência mencionados → pula leitura
3. Redige nas 4 seções, com fundamentação em CF/88 art. 195, Lei 10.833/2003, jurisprudência do STJ
4. Aplica tom acessível ao produtor
5. Gera .docx com formatação Visual Law
6. Valida e entrega

**Usuário:** "Preciso de um briefing rápido sobre FUNDEINFRA. Olha o contrato que tá na pasta Downloads."

**Skill executa:**
1. Tipo: briefing (versão compacta)
2. Lê o contrato na pasta Downloads
3. Redige briefing de 2 páginas
4. Gera .docx compacto
5. Entrega

## Dependências

Esta skill depende da skill `docx` para geração de arquivos Word. Garanta que `npm install -g docx` está disponível no ambiente.
