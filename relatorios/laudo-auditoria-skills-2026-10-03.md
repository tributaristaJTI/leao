# Laudo da auditoria de skills · decisões aprovadas

Auditoria manual das skills da conta e das preferências de usuário pelos critérios do `/checkup prompt-audit` do Claude Code, outubro de 2026. Este arquivo reúne as decisões que Leonardo aprovou e serve de entrada para o Prompt 1.2 do PLANO-CODE-AEM.md. O laudo item a item da auditoria não foi localizado como arquivo no Drive; o que está aqui é o registro das decisões, que é o que a execução precisa.

Objetivo declarado por Leonardo: o plano de ação deve tornar desnecessária a participação dele na execução das correções.

## Decisões por skill

| # | Skill | Decisão aprovada | Como aplicar |
|---|---|---|---|
| 1 | mod-ir-venda-imovel, mod-comparativo-pf-pj, mod-grupo-economico, mod-funrural, mod-ibs-cbs-diferimento | Os módulos devem conferir dispositivo, alíquota e prazo em fonte oficial ou no conector Jusratio, em vez de depender de arquivos de referência embarcados. | Substituir, em cada SKILL.md, a instrução de "ler references/" por instrução de conferir no Jusratio ou na fonte oficial consolidada; manter references/ só como mapa de onde procurar. |
| 2 | briefing-juridico | Migra para a layout-aem (identidade visual e papel timbrado passam a vir dessa skill). | Remover da briefing-juridico a instrução própria de layout; apontar para layout-aem. |
| 3 | Todas as skills que citam norma ou julgado | Texto único de conferência de citação, igual em todas. | Redigir um parágrafo padrão (dispositivo só entra depois de conferido no Jusratio ou em fonte oficial; o não conferido fica fora ou marcado [A CONFERIR: fonte]) e inserir o mesmo texto em cada SKILL.md, no mesmo ponto. |
| 4 | Plugin legal | Manter só a contract-review; as demais skills do plugin (brief, compliance-check, respond, signature-request, triage-nda, vendor-check, canned-responses, compliance, legal-risk-assessment, meeting-briefing, nda-triage) saem. | Plugin de terceiro: não editar a cópia; registrar em "Pendentes de decisão" a desativação das skills no painel do plugin, que é ação de Leonardo no chat. |
| 5 | pipeline, meu-dia, pauta-socios (ecossistema-do-leao) | Podem ler o Monday pelo conector. | Incluir na instrução de cada uma a leitura dos quadros do Monday como fonte. |
| 6 | cerebro-pbc | Dizer "modelo de maior capacidade disponível" em vez de nome de modelo. | Substituir qualquer nome de modelo pela expressão genérica. |
| 7 | destila | Ganha a etapa do catálogo (registro da nota no catálogo do Notion, no mesmo passo da gravação no Drive). | Acrescentar a etapa ao fluxo, depois da gravação no Drive e antes da confirmação ao usuário. |
| 8 | voz-autoral-leonardo e preferências | A voz-autoral-leonardo é a fonte única das proibições de estilo; as preferências carregam só o resumo e remetem à skill. | Na skill, consolidar a lista completa em "Proibições globais de estilo", com exemplos e testes; em outras skills que repitam a lista, substituir por remissão. |
| 9 | mod-ibs-cbs-diferimento | Avaliar se vale reescrever toda a instrução, para ficar mais eficiente e segura. | Não reescrever sem decisão. Produzir a versão proposta ao lado da atual e levar a "Pendentes de decisão". |
| 10 | braco-direito e preferências | Ajustar ao papel atual de Leonardo (fora da execução desde ago/2026): sócio fundador responsável por geração de negócios e estratégia de casos complexos de grupos familiares rurais; revisão final e protocolo cabem ao advogado responsável. | Na braco-direito, trocar o destinatário das entregas: o pacote final vai ao advogado responsável, e a Leonardo vai o resumo de estratégia. Preferências são editadas por Leonardo no chat; registrar em "Pendentes de decisão" o texto sugerido. |

## Fato que condiciona a publicação

As skills da conta são adicionadas por Leonardo no chat do Claude: o Claude gera o cartão de proposta e ele clica para adicionar. Não há marketplace nem upload por outra via. O Code corrige e versiona; a publicação segue o Prompt 1.3 do plano.

## O que não está neste laudo

Itens da auditoria que não geraram decisão registrada ficam fora da execução. Se, ao aplicar os itens acima, o executor encontrar na SKILL.md problema evidente do mesmo tipo (nome de modelo, lista de estilo duplicada, citação sem regra de conferência), registra em "Pendentes de decisão" sem corrigir.
