# Publicar · plugin ecossistema-do-leao (v0.1.0)

Origem: `plugins/ecossistema-do-leao/` no repositório tributaristaJTI/leao. Plugin carregado pela conta ("My Uploads"), não skill avulsa: o cartão de proposta do chat não se aplica. A atualização é um novo envio do plugin pelo mesmo caminho por onde ele entrou [A CONFERIR: tela de plugins da conta em claude.ai]. Os demais arquivos do plugin não mudaram; enviar a pasta inteira de `plugins/ecossistema-do-leao/`, sem o arquivo `.in_use`, que é marcador de execução local.

## 1. Arquivos alterados, completos e finais

### `skills/marca-raro/SKILL.md`

`````markdown
---
name: marca-raro
description: >
  Skill de DNA de marca e conteúdo para o ecossistema Amaral e Melo + Agricompany. Use SEMPRE
  que o usuário mencionar "post LinkedIn", "conteúdo", "posicionamento", "marca", "tom de voz",
  "comunicação", "texto institucional", "Instagram", "WhatsApp marketing", "palestra",
  "marca RARO", "como comunicar", "rascunhar post", "criar conteúdo", "estratégia de conteúdo",
  ou qualquer variação de produção de conteúdo público ou posicionamento de marca.
version: 0.1.0
---

# DNA de Marca — Conceito RARO

Skill de conteúdo e posicionamento para Leonardo Amaral e o ecossistema Amaral e Melo + Agricompany.

## Conceito Central: Ser RARO

RARO não é "diferente". É criar uma categoria própria em vez de competir dentro de uma existente. O escritório que só compete por preço e volume está na vala comum. O RARO cria um jogo que só ele joga.

Lema: **"Quem tem planejamento tem futuro; quem não tem, tem destino."**

## Público-Alvo

- **Produtores rurais**: Famílias sojicultoras, pecuaristas, produtores de milho no cerrado — pragmáticos, desconfiados de juridiquês, valorizam resultado concreto
- **Contadores do agro**: Parceiros técnicos, precisam de conteúdo que os ajude a enxergar valor no jurídico
- **Advogados tributaristas**: Pares que acompanham Leonardo como referência técnica
- **Mercado institucional**: IBET, AGET-Agro, sindicatos rurais, cooperativas

## Tom de Voz por Canal

### LinkedIn (principal canal de posicionamento)

**Formato obrigatório:**
- Máximo 1.300 caracteres
- Gancho forte na primeira linha (dado surpreendente, provocação, pergunta retórica, afirmação contraintuitiva)
- Uma ideia por post — não misturar temas
- Sem hashtags genéricas (no máximo 2-3 específicas se essencial)
- Fechar com reflexão ou provocação — nunca com CTA genérico tipo "Comente aqui"
- Parágrafos curtos (1-2 frases)
- Espaçamento entre parágrafos para leitura mobile

**Tom**: Firme, direto, com autoridade técnica mas sem pedantismo. Acessível sem ser simplista. Provocativo sem ser arrogante.

**O que funciona:**
- Casos reais anonimizados com lição prática
- Dados concretos + insight ("O produtor rural paga em média X% de IR. Mas se ele soubesse que...")
- Quebra de mitos tributários do agro
- Bastidores do escritório (humaniza sem banalizar)
- Reflexões sobre liderança e gestão com referências estoicas

**O que NÃO fazer:**
- Posts genéricos tipo "5 dicas para..." (comoditiza)
- Elogios próprios ou humblebragging
- Juridiquês denso sem tradução
- Hashtags estilo #sucesso #empreendedorismo #agro
- Começar com "É com grande alegria que..." ou "Hoje gostaria de compartilhar..."

### WhatsApp (comunicação com produtores)

**Tom**: Próximo, profissional, direto. Uma ideia por mensagem. Zero juridiquês.

**Formato**: Mensagens curtas. Se precisar de mais contexto, use áudio ou link para documento.

### Instagram (institucional)

**Tom**: Visual, didático, acessível. Carrosséis com dados e gráficos simples. Reels curtos com provocações.

### Palestras e Aulas (IBET, AGET, painéis)

**Tom**: Acadêmico-didático. Narrativa pedagógica com exemplos práticos do agro para ilustrar conceitos tributários densos. Pense na jornada do aluno.

## Referências Intelectuais para Analogias

Usar quando couber — nunca forçar:

- **Shane Parrish**: Modelos mentais, inversão, pensamento de segunda ordem
- **Brendon Burchard**: Alta performance, clareza, energia, necessidade, coragem
- **Angela Duckworth**: Grit, perseverança deliberada
- **Estoicismo** (Marco Aurélio, Sêneca, Epicteto): Foco no que depende de nós, amor fati, obstáculo como caminho
- **Ryan Holiday**: O ego é seu inimigo, obstáculo é o caminho
- **Jim Collins**: Nível 5, conceito do porco-espinho, volante
- **Simon Sinek**: Jogo infinito, comece pelo porquê

## Temas Recorrentes de Conteúdo

1. **IR na atividade rural** — zona de expertise máxima, livro publicado
2. **Planejamento tributário no agro** — economia real, caso prático
3. **Planejamento sucessório** — preservar patrimônio, governança familiar
4. **Gestão e mentalidade do produtor rural** — Agricompany, profissionalização
5. **Reforma tributária e agro** — IBS/CBS, impacto no produtor
6. **Liderança e gestão de escritório** — Ecossistema do Leão, formar RAROs
7. **Filosofia estoica aplicada ao negócio** — disciplina, antifragilidade

## Anti-Padrões de Conteúdo

- As proibições globais de estilo (consultoria e coaching, reformulação como insight, disclaimer óbvio, excesso de tópicos e as demais): lista completa, com exemplos e testes, na skill `voz-autoral-leonardo`, seção "Proibições globais de estilo"
- Posts longos demais (LinkedIn mobile = atenção curta)

## Recursos Adicionais

- **`references/exemplos-posts.md`** — Exemplos de posts LinkedIn no tom certo
- **`references/calendario-temas.md`** — Calendário temático sugerido
`````

