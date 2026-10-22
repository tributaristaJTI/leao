---
name: "apple-design"
description: "Fundamentos de design da Apple (hierarquia, tipografia, profundidade, consistência, feedback) e interfaces fluidas (springs, gestos, interrupção) para construir ou revisar deck, documento, poster, painel ou artifact HTML da casa. Complementa layout-aem."
---

# Apple Design: fundamentos e interfaces fluidas, aplicados à casa

Origem: Emil Kowalski, github.com/emilkowalski/skills (apple-design), licença MIT. Destilado das palestras de design da WWDC (conferência anual de desenvolvedores da Apple): *Designing Fluid Interfaces* (2018), *The Details of UI Typography* (2020), *Designing Audio-Haptic Experiences* e *Principles of Great Design*. Tradução e adaptação PT-BR para o ecossistema Amaral e Melo.

## 0. Como esta skill se encaixa na casa

Skill de referência, lida por dependência. Não gera arquivo; fornece o critério de composição que os designers da casa aplicam.

Divisão de competência:
- `layout-aem` decide identidade: cores, fontes, logo, margens, papel timbrado, tokens de `references/visual-tokens.md`. Em conflito, o token da marca vence.
- `apple-design` decide composição e comportamento: hierarquia, escala tipográfica, profundidade, consistência espacial, feedback, movimento.

Quem lê o quê (economia de contexto é parte do padrão; entregável estático não carrega a Parte II):

| Designer | Lê obrigatoriamente | Lê se houver |
|---|---|---|
| `deck-aula-aem`, deck institucional (.pptx) | Parte I inteira; Referência rápida (estático) | nada |
| `layout-aem`, documento .docx timbrado | §2, §3, §5 | nada |
| `canvas-design` (poster, imagem) | §2, §3, §4 | nada |
| `entregavel-cliente` | §2 (táticas), §3 | nada |
| artifact HTML estático (painel, dashboard, aula para revisitar) | Parte I inteira | §8, §16 |
| artifact HTML interativo (arrasto, sheet, carrossel, fluxograma passo a passo por clique) | Parte I e Parte II inteiras | tudo |

Tradução dos termos para o entregável estático: "feedback" vira legibilidade imediata do que o slide afirma; "interrupção" vira a possibilidade de o leitor entrar em qualquer página e se situar; "spring" não se aplica.

## A ideia central

> "Quando alinhamos a interface à forma como pensamos e nos movemos, algo acontece: ela deixa de parecer um computador e passa a parecer uma extensão contínua de nós."

Uma interface parece viva quando o movimento parte do valor atual na tela, herda a velocidade do usuário, projeta momentum à frente e pode ser agarrada e revertida a qualquer instante. Um entregável estático parece vivo quando cada elemento ocupa o lugar que o leitor esperava e nada exige explicação.

A Apple enquadra o design como serviço a quatro necessidades humanas: segurança e previsibilidade, compreensão, realização e alegria. Cada regra abaixo serve a uma delas.

---

# PARTE I: FUNDAÇÕES (todo entregável visual)

## 1. Propósito do design

Design bem feito responde às quatro necessidades na ordem: primeiro o leitor se sente seguro (sabe onde está), depois compreende, depois realiza o que veio fazer, e só então há espaço para alegria. Inverter a ordem (começar pelo efeito) produz material bonito e inútil.

## 2. Os oito princípios e as regras táticas

Use estes nomes para raciocinar e para criticar um entregável.

