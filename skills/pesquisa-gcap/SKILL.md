---
name: "pesquisa-gcap"
description: "Pesquisa dirigida de IR-GCAP em reorganizações patrimoniais rurais (régua do VTN, art. 22, promessa de compra e venda, Lei 15.270, ITBI, comodato). Acione com /gcap seguido do cliente, ou 'pesquisa o ganho de capital do caso X', 'pontos de atenção do GCAP'."
---

# Pesquisa GCAP — ganho de capital em reorganizações patrimoniais rurais

## Missão

Mapear, com fontes primárias verificadas na rodada, o estado da legislação, da jurisprudência (CARF e Câmara Superior, STF, STJ, TRFs, TJs) e das manifestações da Receita Federal sobre o imposto de renda do ganho de capital em saídas de sócio, partilhas de imóveis rurais e reorganizações de grupos familiares do agro, e devolver uma matriz de pontos de atenção para o caso. Esta skill pesquisa e classifica; não opina sem fonte, não redige parecer (parecer-aem, tributarista-consultivo), não grava tese no acervo (destila), não altera dossiê (guardiao-de-caso). O leitor é o advogado do caso.

## Comandos

- **/gcap `<cliente>`** — roda a pesquisa aqui, com o motor de jurisprudência disponível na sessão (Jusratio: pesquisa de documentos e de legislação), sobre o caso aberto no dossiê do cliente.
- **/gcap `<cliente>` `Q1,Q3,Q8`** — recorte: só as questões listadas. Sem recorte, roda as nove.
- **/gcap `<cliente>` desde `AAAA-MM-DD`** — data-base: só interessa o que mudou depois dela (padrão: data do último ledger do caso).
- **/gcap comando `<cliente>`** — não pesquisa; emite o texto do comando pseudonimizado para rodar em outra IA (ChatGPT, Codex, outra sessão), com o contexto do caso preenchido e o bloco de método e formato. Grava o `.md` em `_Entrada/` do Arquivo AeM com nome `AAAA-MM-DD_script_<cliente>_comando-gcap.md` para a arquivo-do-leao arquivar.
- **/gcap livre** — caso sem dossiê: pede o contexto fático no template abaixo e roda.

## Entrada: contexto fático (template)

Sem estes seis campos a pesquisa devolve precedente genérico. Ler do `_estado.md` e do último `_ledger/` do caso (por ID, via guardiao-de-caso) ou pedir ao usuário:

1. Estrutura: sociedades, data de constituição, forma de integralização dos imóveis, custo contábil por hectare, quem era contribuinte do ITR no ano da integralização.
2. Negócio de base: instrumento (compromisso, alteração contratual, escritura), data, registro ou gaveta, valores pagos e a pagar, forma de pagamento (dinheiro, sacas, bens).
3. Posse: quem explora cada área e por qual título (comodato, parceria, arrendamento, nenhum), desde quando.
4. Rota em execução: passos, ano-calendário de cada um, tributos estimados, condições (DITR, VTN uniforme, ordem das escrituras).
5. Alternativas descartadas e por quê.
6. Premissas de trabalho ainda em aberto.

Os números do caso não são objeto de pesquisa; entram só para direcionar.

## Questionário canônico (Q1 a Q9)

Para cada questão a saída traz: norma vigente com redação literal e data; precedentes com número, órgão, data e trecho; divergência entre correntes; o que mudou depois da data-base; o ponto de atenção para a rota do caso.

