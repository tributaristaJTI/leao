---
name: "coleta-inteligente"
description: "Coleta inicial de planejamento tributário: questionário ao cliente e checklist de documentos. Padrão fixado para IR-GCAP na venda de imóvel rural. Use em 'coleta', 'checklist', 'documentos'."
---

# Coleta Inteligente — Questionário Preliminar e Lista de Documentos

Skill transversal que funciona como primeira etapa de qualquer planejamento tributário. Gera questionário sob medida para o cliente e, a partir das respostas (ou dos dados já disponíveis), monta o checklist de documentos necessários. Acione em 'coleta', 'questionário', 'checklist', 'documentos necessários', 'lista de documentos', 'preparar o caso', 'iniciar caso novo', 'levantar informações', 'preciso dos documentos para', 'o que pedir pro cliente', 'montar o checklist', ou ao iniciar caso novo sem dados. Funciona de forma independente de qualquer módulo analítico.

## Princípio

O cliente é produtor rural, não é jurista nem contador. As perguntas devem ser simples, em linguagem do agro, sem sigla técnica sem glosa na primeira aparição. O objetivo é extrair as informações certas sem intimidar. A ausência de um documento também é informação: nunca trave a coleta por falta de dado, sinalize a lacuna.

## Dependências

- Formatação do .docx: skill `layout-aem` (modo Cliente para o roteiro; modo Interno para a nota de status). Nunca definir cores, fontes ou margens localmente.
- Módulo analítico de destino (mod-ir-venda-imovel, mod-comparativo-pf-pj, mod-funrural, mod-ibs-cbs-diferimento, mod-grupo-economico): o checklist deve entregar exatamente as variáveis que o módulo consome.
- Acervo AeM (Drive): antes de gerar, consultar a nota `IR-rural/roteiro-coleta-gcap-venda-imovel-rural-vendedor.md` e as notas correlatas de VTN e benfeitorias, quando o Drive estiver conectado.

## Fluxo de trabalho

### Etapa 1 — Identificar o tipo de caso

Identifique qual módulo analítico será acionado. Se não estiver claro, pergunte: "Esse caso envolve qual tipo de operação?" e apresente as opções dos cinco módulos. Se houver pasta do cliente conectada, liste-a antes de perguntar: muitas respostas já estão nos documentos.

### Etapa 2 — Gerar o questionário preliminar

Perguntas agrupadas em blocos. Cada pergunta: linguagem acessível; explicação curta entre parênteses do porquê, quando não for óbvio; marcação Obrigatória (sem ela a análise trava) ou Complementar (melhora a análise).

#### PADRÃO FIXADO — IR na Venda de Imóvel Rural (decisão de 04/09/2026)

Este é o questionário padrão para esse tipo de trabalho. Use-o integralmente; adapte nomes e acrescente perguntas do caso, sem remover blocos. Versão canônica com formatação: project PORTEIRA FECHADA, `coleta/roteiro-coleta-ir-gcap-venda-imovel-rural.md`.

**Bloco 1. Quem vende**
- 1.1 Nome completo, CPF e telefone de cada proprietário. (Obrigatória)
- 1.2 Estado civil e regime de casamento de cada proprietário (comunhão universal, parcial ou separação); casamento anterior a 1977 ou pacto antenupcial, avisar. Define de quem é o ganho e como se divide. (Obrigatória)
- 1.3 Todos moram no Brasil? Alguém no exterior ou que saiu do país? Regra e responsável pelo pagamento diferentes. (Obrigatória)
- 1.4 Imóvel em nome de pessoa física ou de empresa? Se empresa: nome, CNPJ e regime (Simples, presumido, real). (Obrigatória)
- 1.5 Fração de cada proprietário. (Obrigatória)