1. **Propósito.** Faça com intenção; decida o que NÃO construir. Cada elemento pede tempo, atenção e confiança do leitor. Em deck: um slide que não muda a decisão da plateia sai.
2. **Agência.** Mantenha a pessoa no controle: ofereça escolhas, não force um caminho único. Confirmação só para ação destrutiva e irreversível; confirmar demais ensina a clicar sem ler.
3. **Responsabilidade.** Aja no interesse de quem lê. Antecipe mau uso e dano. Em material jurídico: número ilustrativo declara a base; pendência normativa declarada, nunca escondida.
4. **Familiaridade.** Construa sobre o que a pessoa já conhece. Metáfora nem literal demais nem abstrata demais, e honre a física dela (a metáfora-mestra do registro porteira segue esta regra). Coisas iguais se comportam igual e moram no mesmo lugar. Só quebre um padrão familiar se provar que é melhor; depois teste.
5. **Flexibilidade.** Projete para contextos diferentes: projetado em sala, lido no celular, impresso. Inclusivo em idade, idioma, expertise e acessibilidade.
6. **Simplicidade, que é diferente de minimalismo.** Retire o desnecessário para que o propósito central apareça; enterrar tudo num só lugar parece minimal e não é simples. Conciso (linguagem simples, menos passos) e claro (hierarquia por ordem, espaçamento e contraste, para que o mais importante seja o mais óbvio). Às vezes ADICIONAR contexto simplifica. Caminho comum primeiro, opção avançada um nível abaixo.
7. **Craft.** Atenção intransigente ao detalhe constrói confiança. Nada é aleatório: cada espaçamento, tempo e alinhamento é uma escolha que você consegue defender. Texto estourando a caixa, ícone desalinhado e layout que quebra na rotação são lidos como descuido, e descuido no visual contamina a credibilidade do conteúdo jurídico.
8. **Deleite.** Resultado de acertar os outros sete, não confete por cima. Decida a emoção que a pessoa deve sentir (calma, confiança, urgência) e reforce em cada decisão.

Regras táticas:
- **Feedback vem em quatro tipos:** status, conclusão, aviso, erro. Confirme ações significativas, exponha status contínuo, avise antes do problema, valide inline (não no envio).
- **Wayfinding (orientação).** Toda tela ou página responde: onde estou? para onde posso ir? o que há lá? como saio? Em deck: eyebrow do bloco, numeração e título curto no rodapé fazem esse papel. Em documento: sumário, títulos numerados, cabeçalho de seção.
- **Agrupamento e mapeamento.** Proximidade implica relação; coloque o controle perto do que ele afeta e a legenda perto do dado. Se precisa de rótulo para explicar um controle, o mapeamento é fraco.
- **Rótulo direto e específico vence genérico seguro.** Nomeie pelo conteúdo ("Progresso", "Calendário do diferimento"), não por guarda-chuva vago ("Home", "Informações"). Título de slide é afirmação, nunca rótulo.

## 3. Tipografia: optical sizing, tracking, leading

A Apple desenha o tipo para mudar de forma com o tamanho; a mesma disciplina vale em deck, docx e HTML. (De *The Details of UI Typography*, WWDC 2020.)

- **Tracking (espaçamento entre letras) é específico por tamanho; nunca um valor para todos.** Texto grande de display pede tracking NEGATIVO (as letras parecem distantes quando crescem); texto pequeno pede tracking levemente POSITIVO. Um `letter-spacing` fixo está errado em algum tamanho. Aperte títulos, deixe corpo perto de 0.
- **Leading (entrelinha) acompanha o tamanho inversamente.** Apertado em título grande, mais solto em corpo. Aumente para texto longo; aperte para UI densa.
- **Hierarquia nasce de peso + tamanho + entrelinha como conjunto,** não só de tamanho. Enfatize com peso: adiciona presença sem ocupar espaço.
- **Respeite o tamanho de texto do usuário.** Espaçamento em `rem`/`em`, não px fixo, para que fonte maior não quebre o layout.
- **Fonte de sistema antes de face custom**, salvo razão de marca. Na casa a razão existe: Georgia (títulos) e Arial (corpo) vêm de `layout-aem` e prevalecem; esta seção governa como escalá-las.

```css
:root { font: 100%/1.5 system-ui, sans-serif; } /* corpo: entrelinha confortável */
.display {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.05;        /* entrelinha apertada em texto grande */
  letter-spacing: -0.02em;  /* tracking negativo conforme cresce */
  font-optical-sizing: auto;
}
```

