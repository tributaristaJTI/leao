---
name: poda
description: "Enxuga documento jurídico produzido pelo escritório (contrato, minuta de caso, modelo padrão) sem perder validade nem proteção. Mede o excesso contra a finalidade do documento, separa núcleo, função, proteção e trecho podável, propõe cortes tipificados em laudo para aprovação e, aprovado, gera a versão enxuta com controle de alterações, inventário de obrigações e conferência de remissões. Use SEMPRE que o usuário digitar /poda ou /poda aplica, ou pedir para enxugar, podar, cortar excesso, tirar exagero, simplificar, reduzir ou encurtar um contrato, minuta ou modelo, ou disser que o documento ficou longo, extenso, prolixo, pesado ou exagerado. NÃO use para verificar erro, citação ou consistência (crivo-do-leao), para redigir ou redesenhar a estrutura do contrato (braco-direito), para revisar contra o playbook de negociação (legal:contract-review) nem para explicar ao cliente documento de terceiro. A poda corta; não acrescenta cláusula nem muda o negócio."
---

# Poda — enxugamento de documento do escritório

Recebe um documento jurídico que o próprio escritório produziu e devolve, em dois tempos, o laudo de poda (o que cortar, por quê e com que efeito) e, depois da aprovação do advogado, a versão enxuta. Esta versão cobre contratos, minutas de caso e modelos padrão. Pareceres ficam fora até existir tipologia própria.

## 1. A régua é a finalidade

Tamanho não mede excesso: o mesmo parágrafo pode ser gordura num contrato e estrutura em outro. Numa parceria rural montada para manter a apuração do imposto de renda na pessoa física, o detalhamento da partilha de riscos e da contribuição de cada parte sustenta a qualificação como parceria e afasta a leitura de arrendamento; cortá-lo por elegância enfraquece o negócio. No sentido oposto, a motivação tributária escrita dentro do instrumento serve de prova contra o propósito negocial numa fiscalização, e por isso sai do contrato e vai para o guia interno. Nenhum corte é proposto antes do Passo 0.

## 2. Fronteiras

| Pedido | Destino |
|---|---|
| Verificar citação, cláusula mínima, contradição, remissão | crivo-do-leao |
| Redigir contrato ou mudar a estrutura do negócio | braco-direito |
| Comparar com o playbook de negociação | legal:contract-review |
| Explicar ao cliente leigo | entregavel-cliente (análise nossa) ou resposta direta |

A poda não acrescenta cláusula, não muda valor, prazo, percentual, parte, garantia, condição ou sanção, e não redesenha o negócio. Quando o excesso decorre do desenho, ela aponta e devolve a decisão (Passo 1, marcação D).

## 3. Entrada

- **Documento:** .docx enviado na conversa, ID do Google Drive, ou localização pelo `/acha` da arquivo-do-leao. Ler o documento inteiro antes de classificar; em .docx, extrair o texto seguindo a skill docx.
- **Espécie:** contrato de caso ou modelo padrão. Em modelo, notas ao redator, módulos opcionais e campos de preenchimento também são objeto da poda (T5 e T8).

## 4. Passo 0 — Finalidade

Identificar para que o documento existe, nesta ordem de fonte:

1. o pedido do usuário na conversa;
2. o `_estado.md` do caso, quando houver dossiê da guardiao-de-caso;
3. o guia de uso ou a nota de abertura do próprio documento.

Sem nenhuma das três, fazer UMA pergunta: "Qual a finalidade principal deste contrato: tributária, sucessória, patrimonial, operacional ou outra?"

Da finalidade saem as **cláusulas de função**, as que materializam o motivo do documento. Listá-las no laudo com o motivo em uma linha. Exemplo, na parceria de finalidade tributária: partilha de riscos, vedação de remuneração fixa, partilha em produto, apuração individual de cada parte, documentação que prova a partilha.

## 5. Passo 1 — Mapa em camadas

Percorrer o documento cláusula a cláusula e atribuir a cada trecho uma camada:

- **Núcleo** — o que o tipo contratual exige para existir e valer. Fonte: checklist 3 da skill crivo-do-leao (`references/checklists.md`: cláusulas mínimas por tipo, consistência interna, foro e legislação aplicável). Se o checklist não estiver montado na sessão, declarar isso no laudo e tratar como núcleo as cláusulas universais (qualificação das partes, objeto, obrigações, prazo, preço ou remuneração, extinção, foro) e as cláusulas obrigatórias por lei do tipo, conferidas na fonte oficial.
- **Função** — resultado do Passo 0.
- **Proteção** — alocação de risco a favor do cliente: garantias, responsabilidade, sucessão, saída, título executivo. Só a redação pode mudar.
- **Podável** — o resto.

Duas marcações não são poda e vão para seções próprias do laudo:

- **D — Excesso de desenho.** Bloco de cláusulas que existe por causa de uma escolha estrutural. Contrato estruturado como condomínio ou sociedade carrega denominação, sede, administração, quóruns, caixa comum, balanço e dissolução; trocada a estrutura por parceria sem sociedade, o bloco inteiro cai. A poda lista o bloco e a escolha que o sustenta e devolve a decisão ao advogado (redesenho pelo braco-direito). Não corta.
- **R — Risco encontrado.** Cláusula que não é excesso mas expõe o cliente: fiança ou aval cruzado entre parceiros, autorização para onerar bem de uma parte em dívida de outra, remuneração que descaracteriza o tipo. A poda registra em "Achados fora do escopo" e encaminha ao crivo ou ao advogado. Não reescreve conteúdo.

