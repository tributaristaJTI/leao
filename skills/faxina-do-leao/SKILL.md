---
name: faxina-do-leao
description: >-
  Skill de organização dos arquivos locais do Mac do Leonardo (Desktop,
  Downloads e Documents), operando pela ponte com o computador (Cowork) ou em
  sessão rodando no próprio computador. Use SEMPRE que o usuário digitar
  /faxina, /faxina direto ou /faxina diagnostico, ou mencionar "organizar meus
  arquivos", "arruma o desktop", "limpa os downloads", "organiza as pastas do
  mac", "faxina nos arquivos", "meu mac tá uma bagunça", "coloca ordem nos
  arquivos", "onde foi parar aquele arquivo" (consultar relatórios), ou
  qualquer variação de pedido para varrer, classificar, renomear ou mover
  arquivos locais do computador. NÃO use para o acervo institucional no Google
  Drive (destila cuida disso) nem para organizar knowledge de projects. Regra
  inegociável: esta skill NUNCA apaga arquivo — classifica, nomeia, move e
  relata; na dúvida, move para _Para_Revisar.
---

# Faxina do Leão — organização dos arquivos do Mac

## Missão

Manter as zonas de entrada do Mac (Desktop e Downloads) vazias e os arquivos
navegáveis por cliente, com o mínimo de decisão humana por arquivo. O Leonardo
acha arquivo NAVEGANDO por pastas, não buscando por nome: a estrutura precisa
ser rasa (máx. 3 níveis), previsível e com ordenação estável. O Google Drive
segue sendo o acervo institucional do escritório — esta skill governa apenas a
bancada local e nunca replica nem toca a estrutura do Drive.

## Princípios (por que as regras são como são)

1. **Nunca apagar.** Um arquivo movido para o lugar errado se recupera; um
   apagado, não. Lixo provável é SEPARADO (não removido) para o clique final
   de deletar ser humano e barato. A ponte com o computador nem permite `rm` —
   trate isso como regra de projeto, não limitação.
2. **Na dúvida, não chutar.** Um arquivo arquivado no cliente errado corrói a
   confiança no sistema inteiro (o usuário volta a conferir tudo, e a
   automação morre). Confiança baixa → `_Para_Revisar/`, sempre com sugestão
   no relatório.
3. **Preservar o que funciona.** Pastas vivas listadas no mapa como
   preservadas não têm o interior reorganizado. A skill arquiva PARA DENTRO
   delas (no nível de topo), nunca mexe no arranjo interno.
4. **Estrutura rasa vence taxonomia profunda.** Cada nível extra cobra pedágio
   em toda guarda e toda busca. Criar subpasta só quando o volume doer
   (mais de ~15 arquivos soltos numa pasta → propor divisão no relatório).

## Arquivo de estado — o mapa

Fonte primária: `Documents/00 Sistema/mapa-do-territorio.md`. A skill só
enxerga o que o mapa contém. Toda execução começa lendo o mapa e termina
gravando o mapa atualizado. Seções obrigatórias:

```
## Config          → modo_padrao: propor | direto; raiz_documents (caminho real)
## Taxonomia       → a árvore vigente e o destino de cada frente
## Clientes        → um por linha: Nome canônico | aliases (como aparece em nomes de arquivo)
## Preservadas     → pastas intocáveis por dentro
## Regras          → padrão → destino | status: proposta | ativa
## Fora de escopo  → ASSINADOR, RotaMonitor, Creative Cloud, Sites, pastas de app
## HISTÓRICO       → uma linha por faxina: data | movidos | para revisar | observação
```

Regras de roteamento nascem com status `proposta` (a skill detectou padrão
repetido, ex.: "extrato Sicoob → Grupo X/Documentos") e só executam sozinhas
depois que o usuário ratificar (status `ativa`).

## Taxonomia v1 (padrão; o mapa vigente prevalece)

