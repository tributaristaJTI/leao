# Fluxo: planejamento sucessório e patrimonial (grupo familiar rural)

**Donas do conteúdo:** `mod-grupo-economico` (mapeamento → diagnóstico → cenários → propósito negocial → recomendação e cronograma), `tributarista-consultivo` (enquadramento, mapeamento tributário, teses com grau de risco, precedentes via `jusratio`, recomendação), `coleta-inteligente` (checklist de documentos), `parecer-aem` (peça consultiva), `entregavel-cliente` (material de decisão para a família), `monday-caso` (frentes: Sucessão e Governança, Societário, Fiscal e Cadastral, Contratos de Exploração). Este arquivo só ordena as fases e as dependências; o método de cada uma mora na skill dona.

**Gatilho quase sempre presente:** múltiplas entidades (gatilho 3 da `proposta-aem`). Consequência: F2 é o Diagnóstico pago e as fases seguintes ficam condicionadas ao resultado dele. Gatilho de planejamento abusivo (contrato de parceria entre PJ e sócios PF, por exemplo) mantém o Diagnóstico apenas dimensionando a exposição, sem entregar a saída.

**Entidade dona:** conjunto por natureza. AeM na raia jurídica (societário, tributário, contratos, sucessão formal); Agricompany na raia de gestão, governança familiar e integração contábil (`contador-rural`, `consultor-governanca`, `gestor-financeiro`).

## Fases (esquema comum)

| id | nome | entregável | critério de conclusão | dependências | perfis | esforço | executor | frente Monday |
|---|---|---|---|---|---|---|---|---|
| F1 | Coleta e mapeamento | checklist emitido ao cliente; organograma completo do grupo (pessoas, PJs, participações, imóveis, contratos, fluxos) | organograma sem ponta aberta; documentos críticos recebidos | documento do cliente; contador-do-cliente | advogado-assistente (coleta), contador-rural (regimes e balanços), decisor | M | `coleta-inteligente` + `mod-grupo-economico` etapa 1 | Coleta e Mapeamento |
| F2 | Diagnóstico | carga tributária por ponta; riscos estruturais (confusão patrimonial, art. 124 do CTN, partes relacionadas, concentração no patriarca); exposição dimensionada | relatório de diagnóstico entregue e aceito | F1 | socio-responsavel, contador-rural, gestor-financeiro (raia Agricompany: diagnóstico financeiro) | G | `mod-grupo-economico` etapas 2 e 3 + `mod-comparativo-pf-pj` e `mod-funrural` quando couber | Diagnóstico |
| F3 | Cenários e parecer | dois ou três cenários (segregação, consolidação, mista) com custo de implementação, economia anual, ITCMD projetado e propósito negocial; parecer consultivo | parecer passado pelo crivo (perfil Análise Tributária) | F2; decisao-socio (régua de risco) | socio-responsavel, advogado-associado, contador-rural | G | `mod-grupo-economico` etapas 4 a 6 + `tributarista-consultivo` + `parecer-aem` + `crivo-do-leao` | Cenários e Parecer |
| F4 | Decisão da família | material de decisão para leigo; reunião de família; cenário escolhido registrado no `_ledger.md` | ata da reunião com cenário escolhido | F3; decisao-cliente | socio-responsavel, diretor-executivo, consultor-governanca, decisor, herdeiros | P–M | `entregavel-cliente` + `atas-leao` (ata da reunião) | Decisão da Família |
| F5 | Operação societária | holding constituída ou alterada; integralizações; alterações contratuais registradas; contratos entre partes formalizados (arrendamento, parceria, cessão) | registros na junta e no cartório comprovados | F4; junta-comercial; cartorio-registro; fisco (ITBI, CNPJ, inscrições) | advogado-assistente, administrativo-aem, contador-rural | G | produção própria (`braco-direito` para minutas) + `legal:contract-review` quando A-02 e A-08 fecharem | Societário |
| F6 | Fiscal e cadastral | regimes escolhidos formalizados; inscrições; obrigações acessórias do novo desenho; efeitos IBS/CBS a partir de 2027 mapeados | cadastros e regimes ativos | F5; fisco | contador-rural, advogado-assistente | M | `mod-ibs-cbs-diferimento` (regime das partes) + `mod-funrural` | Fiscal e Cadastral |
| F7 | Sucessão e governança | doações com ou sem usufruto, cláusulas restritivas, testamento quando couber; acordo de sócios ou de quotistas; protocolo familiar; conselho de família | instrumentos assinados e registrados; protocolo aprovado pela família | F5; cartorio-notas; decisao-cliente | socio-responsavel, advogado-assistente, consultor-governanca, herdeiros | G | produção própria (raia AeM) + Agricompany (raia governança) | Sucessão e Governança |
| F8 | Pós-implementação | calendário de monitoramento (obrigações, distribuição de resultados, contratos entre partes a valor de mercado); teses candidatas listadas para `/destila` | primeiro ciclo de monitoramento cumprido | F6, F7 | contador-rural, gestor-financeiro, advogado-assistente | P | Agricompany (BPO) + `destila` | Pós-implementação |

## Escopos candidatos típicos

- **Opção A (dor declarada):** F1 a F5 (mapear, diagnosticar, escolher o cenário com a família e implantar a operação societária). F4 nunca sai de nenhuma opção: implementação sem decisão registrada da família é o erro que o plano existe para impedir. Sucessão formal (F7) e governança ficam fora, com a lacuna `decisao-cliente` registrada.
- **Opção B (causa-raiz):** F1 a F8, com a raia Agricompany explícita em F2, F4, F7 e F8.

## Notas de interface

- A `monday-caso` hoje cria grupos fixos (Foco da Semana · Sucessão e Governança · Societário · Fiscal e Cadastral · Contratos de Exploração · Concluído). As fases acima mapeiam nesses grupos, mais "Coleta e Mapeamento", "Diagnóstico", "Cenários e Parecer" e "Decisão da Família", que não existem lá: passar a lista de grupos no bloco `<caso>` (delta registrado).
- O `mod-grupo-economico` (etapa 7) já produz sequência de implementação, prazos, profissionais e monitoramento: quando o Diagnóstico e os cenários existirem, o v1 deste fluxo consome esse cronograma em vez de reinventá-lo.
