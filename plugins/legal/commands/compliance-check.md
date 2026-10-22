---
description: Verificação de compliance sobre uma ação proposta, operação ou iniciativa de negócio
argument-hint: "<ação ou iniciativa para verificar>"
---

# /compliance-check -- Verificação de Compliance

> Consulte [CONNECTORS.md](../CONNECTORS.md) para ver as ferramentas conectadas.

Executa verificação de compliance sobre uma ação proposta, operação, campanha de marketing ou iniciativa de negócio no contexto do agronegócio brasileiro.

**Importante**: Este comando auxilia nos fluxos de trabalho jurídico. Avaliações de compliance devem ser revisadas pelos advogados do escritório.

## Uso

```
/compliance-check $ARGUMENTS
```

## O que preciso de você

Descreva o que está planejando fazer. Exemplos:
- "Queremos lançar um programa de indicação com bonificação para produtores"
- "Vamos compartilhar dados de clientes com uma fintech para crédito rural"
- "O produtor quer transferir a fazenda para uma holding sem incidência de ITBI"
- "Precisamos enviar comunicação em massa via WhatsApp para clientes"
- "O cliente quer emitir CPR financeira registrada em cartório"
- "Estamos estruturando um FIAGRO com terras de clientes"

## Output

```markdown
## Verificação de Compliance: [Iniciativa]

### Resumo
[Avaliação rápida: Prosseguir / Prosseguir com condições / Requer análise aprofundada]

### Legislação e Normas Aplicáveis
| Legislação/Norma | Relevância | Requisitos-Chave |
|-------------------|-----------|-----------------|
| [LGPD / Código Florestal / Estatuto da Terra / CTN / IN RFB / etc.] | [Como se aplica] | [O que precisa ser feito] |

### Requisitos
| # | Requisito | Status | Ação Necessária |
|---|-----------|--------|---------------|
| 1 | [Requisito] | [Atendido / Não Atendido / A Verificar] | [O que fazer] |

### Áreas de Risco
| Risco | Severidade | Mitigação |
|------|----------|------------|
| [Risco] | [Alto/Médio/Baixo] | [Como endereçar] |

### Ações Recomendadas
1. [Ação mais importante]
2. [Segunda prioridade]
3. [Terceira prioridade]

### Aprovações Necessárias
| Aprovador | Motivo | Status |
|----------|-----|--------|
| [Sócio/Equipe] | [Razão] | [Pendente] |

### Análise Adicional Recomendada
[Áreas onde revisão de sócio ou especialista externo é aconselhada]
```

## Dicas

1. **Seja específico** — "Queremos enviar e-mail marketing para todos os produtores cadastrados" é melhor que "campanha de marketing."
2. **Inclua a jurisdição** — Requisitos variam por estado e município (ICMS, ITCMD, legislação ambiental estadual).
3. **Mencione os dados envolvidos** — Quais dados pessoais estão envolvidos? Isso direciona a maior parte dos requisitos de compliance (LGPD).
4. **Contextualize a operação** — Informe se envolve PF ou PJ, tipo de cultura/atividade, valores envolvidos quando possível.
