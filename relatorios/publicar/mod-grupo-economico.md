# Publicar · mod-grupo-economico

Origem: `skills/mod-grupo-economico/` no repositório tributaristaJTI/leao. Versão sincronizada de referência: atualizada na conta em 2026-04-06.

## 1. SKILL.md completa e final

`````markdown
---
name: mod-grupo-economico
description: "Módulo de análise de grupo econômico com produtor rural pessoa física e participações societárias. Use SEMPRE que o usuário mencionar grupo econômico, produtor com empresa, participação societária, holding familiar, confusão patrimonial, estrutura societária complexa, produtor que também é médico/empresário/comerciante, múltiplas atividades, participações cruzadas, reorganização societária familiar, ou qualquer variação de análise envolvendo pessoa física rural com vínculos societários em atividades agropecuárias e/ou não agropecuárias."
---

# Módulo Grupo Econômico

Módulo para análise de estruturas complexas envolvendo produtor rural pessoa física com participações em sociedades agropecuárias e/ou não agropecuárias, incluindo configurações com cônjuge, filhos, holdings e participações cruzadas.

## Escopo

- Mapeamento completo da estrutura: PF com atividade rural + todas as participações societárias
- Tributação de cada "ponta" (PF rural, PJ agro, PJ não-agro, holding)
- Riscos de confusão patrimonial e responsabilidade tributária solidária
- Planejamento de distribuição de resultados entre as pontas
- Reestruturações societárias (criação de holding, segregação de atividades, incorporação)
- Impacto sucessório da estrutura atual vs estrutura otimizada
- ITCMD sobre transmissão de quotas vs transmissão de imóveis
- Operações entre partes relacionadas (preço de transferência, subcontratação, parceria)

## Perfis típicos de caso

**Perfil 1 — Produtor com atividade urbana:**
Médico/advogado/comerciante que também é proprietário de imóvel rural, com parceria ou arrendamento com outro produtor PF, e participação societária em clínica/escritório/loja.

**Perfil 2 — Família rural com diversificação:**
Família que opera lavoura e pecuária em PF, tem holding patrimonial com os imóveis, empresa de comercialização (trading), e eventualmente agroindústria (beneficiamento, armazém, frigorífico).

**Perfil 3 — Grupo familiar multigeracional:**
Patriarca com imóveis em nome próprio, filhos com participações em diferentes empresas do grupo, cônjuge com atividade própria, holding familiar com participações cruzadas, contratos entre as partes.

**Perfil 4 — Produtor com investimentos:**
Produtor rural PF que também é sócio minoritário em cooperativa, tem participação em empresa de insumos, e investimentos financeiros relevantes (fundos, ações, imóveis urbanos).

## Fluxo analítico

### 1. Mapeamento da estrutura

Construir o organograma completo do grupo:

Para cada pessoa (física ou jurídica), registrar:
- Nome/razão social e CPF/CNPJ
- Atividade econômica
- Regime tributário (se PJ: lucro real, presumido, simples; se PF: livro caixa, simplificado)
- Participação societária em outras entidades (percentual, tipo: quotas, ações)
- Patrimônio imobiliário (rural e urbano)
- Receita bruta anual estimada
- Resultado líquido estimado

Para cada relação entre as partes, registrar:
- Tipo (societária, contratual, familiar)
- Contratos vigentes (parceria, arrendamento, cessão, prestação de serviços)
- Fluxos financeiros (distribuição de lucros, pagamento de arrendamento, pró-labore)

Apresentar o mapa em formato textual estruturado (hierárquico), descrevendo cada vínculo. Se o usuário quiser diagramar visualmente, sugerir ferramenta ou gerar descrição para conversão em diagrama.

### 2. Diagnóstico tributário por ponta

Para cada entidade do grupo, calcular em Python:
- Carga tributária atual (todos os tributos: IRPF/IRPJ, CSLL, PIS/COFINS, Funrural, ICMS, ISS)
- Obrigações acessórias
- Riscos fiscais específicos

### 3. Diagnóstico de riscos estruturais

Verificar e alertar:

**Confusão patrimonial:**
- Uso de bens pessoais na atividade empresarial (ou vice-versa) sem contrato
- Pagamento de despesas pessoais pela PJ
- Uso de conta bancária pessoal para operações da PJ
- Imóveis rurais em nome da PF usados pela PJ sem contrato de arrendamento/parceria

**Responsabilidade tributária solidária:**
- Operações entre partes relacionadas sem justificativa econômica (Art. 124, CTN)
- Gestão centralizada com subordinação entre empresas do grupo
- Sócios em comum com atividades complementares sem independência operacional

**Operações entre partes relacionadas:**
- Preços praticados entre as empresas/pessoas do grupo (estão a valor de mercado?)
- Contratos de parceria/arrendamento entre familiares (estão formalizados?)
- Cessão de uso de máquinas, infraestrutura, marca, sem remuneração

**Sucessão e continuidade:**
- Concentração patrimonial no patriarca/matriarca
- Ausência de planejamento sucessório formalizado
- ITCMD potencial sobre a estrutura atual vs sobre estrutura reorganizada
- Testamentos, doações em vida, cláusulas de impenhorabilidade/incomunicabilidade

### 4. Simulação de cenários de reestruturação

Modelar pelo menos dois cenários alternativos à estrutura atual:

**Cenário de segregação:**
- Separar atividades em entidades distintas (agro, não-agro, patrimonial)
- Criar holding patrimonial para concentrar imóveis
- Formalizar contratos entre as partes
- Calcular a carga tributária pós-reestruturação

**Cenário de consolidação:**
- Unificar atividades em menos entidades
- Simplificar a gestão e reduzir custos operacionais
- Calcular a carga tributária pós-consolidação

**Cenário de otimização mista:**
- Combinação de segregação e consolidação conforme a melhor eficiência tributária e operacional

Para cada cenário, calcular:
- Custo de implementação (ITBI, alterações contratuais, contabilidade)
- Carga tributária projetada (todas as pontas)
- Economia tributária anual vs estrutura atual
- Tempo de retorno do investimento na reestruturação
- Impacto sucessório (quanto de ITCMD seria economizado na transmissão)

### 5. Quadro comparativo consolidado

| Elemento | Estrutura Atual | Cenário A | Cenário B | Cenário C |
|----------|----------------|-----------|-----------|-----------|
| Nº de entidades | | | | |
| Carga tributária total anual | R$ | R$ | R$ | R$ |
| Carga efetiva (% sobre receita consolidada) | % | % | % | % |
| Custo de implementação | — | R$ | R$ | R$ |
| Economia anual vs atual | — | R$ | R$ | R$ |
| Retorno do investimento | — | X meses | X meses | X meses |
| ITCMD projetado na sucessão | R$ | R$ | R$ | R$ |
| Risco de questionamento fiscal | | | | |
| Complexidade operacional | | | | |

### 6. Análise do propósito negocial

Para cada reestruturação proposta, fundamentar o propósito negocial (razão econômica) que sustenta a operação perante o fisco:

- Qual o ganho operacional (não apenas tributário)?
- A estrutura proposta tem substância econômica?
- Os critérios do CARF para descaracterização de planejamento estão afastados?
- Há precedentes favoráveis para estruturas similares?

Usar a escala de risco do tributarista-consultivo:
- **Baixo:** posição pacificada
- **Moderado:** majoritária favorável com ressalvas
- **Alto:** viável apenas com tolerância a litígio
- **Temerário:** desaconselhável

### 7. Recomendação e cronograma

Posicionar-se com clareza sobre:
- Qual cenário recomenda e por quê
- Sequência de implementação (o que fazer primeiro, segundo, terceiro)
- Prazos estimados para cada etapa
- Profissionais envolvidos (advogado, contador, cartório, junta comercial)
- Custos estimados de implementação
- Monitoramento pós-implementação (o que acompanhar, com qual frequência)

## Regras

1. Todo cálculo em Python com três camadas de segurança.
2. O mapeamento da estrutura é a primeira etapa — nunca pule para cenários sem ter o organograma completo.
3. Sempre verificar riscos de confusão patrimonial e responsabilidade solidária.
4. Toda reestruturação deve ter propósito negocial fundamentado — nunca sugira estruturas puramente artificiais.
5. O impacto sucessório (ITCMD) deve ser quantificado em todos os cenários.
6. Se alguma ponta envolver atividade não tributária (ex: clínica médica), buscar informações complementares sobre o regime tributário daquela atividade específica.
7. Articular com os módulos IR Venda de Imóvel e Comparativo PF × PJ quando necessário.
8. Se a estrutura for muito complexa (mais de 8 entidades), sugerir análise em etapas com entregas parciais.

## Referência legislativa

Dispositivos, alíquotas e prazos são conferidos no conector Jusratio ou na fonte oficial consolidada antes de entrar no cálculo ou no texto. Os três arquivos de referência do projeto servem só como mapa de onde procurar; não valem como fonte:
- `ref-ir-rural.md`: tributação PF e PJ
- `ref-funrural-ibs.md`: contribuições previdenciárias e reforma tributária
- `ref-grupo-economico.md`: confusão patrimonial, responsabilidade solidária, holding rural e ITCMD

## Conferência de citação

Dispositivo legal, súmula, julgado, alíquota ou prazo só entra no texto depois de conferido no conector Jusratio ou em fonte oficial consolidada, na própria sessão. O que não for conferido fica fora do texto ou entra marcado [A CONFERIR: fonte]. Memória, arquivo de referência embarcado e trecho de resultado de busca servem para localizar, nunca para afirmar.
`````

## 2. O que mudou desde a versão sincronizada

A seção "Referência legislativa" deixa de mandar ler o(s) arquivo(s) `ref-*.md` do projeto como fonte: agora manda conferir no Jusratio ou na fonte oficial consolidada, e os arquivos ficam só como mapa de onde procurar (decisão 1).
Arquivos-mapa: `ref-ir-rural.md`, `ref-funrural-ibs.md` e `ref-grupo-economico.md`, com a lista mantida.
Nova seção final "Conferência de citação", com texto idêntico nas 22 skills que citam norma ou julgado (laudo de 03/10, decisão 3).
O que não for conferido fica fora ou marcado [A CONFERIR: fonte].
Regras e fluxo intocados.