Em .pptx: título Georgia 27 a 32pt com folga de ~10% na caixa (métrica imprecisa no QA); número-herói 28 a 40pt; corpo Arial 11 a 14pt. Nunca o mesmo tamanho para título e corpo com peso diferente "para economizar".

## 4. Materiais e profundidade: translucidez transmite hierarquia

A Apple usa materiais translúcidos como camada funcional flutuante que traz estrutura sem roubar foco. Na web, aproxime com `backdrop-filter`. Em deck e poster, a mesma lógica vale com sombra, peso de fundo e escurecimento.

- **Peso do material codifica hierarquia:** material mais escuro ou pesado separa região estrutural (barra lateral, capa navy); material mais leve chama atenção para o elemento interativo ou o número-herói. **Nunca empilhe uma superfície translúcida clara sobre outra**; a legibilidade colapsa.
- **Superfície maior parece mais espessa:** blur mais forte e sombra mais profunda que um chip pequeno. Sombra contextual: mais pesada sobre conteúdo denso, mais leve sobre fundo simples.
- **Escureça para focar, separe para manter fluxo.** Tarefa modal usa scrim (véu escuro) e empurra o fundo para trás. Painel paralelo não bloqueante usa translucidez e deslocamento, sem scrim. Em deck: o destaque de um item numa matriz é o mesmo gesto (os demais recuam, o item avança).
- **Vibrancy mantém texto legível sobre fundo variável.** Sobre superfície borrada, nada de cinza chapado: mais contraste, peso levemente maior, pequeno acréscimo de tracking. Cor em camada sólida, não no primeiro plano translúcido.
- **Efeito de borda de rolagem, não divisor duro.** Em vez de linha de 1px sob cabeçalho fixo, uma máscara curta de blur ou gradiente onde o conteúdo encontra o chrome flutuante.
- **Materialize, não só faça fade.** Para superfície de vidro, anime raio de blur e escala juntos no entrar e sair.

```css
.toolbar {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.4); /* borda superior clara = luz batendo no material */
}
```

## 5. Consistência espacial, origem ancorada e direção

> "Se algo desaparece de um jeito, esperamos que volte de onde veio."

- **Entre e saia pelo mesmo caminho.** Painel que desliza da direita é dispensado para a direita. Entrar da direita e sair por baixo parece desconectado.
- **Ancore à origem.** Menu, popover ou sheet nasce do elemento que o acionou (`transform-origin` no gatilho).
- **Espelhe o easing em transição reversível** (pontos de controle cubic-bézier inversos nas duas direções).
- **Dê dica na direção.** Humanos preveem o estado final pela trajetória; o movimento intermediário telegrafa para onde as coisas vão. Em fluxograma progressivo: o próximo nó aparece no eixo da seta, não de qualquer lugar.
- **Em entregável estático, consistência espacial é posição fixa:** logo, numeração, eyebrow e título curto moram no mesmo lugar em TODOS os slides; o mesmo nível de título tem o mesmo estilo em TODAS as páginas. Toda exceção é uma decisão registrada, nunca um acidente do gerador.
- **Movimento em deck .pptx:** nenhum ou fade curto. Nunca bounce, zoom ou rotação. Transição não é conteúdo.

## 6. Acessibilidade: movimento, transparência, contraste

Movimento reduzido não significa sem feedback; significa equivalente mais gentil, não vestibular. Responda a três sinais independentes e incorpore-os nos componentes:

- **`prefers-reduced-motion: reduce`**: troque slide, spring e parallax por cross-fade curto de opacidade. Elimine elástico e overshoot. Mantenha mudança de opacidade e cor que ajuda a compreensão.
- **`prefers-reduced-transparency: reduce`**: superfície translúcida vira fosca ou sólida (sobe opacidade do fundo, elimina o blur).
- **`prefers-contrast: more`**: fundo quase sólido com borda definida e contrastante.