```
Documents/
  00 Sistema/              ← mapa + relatórios (00 Sistema/Faxinas/AAAA-MM-DD-faxina.md)
  01 Clientes/             ← uma pasta por cliente/família, nome como o Leonardo fala
      <Cliente>/             (Grupo Carvalho, Magalhães Lima, Cruvinel…)
        Jurídico/          ← casos AeM (subpasta por caso só se houver mais de um)
        Patrimonial/       ← trabalho Agricompany
        Documentos/        ← docs do cliente (contratos sociais, matrículas, extratos)
  02 Escritório/           ← interno AeM + Agricompany: gestão, sócios, marca, modelos
  03 Docência e Autoral/   ← IBET, AGET, palestras, artigos, livro
  04 Pessoal/              ← Casa RV, família, financeiro pessoal
  90 Arquivo/              ← frio, por ano (2024/, 2025/…) + Instaladores/
  _Para_Revisar/           ← baixa confiança; nada entra sem constar no relatório
```

Subpastas de cliente são criadas SOB DEMANDA (quando o primeiro arquivo
chegar), nunca como esqueleto vazio. Prefixos numéricos existem para a
ordenação no Finder ser estável — não renumerar sem ratificação.

## Comandos

- **/faxina** — ciclo completo: varre → classifica → apresenta o plano →
  ratificação do usuário → executa → relata. Modo padrão.
- **/faxina direto** — executa movimentos de confiança alta sem pausa
  (relatório sai do mesmo jeito). Só disponível se `modo_padrao: direto` no
  mapa OU o usuário pedir explicitamente. Teto: mais de 100 movimentos numa
  rodada → pausar e confirmar mesmo em modo direto.
- **/faxina diagnostico** — censo somente-leitura: conta o solto por zona,
  aponta acúmulos e padrões novos, não move nada.

## Protocolo de execução

### Fase 0 — Pré-voo (mecânico, nunca pular)

1. Detectar a superfície: sessão na nuvem → usar as ferramentas da ponte
   (`device_list_dir`, `device_bash`, `device_stage_files`); sessão rodando no
   computador → ferramentas de arquivo diretas.
2. Confirmar acesso a Desktop, Downloads e à raiz de documentos registrada no
   mapa (`raiz_documents`). Sem ponte ou sem pasta conectada → parar e
   orientar o usuário (abrir o app desktop / conceder as pastas). Não insistir.
3. Ler o mapa. Mapa inexistente → executar a PRIMEIRA EXECUÇÃO abaixo.

### Primeira execução — diagnóstico e pacto (nada se move sem ratificação)

1. Mapear a árvore existente das três zonas (2 níveis), contar arquivos soltos
   por zona, medir idade média do acúmulo. Em volume grande (milhares), fazer
   o censo com `find`/`stat` via `device_bash` — a listagem recursiva da ponte
   trava em 2.000 entradas e subconta.
2. Identificar estruturas vivas (pastas com conteúdo coerente e uso recente) →
   propor como Preservadas.
3. Montar o índice de Clientes a partir das pastas existentes + contexto da
   conversa; apresentar para o usuário completar aliases.
4. Se `~/Documents` não existir ou for gerido pelo iCloud, perguntar onde fica
   a raiz real dos documentos e gravar em `raiz_documents`.
5. Acúmulo de anos → planejar a faxina em LOTES por recência: ano corrente
   com classificação plena (nome + conteúdo quando preciso), anos anteriores
   por nome apenas, e o que não der sinal desce em bloco para
   `90 Arquivo/<ano>/`. Uma primeira faxina que tenta ler milhares de
   arquivos não termina — e faxina que não termina não ganha segunda rodada.
   Pastas-múmia (desktops migrados de máquinas antigas, autos baixados em
   partes) movem-se INTEIRAS para o Arquivo, sem reorganizar por dentro.
6. Emitir: proposta de mapa completo + plano da primeira faxina (amostra de
   20-30 classificações para calibrar o olho do usuário). Só depois do OK:
   executar, gravar mapa, gravar relatório.

### Fase 1 — Varredura