**Bloco 2. O imóvel**
- 2.1 Nome da fazenda, município e estado. (Obrigatória)
- 2.2 Matrícula e cartório. A área veio de mais de uma matrícula ou de compras em datas diferentes? Cada pedaço pode ter data e custo próprios. (Obrigatória)
- 2.3 Área total e área vendida (todo ou parte). (Obrigatória)
- 2.4 CIB (antigo NIRF) e código do imóvel no INCRA. (Complementar)
- 2.5 Parte da área só em posse, sem registro, ou promessa de venda de parte a terceiros? (Obrigatória)

**Bloco 3. Como e quando a fazenda chegou às suas mãos**
- 3.1 Forma de aquisição de cada fração: compra, herança, doação, partilha em divórcio, permuta, usucapião. (Obrigatória)
- 3.2 Mês e ano de cada aquisição; se herança, data do falecimento e da partilha. A data define regime de cálculo e descontos por tempo. (Obrigatória)
- 3.3 Valor na escritura, no formal de partilha ou na doação. (Obrigatória)
- 3.4 O imóvel está na declaração de IR (Bens e Direitos)? Por qual valor? (Obrigatória)
- 3.5 Se herança ou doação: transferência pelo valor da declaração ou a valor de mercado? Houve IR naquela transferência? (Obrigatória)

**Bloco 4. Quem explora a fazenda**
- 4.1 Quem usa a terra: dono, arrendatário ou parceiro? Desde quando? Muda todo o tratamento das benfeitorias. (Obrigatória)
- 4.2 Os proprietários declaram atividade rural (livro caixa/LCDPR) ou recebem só arrendamento? (Obrigatória)
- 4.3 Se declaram atividade rural: prejuízo acumulado? Prejuízo fiscal, não financeiro. (Complementar)
- 4.4 O que é produzido e qual a área utilizada. (Complementar)

**Bloco 5. Benfeitorias**
- 5.1 Quais existem: casas, galpões, currais, cercas, pivôs, silos, energia, estradas, curvas de nível, correção de solo, pastagem formada, florestas plantadas. (Obrigatória)
- 5.2 Quem fez cada uma e em que ano: dono atual, dono anterior ou arrendatário. (Obrigatória)
- 5.3 Há notas fiscais, recibos ou contratos? Sem documento o valor não entra no custo. (Obrigatória)
- 5.4 Foram lançadas como despesa/investimento na atividade rural de algum proprietário? Em que anos? Se sim, o valor na venda é receita rural, não ganho de capital. (Obrigatória)
- 5.5 Valor de mercado das benfeitorias separado da terra nua; existe laudo? (Complementar)

**Bloco 6. ITR e VTN**
- 6.1 A DITR foi entregue todos os anos desde a aquisição, em especial no ano da aquisição e no ano da venda? A lei usa o VTN dessas duas declarações como custo e valor de venda. (Obrigatória)
- 6.2 VTN declarado nos últimos 5 anos e valores declarados de benfeitorias e culturas/pastagens. (Obrigatória)
- 6.3 A DITR do ano da venda já foi entregue? Quem entrega? Se não foi, não entregar antes de alinhar. (Obrigatória)
- 6.4 A Receita já questionou o VTN, cobrou ITR ou notificou algo sobre o imóvel? (Obrigatória)
- 6.5 Existe laudo técnico de avaliação da terra nua? (Complementar)

**Bloco 7. A venda**
- 7.1 Valor total e o que está incluído: só terra? Benfeitorias? Máquinas, gado, estoque, safra em pé? Cada item tem tributação própria. (Obrigatória)
- 7.2 Divisão do preço no contrato entre terra nua, benfeitorias e outros itens; quem propôs e com base em quê. (Obrigatória)
- 7.3 Quem é o comprador (PF ou PJ; produtor rural?) e onde mora. (Complementar)
- 7.4 Data do compromisso/contrato e data prevista da escritura. A data do contrato define o ano da venda. (Obrigatória)
- 7.5 Forma de pagamento: à vista, parcelas (datas e valores), permuta, sacas, gado, assunção de dívida. Imposto parcela a parcela; permuta e pagamento em produto têm regra própria. (Obrigatória)
- 7.6 Alguma parcela já recebida? O DARF sobre ela foi recolhido? Com que base? (Obrigatória)
- 7.7 Corretagem: quem pagou e quanto. (Complementar)
- 7.8 Dívidas com garantia sobre a fazenda (hipoteca, alienação fiduciária, CPR, penhor de safra) a quitar com a venda. (Complementar)