Evite também: fundo em movimento ocupando a tela inteira, oscilação lenta em loop (perto de 0,2 Hz, um ciclo a cada 5 s) e salto abrupto de brilho (suavize a troca de tema claro e escuro). Objeto grande em movimento fica semitransparente enquanto viaja.

Para deck projetado e documento impresso, a regra equivalente: contraste suficiente para sala com luz acesa; informação nunca só por cor (ícone ou rótulo junto, como já exige `deck-aula-aem`); tamanho mínimo legível da última fileira.

```css
@media (prefers-reduced-motion: reduce) {
  .sheet { transition: opacity 200ms ease; transform: none !important; }
}
@media (prefers-reduced-transparency: reduce) {
  .toolbar { background: white; backdrop-filter: none; }
}
```

## 7. Processo

- **Prototipe interativamente: um demo funcionando vale "um milhão de designs estáticos".** Você descobre a interface construindo e mexendo nela; o protótipo também fixa uma barra concreta que impede implementação final medíocre.
- **Projete interação e visual juntos.** Movimento não é camada adicionada depois dos pixels.
- **Revise com olhos frescos e em câmera lenta.** Reproduza quadro a quadro para pegar o que é invisível em velocidade normal. Em deck, o equivalente é o passo 3 do QA de `deck-aula-aem`: renderizar TODAS as lâminas e olhar uma a uma (estouro de texto, colisão, contraste, coerência de números entre slides). Não existe entrega sem essa passagem.

---

# PARTE II: INTERFACES FLUIDAS (só UI interativa: artifact com gesto, sheet, carrossel, arrasto, passo a passo)

Springs (animações por mola física) são a ferramenta que torna tudo isto natural, porque são inerentemente interrompíveis e conscientes de velocidade.

## 8. Resposta: mate a latência

No instante em que o lag aparece, a sensação de manipulação direta "cai do penhasco". Resposta é a fundação de todo o resto.

- **Responda no pointer-down, não no release.** Destaque o botão quando ele é pressionado. Esperar o `click` para mostrar feedback parece morto.
- **Audite cada latência:** debounces, timers artificiais, esperas de transição, o delay de ~300 ms do tap. O que não é essencial no caminho do input é regressão.
- **Feedback contínuo DURANTE a interação, não só no fim.** Arrasto, slider ou drawer atualizam 1:1 com o ponteiro o tempo todo.

```css
.button:active {
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}
```

## 9. Manipulação direta: tracking 1:1

> "Toque e conteúdo devem se mover juntos."

O que o usuário arrasta fica grudado no dedo e respeita o offset de ONDE ele agarrou. Dar snap para o centro ao agarrar quebra a ilusão.

- Pointer Events com `setPointerCapture`, para o tracking continuar fora dos limites do elemento.
- Mantenha histórico curto de posição e tempo (últimos `pointermove`); a velocidade no release vem daí.

```js
el.addEventListener('pointerdown', (e) => {
  el.setPointerCapture(e.pointerId);
  const grabOffset = e.clientY - el.getBoundingClientRect().top; // respeite onde agarrou
  // ...guardar posição + timestamp para calcular velocidade
});
```

## 10. Interrompibilidade: o princípio mais importante

> "O pensamento e o gesto acontecem em paralelo."

Toda animação é interrompível e redirecionável a qualquer momento. Um modal fechando que o usuário agarra de novo segue o dedo; não termina de fechar para depois reabrir.

- **Nunca bloqueie input durante uma transição.**
- **Anime sempre a partir do valor de apresentação (atual), nunca do valor alvo.** Ao interromper, leia o transform ao vivo e comece dali. Partir do valor lógico causa pulo visível.
- **Evite CSS transitions e @keyframes para o que é guiado por gesto**; não podem ser agarradas e revertidas no meio do voo. Springs animam do valor atual por padrão.
- **Na reversão, faça blend da velocidade, não corte seco.** Trocar uma animação por outra cria descontinuidade de velocidade ("muro de tijolos"). Escolha biblioteca de spring que faça re-target carregando a velocidade atual (equivalente web das *additive animations* do iOS).
- **Decomponha movimento 2D em springs independentes X e Y.** Um spring único em distância 2D dessincroniza quando X e Y têm velocidades diferentes.

