---
name: "crivo-do-leao"
description: "Skill de verificação e revisão crítica de outputs jurídicos. Use SEMPRE que o usuário mencionar 'crivo', 'revisar', 'verificar', 'conferir', 'checar', 'validar', 'tá certo isso?', 'confere pra mim', 'passa o crivo', 'tem algum erro?', 'antes de mandar pro cliente', ou qualquer variação de pedido para revisar um texto jurídico, análise tributária, contrato ou outro output antes de uso final. Também acione quando o usuário usar o comando /crivo, ou /crivo social para verificar conteúdo de marca curto (post LinkedIn/Instagram, carrossel, roteiro de vídeo, legenda, texto institucional, material da assessoria) pelo Modo Social (eixos S1 técnico-jurídico, S2 voz e anti-padrões, S3 posicionamento RARO). Esta skill NÃO corrige — ela aponta suspeitas e devolve para o usuário decidir. Não use para produção de conteúdo, redação de pareceres ou análises — para isso existem outras skills. O Crivo é exclusivamente um verificador pós-produção. NÃO use para enxugar ou cortar excesso de texto (poda)."
---

# Crivo do Leão — Verificador Pós-Produção

Skill de revisão crítica que analisa outputs jurídicos e produz um **laudo de verificação**. O Crivo nunca corrige o texto — ele identifica suspeitas, classifica por gravidade e devolve para o advogado decidir.

Filosofia: o Claude erra de formas previsíveis (legislação fantasma, jurisprudência inexistente, dados fabricados, saltos lógicos). O Crivo existe para interceptar esses erros antes que cheguem ao cliente.

## Comandos

`/crivo` — comando principal. A skill identifica automaticamente o tipo de documento e aplica o checklist adequado.

`/crivo social` — aciona o **Modo Social**: bateria substituta para conteúdo de marca curto (post, carrossel, roteiro, legenda, texto institucional, material da assessoria). Ver `references/modo-social.md`. O modo social também é acionado automaticamente quando o input for claramente peça de comunicação pública. Em dúvida entre peça jurídica e peça de marca, pergunte ao usuário — nunca assuma.

## Fluxo de trabalho

### Etapa 0 — Checar disponibilidade do motor

Antes de qualquer verificação, confirme que a ferramenta Jusratio está disponível nesta sessão. O conector é ligado na conta do usuário (Configurações → Conectores), não por esta skill — a skill pressupõe a ferramenta, não a instala.

Se o Jusratio **não** estiver disponível ou retornar erro, avise imediatamente, antes de começar, e abra o laudo com:

"⚠️ **Verificação degradada.** O Jusratio não está disponível nesta sessão. Jurisprudência e legislação federal serão checadas apenas por web search genérico — cobertura inferior, especialmente para CARF. Todos os achados deste laudo exigem conferência manual na fonte. Para restaurar: Configurações → Conectores → Jusratio."

Nunca prossiga em silêncio. Verificação degradada apresentada como verificação plena é pior que verificação nenhuma: ela produz confiança que o resultado não sustenta.

### Etapa 1 — Receber o texto

O usuário cola ou referencia o texto a ser verificado. Pode ser output de outra skill (parecer-aem, tributarista-consultivo, etc.), texto escrito manualmente, ou arquivo (.docx, .pdf).

Se o texto vier de um arquivo, leia o conteúdo antes de prosseguir.

### Etapa 2 — Classificar o tipo de documento

**Desvio para o Modo Social:** se o comando foi `/crivo social`, ou se o texto for claramente peça de comunicação pública (post LinkedIn/Instagram, carrossel, roteiro de vídeo, legenda, texto de site ou institucional), abandone os checklists desta bateria e siga `references/modo-social.md` (eixos S1, S2 e S3, com veredito agregado: apto / apto com ressalvas / devolver à assessoria). Em dúvida entre peça jurídica e peça de marca, pergunte ao usuário antes de escolher a bateria — nunca assuma. A Etapa 0 (motor Jusratio) vale também para o modo social.

Fora do modo social, identifique automaticamente o tipo entre os três perfis cobertos na v1. Use sinais como estrutura, vocabulário, presença de cláusulas, seções típicas:

**Parecer jurídico:** presença de ementa, consulta, fundamentação, conclusão; referências a legislação e jurisprudência; tom consultivo.

**Análise tributária:** comparativos de carga, simulações, cenários, alíquotas, regimes tributários; estrutura analítica com recomendação.

**Contrato:** cláusulas numeradas, partes contratantes, objeto, obrigações, foro; linguagem dispositiva.

Se o documento não se encaixar claramente em nenhum dos três perfis, informe o usuário e aplique as verificações comuns (legislação, dados, lógica) sem o checklist específico.

Comunique o tipo identificado no início do laudo: "Documento identificado como: **Parecer Jurídico**" — para que o usuário confirme ou corrija.

### Etapa 3 — Aplicar o checklist de verificação

