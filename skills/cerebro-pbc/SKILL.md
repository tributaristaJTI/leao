---
name: cerebro-pbc
description: "Estuda um corpo normativo e mapeia as interpretações possíveis pelo Percurso Gerativo de Sentido (S1→S4) de Paulo de Barros Carvalho, ranqueadas por defensabilidade. Use para ESTUDAR um recorte da reforma (tema, capítulo, conjunto de dispositivos) ou uma questão interpretativa aberta — 'estudar a reforma', 'mapear as interpretações de', 'quais as leituras possíveis de', 'levantar as controvérsias de', 'modo corpus'. NÃO é a regra-matriz (que decompõe UMA norma) — esta orquestra MUITAS e a chama como motor; NÃO é parecer de operação concreta (tributarista-consultivo) nem contencioso. Arquiva via destila."
---

# Cérebro PBC — Estudo Interpretativo de um Corpo Normativo

Aplica o Percurso Gerativo de Sentido (S1→S4) a um recorte de corpus e produz o mapa das leituras concorrentes, ranqueado por defensabilidade. Não reimplementa o método: chama a `regra-matriz` como motor por norma.

## Método (fidelidade)

Percurso = 4 planos: S1 literalidade → S2 proposições isoladas → S3 significações normativas (RMIT) → S4 sistematização. Dois princípios inegociáveis:
- **A norma é montada, não lida:** nenhuma norma completa mora num dispositivo; S3 reúne proposições dispersas — por isso exige o corpus inteiro em contexto.
- **Os planos se interpenetram:** S1→S4 é didático, não linear; S3 volta a S1/S2. A divisão em blocos abaixo é de custo, não de doutrina.

## Operação — dois pontos de entrada

A skill estrutura o raciocínio; NÃO troca o modelo (roteamento é manual).
- **completo** (padrão): Base → Bloco 1 → Bloco 2 → arquivamento, numa passada (ideal no modelo de maior capacidade disponível). Estudo pontual.
- **dividido** (varredura de muitos dispositivos): `parar-após-extração` devolve o artefato destilado; `retomar` recebe o artefato e roda Bloco 2 → arquivamento (chat novo com o modelo de maior capacidade disponível, mesmo Project).

Sem indicação, assuma `completo`.

## Base (infra — não é plano)

**Etapa 0:** consultar o acervo (teses + `posicoes-la`) — construir sobre o que já existe; registrar o que fica em aberto.
**Corpus fixo (cachear no Project):** EC 132/2023, LC 214/2025, LC 227/2026, RCBS (Dec. 12.955/2026), Res. CGIBS 6/2026, LC 224/2025, legislação estadual (CTE/RCTE-GO).
**Calibragem (perguntar uma vez):** parecer (denso, citação completa) ou didático (IBET/AGET, exemplos do agro)?

## Bloco 1 — Extração (modelo barato / batch)

S1 + camada mecânica de S2. Matéria-prima; não decide.
- **S1:** mapear os dispositivos do recorte (justificativa breve) e transcrever enunciados centrais + remissões + definições legais. Não confirmável → "⚠️ verificar contra texto oficial".
- **S2 mecânico:** glossário das significações não-controversas com fundamento. NÃO resolve ambiguidade — marca cada termo polissêmico como bifurcação candidata.

**Artefato destilado (saída):** (1) índice de enunciados + localizador; (2) glossário; (3) bifurcações candidatas marcadas.

## Bloco 2 — Construção (modelo de maior capacidade disponível, recursivo)

Roda S2-bifurcações + S3 + S4 como um só raciocínio, com o corpus em contexto; volta ao texto/Bloco 1 quando preciso.
- **S2-bifurcações:** construir as significações concorrentes de cada termo marcado, com fundamento (distinguir conceito de direito privado absorvido vs. autônomo — arts. 109/110 CTN).
- **S3-articulação:** para cada bifurcação, reunir do corpus os enunciados que compõem a norma e **chamar a `regra-matriz` em modo bifurcação** para montar a RMIT de cada leitura. Registrar bifurcação de articulação (normas distintas dos mesmos enunciados) + tabela de divergência (qual critério muda).
- **S4-sistematização:** coordenar cada leitura contra Constituição (art. 156-A/195,V), arquitetura da LC 214, normas de mutilação (isenção, redução, imunidade de exportação, diferimento art. 138), regimes especiais (produtor PF, imobiliário, cooperativa, exportação indireta, transição), antinomias. **Ranquear por defensabilidade** (com Posição LA quando houver, mantendo neutralidade). Isolar a **zona cinzenta residual**.

## Arquivamento (pós — não é plano)

Acionar a `destila` com a tese vencedora + bifurcações → nota canônica. A `destila` confirma antes de gravar; esta skill sugere, não grava. Fecha o ciclo: alimenta a Etapa 0 do próximo estudo.

## Regras

1. **Ancoragem:** leitura só entra no mapa se prende-se a texto (S1) e sobrevive ao teste sistêmico (S4). O que não ancora é descartado, não "considerado".
2. **Não inventar dispositivos;** "[verificar]" > citar errado.
3. **Distinguir certeza de interpretação** (texto expresso / doutrina / analista).
4. **Cada RMIT é autônoma** (múltiplos fatos → múltiplas RMITs).
5. **Self-review:** artigos corretos? material coerente com base de cálculo? remissões completas? ranqueamento fundamentado?

## Saída — o mapa

Ordem: (0) o que o acervo resolve → (1) bifurcações (semânticas + de articulação) → (2) RMITs concorrentes + tabela de divergência → (3) ranqueamento por defensabilidade → (4) zona cinzenta.
Parecer: denso, citação completa. Didático: cada etapa explicada, exemplos do agro.

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
