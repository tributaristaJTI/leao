# Publicar · entregavel-cliente

Origem: `skills/entregavel-cliente/` no repositório tributaristaJTI/leao. Versão sincronizada de referência: atualizada na conta em 2026-04-06.

## 1. SKILL.md completa e final

`````markdown
---
name: entregavel-cliente
description: "Skill transversal para formatação de entregáveis ao cliente. Use SEMPRE que o usuário mencionar 'entregável', 'documento para o cliente', 'formatar para o cliente', 'relatório para o produtor', 'apresentar os cenários', 'montar o documento de decisão', 'relatório executivo', ou qualquer variação de pedido para transformar uma análise técnica em material de decisão para o cliente leigo. Também acione quando o usuário disser 'agora formata isso pro cliente', 'monta o documento final', 'prepara pra mandar pro cliente'. Funciona de forma independente — pode ser acionada com análise já feita em outro módulo ou em outro Project."
---

# Entregável para Cliente — Documento de Decisão

Skill que transforma a análise técnica do planejamento tributário em um documento de decisão acessível ao produtor rural. O objetivo é que o cliente entenda as opções, compare os números e tome a decisão informada — sem precisar ser jurista.

## Princípio

O produtor rural é um empresário sofisticado no que faz, mas não é especialista em tributação. O entregável deve tratar o cliente com respeito intelectual — sem ser paternalista, mas sem exigir conhecimento jurídico. A regra é: se o produtor precisar perguntar o que uma palavra significa, o documento falhou.

## Estrutura do entregável

Todo documento de decisão segue esta estrutura. Seções podem ser comprimidas ou expandidas conforme a complexidade, mas a ordem é fixa.

### 1. Resumo da Situação (máximo 1 página)

Em linguagem simples, explique:
- O que o cliente está fazendo ou pretende fazer (vender fazenda, reestruturar operação, etc.)
- Qual a questão tributária envolvida
- O que o escritório analisou

Exemplo de tom: "O senhor está vendendo a Fazenda Boa Esperança. Essa venda gera um imposto chamado Ganho de Capital. Nosso trabalho foi calcular quanto o senhor paga de imposto e encontrar a forma legal de pagar menos."

### 2. Cenário sem Planejamento

O "quanto custa se não fizer nada". Destaque visual (caixa vermelha ou bordas em destaque). Inclua:
- Valor do imposto em reais
- Tradução para referência do produtor: sacas de soja, hectares, fração de safra
- Breve explicação de como se chega a esse valor (sem fórmulas — com analogias)

### 3. Cenário com Planejamento

O resultado otimizado. Destaque visual (caixa verde). Inclua:
- Valor do imposto com planejamento
- Economia obtida em reais
- Tradução para referência do produtor
- Explicação acessível do que muda (sem jargão jurídico)

### 4. Quadro Comparativo de Cenários

Tabela limpa e visual com todos os cenários analisados. Colunas:

| Elemento | Cenário A (nome descritivo) | Cenário B (nome descritivo) | Cenário C (se houver) |
|----------|---------------------------|---------------------------|----------------------|
| Descrição do caminho | ... | ... | ... |
| Imposto a pagar | R$ ... | R$ ... | R$ ... |
| Economia vs pior cenário | — | R$ ... | R$ ... |
| Risco | Baixo/Moderado/Alto | ... | ... |
| Prazo de implementação | ... | ... | ... |
| Complexidade | Simples/Média/Alta | ... | ... |

A última linha deve ser "Recomendação do escritório" com destaque visual no cenário indicado.

### 5. Recomendação Fundamentada

Em linguagem acessível:
- Qual caminho o escritório recomenda e por quê
- O que acontece se o cliente não seguir a recomendação (cenário de inação, quantificado)
- Quais premissas sustentam a recomendação (para o cliente entender que a análise depende de certos dados serem verdadeiros)

Tom: firme mas respeitoso. O escritório se posiciona — não joga a decisão inteira no colo do cliente.

### 6. Próximos Passos

Lista visual e objetiva:

| Passo | O que precisa ser feito | Quem faz | Prazo sugerido |
|-------|------------------------|----------|----------------|
| 1 | ... | Cliente / Escritório / Contador | ... |
| 2 | ... | ... | ... |

### 7. Riscos e Cuidados (caixa de alerta)

Formatação: caixa com borda lateral em vermelho/laranja. Linguagem direta:
- O que pode dar errado
- O que o cliente NÃO deve fazer (ex: declarar valor diferente do contrato, omitir informação)
- O que depende de terceiros (Receita Federal, cartório, banco)

### 8. Anexo Técnico (opcional)

A fundamentação completa — legislação, jurisprudência, cálculos detalhados — fica como anexo para quem quiser consultar. Não polui o corpo principal. Este anexo pode ser o próprio parecer consultivo gerado pelo módulo analítico, referenciado no entregável.

## Formatação do documento

Gerar .docx com identidade visual da Amaral e Melo (conforme protocolo no system prompt do projeto). Elementos adicionais específicos do entregável:

**Caixas de destaque:**
- Cenário sem planejamento: fundo vermelho claro (#FFF0F0), borda esquerda vermelha (#C0392B)
- Cenário com planejamento: fundo verde claro (#F0FFF0), borda esquerda verde (#27AE60)
- Alertas: fundo amarelo claro (#FFF9E6), borda esquerda laranja (#E67E22)
- Recomendação: fundo azul claro (#F0F5FF), borda esquerda azul marinho (#1D3D69)

**Tabelas:**
- Cabeçalho com fundo azul marinho (#1D3D69), texto branco
- Linhas alternadas em cinza claro (#F5F5F5) e branco
- Célula da recomendação com fundo dourado claro (#FFF8EE)

**Página de rosto (primeira página):**
- Logo/nome do escritório
- Título: "RELATÓRIO DE PLANEJAMENTO TRIBUTÁRIO"
- Subtítulo com o nome do cliente e tipo de operação
- Data
- "CONFIDENCIAL — ELABORADO PARA [NOME DO CLIENTE]"

## Modos de entrada

### Com análise já pronta
O usuário cola ou referencia uma análise feita neste ou em outro Project. O agente extrai os dados, cenários e recomendações e reformata no padrão do entregável.

### Com dados brutos
O usuário fornece os dados do caso e os cenários informalmente. O agente estrutura no formato do entregável, sinalizando onde faltam informações.

### Pós-módulo analítico
Fluxo natural: o usuário rodou um módulo analítico (ex: IR Venda de Imóvel), validou os cenários, e agora pede para formatar o entregável. O agente puxa os dados da conversa atual e gera o documento.

## Regras

1. Nunca use jargão jurídico no corpo principal sem tradução imediata. Termos técnicos ficam no anexo.
2. A tradução para sacas/hectares é obrigatória em todos os valores relevantes. Use a cotação da soja informada pelo usuário ou, na ausência, a cotação vigente pesquisada na web.
3. Todo cenário deve ter o grau de risco explícito (Baixo, Moderado, Alto).
4. O cenário de inação (o que acontece se não fizer nada) é obrigatório.
5. Se a análise ainda não foi validada pelo usuário, sinalize que o entregável é preliminar.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
`````

## 2. O que mudou desde a versão sincronizada

Nova seção final "Conferência de citação", com texto idêntico nas 22 skills que citam norma ou julgado (laudo de 03/10, decisão 3).
Regra: dispositivo, súmula, julgado, alíquota ou prazo só entra no texto conferido no Jusratio ou em fonte oficial consolidada, na própria sessão.
O que não for conferido fica fora ou marcado [A CONFERIR: fonte].
Memória, arquivo de referência embarcado e trecho de busca servem para localizar, nunca para afirmar. Inclusão aprovada por Leonardo em 22/10 (pendente 6).
Nenhuma outra linha mudou.
