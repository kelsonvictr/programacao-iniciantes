# 5. Padrão "Olhinho 👀"

> Inspirado no `backend-fullstack/index.html` (desafio Petshop). É o **mecanismo central** de todos os exercícios práticos: o aluno **tenta sozinho primeiro**, e só depois vê a solução.

## 🎯 Por que existe

Quando a solução está visível, o cérebro NÃO se esforça para resolver. O aluno lê, balança a cabeça e segue — não aprende. Esconder a resposta atrás de um clique, com **dica didática antes**, força o engajamento real.

## 🧱 Estrutura visual de um exercício "olhinho"

```
┌──────────────────────────────────────────────┐
│ 💡 Dica para fazer sozinho                   │
│ Texto explicando O QUE fazer com referência  │
│ a conceitos já vistos. NUNCA dar a solução.  │
├──────────────────────────────────────────────┤
│ 🚨 PARE! Tente sozinho primeiro.             │  ← .try-first
│ Banner vermelho/coral, urgente, encorajador. │
├──────────────────────────────────────────────┤
│ 👀 Só clique aqui DEPOIS de tentar — Ver  ▼ │  ← .toggler-header
│ código completo                              │
└──────────────────────────────────────────────┘
   ↓ (ao clicar, expande)
┌──────────────────────────────────────────────┐
│ ```python                                    │
│ # solução completa com syntax highlight      │
│ ```                                          │
│ + comentário explicativo opcional            │
└──────────────────────────────────────────────┘
```

## 🧩 HTML padrão (template)

```html
<div class="exercise-solo">
  <div class="exercise-header">
    <span class="exercise-icon">💪</span>
    <div>
      <div class="exercise-title">Desafio Individual — apresentacao.py</div>
      <div class="exercise-sub">Faça sozinho antes de espiar!</div>
    </div>
  </div>

  <div class="concept">
    <div class="concept-title">💡 Dica para fazer sozinho</div>
    <p>
      Crie um arquivo <code>apresentacao.py</code>. Dentro, peça três coisas
      ao usuário com <code>input()</code>: <strong>nome</strong>,
      <strong>idade</strong> e <strong>hobby</strong>. Depois mostre uma
      frase usando <strong>f-string</strong> juntando os três.
      Lembra do exercício do cadastro simples? É bem parecido!
    </p>
  </div>

  <div class="try-first">
    <div class="try-first-icon">🚨</div>
    <div class="try-first-content">
      <strong>PARE! Tente sozinho primeiro.</strong> Abra o PyCharm,
      crie o arquivo e tente. Errar é parte do processo —
      <strong>quem espia antes de tentar perde a maior parte do aprendizado!</strong>
    </div>
  </div>

  <div class="toggler">
    <div class="toggler-header" onclick="toggleSection(this)">
      <span>👀 Só clique aqui DEPOIS de tentar — Ver código completo</span>
      <span class="toggler-arrow">▼</span>
    </div>
    <div class="toggler-body">
      <div class="code-block with-lines">
        <div class="code-header">
          <div class="dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
          <span class="filename">apresentacao.py</span>
          <span class="lang-badge python">Python</span>
        </div>
        <div class="line-numbers">1<br>2<br>3<br>4</div>
        <pre>
<span class="cm"># pega os dados do usuário</span>
nome  = input(<span class="st">"Seu nome: "</span>)
idade = input(<span class="st">"Sua idade: "</span>)
hobby = input(<span class="st">"Seu hobby: "</span>)

print(<span class="st">f"Prazer, eu sou {nome}, tenho {idade} anos e adoro {hobby}!"</span>)</pre>
      </div>

      <div class="tip" style="margin-top:14px">
        <span class="tip-icon">✨</span>
        <div class="tip-content">
          <strong>Reparou?</strong> Não converti idade pra <code>int()</code>
          aqui porque só vou exibir, não vou fazer conta.
          No próximo exercício a gente vai precisar converter!
        </div>
      </div>
    </div>
  </div>
</div>
```

## 📐 Regras da dica

A dica DEVE:
- ✅ Indicar **qual arquivo criar** (nome explícito)
- ✅ Listar os **passos numerados ou em ordem natural**
- ✅ Referenciar **conceitos já vistos** ("lembra do que vimos em…")
- ✅ Apontar **que função/comando usar** (input, print, if, etc)

A dica NÃO DEVE:
- ❌ Mostrar nenhuma linha de código pronta
- ❌ Dar o resultado já calculado
- ❌ Resolver para o aluno

## 📐 Regras do banner "PARE!"

- Sempre **vermelho/coral** — é um sinal visual forte
- Sempre com **🚨**
- Texto curto e em **negrito**
- Termina com encorajamento ("você consegue!" / "errar é parte do processo!")

## 📐 Regras do toggler

- Texto: `👀 Só clique aqui DEPOIS de tentar — Ver código completo`
- Setinha rotaciona ao abrir
- Animação suave de expansão
- Solução **completa** (não pode estar incompleta com `# preencha aqui`)
- Pode ter explicação adicional após o código (em `.tip`)

## 🎯 Quando NÃO usar o padrão olhinho

- Em **exemplos** (lá a gente quer que o aluno veja já)
- Em **demos guiadas pelo professor** (`Bora Codar (1.0)` etc — o prof faz junto, código fica visível)
- Em **trechos curtos** (1-2 linhas; nesse caso não há "tentar")

## 🌟 Variação: "Spoiler de Quiz"

Para quiz, o mesmo padrão se aplica:

```html
<div class="quiz">
  <div class="quiz-q">1️⃣ Em Python, o valor 3.14 é do tipo:</div>
  <div class="quiz-options">
    <button class="quiz-opt" onclick="checkQuiz(this, false)">A) int</button>
    <button class="quiz-opt" onclick="checkQuiz(this, true)">B) float</button>
    <button class="quiz-opt" onclick="checkQuiz(this, false)">C) string</button>
    <button class="quiz-opt" onclick="checkQuiz(this, false)">D) bool</button>
  </div>
  <div class="quiz-feedback"></div>
</div>
```

A resposta certa **só aparece quando o aluno clica**. Mesmo princípio do olhinho.

## 🔥 Filosofia em uma frase

> **"O esforço de tentar é onde mora o aprendizado.
> O olhinho protege esse esforço."**