**Bloco 8. Histórico e situação fiscal**
- 8.1 Algum proprietário vendeu outro imóvel nos últimos 5 anos? Pagou o imposto? (Obrigatória)
- 8.2 É o único imóvel de cada proprietário? Isenção do único imóvel até R$ 440 mil. (Obrigatória)
- 8.3 Já houve venda ou promessa de venda de parte desta área? Foi pago imposto? (Obrigatória)
- 8.4 Declarações de IR dos últimos 5 anos entregues e sem pendência? Fiscalização em andamento? (Obrigatória)

**Bloco 9. Objetivos**
- 9.1 Destino do dinheiro: outra fazenda, aplicação, empresa, filhos. Abre ou fecha caminhos (permuta, reorganização patrimonial). (Complementar)
- 9.2 Existe holding, empresa rural ou inventário em andamento? (Complementar)
- 9.3 Prazo ou urgência (escritura, condições do comprador). (Obrigatória)

#### Para Comparativo PF × PJ

Bloco 1 — Situação atual: atividade rural como PF ou já tem empresa; se PF, livro caixa (LCDPR) ou resultado presumido; faturamento bruto anual estimado (reais ou sacas).
Bloco 2 — Atividade e patrimônio: culturas/atividades; área total explorada (própria + arrendada/parceria); patrimônio imobiliário rural (quantas propriedades).
Bloco 3 — Estrutura familiar e societária: regime de casamento; filhos maiores na atividade; empresas constituídas (holding, trading, cooperativa); sociedades fora do agro.
Bloco 4 — Projeção: expandir, manter ou reduzir em 5 anos; plano de sucessão em andamento; interesse em crédito rural por PJ.

#### Para Simulação Funrural

Bloco 1 — Atividade: tipo de produção (lavoura, pecuária, ambos); faturamento bruto anual; empregados rurais registrados; folha mensal estimada.
Bloco 2 — Comercialização: vende para quem (cooperativa, trading, indústria, PF); exportação direta; como recolhe o Funrural hoje (receita ou folha).

#### Para IBS/CBS e Diferimento

Bloco 1 — Operação: atividade principal (lavoura, pecuária, agroindústria); faturamento bruto anual; compras anuais de insumos (sementes, fertilizantes, defensivos, combustível); percentual exportação vs mercado interno.
Bloco 2 — Regime atual: PF ou PJ; se PJ, regime (real, presumido, Simples); apura PIS/COFINS e em qual regime.

#### Para Grupo Econômico

Bloco 1 — Mapa do grupo: atividades do titular (rural + não rural); empresas com participação (nome, CNPJ, atividade, percentual); participações cruzadas.
Bloco 2 — Estrutura familiar: atividade própria do cônjuge; regime de casamento; filhos maiores com participação; holding familiar (objeto e sócios).
Bloco 3 — Patrimônio rural: imóveis em nome de quem (PF, holding, operacional); parcerias/arrendamentos entre pessoas do grupo; cessão de máquinas e infraestrutura entre as partes.
Bloco 4 — Tributação: regime de cada empresa; atividade rural PF pelo livro caixa; distribuição de lucros entre as empresas.

### Etapa 3 — Gerar o checklist de documentos

Cada item com: nome claro; motivo (uma frase); prioridade (Essencial ou Complementar, com a condição quando houver); onde conseguir (orientação prática).

#### PADRÃO FIXADO — IR na Venda de Imóvel Rural (grupos A a G)

