---
name: "destila"
description: "Skill transversal de destilação e arquivamento no acervo do escritório. Use SEMPRE que o usuário digitar /destila, ou mencionar 'destila isso', 'arquiva no acervo', 'manda pro acervo', 'salva no acervo', 'vira nota canônica', 'transforma em nota', 'guarda essa tese', 'preserva essa decisão', ou qualquer variação de pedido para transformar um output pronto (parecer, análise, contrato) ou uma decisão externa (CARF, STJ, STF, TJ) em nota consultável do acervo. A skill extrai a tese para o esquema canônico, separando o que é durável do que é volátil, pede confirmação, e grava o .md direto na pasta do acervo no Google Drive. NÃO use para revisar ou verificar texto — para isso existe o crivo-do-leao. NÃO use para produzir conteúdo (pareceres, contratos, artigos) — para isso existem as skills de produção. O destila é exclusivamente pós-produção: preserva o que já está pronto, não cria nem corrige."
---

# Destila — Destilador do Acervo

*v1.2 (2026-10-21): economia de contexto nas Etapas 2, 6 e 7 e consolidação do aditivo. A skill roda no fim da conversa mais longa da sessão, e cada chamada de ferramenta reprocessa a conversa inteira: menos chamadas e nenhuma emissão dupla.*

Skill transversal que transforma um output finalizado em **nota canônica consultável** e a grava no acervo do escritório (Google Drive). É o espelho do crivo: o crivo verifica *antes* de o documento sair para o cliente; o destila preserva *depois* de o documento estar pronto.

Filosofia: cada peça que o escritório produz deveria baratear e melhorar a próxima. Sem acervo, a experiência não compõe — o décimo parecer custa o mesmo que o primeiro. O destila captura onde a produção acontece, com custo humano marginal (uma confirmação de dez segundos), para que o conhecimento vire ativo institucional em vez de evaporar.

O destila **não julga mérito nem decide o que merece ser arquivado** — isso é decisão do advogado. Ele industrializa o *formato*, não o *juízo*.

## Comando

`/destila` — comando único. A skill identifica automaticamente o tipo de nota e a natureza, e propõe a classificação para o usuário confirmar.

## Pré-requisito

A skill grava no Google Drive. O conector do Google Drive precisa estar ativo na sessão.

## Âncoras fixas do acervo — navegar sempre por ID

A busca por nome no Drive é não confiável (latência de indexação, pastas homônimas) e falha justamente no arquivo recente. Toda navegação parte destes identificadores:

- Raiz do acervo (`Acervo AeM`): **`1V4xYyffyXXT7lSY2i51tVd7l1P5xIGIh`**
- Histórico do acervo (`Acervo AeM/_historico/`): **`1rmOgyyKbuyoNrEw8rDP_xbLaYPx0bi0-`**

A pasta da matéria resolve-se por `parentId = '<raiz>' and title = '<materia>'`. Se não existir, oferecer criá-la antes de gravar.

Os arquivos de governança **não têm ID fixo** — cada reemissão cria arquivo novo. Resolver sempre por raiz + título exato:

- `parentId = '<raiz>' and title = '_esquema-nota-canonica.md'`
- `parentId = '<raiz>' and title = '_vocabulario-termos-novos.md'`

## Fonte única do vocabulário — regra dura

O vocabulário controlado vivo é o do **Drive**, em duas peças que se leem juntas: o apêndice do `_esquema-nota-canonica.md` (raiz do acervo) e o aditivo `_vocabulario-termos-novos.md` (mesma pasta), que carrega os termos aprovados depois da última revisão do esquema.

A cópia em `references/esquema-nota-canonica.md` deste pacote serve **apenas como molde estrutural de emergência** — as cinco seções do corpo e a forma do frontmatter, que são estáveis. **O vocabulário dela está desatualizado e não vale.** Nunca classificar `materia` ou `tags` por ela.

Por quê: em 08/09/2026 uma sessão classificou pela cópia do pacote e registrou como "lacuna de governança" uma matéria e quatro tags que já estavam aprovadas no Drive havia semanas. Vocabulário lido do lugar errado não produz erro visível — produz retrabalho com aparência de rigor, e deixa a conclusão errada escrita para a próxima sessão ler.

Se o Drive estiver indisponível: usar o molde estrutural do pacote, marcar `materia` e `tags` como `[a ratificar — vocabulário não lido do Drive]` e avisar o usuário, na entrega, que a nota precisa de uma passada de classificação quando o conector voltar. Nunca inventar termo nesse estado.

## Fluxo de trabalho

### Etapa 1 — Receber o material
O material pode ser: output de outra skill (parecer-aem, tributarista-consultivo, etc.) presente na conversa, texto colado, ou arquivo (.docx, .pdf). Se vier de arquivo, leia o conteúdo antes de prosseguir.

### Etapa 2 — Ler o vocabulário vivo, do Drive
Antes de classificar qualquer coisa, ler as duas peças pelas âncoras acima: o `_esquema-nota-canonica.md` (molde + apêndice) e o `_vocabulario-termos-novos.md` (aditivo). O que vale para `materia` e `tags` é a união das duas.

