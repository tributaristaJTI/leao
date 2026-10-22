# Extração de atas — taxonomia, marcadores e gradiente de confiança

**Versão:** v1.1 — 2026-08-29 (reconstruído a partir do contrato do SKILL.md; o arquivo original de 26/06 não foi instalado com a skill). Este arquivo é a fonte da taxonomia; o SKILL.md só a resume.

## 1. Esquema de saída

A extração é uma lista de itens, cada um com estes campos. Campo sem informação recebe `null`, nunca valor suposto.

```
id:                  D1, A1, P1, R1 (categoria + sequência)
categoria:           decisao | acao | pendencia | risco
texto:               formulação fiel, uma frase, sem juridiquês acrescentado
trecho_origem:       span literal da ata que sustenta o item (obrigatório)
tipo_captura:        explicito | inferido
confianca:           alta | media | baixa
--- só decisao ---
requer_acao:         true | false   (declaratória ou autoexecutável = false)
responsavel_execucao: nome | null   (null com requer_acao = true → decisão órfã)
--- só acao ---
responsavel:         nome | null
responsavel_ambiguo: true quando "alguém", "a equipe", "o pessoal do contencioso", "eles"
prazo_literal:       texto exato do prazo | null
prazo_absoluto:      ISO, só via scripts/resolver_prazos.py, sempre com derivado = true
tipo_ator:           equipe_juridica | cliente | externo | reuniao_followup
status:              aberto | em_andamento | concluido
decisao_origem:      id da decisão que gerou a ação | null
--- só pendencia ---
encaminhamento:      quem ficou de levar adiante | null
--- só risco ---
dono_do_alerta:      quem levantou | null
```

Metadados da ata, no cabeçalho: `data_reuniao` (ISO ou null), `tipo_fonte` (ata_formal | notas_informais | transcricao_bruta), `tipo_reuniao` (socios | cliente | comite | agricompany | contencioso | outra), `participantes` (lista literal).

## 2. As quatro categorias e os marcadores de detecção

Os marcadores são pistas lexicais em português; nunca decidem sozinhos. Onde a mesma frase cabe em duas categorias, a regra de desempate está na seção 3.

### 2.1 Decisão (resolvido, settled)
Marcadores: "ficou decidido", "decidimos", "aprovado", "aprovamos", "fechamos que", "vamos seguir com", "definido", "fica mantido", "não vamos", "descartado", "o escritório assume", "combinado".
Teste: a frase encerra uma alternativa? Se sim, decisão. Decisão que só declara ("aprovamos a ata anterior", "registrada a presença") tem `requer_acao = false`.
Decisão que manda fazer algo ("ficou decidido que vamos protocolar") tem `requer_acao = true`; se ninguém assumiu, `responsavel_execucao = null` e ela entra nos defeitos como órfã. Ela também gera uma ação, com `decisao_origem` apontando para ela, e a ação nasce sem dono, o que é registrado uma vez só (na decisão órfã), não duas.

### 2.2 Ação / próximo passo (tarefa com dono e prazo esperados)
Marcadores: "fulano vai", "fulano fica de", "fulano faz", "manda para", "protocola", "agenda", "levanta", "pede ao cliente", "até", "em X dias", "próxima semana", "antes da reunião", "assume", "leva".
Teste: existe um verbo de execução com objeto? Se sim, ação. Sem sujeito nomeado, `responsavel = null`; sujeito coletivo ("a equipe", "alguém", "o pessoal", "eles"), `responsavel_ambiguo = true`.
`tipo_ator`: equipe_juridica (advogados, assistentes, sócios); cliente (produtor, família, contador do cliente); externo (cartório, banco, junta, corretor, contador externo, fisco); reuniao_followup (a própria próxima reunião é a "executora": "retomar na próxima", "voltar ao tema").

### 2.3 Pendência (levantado e não resolvido)
Marcadores: "ficou em aberto", "não fechamos", "vamos pensar", "depende de", "precisa ver", "não decidimos", "a definir", "em dúvida se", "ou... ou", "aguardar".
Teste: houve alternativa e ela continua aberta? Se sim, pendência. Pendência não tem dono porque não houve decisão; pode ter `encaminhamento` ("o Leonardo vai pensar e trazer") sem virar ação, porque o encaminhamento é sobre a decisão, não sobre a execução.

