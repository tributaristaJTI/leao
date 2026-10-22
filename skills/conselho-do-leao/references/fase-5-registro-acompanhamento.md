# Fase 5 — Registro e Acompanhamento

**Objetivo:** documentar a decisão para revisão futura e criar mecanismos automáticos contra inércia pós-decisão.

---

## Diário de Decisão

Ao final de cada protocolo completo, gere um registro estruturado:

```
═══════════════════════════════════════════
REGISTRO DE DECISÃO — CONSELHO DO LEÃO
═══════════════════════════════════════════

Data: [data]
Decisão: [descrição concisa]
Camada: [1 ou 3]
Dimensão do Ecossistema: [qual]
Modo: [individual / colegiado]

DEFINIÇÃO DO PROBLEMA
Problema original: [como Leonardo trouxe]
Problema reformulado: [versão clarificada]
Causa raiz: [identificada na Fase 1]
Decisões embutidas: [se houver]
Lacunas de informação: [o que faltava saber]

DIAGNÓSTICO DE DEFAULTS
Default(s) detectado(s): [qual/quais]
Evidências: [resumo das evidências]

EXPLORAÇÃO DE SOLUÇÕES
Alternativas geradas: [listar todas com origem]
Técnicas utilizadas: [3+, inversão, cenário temporal, etc.]

AVALIAÇÃO
Alternativa escolhida: [qual e por quê]
Alternativas descartadas: [quais e por quê]
Pensamento de segunda ordem: [consequências em cadeia]
Pré-mortem: [principais riscos identificados]
Resultado do stress test: [sobreviveu ao advogado do diabo? como?]

DECISÃO FINAL
O que foi decidido: [ação concreta]
O que se espera que aconteça: [resultado esperado, com prazo]
O que precisaria ser verdade para essa decisão estar errada: [condições de invalidação]

TRIPWIRE
Gatilho: [evento, data ou indicador específico]
Prazo máximo de revisão: [data]
Ação se o tripwire disparar: [o que fazer]

LENTE RARO
Essa decisão cria categoria ou compete dentro de uma existente? [resposta]
═══════════════════════════════════════════
```

**Instrução ao usuário:** após gerar o Diário, salve como arquivo `.md` no diretório de trabalho e diga: "Salve esse registro no local onde você mantém a documentação do Ecossistema (Obsidian, pasta local, etc.) para consulta futura. Se precisar revisar essa decisão depois, traga o arquivo de volta."

---

## Regras para Tripwires

Um tripwire deve ser:

- **Específico:** "se o faturamento do novo produto ficar abaixo de R$ X em 6 meses", não "se não der certo".
- **Observável:** baseado em dados ou eventos concretos, não em impressões subjetivas.
- **Pré-comprometido:** definido *antes* de a decisão ser implementada, quando o julgamento ainda está claro.
- **Conectado a uma ação:** "se o tripwire disparar, a ação é [X]" — não apenas "repensar".

---

## Loop de Revisão

Quando Leonardo acionar `/revisao` ou mencionar uma decisão passada, conduza a **revisão pós-decisão** (ele pode trazer o arquivo de registro salvo anteriormente):

- "O que você esperava que acontecesse? O que de fato aconteceu?"
- "O default que diagnosticamos estava correto? Algum outro default apareceu depois?"
- "O que você faria diferente com o que sabe agora?"
- "O tripwire foi respeitado ou ignorado? Se ignorado, por quê?" (provavelmente inércia pós-decisão)

Esse loop é o mecanismo de calibração — sem ele, o julgamento não melhora ao longo do tempo.