Economia: localizar as duas numa consulta só, só com metadados (`parentId = '<raiz>' and (title = '_esquema-nota-canonica.md' or title = '_vocabulario-termos-novos.md')`), e ler as duas em paralelo. Na mesma sessão, a leitura vale para todas as notas: não reler a cada nota.

### Etapa 3 — Classificar tipo e natureza
Determine, a partir do material:

**tipo:**
- `destilacao-propria` — peça produzida pelo escritório (parecer, análise tributária, contrato, nota técnica).
- `precedente-jurisprudencial` — decisão externa (CARF, STJ, STF, TJ) que se quer preservar para reuso.

**natureza:** `consultivo-preventivo` | `contencioso`.

Se for precedente, determine também a **polaridade**: `favoravel-ao-contribuinte` | `desfavoravel-ao-contribuinte` | `mista`.

A classificação é proposta, não definitiva — será mostrada ao usuário na Etapa 6 para confirmação ou correção.

### Etapa 4 — Verificar granularidade (uma nota por tese)
Se o output carrega **mais de uma tese reaproveitável** (ex.: um parecer de holding rural com ângulos de integralização, ITCMD e Funrural), **não** produza uma nota-balaio. Proponha **N notas separadas**, cada uma com sua tese, todas cruzadas-linkadas à mesma `peca-fonte`. Um output, várias notas — cada uma diretamente recuperável.

### Etapa 5 — Extrair para o esquema, com separação durável/volátil
Preencha o molde. A separação durável/volátil é a espinha da nota:

- **Tese central, Fundamento nuclear, Exceções e limites** → camadas **DURÁVEIS**. Capture a *arquitetura* do argumento (os eixos, a engrenagem, a jogada), não o dispositivo. É o que compõe e envelhece bem.
- **Âncoras normativas** → camada **VOLÁTIL**. Todo dispositivo, súmula, tema repetitivo ou solução de consulta vai aqui, sob o rótulo `⚠ VERIFICAR ANTES DE CITAR`. Sinalize expressamente vetores de instabilidade conhecidos — reforma tributária (LC 214/2025, LC 227/2026), lei alteradora (ex.: Lei 14.689/2023 no regime da multa qualificada), tese pendente de julgamento.
- **Frontmatter**: `tema`, `materia` (vocabulário controlado), `tipo`, `natureza`, `tags` (vocabulário controlado), `data-emissao` (data de hoje), `peca-fonte`, `notas-relacionadas` (opcional). Se for precedente, preencha também o bloco de rastreabilidade.

### Etapa 6 — Mostrar a ficha de revisão e PEDIR CONFIRMAÇÃO
**Nunca grave antes do "ok".** Mostre no chat a ficha de revisão, não a nota inteira, porque o corpo completo seria emitido duas vezes (no chat e na gravação) sem acrescentar nada ao que a revisão de dez segundos confere. A ficha traz, por nota:
- a **tese central**, como vai ficar na nota;
- tipo e natureza classificados (e polaridade, se precedente);
- `materia` e `tags` escolhidas — sinalizando qualquer **termo novo** proposto fora do vocabulário lido na Etapa 2;
- **quais âncoras ficaram sob ⚠ e por quê** — esta é a checagem mais importante;
- o nome de arquivo e a pasta de destino propostos.

Se o usuário pedir a nota inteira ("mostra inteira"), mostre-a. Com N notas da mesma peça (Etapa 4), uma ficha por nota num bloco só e uma confirmação para todas.

Encerre com pergunta direta: **"Confirma ou ajusta?"**

### Etapa 7 — Gravar no acervo (Drive), só após confirmação
1. Resolver a pasta da matéria por `parentId` a partir da raiz-âncora. Se a estrutura não existir, ofereça criá-la antes de gravar.
2. Nome do arquivo: derivado do `tema`, minúsculo, com hífens, sem acento, descritivo (ex.: `parceria-rural-simulada-familiares-interpostas.md`).
3. Criar o `.md` na pasta da matéria com `disableConversionToGoogleType=true` e `contentMimeType='text/markdown'` — sem isso o Drive converte o arquivo em Google Doc. O corpo completo é montado aqui, uma única vez, com os ajustes da Etapa 6 aplicados.
4. Confirmar ao usuário o caminho final onde a nota foi gravada.

### Etapa 8 — Termo novo aprovado entra no vocabulário na mesma sessão
Se o usuário aprovou termo novo na Etapa 6, ele **não fica pendente para a próxima consolidação**: gravar o aditivo `_vocabulario-termos-novos.md` atualizado na mesma resposta — termo, família, data de aprovação, justificativa de por que nenhum termo existente cobria o eixo, notas que o usam — e rotacionar a versão anterior conforme a governança de arquivos abaixo. Termo aprovado que não é escrito na mesma sessão é termo que a próxima sessão reinventa com outro nome.

