# Esquema do `plano.md`

Esquema fixo. Todo plano tem estes blocos, nesta ordem. Campo sem informação recebe `[LACUNA — ...]` conforme `lacunas.md`, nunca fica em branco nem é estimado.

## 1. Cabeçalho

```
CASO:                 [slug-do-caso]  ·  [Cliente / Família por extenso]
ENTIDADE DONA:        AeM | Agricompany | conjunto (raia por fase na seção 3)
OBJETO:               [uma linha]
FLUXO:                transacao-fazenda | sucessorio-patrimonial | sem-fluxo (família candidata: [nome])
NÍVEL / VERSÃO:       v0 macro | v1 execução   ·   data
FONTE DE ENTRADA:     extração /ata de [data] | /comercial de [data] | /operacional de [data]
TRILHA CONTRATADA:    [só no v1: opção aceita e data do aceite]
COMPLEXIDADE:         baixa | média | alta   (vocabulário do /comercial, seção 6)
ESFORÇO TOTAL:        P | M | G | GG   (faixas provisórias, ver seção 6 deste esquema)
GATILHOS:             nenhum | protocolo da reforma | planejamento abusivo | múltiplas entidades
MARCOS:               M0 aceite · M1 [ ] · M2 [ ] ...
```

## 2. Escopo

- **Escopos candidatos (v0):** Opção A (mínimo que resolve a dor declarada) e Opção B (causa-raiz), cada uma como lista das fases que inclui. Mesmo formato do "escopo em opções" da `proposta-aem`.
- **Escopo vendido (v1):** a opção aceita. **Fora de escopo:** fases das outras opções, listadas para não serem esquecidas nem executadas sem contrato.

## 3. Fases (esquema comum, compartilhado com a `porteira-fechada`)

Uma tabela, uma linha por fase:

| Campo | Conteúdo |
|---|---|
| `id` | F1, F2 ... |
| `nome` | curto, no vocabulário do fluxo |
| `entregável` | o que existe no fim da fase (documento, decisão, registro) |
| `critério de conclusão` | prova de que acabou (comprovação documental, como na `monday-caso`) |
| `entradas` | o que precisa existir antes (documento, decisão, resultado de fase anterior) |
| `dependências` | tipadas: fase anterior · documento do cliente · decisão do cliente · decisão de sócio · terceiro (cartório, junta, banco, fisco, contador externo) |
| `perfis` | papéis de `perfis.md`, com a raia (AeM / Agricompany) quando a entidade dona for "conjunto" |
| `esforço` | faixa P/M/G/GG |
| `executor` | skill ou comando que produz a fase, quando houver (`/fazenda dd`, `mod-grupo-economico`, `parecer-aem`, `coleta-inteligente`) |
| `frente Monday` | nome do grupo que a `monday-caso` deve criar para a fase |

Regra de ordem: dependência de terceiro entra como status "Aguardando terceiro" no Monday, nunca como "Travado".

## 4. Tarefas (só no v1)

| Campo | Conteúdo |
|---|---|
| `id` | T1.1, T1.2 (fase.sequência) |
| `tarefa` | verbo no infinitivo + objeto específico do caso |
| `perfil` | um papel de `perfis.md` |
| `delegável` | S · N (com motivo: decisão de sócio, contato com o cliente, tese, assinatura) |
| `executor` | skill/comando quando houver; "produção própria" quando não |
| `dependência` | T-id(s) ou terceiro nomeado |
| `prazo relativo` | D+n após marco (M0 aceite, recebimento de documento X, registro na junta) |
| `prioridade` | Crítica · Alta · Média · Baixa |

Data absoluta só com marco datado, marcada `(derivada de Mn = dd/mm)`.

## 5. Lacunas

Lista no formato de `lacunas.md`. Vai no fim do plano, com contagem no relatório de fechamento.

## 6. Faixas de esforço (provisórias)

Horas totais estimadas da equipe, todas as raias: **P** até 10 h · **M** 10 a 40 h · **G** 40 a 120 h · **GG** acima de 120 h. Faixas iniciais, a calibrar contra o realizado (ponto e Monday) e a reconciliar com a `matriz_precificacao.md` da `proposta-aem` quando ela estiver reinstalada (A-13). Até lá, o plano entrega faixa, e a proposta decide o número.

## 7. Histórico do arquivo

O `plano.md` v1 preserva o v0 integral numa seção final "Histórico — v0 macro de dd/mm". Toda reemissão é arquivo novo no Drive, com a anterior renomeada com sufixo de versão.

## 8. Bloco `<caso>` (saída do v1 para a `monday-caso`)

```
FAMÍLIA / CLIENTE:            [por extenso]
PASTA DO CASO:                [pasta do dossiê | pasta em planos/ | "vou anexar"]
OBJETO DO PROJETO:            [objeto + opção aceita]
RESPONSÁVEL(IS):              [pessoa nomeada quando houver; senão o perfil entre colchetes: [advogado assistente]]
GRUPOS POR FASE:              [F1 nome · F2 nome · ... na ordem do fluxo]   ← parâmetro novo, ver deltas-fora-da-skill.md
TAREFAS DA PRÓXIMA SEMANA:    [as T-ids da primeira semana, com texto]
ALERTA:                       [dia e hora]
```
