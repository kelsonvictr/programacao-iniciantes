# 2. Design System

> Toda decisão visual deste projeto vive aqui. Antes de criar uma nova classe CSS, veja se já existe uma equivalente.

## 🎨 Paleta de cores

```css
:root {
  /* Backgrounds */
  --bg:        #0a0a12;   /* fundo principal (dark) */
  --surface:   #12121e;   /* cards */
  --surface2:  #1a1a2e;   /* cards aninhados */
  --surface3:  #222240;   /* destaque sutil */
  --code-bg:   #0d0d1a;   /* fundo de código */

  /* Texto */
  --text:      #eef0f8;   /* texto principal */
  --text-dim:  #8892b0;   /* texto secundário */

  /* Acentos genéricos (numerados — usados em badges, cards, gradientes) */
  --accent:    #6c63ff;   /* roxo principal */
  --accent2:   #ff6b6b;   /* vermelho/coral */
  --accent3:   #4ecdc4;   /* turquesa */
  --accent4:   #45b7d1;   /* azul claro */
  --accent5:   #f7b731;   /* amarelo/dourado */
  --accent6:   #a78bfa;   /* lilás */
  --accent7:   #06d6a0;   /* verde menta */

  /* Cores temáticas Python/bootcamp */
  --python:    #3776ab;   /* azul Python oficial */
  --python-y:  #ffd43b;   /* amarelo Python oficial */
  --bug:       #ff4757;   /* BugZilla 🐛 */
  --tinydb:    #f7b731;
  --streamlit: #ff4b4b;
}
```

## 🔠 Tipografia

| Uso | Família | Peso |
|---|---|---|
| Texto corrido | `Nunito` | 400/600/700 |
| Títulos / destaques | `Nunito` | 800/900 |
| Conceitos manuscritos ("Receita = Código") | `Caveat` | 600/700 |
| Código / monospace | `JetBrains Mono` | 400/600/700 |

Tamanhos:
- H1 hero: `clamp(2.2rem, 5.5vw, 3.8rem)` (peso 900)
- H2 capítulos: `clamp(1.8rem, 4vw, 2.6rem)` (peso 900, com gradient)
- H3 seções: `1.45rem` (peso 800)
- Corpo: `1rem` / line-height 1.7
- Código: `0.82rem` / line-height 1.85

## 🧱 Componentes obrigatórios

| Classe | Uso | Detalhes |
|---|---|---|
| `.card` | Container principal de conteúdo | radius 20px, padding 32px, borda sutil que ilumina no hover |
| `.concept` | Conceito-chave com borda lateral amarela | título em fonte Caveat |
| `.analogy` | Analogia do mundo real (💡) | gradient lilás-azul, ícone absoluto |
| `.tip` | Dica útil (verde menta) | ícone à esquerda |
| `.warning` | Aviso/atenção (amarelo) | ícone à esquerda |
| `.bug-box` | Aparição do BugZilla 🐛 | vermelho/coral, mascote |
| `.code-block` | Código com syntax highlight | header com 3 dots e filename + lang-badge |
| `.toggler` | "Ver código completo" 👀 | ver `05-padrao-olhinho.md` |
| `.try-first` | "PARE! Tente sozinho" | ver `05-padrao-olhinho.md` |
| `.flow-container` | Diagrama de fluxo vertical animado | autoplay com `animation` |
| `.quiz` | Caixa de quiz com opções A/B/C/D | ver `03-padroes-didaticos.md` |
| `.chapter-divider` | Divisor entre capítulos | número, ícone bouncing, título com gradiente |
| `.step-section` | Seção numerada dentro de um capítulo | scroll-reveal automático |
| `.exercise-guided` | "🎯 Bora codar! (1.0)" — exercício guiado | borda azul |
| `.exercise-solo` | "💪 Desafio Individual" — exercício do aluno | borda roxa |
| `.bugzilla-card` | Caixa de erro famoso "BugZilla ataca!" | vermelha, com correção em toggler |

## 🎬 Animações padronizadas

| Keyframe | Uso |
|---|---|
| `fadeSlideDown` | hero, badges (entrada do topo) |
| `fadeSlideUp` | cards entrando ao scroll-reveal |
| `popIn` | ícones, badges (entrada com escala) |
| `bounce` | ícone de capítulo |
| `pulse` | indicadores de "agora" (bolinhas piscando) |
| `typing` + `blink` | terminal/print() |
| `flowAutoplay` | seta deslizando entre boxes em fluxos |
| `bugZillaShake` | bug aparecendo |
| `confetti` | celebração ao final de exercícios (opcional) |

**Regra de ouro:** toda animação importante tem **autoplay** quando a seção entra no viewport (via `IntersectionObserver`), não exige clique. Iniciante não sabe que pode interagir.

## 🌈 Gradientes oficiais

```css
/* Hero principal */
background: linear-gradient(135deg, var(--text), var(--accent4));

/* Capítulos por fase */
.grad-intro      { linear-gradient(135deg, var(--python), var(--python-y));   }
.grad-vars       { linear-gradient(135deg, var(--accent5), var(--accent2));   }
.grad-cond       { linear-gradient(135deg, var(--accent4), var(--accent3));   }
.grad-loops      { linear-gradient(135deg, var(--accent6), var(--accent));    }
.grad-funcs      { linear-gradient(135deg, var(--accent7), var(--accent3));   }
.grad-desafios   { linear-gradient(135deg, var(--accent2), var(--accent5));   }
.grad-dicts      { linear-gradient(135deg, var(--accent), var(--accent6));    }
.grad-json       { linear-gradient(135deg, var(--accent5), var(--accent3));   }
.grad-tinydb     { linear-gradient(135deg, var(--accent5), var(--accent3));   }
.grad-streamlit  { linear-gradient(135deg, var(--streamlit), var(--accent5)); }
```

## 📐 Layout

- Container: `max-width: 960px; margin: 0 auto; padding: 20px`
- Background: grid sutil + 3 orbs de blur com float lento
- Sidebar: 290px, off-canvas com overlay
- Progress bar: 4px no topo, gradient roxo→verde→azul
- Mobile-first: tudo precisa fluir em telas estreitas (testar em 375px)

## ✅ Checklist antes de criar um capítulo
- [ ] importou `../../shared/styles.css`, `../../shared/components.css`, `../../shared/animations.css`
- [ ] importou `../../shared/scripts.js` (no fim do `<body>`, com `defer`)
- [ ] tem `<div class="bg-grid">` e `<div class="bg-orbs">`
- [ ] tem `.progress-track > .progress-bar`
- [ ] tem sidebar nav com link "← Voltar ao hub"
- [ ] tem ao menos 1 `.analogy`, 1 `.flow-container`, 1 `.bugzilla-card`, 2 exercícios olhinho
- [ ] título usa um dos `grad-*` definidos acima