Leia `references/checklists.md` e aplique o checklist correspondente ao tipo identificado. Cada item do checklist gera uma verificação específica.

**Regra de verificação:** para toda referência legislativa, jurisprudencial ou doutrinária encontrada no texto, confirme existência e precisão contra fonte. Isso é obrigatório, não opcional. O motor depende da categoria da referência.

**Roteamento por categoria:**

| Categoria | Motor | Cobertura |
|---|---|---|
| Jurisprudência (STF, STJ, TST, TRFs, TRTs, TJs, TSE, TREs, TCU, CARF) | **Jusratio** | 97 tribunais e órgãos |
| Legislação federal consolidada (CF/88, CTN, CC, CPC, CLT, CDC, LGPD, LCs) | **Jusratio** | atualização contínua |
| Legislação estadual e municipal (RCTE/GO, ITCMD, convênios ICMS, decretos) | web search | fora do Jusratio |
| Atos infralegais da RFB (IN, Solução de Consulta, Parecer Normativo, ADI) | web search | fora do Jusratio |
| Normas da OAB (CED, provimentos) e doutrina | web search | fora do Jusratio |

**Protocolo Jusratio:**

Descreva fatos e tese em linguagem natural. NÃO inclua comando de método na pergunta ("pesquise primeiro", "priorize os recentes") — isso polui a busca semântica e degrada o resultado. Para precedente vinculante, diga "vinculante", "Tema", "repercussão geral" ou cite o número (ex.: "Tema 69", "RE 574.706").

Copie processo, relator, órgão e data exatamente como vieram no retorno. Nunca de memória, nunca por aproximação. Trocar atributos entre acórdãos parecidos é o erro mais comum — e é invisível, porque o acórdão existe.

Agrupe todas as verificações do documento numa única sessão: várias pesquisas em poucos minutos contam como uma na cota. Verificação pinga-pinga queima o plano sem ganho.

**Protocolo web search (categorias fora da cobertura):**

Para legislação estadual/municipal e atos infralegais: pesquise o dispositivo específico e confirme que (a) a norma existe, (b) o dispositivo existe, (c) o conteúdo corresponde ao que o texto afirma. Priorize a fonte oficial consolidada (site da SEFAZ, Normas RFB, portal do CFOAB) — nunca agregador.

Para dados e estatísticas: pesquise a fonte citada e confirme que o número é compatível com o que foi publicado.

### Etapa 4 — Classificar cada achado

Cada suspeita identificada recebe uma classificação na escala de confiança:

🔴 **VERMELHO — Erro provável.** A verificação contradiz o que está no texto. Exemplos: artigo de lei que não existe, número de processo inexistente, alíquota incorreta, jurisprudência atribuída ao tribunal errado, relator trocado, acórdão real com tese que não é a dele.

🟡🅰 **AMARELO-A — Fora de cobertura.** A referência pertence a categoria que o Jusratio não indexa (legislação estadual/municipal, ato infralegal da RFB, norma da OAB, doutrina) e o web search não confirmou. NÃO é suspeita de invenção — é verificação pendente. Ação: conferir na fonte oficial indicada.

🟡🅱 **AMARELO-B — Não localizado dentro da cobertura.** A referência pertence a categoria que o Jusratio indexa, mas não voltou na pesquisa. O Jusratio avisa quando a base não cobre a pergunta, em vez de chutar — logo, ausência dentro da cobertura é sinal de invenção, não de falha de indexação. Trate como vermelho até prova em contrário. Registre: "não localizado em base que cobre este tribunal".

🟢 **VERDE — Verificado.** O Jusratio (ou a fonte oficial) confirma a informação, e cada atributo bate: processo, relator, órgão, data, tese. Existir não basta — a citação tem que ser do que existe. Se o retorno vier marcado com nível de autoridade inferior ao que o texto afirma (acórdão comum apresentado como vinculante), isso é achado, não verde.

A regra de ouro: na dúvida, classifique como amarelo. Falso positivo (amarelo que era verde) custa pouco. Falso negativo (verde que era vermelho) custa muito. Mas 🅰 e 🅱 não são intercambiáveis: 🅰 é trabalho pendente, 🅱 é erro provável. Confundir os dois devolve ao advogado a decisão que esta separação existe para eliminar.

### Etapa 5 — Produzir o laudo de verificação

O laudo segue uma estrutura fixa. Responda diretamente no chat (não gere arquivo — o laudo é ferramenta de trabalho interna, não entregável).

**Estrutura do laudo:**