**A. Do imóvel**
- Certidão de inteiro teor da matrícula atualizada (30 dias): proprietários, frações, área, ônus, origem. Essencial. CRI da comarca ou Central dos Registradores.
- Certidões das matrículas de origem ("registro anterior"): quando, como e por quanto cada parte foi adquirida. Essencial se a matrícula atual for unificada ou recente. Mesmo cartório.
- CCIR vigente. Essencial. SNCR/INCRA, gratuito.
- Comprovante do CIB (antigo NIRF). Complementar. Site da RFB ou recibo da DITR.
- CND do ITR do imóvel. Complementar para o cálculo, exigida na escritura. Site da RFB com o CIB.
- Recibo/demonstrativo do CAR e memorial do georreferenciamento. Complementar. SICAR; técnico responsável ou matrícula.

**B. Da aquisição (custo)**
- Escritura de compra (ou contrato registrado) de cada aquisição. Essencial. Cliente ou tabelionato.
- Formal de partilha, escritura de inventário ou de doação. Essencial se herança/doação. Processo de inventário ou tabelionato.
- Certidão de óbito e última DIRPF do falecido (ou declaração final de espólio). Essencial se herança. Registro civil; contador ou e-CAC do espólio.
- Guia do ITCMD paga. Complementar. SEFAZ ou advogado do inventário.
- DIRPF do ano da aquisição (Bens e Direitos). Essencial. e-CAC ou contador.
- DITR do ano da aquisição, completa (DIAT/VTN): custo legal para aquisições a partir de 1997. Essencial. Portal de Serviços da RFB (Minhas Declarações do ITR), programa ITR do ano ou declarante da época.

**C. ITR e VTN**
- DITRs dos últimos 5 anos completas (DIAC e DIAT), com recibo. Essencial.
- DITR do ano da venda (se entregue) ou quem entrega e quando: o VTN deste ano é o valor de venda pela regra legal. Essencial. Não entregar antes de alinhar.
- DARFs do ITR dos últimos 5 anos. Complementar.
- Notificações, intimações ou autos de ITR/VTN. Essencial se existirem. Cliente; caixa postal do e-CAC.
- Laudo de avaliação da terra nua e benfeitorias (engenheiro agrônomo, NBR 14.653-3, com ART). Complementar, recomendado em vendas de valor alto.

**D. Benfeitorias**
- Notas fiscais, recibos e contratos das benfeitorias. Essencial. Cliente/contador.
- Comprovantes de pagamento. Complementar. Extratos.
- Livro caixa/LCDPR dos anos das benfeitorias e dos últimos 5 anos. Essencial se houver atividade rural. e-CAC ou contador.
- Relação das benfeitorias com ano e autor (dono atual, anterior ou arrendatário). Essencial. Elaborada com o cliente.

**E. Imposto de Renda dos vendedores**
- DIRPFs completas dos últimos 5 exercícios com recibo, de todos os proprietários e cônjuges. Essencial.
- DIRPF mais antiga disponível, se aquisição anterior a 1997. Complementar.
- DARF e demonstrativo GCAP de venda anterior de imóvel (5 anos). Essencial se houve venda.
- Demonstrativo GCAP e DARF de parcela já recebida desta venda. Essencial se houve recebimento.

**F. Pessoais e estado civil**
- RG/CNH e CPF de proprietários e cônjuges. Essencial.
- Certidão de casamento atualizada (regime de bens) e pacto antenupcial. Essencial. Registro civil (registrocivil.org.br).
- Comprovante de residência. Complementar.
- Morador no exterior: saída definitiva e procuração do procurador no Brasil. Essencial nesse caso.

**G. Da venda**
- Compromisso/contrato assinado, com aditivos. Essencial.
- Minuta da escritura. Complementar.
- Comprovantes de recebimento das parcelas. Essencial para parcelas recebidas.
- Recibo de corretagem. Complementar.
- Contratos de arrendamento/parceria, distratos e declarações dos arrendatários. Essencial se houver arrendamento.
- Cédulas e contratos com garantia sobre o imóvel (CPR, penhor, hipoteca). Complementar.
- Se o imóvel estiver em empresa: contrato social consolidado, balanço, razão contábil do imóvel (custo e depreciação) e regime tributário. Essencial nesse caso.