### `commands/pipeline.md`

`````markdown
---
description: Visão rápida do pipeline comercial do escritório e da Agricompany
---

# /pipeline — Pipeline Comercial

Gerar visão consolidada do pipeline comercial da Amaral e Melo Advogados e da Agricompany.

## Instruções

Ler os quadros do Monday pelo conector como fonte dos números do funil, das propostas, dos fechamentos e das indicações. O que não estiver no Monday, ou se o conector não estiver disponível, perguntar a Leonardo. Estruturar o output independentemente.

## Output

```
## Pipeline Comercial — [Data]

### Amaral e Melo Advogados

#### Funil de Vendas
| Etapa | Quantidade | Valor Estimado |
|-------|-----------|----------------|
| Leads (contatos iniciais) | [X] | — |
| Reunião agendada | [X] | — |
| Proposta enviada | [X] | R$ [X] |
| Em negociação | [X] | R$ [X] |
| Fechado (mês atual) | [X] | R$ [X] |
| Perdido (mês atual) | [X] | R$ [X] |

#### Por Tipo de Produto
| Produto | Propostas | Fechamentos | Taxa |
|---------|----------|-------------|------|
| Recuperação Judicial | [X] | [X] | [X]% |
| Transação Tributária | [X] | [X] | [X]% |
| Planejamento Tributário | [X] | [X] | [X]% |
| Reestruturação Societária | [X] | [X] | [X]% |
| Contratos recorrentes | [X] | [X] | [X]% |

#### Indicações
- Indicações recebidas no mês: [X]
- Convertidas em proposta: [X]
- Fechadas: [X]
- Fonte principal: [quem indicou mais]

### Agricompany

#### Funil
| Etapa | Famílias |
|-------|---------|
| Lead / interesse | [X] |
| Diagnóstico agendado | [X] |
| Diagnóstico realizado | [X] |
| Proposta de programa | [X] |
| Em mentoria ativa | [X] |

#### Métricas
- Ticket médio por família/mês: R$ [X]
- Taxa de conversão diagnóstico → programa: [X]%
- Renovações previstas: [X]

### Análise Rápida
[2-3 frases sobre o que está funcionando, o que preocupa, e 1 ação sugerida]

### Lente RARO
[Os novos casos estão posicionando o escritório como categoria única ou estamos competindo por preço?]
```

## Tom
Números primeiro, análise depois. Direto e visual. Se faltar dados, indicar o que está faltando sem inventar.
`````

### `commands/meu-dia.md`

`````markdown
---
description: Briefing matinal — agenda, prioridades, pendências e prazos críticos
---

# /meu-dia — Briefing Matinal do CEO

Gerar o briefing matinal de Leonardo Amaral como CEO/fundador da Amaral e Melo e Agricompany.

## Fontes para Consultar

**Google Calendar (se conectado):**
- Reuniões de hoje e amanhã
- Quais precisam de preparação (negociação, reunião de sócios, mentoria Agricompany)
- Conflitos de agenda

**Gmail (se conectado):**
- E-mails não respondidos que precisam de ação
- Comunicações de sócios (Leandro, Thiago, Ricardo)
- Mensagens de clientes Top 10
- Notificações relevantes (prazos judiciais, fiscais)

**Notion (se conectado):**
- Tarefas pendentes atribuídas a Leonardo
- Projetos com prazo próximo
- Decisões pendentes de governança

**Monday (se conectado):**
- Quadros do Monday: tarefas, prazos e pendências de casos e projetos, inclusive as atribuídas a Leonardo e aos sócios

**Se fontes não estiverem conectadas:**
- Perguntar diretamente o que Leonardo tem na agenda e quais são as pendências
- Estruturar o output mesmo com informação parcial

## Output

```
## Bom dia, Leonardo — [Data]

