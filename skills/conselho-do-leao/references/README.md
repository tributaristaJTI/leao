# References — Conselho do Leão

Arquivos de contexto por fase do protocolo de decisão. Cada arquivo contém as instruções detalhadas que o SKILL.md referencia.

## Arquivos necessários

| Arquivo | Conteúdo | Origem |
|---------|----------|--------|
| `fase-1-definicao-problema.md` | Protocolo de enquadramento do problema real | Project "CEO do Leão" / Clear Thinking |
| `fase-2-diagnostico-defaults.md` | Checklist dos 4 defaults cognitivos | Project "CEO do Leão" / Clear Thinking |
| `fase-3-exploracao-solucoes.md` | Técnicas de geração divergente de alternativas | Project "CEO do Leão" / Clear Thinking |
| `fase-4-avaliacao-stress-test.md` | Matriz de avaliação e stress test das opções | Project "CEO do Leão" / Clear Thinking |
| `fase-5-registro-acompanhamento.md` | Template do Diário de Decisão e loop de revisão | Project "CEO do Leão" / Clear Thinking |
| `exemplo-protocolo-completo.md` | Caso fictício rodando as 6 fases (few-shot calibrador) | Project "CEO do Leão" |

## Instruções de migração

1. Abra o Project "Pensamento Eficaz / Clear Thinking" ou "CEO do Leão" no claude.ai
2. Copie o conteúdo de cada arquivo de fase para o arquivo correspondente nesta pasta
3. Se os arquivos originais tiverem referências a "Project Knowledge", substitua por "registros locais"
4. Se tiverem referências a "salve neste Project", substitua pela instrução de salvar em arquivo `.md`

## Peso de contexto

Todos estes arquivos carregam quando a skill é acionada. Mantenha cada um abaixo de 300 linhas para não estourar o contexto — o SKILL.md já tem ~180 linhas.
