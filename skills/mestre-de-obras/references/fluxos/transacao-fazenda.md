# Fluxo: transação de fazenda (compra e venda de imóvel rural)

**Dona do conteúdo:** `porteira-fechada` (F-11; `interfaces.md` v2 de 21/08, Fase 4 liberada). Este arquivo aponta para as fases dela e não redesenha nada. Quando a skill estiver instalada, `/fazenda abrir` produz o próprio plano macro deste fluxo e o `mestre-de-obras` apenas o transcreve no esquema comum; até lá, o macro é montado daqui.

**Estado do caso:** lado (`vendedor` | `comprador` | `neutro`) é campo obrigatório do cabeçalho. Modo neutro exige o gate ético da porteira (art. 22 do CED e seis regras) e dois contratantes na proposta (achado 4 da porteira).

**Gatilhos:** múltiplas entidades em qualquer ponta → `mod-grupo-economico` antes da estrutura (mesmo gatilho 3 da `proposta-aem`); parcelas além de 2026 ou partes contribuintes → regime das partes no `mod-ibs-cbs-diferimento`; semoventes ou estoque no preço → `mod-funrural` e vermelho de CPR (Lei 8.929/94, art. 11).

## Fases (esquema comum)

| id | nome | entregável | critério de conclusão | dependências | perfis | esforço | executor | frente Monday |
|---|---|---|---|---|---|---|---|---|
| F1 | Preparação | carta de contratação com o limite do art. 22 do CED; `_estado.md` aberto; lado fixado | carta assinada | decisao-socio (lado e régua) | socio-responsavel, advogado-assistente | P | `/fazenda abrir` | Preparação |
| F2 | Due diligence | matriz de risco 5×5 calibrada; checklist de DD emitido ao cliente; relatório de DD | relatório passado pelo crivo (perfil A-10 quando existir) | documento do cliente; cartorio-registro; fisco (certidões) | advogado-assistente (coleta), socio-responsavel (laudo), contador-rural (bloco tributário do vendedor) | G | `/fazenda dd` + `coleta-inteligente` (formato) + `crivo-do-leao` | DD |
| F3 | Origem de recursos e KYC | mapa de pagamento do art. 165-A do CNN; `_kyc.md` | mapa completo, sem recusa a averbar | banco; decisor (terceiro pagador) | advogado-assistente, banco | M | `/fazenda origem` | Origem |
| F4 | Estrutura | cenários tributários ratificados (`_estrutura.md`) | cenário escolhido pelo cliente | F2, F3; decisao-cliente | socio-responsavel, contador-rural | M–G | `/fazenda estrutura` → `mod-ir-venda-imovel`, `mod-comparativo-pf-pj`, `mod-grupo-economico` | Estrutura |
| F5 | Minuta | minuta com banco de cláusulas (três versões por cláusula); redlines | minuta aprovada pelas partes e passada pelo crivo (perfil Contrato) | F4; decisao-cliente | socio-responsavel, advogado-assistente | M | `/fazenda minuta` + `crivo-do-leao` | Minuta |
| F6 | Fechamento | escritura lavrada com meios e formas de pagamento; checklist de fechamento | escritura registrada | cartorio-notas, cartorio-registro, banco | advogado-assistente, administrativo-aem, cartorio-notas | M | `/fazenda fechar` | Fechamento |
| F7 | Pós-fechamento | calendário pós-fechamento (averbações, DITR, CAR, ITBI, obrigações); teses candidatas listadas para `/destila`; impedimento do art. 22 registrado no `_ledger.md` | calendário entregue e primeiro marco cumprido | F6 | advogado-assistente, contador-rural | P | `/fazenda fechar` (pós) + `destila` | Pós-fechamento |

Vermelhos automáticos da porteira (CPR física com preço antecipado ou barter; vendedor em recuperação judicial) entram como tarefas de prioridade Crítica na F2 e bloqueiam o sinal.

## Escopos candidatos típicos

- **Opção A:** F1, F2, F3, F5, F6 (DD, origem de recursos e contrato; estrutura só quando o cliente já decidiu o veículo). F3 nunca sai de nenhuma opção: sem mapa de pagamento do art. 165-A do CNN a escritura sai com recusa averbada.
- **Opção B:** F1 a F7 (com estrutura tributária e pós-fechamento). Entidade dona: conjunto quando a estrutura envolver reorganização do grupo (raia Agricompany em F4 e F7).

## Entidade dona

AeM por padrão. Conjunto quando F4 acionar `mod-grupo-economico` ou quando o pós-fechamento incluir gestão financeira da parcela ou da dívida.
