---
name: proposta-aem
description: "Sistema comercial da Amaral e Melo Advogados: contextualiza o caso, dimensiona a dor e o valor em jogo, precifica e redige propostas de honorários persuasivas — em conformidade com o Provimento 205/2021 da OAB — em documento .docx timbrado. Use SEMPRE que o usuário digitar /proposta, ou pedir para 'montar/gerar/redigir uma proposta', 'proposta comercial', 'proposta de honorários', 'precificar um caso', 'preço para o cliente', 'quanto cobrar', 'proposta para a reunião de fechamento', ou qualquer variação de elaboração de proposta de serviços jurídicos. NÃO use para o briefing que prepara a reunião comercial (isso é o /comercial do briefing-juridico) nem para refazer a análise jurídica (isso vem das skills tributarista-consultivo, tributarista-contencioso e dívida-rural). A proposta-aem é a camada COMERCIAL: precifica e persuade sobre uma análise que já existe — não reabre a tese."
---

# Proposta AeM — Sistema Comercial

Transforma um caso já analisado em proposta de honorários pronta para o cliente. A análise jurídica (tese, riscos, estratégia) **não nasce aqui** — é consumida das skills analíticas como fonte primária. Esta skill faz três coisas que aquelas não fazem: **dimensiona o valor comercial** do caso, **precifica** com faixa e cenários, e **redige** a proposta com persuasão e dentro dos limites éticos. O produto é sempre um `.docx` timbrado.

## Dependências

- **Formatação:** leia `layout-aem` em `/mnt/skills/user/layout-aem/SKILL.md` antes de gerar o `.docx`. Use o **Modo Cliente** (o destinatário é o produtor rural). Não defina cores, fontes ou margens localmente.
- **Geração de Word:** leia também `/mnt/skills/public/docx/SKILL.md`.
- **Intake comercial:** quando houver, consuma o Briefing Comercial produzido pelo `/comercial` do `briefing-juridico` como insumo do 1º atendimento.
- **Análise jurídica (fonte primária):** `tributarista-consultivo`, `tributarista-contencioso`, `dívida-rural`, módulos do planejador. A estratégia e a complexidade vêm de lá.
- **Precificação:** `scripts/proposta.py` desta skill.
- **Conhecimento do escritório:** `references/matriz_precificacao.md` (trilhas, faixas, cadeia de crédito) e `references/persuasao_proposta.md` (espinha de persuasão, estrutura do documento e restrições do Provimento 205). **Leia os dois antes de precificar ou redigir.** Enquanto a matriz estiver com campos `null`, o script para com "MATRIZ NÃO PREENCHIDA" e a proposta não é precificada (reconstrução de 2026-08-29, A-13).

## Quem opera

Leonardo e Juliane (advogada assistente); perfis de executor no `perfis.md` da `mestre-de-obras`. Nesta fase **não há trava de operador** — Leonardo revisa toda proposta antes do envio. Os critérios de classificação de complexidade serão calibrados com o uso (ver registro abaixo).

## O pipeline — seis passos

```
1. Leitura do Caso   → sintetiza intake + leitura jurídica; mapeia dor, custo da
   (interno)            inação, valor em jogo, urgência, recorrência. Detecta gatilhos.
2. Roteamento        → decide a trilha e se há etapa de Diagnóstico antes da proposta.
3. Precificação      → roda proposta.py: faixa + modelo + cenários.
4. Ratificação       → Leonardo revisa o número antes da redação.
5. Redação           → texto da proposta por trilha × camada da Garra (persuasão + freios 205).
6. Saída             → .docx no Modo Cliente do layout-aem.
```

**Nomenclatura (não confundir no treino da equipe):** *Leitura do Caso* é o passo 1, interno, sempre. *Diagnóstico* é um produto pago, só em casos complexos. Nomes diferentes de propósito.

## Passo 1 — Leitura do Caso (interno)

Sintetize o intake do 1º atendimento (comercial) com a leitura jurídica do 2º atendimento (advogado responsável). Produza, em poucas linhas: a **dor real** (quase nunca é a declarada), o **custo de não agir** (quantificado quando possível), o **valor econômico em jogo**, a **urgência**, e o **potencial de recorrência**. Puxe tese e riscos das skills analíticas e a **complexidade, a faixa de esforço, os gatilhos e as opções de escopo do `plano.md` v0 da `mestre-de-obras`**, quando ele existir; sem plano macro, peça-o antes de precificar. **Não recalcule nada disso aqui.**