## 11. Comportamento sobre animação: use springs

> "Pense em animação como conversa entre você e o objeto, não algo prescrito pela interface."

Animação roteirizada de duração fixa não responde a input novo. Spring responde: input novo só muda o alvo e o movimento continua. Use spring para tudo que o usuário possa tocar.

A Apple trocou o trio físico (mass, stiffness, damping) por dois parâmetros amigáveis ao designer:

- **Damping ratio**: controla o overshoot. `1.0` = criticamente amortecido, sem bounce. `< 1.0` = ultrapassa e oscila.
- **Response**: quão rápido o valor chega ao alvo, em segundos. Menor = mais rápido. Não é "duração": spring não tem duração fixa.

Defaults:
- Comece quase toda UI em **damping `1.0`**: gracioso e não distrativo.
- Bounce (**damping ~`0.8`**) **só quando o gesto carregou momentum** (flick, arremesso, release de arrasto). Overshoot num menu que só fez fade parece errado; num card arremessado parece certo.

Valores que a Apple usa:

| Interação | Damping | Response |
|---|---|---|
| Mover / reposicionar (ex.: PiP) | 1.0 | 0.4 |
| Rotação | 0.8 | 0.4 |
| Drawer / sheet | 0.8 | 0.3 |

Mapeamento web (Motion / Framer Motion): `bounce` + `duration` mapeiam para damping + response. House style seguro: `bounce: 0` em todo lugar por padrão; bounce reservado a interação física com momentum.

```js
import { animate } from 'motion';
// Criticamente amortecido (sem overshoot)
animate(el, { y: 0 }, { type: 'spring', bounce: 0, duration: 0.4 });
// Interação com momentum: um pouco de bounce, só porque houve flick
animate(el, { y: target }, { type: 'spring', bounce: 0.2, duration: 0.4 });
```

## 12. Handoff de velocidade: a costura entre arrasto e animação

Quando o gesto termina, a animação continua na velocidade exata do dedo, sem costura visível. É o detalhe que mais separa "fluido" de "ok".

Passe a velocidade de release como velocidade inicial do spring. APIs que pedem velocidade RELATIVA: normalize pela distância restante.
```
relativeVelocity = gestureVelocity / (targetValue − currentValue)
```
Exemplo: elemento em `y=50`, alvo `y=150` (faltam 100 px), dedo a 50 px/s → velocidade inicial = `50 / 100 = 0.5`. Motion / Framer Motion aceitam velocidade absoluta em px/s (`velocity`); passe o valor bruto.

## 13. Projeção de momentum: anime para onde o gesto está INDO

> "Pegue um input pequeno e faça um output grande."

Não faça snap para a borda mais próxima do ponto de release. Use a velocidade para PROJETAR a posição de repouso (como desaceleração de scroll) e faça snap para o alvo mais próximo desse ponto projetado.

Função exata da Apple (código de exemplo de *Designing Fluid Interfaces*):
```js
// decelerationRate ≈ 0.998 para sensação normal de scroll; 0.99 para mais seco
function project(initialVelocity /* px/s */, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}
const projectedEndpoint = currentPosition + project(releaseVelocity);
const target = nearestSnapPoint(projectedEndpoint);   // alvo a partir da projeção
animateSpringTo(target, { velocity: releaseVelocity }); // depois handoff de velocidade (§12)
```
A fórmula `v²/(2·decel)` de livro de física NÃO é a que a Apple usa; use o decaimento exponencial acima. É o comportamento padrão de bottom-sheets e carrosséis bons (Vaul, Embla).

## 14. Rubber-banding: bordas suaves

Na borda, resista progressivamente em vez de parar seco. Parada dura é lida como "travou"; resistência contínua é lida como "responsivo, mas acabou".