### 2.4 Risco / alerta (preocupação que não virou decisão nem tarefa)
Marcadores: "cuidado com", "preocupa", "risco de", "pode dar problema", "atenção ao prazo", "o fisco pode", "se não fizermos", "alerta".
Teste: a frase descreve consequência possível sem mandar fazer nem decidir? Se sim, risco. Risco com dono de execução ("o Ricardo vai monitorar") gera também uma ação.

## 3. Regras de desempate

1. **Pendência × ação órfã.** Houve direção? ("precisamos protocolar" é direção; "não sei se vamos protocolar" não é). Direção sem executor = ação órfã (defeito). Sem direção = pendência.
2. **Decisão × ação.** A decisão encerra a alternativa; a ação executa. "Decidimos migrar para PJ" (decisão) e "a Juliane prepara a minuta da constituição" (ação, `decisao_origem = D-n`).
3. **Risco × pendência.** O risco descreve consequência; a pendência descreve escolha em aberto. "Se não regularizar o arrendamento, cai no art. 124" é risco; "não sabemos se regularizamos ou desfazemos" é pendência.
4. **Fala sobreposta em transcrição.** Quando duas falas se contradizem e nenhuma fecha, registrar pendência com `trecho_origem` das duas e `confianca = baixa`.

## 4. Gradiente de confiança

| Tipo de fonte | Inferência permitida | `confianca` padrão | O que rebaixa |
|---|---|---|---|
| Ata formal | mínima | alta | item sem trecho literal correspondente |
| Notas informais | moderada | media | sujeito omitido; verbo sem objeto; prazo relativo sem data da reunião |
| Transcrição bruta | pesada | media, baixa quando houver fala sobreposta ou contradição não resolvida | referente ambíguo; corrupção de transcrição em nome, valor ou data |

`tipo_captura = inferido` é obrigatório sempre que o item não puder ser lido literalmente no `trecho_origem`; inferido com `confianca = baixa` entra no relatório como candidato, não como item.

## 5. Referente ambíguo e nome não confirmado (gatilhos)

Marcar como defeito (não corrigir, não escolher) quando o referente entra em cláusula, prazo ou cálculo e a fonte o deixou:
- **contraditório**: dois nomes para a mesma parte ("Agro Guimarães" e "Guimarães Agro"), dois valores para o mesmo item, duas datas para a mesma reunião;
- **corrompido**: transcrição fonética ("Jataí" grafado "Jatahy", "Funrural" grafado "fum rural") em posição decisiva;
- **elíptico**: pronome ou apelido sem antecedente claro ("ele assina", "o doutor vê") quando o antecedente decide quem executa;
- **numericamente instável**: "uns 2.400 ha", "mais ou menos R$ 1 milhão" quando o número vai para cálculo.
Fora dessas posições (narrativa, contexto), o referente ambíguo só recebe nota, não defeito.

## 6. Defeitos da ata (visão computada, não categoria)

Computar a partir dos campos, nesta ordem, sem duplicar:
1. Decisões órfãs: `categoria = decisao`, `requer_acao = true`, `responsavel_execucao = null`.
2. Ações sem prazo: `categoria = acao`, `prazo_literal = null`.
3. Ações com responsável ambíguo: `responsavel_ambiguo = true` (ação sem responsável nenhum já conta na decisão órfã de origem; se não houver decisão de origem, conta aqui como "ação sem dono").
4. Pendências sem encaminhamento: `categoria = pendencia`, `encaminhamento = null`.
5. Referentes ambíguos / nomes não confirmados: lista da seção 5 com o trecho de cada conflito.

O relatório de defeitos vem antes do resumo, porque é o produto que o resumo comum não entrega.

## 7. Saída mínima do `/ata`

1. Cabeçalho (metadados).
2. Defeitos da ata (seção 6).
3. Decisões, ações (agregadas por responsável pelo script), pendências, riscos, cada item com `trecho_origem` e `tipo_captura` visíveis.
4. Oferta dos passos a jusante: render (`layout-aem`, modo Interno), arquivamento (`destila`), plano de trabalho (`mestre-de-obras`, `/plano macro`) quando a ata for de atendimento de cliente. Nenhum roda sozinho.