## 6. Passo 2 — Classificação do podável

Ler `references/tipologia-de-excesso.md` e atribuir a cada trecho podável um tipo de T1 a T8. Trecho que não se encaixa em tipo algum fica como está.

| Tipo | Excesso | Ação padrão |
|---|---|---|
| T1 | Repete a lei sem alterar o regime | excluir ou remeter |
| T2 | Duplicação interna | fundir |
| T3 | Texto padrão sem efeito ou sem pertinência (inclui definição não usada) | excluir |
| T4 | Detalhe operacional no corpo | mover para anexo |
| T5 | Didática, motivação ou instrução interna no instrumento | mover para guia interno |
| T6 | Prolixidade em cláusula necessária | reescrever |
| T7 | Declaração sem efeito operativo | reduzir ou fundir |
| T8 | Dado variável disperso (modelo padrão) | mover para quadro-resumo |

T1 exige conferir o texto da norma na fonte oficial na própria sessão (jusratio para legislação federal consolidada; fonte oficial na web para estadual, municipal e infralegal). Sem conferência, o item vira "T1 a conferir", vai para a seção 4 do laudo e não entra na aplicação.

## 7. Passo 3 — Laudo de poda

Responder no chat: o laudo é ferramenta de trabalho, como o do crivo. Estrutura fixa:

```
## Laudo de Poda
**Documento:** [título] · [contrato de caso | modelo padrão]
**Finalidade:** [finalidade] (fonte: [pedido | _estado.md | guia do documento | resposta do usuário])
**Extensão atual:** [N] palavras · [N] cláusulas

### 1. Núcleo e função (fora do alcance da poda)
[cláusula — por que é núcleo ou função]

### 2. Cortes propostos
| # | Onde | Ação | Tipo | Motivo | Efeito jurídico do corte | Palavras |
|---|---|---|---|---|---|---|
| 1 | Cl. 7.1.1 | excluir | T3 | tautologia: obriga a cumprir o próprio contrato | nenhum | 12 → 0 |

### 3. Decisões de desenho (não são poda)
[bloco D: cláusulas dependentes · escolha que as sustenta · o que cai se a escolha mudar]

### 4. Achados fora do escopo
[itens R e "T1 a conferir", com destino]

### 5. Projeção
Palavras: [antes] → [depois] (−[%]) · Cláusulas: [antes] → [depois]
Distribuição por tipo: [T2 x%, T5 y%, ...]

Aprovar em bloco, por número de item ou com ressalvas?
```

A coluna "Efeito jurídico do corte" admite só três respostas: "nenhum"; "volta a valer a regra supletiva de [norma conferida]"; "o conteúdo passa a morar em [anexo, quadro-resumo ou guia]". Qualquer outra resposta indica que o item não é poda e sai da tabela para a seção 3 ou 4.

Palavras de antes e depois vêm de contagem por script sobre o texto extraído, nunca de estimativa.

## 8. Passo 4 — /poda aplica

Só após aprovação expressa, e só os itens aprovados.

1. **Aplicar** no próprio arquivo quando a entrada for .docx, seguindo a skill docx: uma versão com controle de alterações (cada corte visível, com o número do item do laudo em comentário) e uma versão limpa. Formatação nova, quando necessária, pela layout-aem no modo contrato.
2. **Guia interno:** itens T5 aprovados vão para guia interno apartado (novo, ou o existente quando o documento já tiver guia), com remissão à cláusula de origem.
3. **Inventário de obrigações e direitos:** listar cada obrigação, direito, vedação, prazo e condição do original e o seu destino na versão nova: mantido (onde), fundido (onde), movido (anexo, quadro ou guia) ou excluído (item do laudo). Item sem destino trava a entrega até ser resolvido.
4. **Remissões:** listar toda remissão interna da versão nova (cláusula, item, parágrafo, alínea, anexo) e confirmar que o alvo existe e trata do que a remissão afirma, depois da renumeração.
5. **Crivo:** rodar o crivo-do-leao, perfil Contrato, sobre a versão limpa. Suspeita vermelha trava a entrega.
6. **Entrega:** arquivos e resumo (itens aplicados, palavras antes e depois, inventário sem pendência, resultado do crivo). Contrato de cliente é gravado pelo `/guarda` da arquivo-do-leao; modelo padrão é gravado ao lado da versão anterior, com número de versão novo. Registrar a sessão pela ponto-do-leao.

## 9. Regras invariáveis

1. Nenhum corte sem tipo T1 a T8 declarado.
2. Nenhum corte em núcleo ou função. Função duplicada se resolve por fusão, com a redação de maior alcance.
3. Nenhuma alteração de substância: valor, prazo, percentual, parte, garantia, condição, sanção.
4. A poda não acrescenta conteúdo. Texto novo só de fusão, de remissão ou de reescrita com o mesmo efeito; lacuna encontrada vai para a seção 4 do laudo.
5. Excesso de desenho e risco nunca viram corte.
6. Aplicação só com aprovação, item a item ou em bloco.
7. T1 sem conferência na fonte não se aplica.

## 10. Retroalimentação

Tipo que aparecer em dois laudos do mesmo produtor (mesma skill ou mesmo modelo) é candidato a regra na origem. Fechar o laudo com a linha "Padrão recorrente: [tipo e exemplo] — candidato à seção 8-A do braco-direito ou ao modelo padrão", para ratificação do Leonardo. A poda não edita outras skills.