- **Q1. Régua do VTN** (Lei 9.393/96, art. 19): custo e valor de alienação pelo VTN dos DIATs dos anos de aquisição e de alienação; mesmo ano; DIAT entregue antes da alienação; ausência de DIAT (IN SRF 84/2001, art. 10, § 2º, contra a corrente da legalidade e do SIPT, art. 14); aplicação à PJ (IN RFB 2.058/2021, art. 33, II; SC Cosit 118/2019). Atenção: posse e pagamento antes do DIAT; DITR retificadora; VTN uniforme entre contribuintes distintos.
- **Q2. Entrega de imóveis ao sócio retirante**: devolução de capital (Lei 9.249/95, art. 22 e § 4º) contra dação em pagamento de haveres (CC, art. 1.031, § 2º; RIR/2018, art. 166); custo do bem na PF; IN SRF 11/96, art. 61; substância e o "separa-sem-separar". Atenção: junção do art. 22 com o art. 19 (contábil na entrada, VTN na saída) e a leitura tudo-ou-nada.
- **Q3. Promessa de compra e venda como alienação** (Lei 7.713/88, art. 3º, § 3º; RIR/2018, art. 166): fato gerador por parcela contra fato gerador único; decadência por parcela (CTN, art. 173, I); efeito de distrato, cancelamento ou aditivo sobre compromisso já pago. Atenção: compromisso de gaveta com posse documentada e pagamentos recebidos.
- **Q4. Venda de quotas pela PF**, se o Fisco mantiver essa qualificação: custo de quotas recebidas por doação ou herança (Lei 9.249/95, art. 23); alienação paga em bens e sacas; alíquotas progressivas vigentes; reduções de imóvel rural (Lei 7.713/88, art. 18; Lei 11.196/2005, art. 40) e sua não aplicação a quotas.
- **Q5. Lei 15.270/2025**: retenção de 10% sobre lucros e dividendos, imposto mínimo da PF (Lei 9.250/95, arts. 6º-A, 16-A e 16-B, redação vigente), redutor, regulamentação e soluções de consulta. Atenção: distribuição de lucros das PJs às sócias para pagar o preço; resultado rural na base do mínimo.
- **Q6. ITBI**: fato gerador no registro; base de cálculo (valor de referência contra valor da transação; verificar tema repetitivo do STJ); incidência na entrega a sócio que não conferiu o bem (CTN, art. 36, parágrafo único; CF, art. 156, § 2º, I); STF Temas 796 e 1348; TJGO.
- **Q7. Parceria contra arrendamento**: requalificação por quota fixa sem partilha de risco; quota do proprietário que entra só com a terra nua (Estatuto da Terra, art. 96, VI, "a", confirmar redação); previdência pela folha (Lei 8.212/91, art. 25, § 13).
- **Q8. Comodato gratuito da PJ ao sócio**: distribuição disfarçada de lucros (RIR/2018, arts. 528, VI, 529, I, e 531, V); precedentes de comodato PJ-sócio; posse do comodatário como "aquisição" para o art. 19 ou como possuidor para o ITR (Lei 9.393/96, art. 4º). Atenção: comodato datado antes da dação como prova de posse antecipada; distrato e cessão onerosa transitória.
- **Q9. ITR e VTN do ano da operação**: VTN uniforme entre contribuintes; município sem convênio com a RFB; arbitramento pelo SIPT; DITR retificadora depois da escritura.

## Banco de precedentes de partida

O dossiê de cada caso pode trazer precedentes já conferidos em rodadas anteriores (no Grupo Ferguson, o ledger de 02 e 03/09/2026 lista os do art. 19, da promessa de compra e venda, da devolução de capital e da parceria). Eles entram na rodada como "conferir na fonte", nunca como verdade dada, e são reverificados antes de citados. Precedente que a rodada não localizar sai da matriz com a marca "não localizado nesta rodada".

## Disciplina

1. Fonte primária somente: Planalto (texto compilado), CARF (acórdão pelo número), STF e STJ (inteiro teor), TRFs e TJs, Receita Federal (SC e IN no site oficial). Trecho de busca não é fonte.
2. Nada de memória: precedente, artigo, alíquota ou prazo só entram com a fonte lida na rodada. O que não foi localizado é declarado, nunca reconstruído.
3. Autoridade classificada em cada fonte: vinculante, qualificada (repetitivo, repercussão geral, súmula) ou orientativa; no CARF, distinguir turma ordinária de Câmara Superior e registrar voto de qualidade quando houver.
4. Divergência explícita: correntes nomeadas com o órgão que adota cada uma; nunca achatar em "o CARF entende".
5. Identificador na busca: ao conferir um precedente, o número vai literal na consulta.
6. Uma rodada ampla por questão, com limite alto, em vez de várias buscas fragmentadas; segunda busca só dirigida por tipo (súmula, repetitivo) ou por identificador.
7. Números do caso não se pesquisam e não se recalculam aqui.
8. Ao emitir comando para IA externa: pseudonimizar (cliente, pessoas, matrículas, CPFs e CNPJs fora; hectares, valores e datas dentro).
9. Português do Brasil, prosa técnica, sem opinião sem fonte, sem resumo final.

## Saída

1. Matriz de pontos de atenção: questão | risco em uma frase | probabilidade (alta, média, baixa) e o motivo | fonte que sustenta | mitigação documental possível.
2. Precedentes verificados por questão, com órgão, data, trecho e link do inteiro teor.
3. Novidades posteriores à data-base.
4. Perguntas abertas, cada uma com a próxima fonte a consultar.
5. Leitura declarada: o que foi aberto e o que ficou de fora.

## Handoffs

- guardiao-de-caso: a matriz e as novidades são entrada para o ledger do caso; esta skill não grava no dossiê, entrega o bloco pronto para o `/dossie fecha`.
- destila: tese que se consolidar em nota canônica sai pelo `/destila`, com o PDF-fonte do precedente ao lado da nota.
- crivo-do-leao: antes de qualquer uso da matriz em peça ou reunião com cliente.
- ponto-do-leao: registro automático ao fim da rodada, eixo tático, finalidade jurídico, cliente = nome curto da taxonomia.

## Guard-rails

Não redige parecer, proposta ou peça. Não grava no Acervo nem no dossiê. Não move nem cria documento fora da `_Entrada/`. Não cita o que não leu na rodada. Não decide a rota do caso: entrega o que a rota precisa saber.