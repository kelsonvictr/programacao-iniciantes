# 🐍 Bootcamp: Programação para Iniciantes — v2

> **Para IAs (Claude, Copilot, ChatGPT…)**: este arquivo é o ponto de entrada de contexto deste projeto. Antes de qualquer mudança, **leia também `context/README.md`** para descobrir os outros documentos de contexto. Sempre que o projeto evoluir, atualize estes arquivos.

---

## 🎯 O que é este projeto

Um **bootcamp 100% visual e interativo** de Lógica de Programação com Python para iniciantes absolutos, ministrado pelo **prof. Kelson Almeida**. Cada capítulo é um HTML auto-contido (didático, animado, com diagramas e exercícios "olhinho").

A v2 substitui o `programacao-iniciantes/index.html` antigo, que cobria apenas TinyDB e Streamlit. A v2 cobre o **bootcamp inteiro** na ordem dos slides oficiais (`programacao-iniciantes/old-slides/Bootcamp_  Programação para Iniciantes - v2.pdf`).

---

## 🗂️ Arquitetura

```
programacao-iniciantes-v2/
├── CLAUDE.md                    ← este arquivo
├── index.html                   ← hub (landing) com cards dos 10 capítulos
├── context/                     ← documentação persistente para IAs
│   ├── README.md
│   ├── 01-projeto-overview.md
│   ├── 02-design-system.md
│   ├── 03-padroes-didaticos.md
│   ├── 04-conteudo-bootcamp.md  ← lista TODOS os tópicos em ordem
│   ├── 05-padrao-olhinho.md
│   └── 06-decisoes-arquitetura.md
├── shared/
│   ├── styles.css               ← design system + reset + tipografia
│   ├── components.css           ← cards, concept, tip, warning, code-block, toggler, flow…
│   ├── animations.css           ← keyframes, scroll-reveal, autoplay flows
│   └── scripts.js               ← toggler, sidebar, progress bar, scroll-reveal
├── capitulos/
│   ├── 01-boas-vindas/          ← Cada capítulo é uma pasta com seu index.html
│   ├── 02-variaveis-tipos/
│   ├── 03-condicionais/
│   ├── 04-loops-listas/
│   ├── 05-funcoes/
│   ├── 06-desafios/
│   ├── 07-dicionarios/
│   ├── 08-json/
│   ├── 09-tinydb/               ← migrado da v1
│   └── 10-streamlit/            ← migrado da v1
└── assets/
    └── images/
```

**Por que modular?** O HTML antigo de 2.851 linhas era difícil de manter. Cada capítulo agora vive em sua pasta, importa o mesmo `shared/styles.css` + `shared/scripts.js` (paths relativos `../../shared/...`), e o `index.html` raiz funciona como hub.

---

## 🧑‍🏫 Filosofia didática (resumo — detalhes em `context/03-padroes-didaticos.md`)

1. **Analogia primeiro, código depois** — receita de bolo, caixinhas, garçom decidindo, etc.
2. **Visual > texto** — fluxos animados com autoplay, diagramas, ícones grandes
3. **WOW factor** — cada capítulo precisa ter ao menos uma animação que faça o aluno sorrir
4. **Padrão olhinho 👀** — exercícios com dica + "tente sozinho" + spoiler escondido (ver `context/05-padrao-olhinho.md`)
5. **BugZilla 🐛** — personagem recorrente que aparece quando há erro comum, vira o "vilão" amigável
6. **Progressão rígida do PDF** — não pular tópicos; pode melhorar a didática, mas a sequência é sagrada

---

## 🚦 Regras de manutenção

- **Sempre** ler `context/04-conteudo-bootcamp.md` antes de editar conteúdo de um capítulo — ele é a "fonte da verdade" da ordem
- **Sempre** importar de `shared/` (não duplicar CSS) — usar paths `../../shared/styles.css` etc.
- **Sempre** atualizar `context/06-decisoes-arquitetura.md` quando tomar decisões estruturais
- **Nunca** ressuscitar o `programacao-iniciantes/index.html` antigo — está congelado para referência histórica
- **Idioma**: português brasileiro, leve, com emojis (não exageros), tom acolhedor — público é iniciante absoluto

---

## 🔗 Referências cruzadas

- **Slides originais**: `../programacao-iniciantes/old-slides/Bootcamp_  Programação para Iniciantes - v2.pdf` (12 MB, ~100 páginas)
- **Padrão olhinho de referência**: `../backend-fullstack/index.html` (procure por `petshop-tutor-model` ou `try-first`)
- **HTML v1 antigo (apenas TinyDB/Streamlit)**: `../programacao-iniciantes/index.html` — usar apenas como base para os capítulos 09 e 10
- **Contexto global do repo**: `../AGENTS.md`

---

> 💡 **Antes de fazer mudanças grandes**, leia `context/06-decisoes-arquitetura.md` e atualize-o se necessário.