#### Documentos recorrentes nos demais tipos (referência, não exaustivo)

Comparativo PF × PJ: DIRPF e LCDPR dos últimos 3 exercícios; faturamento por atividade; relação de bens (imóveis rurais); contratos de arrendamento/parceria; contratos sociais; folha de pagamento; comprovantes de Funrural.
Grupo Econômico: todos os itens acima quando aplicáveis; contratos sociais e alterações de todas as empresas; organograma societário; DIRPF de todos os sócios PF; balanços dos últimos 3 exercícios; contratos entre as empresas/pessoas do grupo; certidão de casamento.

### Etapa 4 — Formatar para envio

**Documento (.docx, layout-aem modo Cliente), estrutura padrão:**
1. Título, subtítulo e ficha (cliente, imóvel, responsável, data) com campos pendentes em itálico cinza.
2. Introdução em três parágrafos curtos (o que é o ganho de capital, por que a lista é detalhada, como usar) e caixa informativa "não espere juntar tudo".
3. Parte 1, Perguntas: um bloco por tabela com colunas Nº | Pergunta | Resposta; a marcação Obrigatória/Complementar vai dentro da célula da pergunta, em cor (vermelho/dourado).
4. Parte 2, Documentos: caixas de alerta (DITR do ano da venda; parcela já recebida vence no último dia útil do mês seguinte) e um grupo por tabela com colunas Documento | Por que precisamos | Prioridade | Onde conseguir | Recebido (☐). Prioridade em negrito colorido com a condição em linha menor.
5. Parte 3, Como enviar: formato (PDF, um arquivo por documento, nome com ano), canal, prazos, o que acontece depois.

**Mensagem (WhatsApp):** sequência de 7 mensagens curtas, uma ideia por mensagem: abertura; origem da fazenda (matrícula, escrituras, formais); IR (DIRPFs 5 anos, todos os vendedores e cônjuges); ITR (DITRs 5 anos e a do ano da venda, com o alerta de não entregar antes de alinhar); benfeitorias (lista, autor, ano, notas); a venda (contrato, pagamento, parcelas recebidas e DARF); como enviar. Modelo genérico e exemplo personalizado no project PORTEIRA FECHADA.

**Nota interna de status (layout-aem modo Interno), obrigatória quando houver pasta do cliente conectada:** (1) pontos com prazo ou impacto imediato em caixas de destaque; (2) ficha do caso com os fatos extraídos da pasta; (3) questionário com situação por bloco (respondido, em parte, aberto) e fonte ou pendência; (4) checklist com status por documento (na pasta, parcial, falta) e observação; (5) notas técnicas por bloco, com a base legal conferida em fonte oficial e a fonte indicada; (6) mensagens de coleta prontas. A nota não é parecer nem cálculo: diz o que a pasta responde, o que falta e por que a lacuna importa.

## Regras

1. Nunca trave a análise por falta de informação: gere questionário e checklist com o que sabe e sinalize as lacunas.
2. Se o usuário fornecer os dados diretamente, pule para o checklist; se houver pasta conectada, cruze antes de perguntar.
3. O checklist é dinâmico: necessidades novas geram checklist complementar.
4. Sempre inclua orientação prática de onde conseguir cada documento.
5. Toda base legal citada na nota interna é conferida em fonte oficial (Planalto, sijut da RFB) antes de escrita; cópia não oficial é sinalizada como tal.
6. Alertas fixos da coleta de IR na venda de imóvel rural: DITR do ano da alienação (o VTN declarado nela é o valor de venda; prazo anual da RFB); parcela recebida (DARF até o último dia útil do mês seguinte); origem de cada fração (o custo legal pós-1997 é o VTN da DIAT do ano de aquisição, não a DIRPF); vendedor arrendador (benfeitorias não deduzidas tendem a ser ganho de capital a valor contratual, o que muda o interesse na divisão terra/benfeitorias).
7. Ao concluir a entrega: acionar ponto-do-leao (defaults) e perguntar "destilar ou descartar?".