Listar arquivos soltos: raiz do Desktop, raiz do Downloads, raiz de Documents
(fora da taxonomia). Ignorar e nunca tocar: aplicativos, atalhos/aliases,
arquivos ocultos, pastas Fora de escopo, e arquivos modificados há menos de
2 horas (podem estar em uso agora — listar no relatório como "quentes").

### Fase 2 — Classificação

Para cada arquivo, nesta ordem: (1) regras `ativas` do mapa; (2) nome do
arquivo contra o índice de Clientes (aliases contam); (3) se inconclusivo e o
formato for legível (pdf, docx, xlsx, txt), ler o conteúdo — na nuvem, via
`device_stage_files` — o suficiente para decidir; (4) atribuir destino +
confiança.

- **Alta** — nome ou conteúdo aponta cliente/frente sem ambiguidade → move.
- **Média** — frente clara, cliente incerto → move para a frente
  (ex.: `03 Docência e Autoral/`), nunca para dentro de um cliente.
  Atenção: isso só vale para frentes não-cliente (Escritório, Docência,
  Pessoal). Material que é claramente de cliente (matrícula, extrato,
  contrato, planilha de fazenda) sem cliente identificado é sempre confiança
  BAIXA — não existe destino genérico dentro de `01 Clientes/`.
- **Baixa** — nada claro → `_Para_Revisar/`, com sugestão de destino no
  relatório.

Dentro da pasta do cliente, se a subpasta certa for ambígua (ex.: proposta de
honorários — Jurídico ou Documentos?), deixar na raiz da pasta do cliente; a
divisão fina é decisão do relatório, não bloqueio da faxina.

Casos padronizados: instaladores (.dmg/.pkg/.zip de app) →
`90 Arquivo/Instaladores/`; capturas de tela e imagens sem contexto →
`_Para_Revisar/Imagens/`; duplicata exata de arquivo já arquivado (mesmo
nome + tamanho) → `_Para_Revisar/Duplicatas prováveis/`. Arquivo que
claramente pertence ao acervo institucional (tese, decisão, nota canônica) →
arquivar normalmente E sugerir `/destila` no relatório, sem executar.

### Fase 3 — Nomeação

Renomear apenas ao arquivar em `01 Clientes/` e só quando o nome atual não
carrega sinal ("doc (3).pdf", "IMG_4412", "Minuta final FINAL v2"). Padrão:
`AAAA-MM-DD Cliente tipo descrição.ext` — data do documento se identificável,
senão data de modificação. Preservar o nome original quando ele já informa.
Todo rename entra no relatório (original → novo). Nunca renomear dentro de
pastas Preservadas.

### Fase 4 — Movimentação

Mover com `mv` (via `device_bash` na nuvem). Colisão de nome → sufixo " (2)",
nunca sobrescrever. Cada movimento logado. Se um lote falhar no meio, o
relatório registra exatamente o que foi e o que não foi movido.

### Fase 5 — Relatório e estado

1. Gravar `00 Sistema/Faxinas/AAAA-MM-DD-faxina.md`: contagem antes/depois por
   zona, tabela de movimentos (compacta), lista de `_Para_Revisar` com
   sugestão de uma linha por item, regras novas propostas, arquivos quentes
   pulados.
2. Atualizar o mapa: clientes novos detectados, regras propostas, linha no
   HISTÓRICO. Gravar o arquivo integral, nunca parcial.
3. No chat: resumo em 3-5 linhas (números + o que precisa de decisão humana).
   O relatório completo fica no arquivo, não no chat.

## Guard-rails finais

- Nunca `rm`, nunca sobrescrever, nunca esvaziar `_Para_Revisar` (só o
  usuário decide o destino final do que está lá).
- Nunca reorganizar o interior de pasta Preservada nem de pasta Fora de
  escopo.
- Nunca tocar no Google Drive, iCloud compartilhado ou pastas de rede — o
  território desta skill é a bancada local definida no mapa.
- Modo `propor` é o default até o usuário mudar o mapa: o plano inteiro é
  apresentado e ratificado antes de qualquer `mv`.