```js
// Quanto mais além do limite, menos o elemento segue
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

## 15. Checklist de gestos ("sensação")

- **Tap:** destaque no touch-down (instantâneo), confirme no touch-up. ~10 px de histerese ao redor do alvo; permita cancelar arrastando para fora e voltando.
- **Drag/swipe:** exija pequeno limiar (~10 px) antes de se comprometer com uma direção; depois track 1:1.
- **Detecte todos os gestos plausíveis em paralelo desde o primeiro movimento** e cancele os perdedores quando a intenção ficar clara. Evite reconhecedores que só reportam estado final (`swipeleft`); jogam fora o tracking contínuo.
- **Minimize delays de desambiguação.** Detecção de double-tap atrasa single taps; pague esse custo só onde double-tap existe.

## 16. Suavidade em nível de frame

Suavidade é sobre o que está NOS frames, não só a taxa.
- Mantenha a mudança posicional por frame abaixo do limiar de percepção para evitar strobing.
- Para movimento muito rápido, leve motion blur ou stretch codifica velocidade melhor que um rastro seco.
- `requestAnimationFrame` é o relógio sincronizado com o display (a Apple usa `CADisplayLink`). Anime só propriedades amigáveis ao compositor: `transform` e `opacity`; `will-change` onde o movimento é iminente.

## 17. Feedback multimodal: movimento + som + háptico

(De *Designing Audio-Haptic Experiences*.)
1. **Causalidade:** deve ser óbvio o que causou o feedback. Dispare no evento causal real (o toggle virando, o item encaixando).
2. **Harmonia:** visual, som e háptico no MESMO frame. Não deixe uma transição CSS atrasar o áudio ou a Vibration API.
3. **Utilidade:** feedback só onde ele ganha o lugar (sucesso, erro, commit, snap). Excesso treina o usuário a ignorar tudo.

---

## Referência rápida

### Entregável estático (deck, docx, poster, painel)

| Necessidade | Técnica | Valor concreto |
|---|---|---|
| Hierarquia | peso + tamanho + entrelinha como conjunto | nunca só tamanho |
| Tracking | específico por tamanho | título −0.02em; corpo ~0 |
| Entrelinha | inversa ao tamanho | título ~1.05; corpo ~1.5 |
| Orientação | eyebrow, numeração, título curto | mesmo lugar em todo slide |
| Rótulo | específico, afirmativo | título é afirmação, não rótulo |
| Destaque | item avança, demais recuam | scrim ou fundo neutro |
| Profundidade | superfície maior = mais espessa | sombra contextual |
| Cor | nunca sozinha | ícone ou rótulo junto |
| Transição .pptx | nenhuma ou fade | nunca bounce/zoom |
| QA | olhar cada lâmina renderizada | sem exceção |

### UI interativa (artifact com gesto)

| Necessidade | Técnica | Valor concreto |
|---|---|---|
| Spring default | criticamente amortecido | damping 1.0, response 0.3 a 0.4 |
| Spring com momentum | leve bounce | damping ~0.8, response 0.3 a 0.4 |
| Gesto → spring | handoff de velocidade | gestureVelocity / (target − current) se normalizado |
| Pouso do flick | projetar momentum | current + (v/1000)·d/(1−d), d ≈ 0.998 |
| Interromper limpo | partir do valor de apresentação | leia o transform ao vivo |
| Evitar "muro" na reversão | carregar velocidade no re-target | spring que faz blend |
| Transição reversível | espelhar easing | cubic-bézier inverso |
| Reverter vs confirmar | sinal da velocidade, não posição | no release |
| Drag 1:1 | Pointer Events + capture | respeite o grab offset |
| Feedback | no pointer-down, contínuo | nunca só no final |
| Borda | rubber-band | resistência progressiva |
| Chrome translúcido | backdrop-filter | conteúdo rola por baixo |
| Movimento reduzido | cross-fade | @media (prefers-reduced-motion) |