# 3. Padrões Didáticos

> Como ensinar dentro deste projeto. Aplicar consistentemente — o aluno aprende o "ritmo" das aulas.

## 🥇 Princípio nº1 — Analogia ANTES do código

**Errado:**
> Variáveis em Python armazenam valores. Exemplo: `nome = "Ana"`.

**Certo:**
> 📦 **Caixinhas com nome.** Imagina caixas no seu armário, cada uma com uma etiqueta: "meias", "camisas", "documentos". Cada caixa guarda uma coisa diferente.
> Em Python a gente faz **a mesma coisa** — só que em vez de pano, a caixa guarda **dados**.
>
> ```python
> nome = "Ana"
> ```
>
> Isso cria uma caixinha chamada `nome` com a palavra `"Ana"` dentro. Pronto, você já sabe o que é variável.

**Sempre nessa ordem:** `analogia → exemplo concreto → código → "pronto, você já sabe"`.

## 🎬 Estrutura padrão de cada capítulo

```
1. Hero do capítulo
   └─ ícone bouncing, badge "Capítulo X", título com gradient
   └─ subtítulo com 1 frase ("hoje você vai aprender X, Y e Z")

2. Aquecimento
   └─ analogia inicial / motivação ("e se a gente quisesse…")
   └─ quiz rápido de 1-2 perguntas (gamificação)

3. Conceito 1
   ├─ analogia
   ├─ exemplo de código (com syntax highlight)
   ├─ visual (fluxo animado, diagrama, ou GIF mental)
   └─ "Bora Codar! (1.0)" — exercício guiado pelo professor

4. Conceito 2
   └─ (mesma estrutura)

5. BugZilla 🐛
   └─ aparição do "vilão" mostrando um erro comum
   └─ correção em toggler 👀

6. Desafios
   ├─ Exercício guiado (junto com o professor)
   └─ Desafio individual (com olhinho 👀)

7. Resumo
   └─ checklist do que aprendeu (✅ ✅ ✅)
   └─ frase de encorajamento ("agora você fala o idioma das máquinas!")

8. Próximo capítulo
   └─ teaser do que vem
```

## 🐛 BugZilla — o vilão amigável

BugZilla é nosso **personagem recorrente**. Aparece sempre que existe um erro comum de iniciante. Características:
- Emoji: 🐛
- Cor: `--bug: #ff4757`
- Tom: "ah não, ele apareceu de novo!" (humor leve, nunca culpando o aluno)
- Sempre seguido de **a correção em toggler** (não dá a resposta na cara)

Erros canônicos do bootcamp (do PDF):
1. Esquecer parênteses no print: `print"Olá"` ❌
2. Esquecer `:` em estruturas: `if idade >= 18` ❌
3. `==` vs `=` em comparações
4. Concatenar string com número: `"Você tem " + idade` (idade é int)
5. Esquecer `int()` em input que espera número
6. Loop infinito (esquecer de incrementar contador)

## 🎯 Exercícios — três níveis

| Tipo | Quando | Visual |
|---|---|---|
| **Bora Codar! (1.0, 1.1…)** | guiado pelo professor em aula | borda azul, ícone 🎯, código mostrado |
| **Desafio Individual** | aluno faz sozinho em aula | borda roxa, ícone 💪, **com olhinho 👀** |
| **Desafio para Casa** | aluno faz em casa | borda dourada, ícone 🏠, **com olhinho 👀** |

## 🧩 Quizzes

Toda introdução nova merece **1 quiz rápido**. Formato:
- Pergunta clara
- 4 opções (A/B/C/D)
- Botões clicáveis
- Resposta correta com confete e mensagem; errada com encorajamento ("quase! tenta de novo")
- Feedback explica POR QUE é a resposta certa

## 💬 Tom de voz

- **Brasileiro, leve, próximo.** "Bora", "tranquilo", "se liga".
- **Nunca condescendente.** Iniciante não é burro — só é novo.
- **Frases curtas.** Parágrafos longos espantam.
- **Emojis pontuais.** Não polui, mas usa quando ajuda (📦 🐍 🐛 💡 ✅).
- **"Você"**, nunca "o aluno" ou "o programador".

## 📊 Visualizações que funcionam para iniciantes

1. **Caixinhas e setas** (variáveis, atribuição) — mais didático que tabelas
2. **Diagrama de decisão** (if/elif/else) — bonequinho seguindo caminho
3. **Linha do tempo** (loops) — bolinhas pulando uma de cada vez
4. **Lista visual** (arrays/listas) — quadradinhos numerados com índices
5. **Receita / fluxograma** (algoritmos) — passos numerados
6. **Terminal animado** (output do print) — efeito de digitação

Sempre com `autoplay` — o iniciante NÃO descobre que precisa clicar em algo.

## ❌ Anti-padrões a evitar

- ❌ Jargão sem definir ("inicializar", "instanciar", "renderizar", "literal")
- ❌ Bloco de código gigante sem antes ter mostrado por partes
- ❌ Exercício sem dica
- ❌ Solução à mostra sem o olhinho 👀
- ❌ "Por enquanto não se preocupe com isso" (gera ansiedade)
- ❌ Comparações com outras linguagens (aluno não conhece nenhuma)
- ❌ Texto centralizado em parágrafos longos (cansa)
- ❌ Animação que exige clique para começar