**Consolidação do aditivo:** o aditivo é reemitido inteiro a cada termo novo, porque o conector do Drive não edita conteúdo, e cada execução lê as duas peças. Quando o aditivo passar de 15 termos, propor ao usuário, na entrega, a consolidação no apêndice do `_esquema-nota-canonica.md` (com rotação das duas versões conforme a governança abaixo). A consolidação é decisão dele, nunca automática.

**Fallback:** se a escrita no Drive estiver indisponível na sessão, salve o `.md` localmente e entregue para o usuário arrastar para o Drive — mas avise que isso quebra a promessa de custo quase zero do acervo, e que o ideal é rodar a skill onde o Drive está conectado.

## Governança de arquivos do acervo

Cada casa rotaciona no próprio histórico. Ao reemitir `_esquema-nota-canonica.md` ou `_vocabulario-termos-novos.md`, a versão substituída vai para `Acervo AeM/_historico/` renomeada `<nome>-v<n>-<AAAA-MM-DD>.md`, e a nova fica na raiz com o nome limpo. Nota superada por correção de fato, de data ou de tese sai da pasta de matéria para o mesmo histórico, com prefixo `_superada-<motivo-curto>-<data>_` antes do nome original.

Três regras sustentam isso:

1. **A rotação é ato da mesma sessão que grava a versão nova.** Versão antiga parada ao lado da viva, com nome quase igual, é o defeito mais barato de cometer e o mais caro de descobrir.
2. **Nada é apagado.** `_historico/` é destino, nunca lixeira: o percurso é prova, e a versão anterior de uma tese explica por que a atual diz o que diz.
3. **Histórico é da casa, não do sistema.** Versão superada do acervo nunca vai para o histórico do `Arquivo AeM`, nem o contrário — as duas árvores são varridas por buscas distintas, e versão morta aparecendo na varredura da casa vizinha é ruído que ninguém sabe ler.

Regra completa, com o percurso que a justifica: `Acervo AeM/gestao-escritorio/historico-por-casa-rotacao-no-proprio-acervo.md`.

## Regras duras de integridade

**Não inventar citação.** Número de acórdão, número de processo, dispositivo legal, relator, data de julgamento — se desconhecidos, marque `[a preencher]`. Nunca fabrique. Citação inventada é o erro que destrói a confiança no acervo e contamina toda peça futura que o consulte.

**Não verificar — preservar sob rótulo.** O destila **não** faz web search de vigência (isso é o crivo). As âncoras nascem sob `⚠`, com `validade-verificada-em: não verificado no arquivamento`. A verificação é deferida ao momento do reuso. Se o usuário informar que o documento acabou de passar pelo crivo, registre a data em `validade-verificada-em`. Não duplique o trabalho do crivo.

**Na dúvida, é volátil.** Se há incerteza sobre se algo é durável ou volátil, trate como volátil (âncora sob ⚠). Falso-volátil custa pouco; falso-durável (citar como assentado o que mudou) custa caro. Em matéria sob reforma (IBS/CBS), trate referência normativa como volátil por padrão.

**Não inventar tag nem matéria.** Use apenas os valores lidos do Drive na Etapa 2. Se faltar um termo, **não o crie silenciosamente** — proponha-o como "novo termo" no rascunho da Etapa 6, peça aprovação e grave-o na Etapa 8. O vocabulário cresce por decisão, não ad hoc, para não fragmentar a recuperação entre os advogados do escritório.

**Não registrar lacuna sem conferir a fonte viva.** Antes de anotar que um termo está "em uso sem aprovação", conferir o apêndice do esquema do Drive e o aditivo. Lacuna registrada por leitura de cópia velha é pior que nenhuma: vira instrução errada para a sessão seguinte.

## Princípios de conduta

**Preserva, não produz.** O destila não reescreve a peça, não melhora o argumento, não corrige o original. Extrai e arquiva o que já existe.

**Confirma antes de gravar.** Sempre. O julgamento sobre qual é a tese certa e o que é volátil é do advogado; a skill formaliza, não decide.

**Específico, não genérico.** "Tese sobre planejamento tributário" é inútil para recuperação. "Parceria rural simulada por interposição de PJ familiar sem substância" é recuperável.

## Limitações conhecidas

A qualidade da nota depende da qualidade do output. Material ruim entra, nota destilada ruim sai — o destila não conserta argumento fraco, apenas o registra fielmente.

A separação durável/volátil é heurística, não infalível. O usuário deve conferir, na revisão de dez segundos, se algo durável escapou para as âncoras ou vice-versa.

A skill não decide o que merece ser arquivado. Ela formaliza o que o usuário mandou destilar.

A cópia em `references/esquema-nota-canonica.md` é molde estrutural de emergência, com vocabulário datado de 08/07/2026. Ela não é atualizada a cada decisão de vocabulário, e não deve ser: a fonte é o Drive. Quando houver revisão do esquema, consolidar o aditivo dentro do `_esquema-nota-canonica.md` da raiz — nunca dentro do pacote.