### Agenda de Hoje
[Lista das reuniões do dia com horário e o que preparar para cada uma]

### Top 3 Prioridades
1. [Ação mais importante — por quê]
2. [Segunda prioridade]
3. [Terceira prioridade]

### Pendências de Sócios
- Leandro: [pendência, se houver]
- Thiago: [pendência, se houver]
- Ricardo: [pendência, se houver]

### Prazos Críticos (7 dias)
[Prazos judiciais, fiscais ou comerciais que vencem em até 7 dias]

### Agricompany
[Mentorias agendadas, diagnósticos pendentes, follow-ups necessários]

### Provocação do Dia
[Uma frase estoica ou de referência intelectual para começar o dia com intenção]
```

## Tom
Direto, executivo, sem floreios. O objetivo é que Leonardo leia em 2 minutos e saiba exatamente o que priorizar.
`````

### `commands/pauta-socios.md`

`````markdown
---
description: Montar pauta para reunião de sócios a partir de pendências e agenda
argument-hint: "[data da reunião ou 'próxima']"
---

# /pauta-socios — Pauta de Reunião de Sócios

Montar pauta estruturada para reunião do Coração do Leão (governança de sócios da Amaral e Melo).

## Participantes Fixos
- **Leonardo Amaral** — Cofundador, Guardião do Clube do Leão (Clientes)
- **Leandro Amaral** — Cofundador, Guardião da Garra do Leão (Produtos)
- **Thiago Amaral** — Sócio, Guardião da Forja do Leão (Pessoas)
- **Ricardo Assis** — Sócio de serviço (sócio-gestor), Guardião do Território do Leão (Infraestrutura)

## Fontes para Consultar

**Google Calendar**: Quando é a próxima reunião de sócios
**Gmail**: Temas pendentes entre sócios, decisões adiadas
**Notion**: Ações pendentes de reuniões anteriores, projetos em andamento
**Monday**: Quadros do Monday com ações pendentes e status de casos e projetos

Se fontes não estiverem conectadas, perguntar a Leonardo quais temas precisa incluir.

## Estrutura da Pauta

```
## Pauta — Reunião de Sócios [Data]

### 1. Abertura e Aprovação da Pauta (5 min)

### 2. Ações Pendentes da Reunião Anterior
| Ação | Responsável | Status |
|------|------------|--------|
| [ação] | [quem] | [concluído/pendente/em andamento] |

### 3. Painel por Dimensão (20 min)

**GARRA (Leandro)** — Produtos e receita
- [Temas para Leandro reportar]

**CLUBE (Leonardo)** — Clientes e relacionamento
- [Temas para Leonardo reportar]

**FORJA (Thiago)** — Pessoas e capacitação
- [Temas para Thiago reportar]

**TERRITÓRIO (Ricardo)** — Operações e infra
- [Temas para Ricardo reportar]

### 4. Decisões Necessárias
| Decisão | Contexto | Opções |
|---------|---------|--------|
| [decisão] | [contexto breve] | [opção A / opção B] |

### 5. Temas Estratégicos (15 min)
[Temas de longo prazo que precisam de discussão: expansão, novos produtos, contratações, Agricompany]

### 6. Agricompany — Ponto de Situação (10 min)
[Status dos 4 pilares, pipeline, próximas mentorias]

### 7. Próximos Passos e Encerramento (5 min)
[Resumo de decisões e novas ações com responsável e prazo]
```

## Regras
- Cada item da pauta deve ter tempo estimado
- Decisões devem vir com opções concretas (não "discutir sobre X")
- Ações da reunião anterior devem ser cobradas — não deixar passar
- Tom: executivo, objetivo
`````

## 2. O que mudou desde a versão sincronizada

`/pipeline`: os números do funil, das propostas, dos fechamentos e das indicações passam a vir dos quadros do Monday pelo conector; o que faltar, perguntar a Leonardo (decisão 5).
`/meu-dia`: novo bloco de fonte "Monday (se conectado)", com tarefas, prazos e pendências de casos e projetos.
`/pauta-socios`: nova linha de fonte "Monday", com ações pendentes e status de casos e projetos.
`marca-raro`: em "Anti-Padrões de Conteúdo", os quatro itens repetidos da lista global de estilo viram remissão à `voz-autoral-leonardo` (decisão 8); fica o item próprio de marca.
Versão no `plugin.json` mantida em 0.1.0 [decisão de Leonardo: subir para 0.2.0 no envio].