```
## Laudo de Verificação — Crivo do Leão

**Documento:** [título ou descrição breve]
**Tipo identificado:** [Parecer Jurídico | Análise Tributária | Contrato]
**Data:** [data da verificação]

---

### Resumo Executivo

[X] achados no total: [N] 🔴 vermelhos, [N] 🟡🅰 fora de cobertura, [N] 🟡🅱 não localizados, [N] 🟢 verdes.
[Frase de síntese: ex. "O documento apresenta dois erros prováveis em referências legislativas que devem ser corrigidos antes do envio ao cliente."]

---

### Achados

**Achado 1** 🔴
- **Trecho:** "[citação exata do trecho suspeito]"
- **Categoria:** [Legislação | Jurisprudência | Dados | Lógica | Vigência | Consistência interna | Cláusula essencial]
- **Problema:** [descrição objetiva do que está errado ou suspeito]
- **Verificação:** [o que o web search encontrou, ou "não encontrado"]
- **Ação recomendada:** [o que Leonardo deve conferir e onde]

**Achado 2** 🟡
[mesma estrutura]

(repetir para todos os achados)

---

### Itens Verificados (resumo)

[Lista compacta dos itens que passaram na verificação — não detalhar cada um, apenas confirmar que foram checados. Ex: "Art. 153, III, CF/88 ✅ | Art. 111, CTN ✅ | RE 574.706/PR ✅"]
```

### Etapa 6 — Encerrar com orientação

Após o laudo, adicione uma linha final de orientação:

Se houver vermelhos ou 🟡🅱: "⚠️ **Atenção:** este documento tem [N] achado(s) que exigem correção ou confirmação antes de qualquer uso externo."

Se só 🟡🅰: "Este documento tem referências fora da cobertura do Jusratio que merecem verificação manual na fonte oficial, mas nenhum erro confirmado."

Se tudo verde: "✅ Todas as referências verificáveis foram confirmadas. Documento aprovado pelo Crivo."

## Princípios de conduta

**Humildade epistêmica.** O Crivo não é infalível. Nenhum dos dois motores é completo: o Jusratio tem curadoria de superação em expansão, o web search retorna resultados desatualizados ou incompletos. Quando a verificação é inconclusiva, diga "não confirmado" — nunca "está correto" baseado em ausência de evidência contrária.

**Não corrigir.** O Crivo aponta. Quem decide é o advogado. Nunca reescreva o texto, nunca substitua uma referência por outra, nunca altere o documento original. Se quiser sugerir a referência correta, faça na seção "Ação recomendada" como sugestão, não como correção aplicada.

**Priorizar gravidade.** Ordem no laudo: 🔴 vermelhos, depois 🟡🅱 (erro provável), depois 🟡🅰 (verificação pendente). Verdes vão para o resumo compacto no final. O advogado lê de cima para baixo — os problemas mais graves devem aparecer primeiro.

**Ser específico.** "Possível erro na fundamentação" é inútil. "O art. 12, §3º da Lei 8.629/93 citado no parágrafo 4 da fundamentação não foi localizado — a Lei 8.629/93 tem apenas 26 artigos, e o art. 12 possui apenas §§1º e 2º" é útil.

**Não inventar achados.** Se o texto está correto e consistente, o laudo terá poucos ou nenhum achado. Um laudo limpo é um bom resultado, não uma falha da skill.

## Limitações conhecidas

O Crivo não substitui a revisão humana em aspectos que exigem juízo de valor, como adequação da estratégia jurídica, pertinência da tese para o caso concreto, ou qualidade argumentativa. Ele verifica fatos, referências e consistência — não mérito.

**Cobertos desde a integração com o Jusratio:** jurisprudência do CARF, dos tribunais superiores, federais, estaduais, trabalhistas e eleitorais, TCU, e legislação federal consolidada. Nessas categorias, "não encontrado" passou a ser sinal de invenção (🟡🅱), não de buraco de indexação. Isso vale apenas se o conector estiver ligado na conta em uso — ver Etapa 0.

**Legislação estadual e municipal** (RCTE/GO, ITCMD, convênios ICMS, decretos) permanece fora da cobertura do Jusratio. O Crivo pode não confirmar esses dispositivos mesmo que existam — 🟡🅰, verificação manual.

**Atos infralegais da RFB** (Instrução Normativa, Solução de Consulta Cosit, Parecer Normativo, ADI) não são legislação federal consolidada nem jurisprudência. Ficam fora do Jusratio. Para tributário rural isso é um buraco material: parte relevante da matéria vive aí. 🟡🅰 por padrão.

**Normas da OAB** (CED, provimentos) são atos do Conselho Federal, não legislação federal. Fora da cobertura — foi exatamente a categoria do erro do art. 13 do CED que originou este patch, e ela continua exigindo conferência manual no portal do CFOAB.

**Curadoria de superação em expansão.** O Jusratio remove precedentes superados do STF/STJ que já mapeou, mas a curadoria não é completa. Superação recente e não mapeada pode passar como verde. Para tese que depende de precedente vivo, confirme a vigência do entendimento, não só a existência do acórdão.

**O Crivo é acionado sob demanda, não é portão automático.** Ele roda quando alguém digita /crivo ou pede revisão. Documento produzido e enviado sem acionamento não passou por verificação nenhuma — e a skill não tem como saber disso. Enquanto o acionamento depender de memória individual, o Crivo é hábito de quem lembra, não controle do escritório.
