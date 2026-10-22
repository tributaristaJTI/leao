# Caso sem fluxo conhecido

Nenhum arquivo em `fluxos/` encaixa quando o objeto do projeto não é transação de fazenda nem sucessório/patrimonial de grupo familiar. Exemplos previsíveis: planejamento tributário de operação isolada (PF → PJ, regime, comercialização), renegociação ou reestruturação de dívida rural, transação tributária, defesa administrativa longa, consultoria financeira da Agricompany sem dimensão societária, protocolo de transição IBS/CBS.

## Esqueleto padrão

Montar as fases a partir deste esqueleto, cortando o que não se aplica e nomeando cada fase no vocabulário do caso:

| id | nome-base | executor habitual |
|---|---|---|
| F1 | Coleta e enquadramento | `coleta-inteligente`; `tributarista-consultivo` etapa 1 (consultivo) ou `tributarista-contencioso` (exigência já formalizada) |
| F2 | Diagnóstico ou análise | skill analítica do domínio; Diagnóstico pago quando houver gatilho |
| F3 | Estratégia, cenários ou parecer | `tributarista-consultivo` etapas 3 a 5, módulos `mod-*`, `parecer-aem`, `crivo-do-leao` |
| F4 | Decisão do cliente | `entregavel-cliente`, reunião, `atas-leao` |
| F5 | Implementação | produção própria, `braco-direito`, terceiros |
| F6 | Pós-implementação e monitoramento | Agricompany (BPO), `destila` |

Regras do esqueleto: dependência de terceiro sempre tipada; perfis por raia; gatilhos da `proposta-aem` verificados; escopos A e B mesmo sem fluxo.

## Marcação e registro

1. Cabeçalho do plano: `FLUXO: sem-fluxo (família candidata: [nome curto do tipo de caso])`.
2. Uma linha em `candidatos-a-fluxo.md` (pasta canônica no Drive, ver SKILL.md seção 7): `data | slug do caso | família candidata | fases usadas (ids e nomes) | entidade dona`.
3. Se `candidatos-a-fluxo.md` já tiver uma linha da mesma família: a skill aponta a coincidência no relatório de fechamento e propõe a promoção a fluxo-padrão, com o arquivo `fluxos/[familia].md` rascunhado a partir dos dois planos. A promoção é ratificação do Leonardo; entra na versão seguinte da skill. A skill não promove sozinha.

## O que não fazer

Não criar fluxo novo para caso único; não copiar o método da skill analítica para dentro do plano; não estimar prazos absolutos; não atribuir pessoa.
