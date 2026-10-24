---
name: "agint-aresp"
description: "Agravo interno (art. 1.021 do CPC) contra decisão monocrática de relator do STJ em AREsp/REsp: parecer de viabilidade GO/NO-GO, redação, teste adversarial e contraminuta. Acione com /agint."
---

# AgInt do Leão — Agravo Interno contra Monocrática no STJ

O agravo interno é a peça mais julgada do STJ e a de menor taxa de reversão. O valor desta skill está em (1) saber quando NÃO agravar, (2) atacar cirurgicamente o fundamento exato da monocrática e (3) jamais repetir as razões do recurso anterior — o erro que os gabinetes mais punem.

A peça tem dois leitores com poderes diferentes: o relator, que pode se retratar antes de levar ao colegiado (art. 1.021, § 2º, do CPC) — dê-lhe uma porta de saída honrosa; e o colegiado, que julga se não houver retratação — demonstre-lhe o erro específico. Escrever para humilhar o relator sabota o primeiro leitor; escrever genericamente perde o segundo.

Nomenclatura: cível o STJ autua como **AgInt**; penal, como **AgRg**. A mecânica vale para ambos; os prazos diferem (Etapa 1).

## Quando acionar

Comando `/agint`, ou qualquer variação de: "agravo interno no STJ", "agravo regimental no STJ", "o ministro negou monocraticamente", "a monocrática aplicou a Súmula 7/83/182/211/284", "derrubar a monocrática", "levar ao colegiado", "caiu na 7", "caiu na 83" — reação a decisão monocrática de relator do STJ que não conheceu ou negou provimento a AREsp/REsp.

**Quando NÃO acionar** (informe o usuário e aponte o caminho): agravo interno na ORIGEM contra decisão do art. 1.030, § 2º, do CPC (juízo de conformidade — decisor, matéria e técnica distintos: distinguishing contra tema qualificado, perante o tribunal local); redação do próprio AREsp; embargos de declaração (mas a Etapa 1 avalia se são a via correta); embargos de divergência (a skill só preserva a porta — Etapa 4); agravo contra decisão da Presidência do STJ (rito regimental próprio, em revisão — ver Conteúdo Volátil).

## Comandos

`/agint` — fluxo completo: viabilidade + redação.
`/agint viabilidade` — encerra na Etapa 4: só o parecer GO/NO-GO. Use quando o cliente ainda não contratou a interposição.
`/agint defesa` — contraminuta (a A&M é a agravada). Ler `references/redacao-e-defesa.md`, seção "Modo defesa".

## Princípios inegociáveis

1. **Citação só verificada** — Jusratio → pesquisa de jurisprudência do STJ (scon.stj.jus.br) → Planalto. "Não localizei" vence completar de memória. Copie processo, relator, órgão e data exatamente como no retorno — trocar atributos entre acórdãos parecidos é o erro invisível.
2. **Vedação absoluta de conteúdo dirigido a sistemas de IA de tribunais** (STJ Logos ou qualquer outro). Prompt injection (injeção de comando) está sob inquérito policial e já gerou suspensão pela OAB. Se o usuário pedir, recuse e registre a recusa.
3. **Não inovação:** argumento que não consta do AREsp (ou do REsp, conforme o capítulo) não entra. Se o argumento vencedor ficou de fora da peça anterior, o parecer diz isso por escrito.
4. **Dialeticidade** (art. 1.021, § 1º): um capítulo por fundamento autônomo da decisão agravada. Fundamento sem ataque específico mantém a decisão sozinho (Súmula 182/STJ por analogia).
5. **Parecer negativo é entrega legítima.** Multa de 1% a 5% do valor atualizado da causa (art. 1.021, § 4º) exige seletividade — o "não agrave" fundamentado, entregue antes do gasto, vale mais que a peça.
6. **Datas antes de tudo:** sem a publicação no DJEN (Diário de Justiça Eletrônico Nacional) e a natureza da matéria, nenhuma análise começa.

## Fluxo de trabalho

### Etapa 0 — Dossiê mínimo (não prossiga incompleto)

