# ESQUEMA CANÔNICO — NOTA DO ACERVO (Amaral e Melo)
#
# Molde operativo executado pela skill destila. Cópia legível e de governança vive na raiz
# do acervo no Drive — manter as duas em sincronia quando o vocabulário crescer por decisão.
#
# Formato único para duas naturezas de nota, distinguidas por `tipo`:
#   - destilacao-propria        → destilação de peça produzida pelo escritório
#   - precedente-jurisprudencial → captura de decisão externa (CARF, STJ, STF, TJ) para reuso
#
# O corpo (Tese / Fundamento / Âncoras / Exceções / Desfecho) é idêntico para ambos.
# A única diferença estrutural está marcada como [SÓ PRECEDENTE].
# Separação durável/volátil é estrutural: o que compõe e envelhece bem fica nas seções DURÁVEL;
# o que decai (dispositivo, estado da lei) fica isolado nas Âncoras, sob rótulo de verificação.
#
# Markdown puro, sem timbre — infraestrutura de recuperação, não entregável a cliente.

---
# ===== FRONTMATTER (metadados parseáveis pela recuperação) =====

tema:            # OBRIGATÓRIO. Matéria + recorte concreto, em uma linha.
materia:         # OBRIGATÓRIO. Vocabulário controlado (ver apêndice). Um valor.
tipo:            # OBRIGATÓRIO. destilacao-propria | precedente-jurisprudencial
natureza:        # OBRIGATÓRIO. consultivo-preventivo | contencioso
tags:            # OBRIGATÓRIO. Lista do vocabulário controlado (ver apêndice).
  - 
  - 
data-emissao:    # OBRIGATÓRIO. Data do arquivamento da nota (AAAA-MM-DD).
peca-fonte:      # destilacao-propria → ID/link da peça no Drive. precedente → deixar vazio (usar bloco abaixo).

# ----- [SÓ PRECEDENTE] preencher apenas quando tipo: precedente-jurisprudencial -----
polaridade:      # favoravel-ao-contribuinte | desfavoravel-ao-contribuinte | mista
orgao-julgador:  # ex.: CARF — 2ª Turma / 2ª Câmara / 2ª Seção
acordao:         # número do acórdão — NUNCA inventar; deixar [a preencher] se desconhecido
processo:        #
data-julgamento: # AAAA-MM-DD
relator:         #
# ------------------------------------------------------------------------------------
---

## Tese central
*(DURÁVEL — a jogada argumentativa)*
> Em 2 a 4 linhas: o que se sustenta e por quê, no nível da arquitetura — não do dispositivo.
> É o núcleo reaproveitável. Deve fazer sentido daqui a anos mesmo se a lei mudar.

## Fundamento nuclear
*(DURÁVEL — o enquadramento, a engrenagem)*
> A estrutura lógica do argumento: os eixos, a sequência, o porquê de funcionar.
> Aqui mora o que compõe entre uma peça e a próxima.

## Âncoras normativas ⚠ VERIFICAR ANTES DE CITAR
*(VOLÁTIL)*
`validade-verificada-em: não verificado no arquivamento — re-checar por busca web no reuso`
> Dispositivos, súmulas, temas repetitivos, soluções de consulta. Ponteiros, não verdades fixas.
> Sinalizar expressamente vetores de instabilidade conhecidos (reforma, lei alteradora, tese pendente).
> O ⚠ instrui quem reusa a re-checar; não promete manutenção da nota.

## Exceções e limites
*(DURÁVEL — onde a tese NÃO se aplica)*
> A fronteira da tese. No reuso preventivo, esta seção lida pelo avesso vira checklist do que
> precisa existir para a estrutura sobreviver. Frequentemente é a parte mais valiosa da nota.

## Desfecho / adoção
> destilacao-propria → onde a peça foi adotada/usada e resultado, se contencioso. (N/A no preventivo puro.)
> precedente → resultado do julgamento + votação (unânime ou voto de qualidade — confirmar no acórdão integral).

---

# ===== APÊNDICE — VOCABULÁRIO CONTROLADO (governança) =====
# Tagueamento livre por ~20 advogados fragmenta a recuperação. Esta lista é a fonte única.
# Cresce POR DECISÃO, não ad hoc. Tudo minúsculo, hífen, sem acento (robustez entre ferramentas).

# materia (eixo primário de recuperação; um valor por nota):
#   IR-rural | ICMS | ITCMD | Funrural | ITR | IBS-CBS | societario
#   (extensível por decisão conforme o acervo cresce)

# tipo:        destilacao-propria | precedente-jurisprudencial
# natureza:    consultivo-preventivo | contencioso
# polaridade:  favoravel-ao-contribuinte | desfavoravel-ao-contribuinte | mista

# tags — semente mínima, em três famílias (cresce por decisão):
#   figura/vício:    simulacao · fraude-fiscal · planejamento-abusivo · ausencia-de-substancia ·
#                    proposito-negocial · interposicao-de-pessoas
#   instituto/operação: parceria-rural · arrendamento · holding-rural · ganho-de-capital ·
#                    integralizacao · diferimento · credito-presumido · sucessao
#   penalidade/efeito:  multa-qualificada

# Exemplo vivo do tipo precedente-jurisprudencial:
#   IR-rural/parceria-rural-simulada-familiares-interpostas.md
