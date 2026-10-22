---
description: Preparar e rotear documento para assinatura eletrônica
argument-hint: "<documento ou contrato para enviar>"
---

# /signature-request -- Roteamento de Assinatura Eletrônica

> Consulte [CONNECTORS.md](../CONNECTORS.md) para ver as ferramentas conectadas.

Prepara um documento para assinatura eletrônica — verifica completude, define ordem de assinatura e roteia para execução via Clicksign.

**Importante**: Este comando auxilia nos fluxos de trabalho jurídico, mas não substitui a análise de um advogado. Verifique se o documento está em sua versão final antes de enviar para assinatura.

## Uso

```
/signature-request $ARGUMENTS
```

Preparar para assinatura: @$1

## Workflow

### Passo 1: Receber o Documento

Aceitar o documento em qualquer formato:
- **Upload de arquivo**: PDF, DOCX
- **URL**: Link para documento no Google Drive
- **Referência**: "O contrato de arrendamento da Fazenda São José que finalizamos ontem"

### Passo 2: Checklist Pré-Assinatura

Antes de rotear para assinatura, verificar:

```markdown
## Checklist Pré-Assinatura

- [ ] Documento em versão final (sem pendências de revisão)
- [ ] Todos os anexos e cronogramas estão incluídos
- [ ] Nomes corretos das partes nos blocos de assinatura (nome completo, CPF/CNPJ)
- [ ] Datas corretas ou em branco para data de execução
- [ ] Blocos de assinatura correspondem aos signatários autorizados
- [ ] Aprovações internas necessárias foram obtidas
- [ ] Documento revisado pelo advogado responsável
- [ ] Testemunhas identificadas (quando necessário)
```

### Passo 3: Configurar Assinatura

Coletar detalhes da assinatura:
- **Signatários**: Quem precisa assinar? (nomes, e-mails, CPF/CNPJ, cargos)
- **Ordem de assinatura**: Sequencial ou simultânea?
- **Aprovação interna**: Alguém precisa aprovar antes da contraparte assinar?
- **Testemunhas**: Quem serão as testemunhas? (2 testemunhas obrigatórias para contratos no Brasil)
- **Cópia para**: Quem deve receber cópia do documento assinado?

### Passo 4: Rotear para Assinatura

**Se Clicksign estiver conectado:**
- Criar o envelope/solicitação de assinatura na Clicksign
- Configurar campos de assinatura e ordem
- Adicionar campos de rubrica ou data quando necessário
- Enviar para assinatura

**Se não estiver conectado:**
- Gerar documento de instruções de assinatura
- Fornecer o documento formatado para assinatura presencial ou envio manual pela Clicksign
- Listar todos os signatários com informações de contato

## Output

```markdown
## Solicitação de Assinatura: [Título do Documento]

### Detalhes do Documento
- **Tipo**: [Contrato de Arrendamento / Parceria Agrícola / Compra e Venda / Procuração / NDA / etc.]
- **Partes**: [Parte A] e [Parte B]
- **Páginas**: [X]

### Verificação Pré-Assinatura: [APROVADO / PENDÊNCIAS ENCONTRADAS]
[Listar pendências que precisam de atenção antes do envio]

### Configuração de Assinatura
| Ordem | Signatário | E-mail | CPF/CNPJ | Função |
|-------|-----------|--------|----------|--------|
| 1 | [Nome] | [email] | [CPF/CNPJ] | [Signatário Parte A] |
| 2 | [Nome] | [email] | [CPF/CNPJ] | [Signatário Parte B] |

### Testemunhas
| Nome | E-mail | CPF |
|------|--------|-----|
| [Nome] | [email] | [CPF] |
| [Nome] | [email] | [CPF] |

### Cópia Para
- [Nome] — [email]

### Status
[Enviado para assinatura / Pronto para enviar / Pendências a resolver]

### Próximos Passos
- [O que esperar após o envio]
- [Prazo estimado para conclusão]
- [Acompanhamento se não assinado em X dias]
```

## Dicas

1. **Verifique os nomes das partes** — O erro mais comum é o nome incorreto das entidades ou CPF/CNPJ errado no bloco de assinatura.
2. **Confirme a autoridade** — Certifique-se de que cada signatário tem poderes para vincular sua organização (verificar contrato social/procuração).
3. **Testemunhas** — No Brasil, contratos requerem duas testemunhas para constituir título executivo extrajudicial (art. 784, III, CPC).
4. **Arquive uma cópia** — Documentos assinados devem ser arquivados imediatamente no Google Drive na pasta do cliente.