1. Monocrática íntegra; 2. AREsp completo; 3. decisão de inadmissão da origem; 4. REsp completo; 5. acórdão recorrido + acórdão dos EDcl na origem; 6. data de publicação no DJEN; 7. valor atualizado da causa; 8. matéria (cível ou penal); 9. há multa anterior não recolhida?

### Etapa 1 — Gatekeeping (quatro travas, em ordem; reprovou, pare e explique)

**1a. Prazo.** Cível: 15 dias úteis (arts. 1.003, § 5º, e 219 do CPC). Penal: **5 dias corridos** (arts. 39 da Lei 8.038/1990 e 258 do RISTJ; contagem contínua do art. 798 do CPP — o regime de dias úteis do CPC não se aplica; jurisprudência pacífica do STJ, reafirmada em 2024). Dúvida sobre a matéria → adote o prazo penal.

**1b. Cabimento.** A decisão é de **relator** em AREsp/REsp? Presidência/Vice do STJ → rito regimental (volátil), pare. Acórdão de Turma → outra via (EDcl, RE, EREsp).

**1c. EDcl antes?** Vício de *integridade* (omissão, contradição, obscuridade, erro material — art. 1.022 do CPC) → EDcl, que interrompem o prazo. Erro de *conteúdo* → AgInt. Na dúvida, AgInt — embargos rejeitados como protelatórios geram multa própria e desgastam o caso no mesmo gabinete.

**1d. Multa pendente** (arts. 1.021, § 4º, ou 1.026): o § 5º do art. 1.021 condiciona qualquer outro recurso ao depósito prévio — exceto Fazenda Pública e gratuidade (pagam ao final). Sem depósito, o agravo nasce morto.

### Etapa 2 — Autópsia da decisão agravada

Classifique a monocrática:

- **Tipo A — não conheceu do AREsp** (vício do próprio agravo: Súmula 182, deserção, intempestividade, procuração). O AgInt discute a regularidade do AREsp, não o REsp.
- **Tipo B — negou provimento ao AREsp**, mantendo a inadmissão do REsp (o cenário mais frequente). O AgInt ataca a aplicação do óbice.
- **Tipo C — conheceu para julgar desde logo o REsp** (poderes do art. 932, IV e V, do CPC, na redação da Lei 15.484/2026, que incluiu os acórdãos do regime de relevância entre os paradigmas). O AgInt vira peça de **distinguishing**.

Extraia: cada **fundamento autônomo**; o **óbice nominado** em cada um; cada **precedente citado** (com o trecho transcrito); o **dispositivo lido literalmente** — "não conheço" ≠ "nego provimento" ≠ "conheço para negar provimento ao recurso especial" (a espécie define o que o colegiado poderá fazer e quais portas se abrem depois). Fundamentação encadeada ("ainda que superado X, incidiria Y"): cada elo é fundamento autônomo e exige ataque próprio.

### Etapa 3 — Matriz de superabilidade

Leia `references/tipologia-obices.md` e aplique, a cada fundamento, o teste e a técnica correspondentes. Registre em três colunas: fundamento / superável? (sim, não, parcial) / técnica + material probatório (trechos do acórdão, páginas do AREsp).

Em paralelo, a **verificação de não inovação**: para cada argumento de ataque, a página da peça anterior onde ele já constava. Sem lastro, o argumento sai da matriz.

Pesquise no Jusratio cada precedente citado pelo relator e confirme que a ratio corresponde ao uso feito. Relator também erra na citação — precedente fora de contexto é ataque de primeira linha e a melhor porta de retratação.

### Etapa 4 — Parecer GO/NO-GO (no chat, não em arquivo)

```
## Parecer de Viabilidade — AgInt
**Processo:** [n.] | **Relator:** [nome] | **Tipo de decisão:** [A/B/C]
**Prazo fatal:** [data, com a base de cálculo explícita]

### Fundamentos da decisão agravada
[lista numerada, cada um com o óbice nominado]

### Matriz de superabilidade
[fundamento × veredicto × técnica]

### Exposição econômica
Valor atualizado da causa: R$ [x] | Multa potencial (§§ 4º-5º): R$ [1% a 5% de x]
[A multa exige três requisitos cumulativos: manifesta inadmissibilidade ou
improcedência + votação unânime + decisão fundamentada. Agravo tecnicamente
sério raramente a atrai — mas em causa de alto valor a exposição entra com
número, não com adjetivo.]

### Valor de opção
[O que o acórdão colegiado destrava: RE ao STF (exaurimento — Súmula 281/STF)
e, se o colegiado JULGAR o REsp, embargos de divergência — a Súmula 315/STJ
fecha os EREsp quando o acórdão do agravo não admite o REsp; a 316/STJ os
abre quando o acórdão decide o REsp. Quando o alvo real for os EREsp, o
pedido deve levar o colegiado a conhecer E julgar.]

### Recomendação
[AGRAVAR / NÃO AGRAVAR / AGRAVAR PARCIALMENTE (capítulos x, y)]
```