## Passo 2 — Roteamento

Sem gatilho de complexidade → a proposta vai direto à precificação (defesa, ou jornada parecer→operação).

**Com qualquer gatilho** → a proposta é encabeçada por uma etapa de **Diagnóstico pago**, que também **classifica a trilha** (defensiva vs. preventiva). Gatilhos:

1. **Protocolo da reforma** (IBS/CBS) — questões de protocolo/transição que exigem dimensionamento.
2. **Risco de planejamento abusivo** — ex.: contrato de parceria rural entre PJ e seus sócios PF. **Atenção:** neste gatilho o Diagnóstico apenas *dimensiona a exposição* (quanto está em risco, quão exposto, o que o fisco enxergaria). **Não entrega a saída** — apontar o caminho da defesa/reestruturação já seria o parecer com outro nome.
3. **Múltiplas entidades** — grupo econômico, participações cruzadas, patrimônio difuso.

A regra de ouro do roteamento: o Diagnóstico mede o tamanho e classifica a trilha; o Parecer entrega a estratégia; a Operação detém a execução. Cada degrau credita no seguinte (ver matriz).

## Passo 3 — Precificação

Rode `scripts/proposta.py`. Ele devolve **faixa, modelo recomendado e cenários** — nunca um preço único. Use as funções conforme a trilha (`trilha_defesa`, `trilha_operacao`, `trilha_parecer`, `trilha_diagnostico`) e os cenários (`calendario_colheita`, `fixo_vs_exito`, `escada_credito`). Os parâmetros financeiros, faixas e a cadeia de crédito estão em `references/matriz_precificacao.md`. **Todo cálculo passa pelo script** — nada de aritmética mental; o módulo se autoverifica por inversão.

## Passo 4 — Ratificação

Apresente faixa e cenários a Leonardo. O número final é julgamento dele. Só então redija.

## Passo 5 — Redação

Siga `references/persuasao_proposta.md`: a estrutura do documento, a espinha de persuasão (ancorar o problema antes do preço; autoridade RARO; enquadrar honorário contra risco/economia; escopo em opções, que são as do plano macro (A: dor declarada; B: causa-raiz), cada uma listando as fases que inclui; integração Agricompany como causa-raiz; decisão faseada na peça única) e as **restrições de geração do Provimento 205** — que são regra de produção, não disclaimer no rodapé.

## Passo 6 — Saída

Gere o `.docx` no **Modo Cliente** do `layout-aem`. Use `caixaDestaque('economia', …)` para o enquadramento de valor e `caixaDestaque('recomendacao', …)` para a opção sugerida. Se usar caixas, aplique o `fix_borders.py` e valide. Os números podem passar pelo `crivo-do-leao` antes do envio (ele checa exatidão numérica e consistência).

## Registro de calibração

Ao fechar cada caso, grave uma linha em um registro no Google Drive (mesma lógica do `destila`→acervo): **data, gatilhos disparados, base de cálculo, preço definido, modelo, fechou (sim/não)**. Depois de ~15–20 casos, os critérios de classificação de complexidade — e o preço do Diagnóstico, hoje aberto — emergem dali, calibrados pela prática, não inventados.

## Regras invioláveis

1. **Não reabrir a análise jurídica.** A tese vem das skills analíticas. Esta camada precifica e persuade.
2. **Faixa e cenários, nunca um preço cravado pelo script.** O número é julgamento do advogado.
3. **Proteger o ativo raro.** O parecer é soberano e a modelagem executável fica na operação. Nunca dissolver o parecer dentro de outro produto.
4. **Provimento 205 como restrição de geração.** Sem garantia de resultado, sem escassez fabricada, sem comparação depreciativa, sem linguagem de oferta/desconto. O crédito é estrutura de honorário, não "promoção".
5. **Sempre `.docx` timbrado** via `layout-aem`, Modo Cliente. Validar o arquivo gerado.