**NO-GO objetivo** (qualquer um basta): (i) o argumento decisivo é inovação; (ii) a Súmula 182 é verdadeira — o AREsp genuinamente não atacou a inadmissão; (iii) resta fundamento autônomo insuperável; (iv) exposição à multa desproporcional sem valor de opção. NO-GO indica sempre o que ainda é aproveitável (RE pendente, rescisória, tese para outro caso da carteira).

Se o comando foi `/agint viabilidade`, pare aqui.

### Etapa 5 — Redação

Leia `references/redacao-e-defesa.md` (estrutura obrigatória da peça, regras de redação, modelo de capítulo). Alavanca estrutural: o § 3º do art. 1.021 veda ao relator julgar o agravo reproduzindo os fundamentos da decisão agravada — construa capítulos que a monocrática *não enfrentou nos termos postos*; confirmação por carimbo nasce com vício (§ 3º c/c art. 489, § 1º, IV) atacável por EDcl e aproveitável no RE. Pedidos em cascata: retratação → provimento pelo colegiado → quando o alvo for os EREsp, que o colegiado conheça E julgue o REsp. Formatação final: .docx via skill layout-aem.

### Etapa 6 — Teste adversarial

Redija a **decisão hipotética que negaria provimento ao agravo** com os padrões de gabinete listados em `references/redacao-e-defesa.md`. Confronte a minuta frase a frase: acusação que encaixa sem neutralização expressa e antecipada → a minuta volta à Etapa 5. Apresente o resultado ao usuário junto com a peça.

### Etapa 7 — Verificação final e entrega

Todas as citações pelo protocolo do princípio 1, agrupadas numa única sessão de pesquisas. Depois: layout-aem; sugerir /crivo em causas de alto valor; registrar a sessão via ponto-do-leao.

## Conteúdo volátil — verificado em 19/08/2026

Reverifique a cada uso; ao confirmar mudança, atualize esta seção:

1. **RISTJ pós-Emendas Regimentais 51 e 53/2026** — rito de julgamento virtual do agravo interno, pedido de destaque e sustentação oral em rearranjo. A regra geral (AgInt sem sustentação oral) deve ser confirmada no regimento consolidado antes de qualquer afirmação na peça. Parecer da OAB-DF aponta suspeitas de inconstitucionalidade nas duas emendas.
2. **Emenda regimental de execução da Lei 15.484/2026** (art. 6º): não editada na data de verificação. Pode alterar órgão competente, rito da relevância e reflexos sobre o AgInt. Vigência da lei: 30 dias da publicação (DOU de 4/8/2026, edição extra).
3. **Primeiros julgados do filtro de relevância** — em especial: exigibilidade do tópico quando a relevância é presumida (art. 1.035-A, §§ 2º a 4º, do CPC); e a irrecorribilidade do não conhecimento por irrelevância (caput), que reduz o espaço futuro do AgInt nessa hipótese.
4. **Gatilho de revisão:** setembro/2026 (vigência da lei) e cada acórdão da Corte Especial sobre o novo regime.

## Integração com o Ecossistema do Leão

- **braco-direito** aciona esta skill quando a delegação envolver reação a monocrática do STJ.
- **layout-aem:** formatação obrigatória da peça final em .docx timbrado.
- **crivo-do-leao:** revisão independente recomendada em alto valor (o teste adversarial da Etapa 6 não o substitui — verificações de natureza distinta).
- **destila:** agravo provido → destilar a tese vencedora (óbice × técnica × relator) para o acervo.
- **ponto-do-leao:** registrar a sessão ao concluir a entrega.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.