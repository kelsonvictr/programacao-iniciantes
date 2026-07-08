# 4. Conteúdo do Bootcamp — Mapa Completo

> **Fonte da verdade.** Toda a ementa do curso, na ordem do PDF oficial. Nenhum capítulo pode ser pulado, mas a didática DENTRO de cada um pode (e deve) ser melhor que o slide.

PDF: `../programacao-iniciantes/old-slides/Bootcamp_  Programação para Iniciantes - v2.pdf`

---

## 🟦 Capítulo 01 — Boas-vindas e Fundamentos
**Pasta:** `capitulos/01-boas-vindas/`
**Cor temática:** azul Python (`--python`) + amarelo Python (`--python-y`)
**Slides cobertos:** Boas-vindas, "O que é programar?", "O idioma das máquinas", "Por que Python?", "Do código à ação", "Pensar como programador", Bora Codar 1.0/1.1/1.2/1.3, BugZilla 1, Resumo

### Tópicos
1. **Boas-vindas** — "Programar é ensinar o computador a resolver problemas"
2. **O idioma das máquinas** — Python é como um idioma para falar com a máquina
3. **Por que Python** — sintaxe simples, web/IA/dados, comunidade, criado por Guido van Rossum, nome vem de Monty Python
4. **Do código à ação** — fluxo: você escreve → Python lê → traduz → executa
5. **Pensar como programador** — decomposição (analogia: fazer café passo a passo)
6. **Bora Codar (1.0)** — `print("Olá, mundo!")` no PyCharm
7. **Bora Codar (1.1)** — `ola_usuario.py` com `input()`
8. **Bora Codar (1.2)** — `boas_vindas.py` (nome + curso, f-string) — *desafio individual*
9. **Bora Codar (1.3)** — `calculo_idade.py` (input, int(), f-string) — *desafio individual*
10. **BugZilla apresentação** — "todo programador erra, está tudo bem"
11. **Resumo + frase de encerramento**

### Quizzes do capítulo
- "Programar é A) ensinar o computador..." (A correto)
- "Linguagem Python é A) tipo de cobra B) linguagem de programação..." (B)
- "O que é programar? A) falar com computador..." (A)

---

## 🟧 Capítulo 02 — Variáveis e Tipos de Dados
**Pasta:** `capitulos/02-variaveis-tipos/`
**Cor temática:** dourado + coral (`--accent5` + `--accent2`)
**Slides cobertos:** Variáveis (caixinhas), tipos (str/int/float/bool), tipagem dinâmica, input/print, conversão, f-strings, Bora Codar 2.0, BugZilla 2

### Tópicos
1. **Variáveis = caixinhas** — `nome = "Kelson"` (analogia caixa com etiqueta)
2. **Exercício rápido — Minhas Caixinhas** (nome, idade, cidade)
3. **Tipos de dados** — string, int, float, bool (com tabela visual)
4. **Tipagem dinâmica** — Python descobre o tipo sozinho
5. **input()** — pegando dados do usuário (input retorna string!)
6. **Conversão de tipos** — `int(input(...))`, `float(...)`
7. **print()** — exibindo, combinando texto e variáveis
8. **F-strings** — `f"{nome} tem {idade} anos"`
9. **Bora Codar (2.0)** — Cadastro simples (nome, idade, cidade) — *guiado*
10. **Desafio Individual** — `apresentacao.py` (nome, idade, hobby)
11. **BugZilla 2** — esquecer parênteses, vírgulas, mistura tipos
12. **Resumo**

### Quizzes
- "3.14 é A)int B)float..." (B)
- "nome = 'programa AI' é A) texto..." (A)

---

## 🟦 Capítulo 03 — Estruturas Condicionais
**Pasta:** `capitulos/03-condicionais/`
**Cor temática:** turquesa + azul (`--accent3` + `--accent4`)
**Slides cobertos:** poder das decisões, if, else, elif, operadores comparação/lógicos, restaurante inteligente, Bora Codar 3.0, controle de acesso, descontos, mini sistema

### Tópicos
1. **O poder das decisões** — quiz V/F (todo if executa? else é opcional? etc)
2. **if** — `if idade >= 18: print("pode entrar!")` (analogia: garçom verificando pedido)
3. **else** — "senão"
4. **elif** — múltiplas opções (analogia: cardápios)
5. **Operadores de comparação** — `==`, `!=`, `>`, `<`, `>=`, `<=` (BugZilla: `=` vs `==`)
6. **Operadores lógicos** — `and`, `or`, `not`
7. **Cenário Restaurante Inteligente** 🍔 — segunda → desconto, sexta → sobremesa
8. **Bora Codar (3.0)** — Sistema de Promoções
9. **Desafio extra** — Pedido com entrega grátis (>100 frete free)
10. **Desafio Criativo** — `entrada_evento.py` (controle de idade) - *individual*
11. **Desafio Casa** — `descontos.py` (faixas de desconto)
12. **Mini Sistema** — `mini_sistema.py` (consolidação)
13. **Resumo**

### Visual obrigatório
- Bonequinho na frente do "if" indo por dois caminhos
- Tabela de operadores com exemplos clicáveis
- Animação do restaurante decidindo

---

## 🟪 Capítulo 04 — Loops e Listas
**Pasta:** `capitulos/04-loops-listas/`
**Cor temática:** lilás + roxo (`--accent6` + `--accent`)
**Slides cobertos:** Parte 02 — quiz aquecimento, while, contagem, for, range, tabuada, BugZilla 3, listas, lista_alunos, lista_interativa, quiz listas

### Tópicos
1. **Por que repetir?** — quiz de aquecimento
2. **while** — repete enquanto verdade (com cuidado: incremento!)
3. **Bora Codar — Contagem animada** (`contagem.py`)
4. **Desafio — Contagem regressiva** (`contagem_regressiva.py`)
5. **for** — percorrer sequências
6. **range(start, stop)** — gera sequência (último não entra!)
7. **Desafio — Tabuada** (`tabuada.py`)
8. **Desafio — Tabuada com intervalo** (`tabuada_intervalo.py`)
9. **BugZilla — esquecer `:`**
10. **Listas** — `["Ana", "João", "Davi"]`, índices começam em 0, `len()`
11. **Desafio — Lista de nomes** (`lista_alunos.py`)
12. **Desafio — Adicionando nomes interativamente** (`lista_interativa.py`)
13. **Quiz sobre listas**
14. ~~Link externo do desafio (Vercel)~~ — removido em 2026-07-08, substituído
    pelas **💥 5 Missões finais** dentro do próprio capítulo (ver abaixo)

### Visual obrigatório
- **Loop while** — bolinhas pulando uma a uma com contador atualizando (autoplay)
- **range()** — régua com números acendendo
- **Lista** — quadradinhos com índices acima

### Motion e Arena (adicionados 2026-07-01, padrão dos caps 3.6/05+)
- **Ciclo do while** (dentro da própria seção `#while`): diagrama
  giratório `data-seq` com 3 nós (testa → executa → atualiza) que roda em círculo —
  a própria animação é um loop.
- **🎥 Máquina de execução #1** (`#maquina-while`, após `soma_naturais.py`): executa
  `soma_ate_3.py` (acumulador) com 13 frames. As linhas usam `data-seq-step="2,5,8,11"`
  (lista de quadros) pro destaque **voltar** pra linha do `while` a cada volta.
- **🥷 Arena de Treino Solo** (`#arena-solo` + `#treino-1..6`, antes do desafio final):
  6 treinos graduados ★☆☆→★★★ no padrão olhinho — `conta_de_3.py` (while passo 3),
  `foguete.py` (range passo **negativo**), `soma_impares.py` (range passo + acumulador),
  `convidados.py` (**for + append**), `fila_do_lanche.py` (**índices negativos**),
  `notas_da_turma.py` (for em lista + contadores paralelos + média).
- **🎥 Máquina de execução #2** (`#maquina-break`, após `lista_interativa.py`): executa
  o próprio `lista_interativa.py` (Ana, Bia, "sair") com 14 frames — lista crescendo
  a cada `append` e o momento exato do `break` pulando pra fora.
- **Atenção ao manter:** nº de quadros = nº de `data-seq-frame` (0..N-1, contíguos);
  todo índice listado em `data-seq-step="…"` deve existir como frame. O engine
  (`shared/scripts.js`) aceita `data-seq-step` sem valor (posicional, como no 3.6)
  OU com lista de quadros (necessário pra loops).

### 💥 5 Missões finais (adicionadas 2026-07-08, no lugar do desafio externo)
Evoluções do `lista_interativa.py` no padrão olhinho (`#missoes` + `#missao-1..5`,
entre `#maquina-break` e o quiz). Cada missão reusa o MESMO esqueleto
(lista vazia + `while True` + `input` + `break` no `"sair"` + `append`) e
adiciona UMA ideia nova:
1. `convidados_festa.py` (★☆☆) — mesmo programa, outro contexto + `len()` no final
2. `lista_numerada.py` (★★☆) — exibição numerada com contador em paralelo no `for`
3. `porteiro.py` (★★☆) — barra repetidos; 🆕 `in` dentro do `if` (membership)
4. `media_notas.py` (★★★) — lista de números com `float()`, acumulador, média `:.2f`;
   pegadinha: checar `"sair"` ANTES de converter; bônus BugZilla: divisão por zero
5. `menu_lista.py` (★★★, "chefão") — menu 1/2/3 com `if/elif/else` dentro do loop

---

## 💪 Capítulo 4.5 — 30 Desafios (Caps 1, 2, 3 e 4)
**Pasta:** `capitulos/04b-desafios-caps-1-2-3-4/`
**Cor temática:** lilás + turquesa + verde menta (`--accent6` + `--accent3` + `--accent7`)
**Origem:** segundo treinão de fixação (após o `03b`), antes de funções. Sem conteúdo novo — só prática.

### Estrutura
- Hero + intro + setup PyCharm (projeto `desafio_caps_1_2_3_4`) + "como usar"
- **Bloco 1 — while (1-10):** contar, regressivo, pular de 2 em 2, tabuada, soma com acumulador, sentinela com `break`, média com soma+contagem
- **Bloco 2 — for + range (11-20):** tabuada, soma de pares, range com passo, quadrados (`**`), múltiplos (`%`), intervalo dinâmico, fatorial (acumulador multiplicativo), enumeração, `for + break` com flag
- **Bloco 3 — listas + for (21-30):** percorrer lista, `sum/len`, maior valor manual, contadores em paralelo (aprovado/reprovado, par/ímpar), `enumerate(start=1)`, operador `in`, dois passes (média + acima), lista vazia + `append` até `"fim"`
- Encerramento com stats + ponte pro cap 05

### Padrão por desafio
Igual ao 03b: cabeçalho (n°+filename) → `exercise solo` → `concept` ("O que fazer") → `tip` conceitual → `try-first` 🚨 → `toggler` 👀 com código completo + terminal output.

### Quando manter atualizado
Se adicionar/remover desafios, sincronizar: sidebar do próprio capítulo + card no `index.html` do hub + linha do mapa rápido no fim deste arquivo.

---

## 🏆 Capítulo 3.6 — Super Desafio (Caps 1, 2 e 3)
**Pasta:** `capitulos/03c-super-desafio/`
**Cor temática:** dourado + coral + lilás (`--accent5` + `--accent2` + `--accent6`)
**Origem:** vem **depois** do `03b` (30 desafios) e **antes** do cap 04. Sem conteúdo novo —
só caps 1, 2 e 3 (input/conversão, variáveis, tipos, f-string, if/elif/else, and/or). **Sem loops,
sem listas, sem funções.**

### Estrutura
- Hero + intro ("luta de chefão") + arsenal (revisão caps 1–3) + setup PyCharm (projeto `super_desafio`)
- **Parte A — GUIADO · `cinema_ai.py`** (Bilheteria do Cinema AI): construído em 4 etapas
  (cadastro → preço por faixa de idade com `if/elif/else` → benefício meia-entrada com
  `and/or` → pagamento e troco), depois o programa completo
- **🎥 Máquina de execução:** animação `data-seq` (autoplay) que executa o `cinema_ai.py` linha a
  linha com 7 frames-snapshot das variáveis enchendo — o "motion/remotion" do capítulo
- **BugZilla:** esquecer `int()` na idade → `TypeError` comparando texto com número
- **Parte B — SOZINHO · `parque_ai.py`** (Parque AI Adventure): mesma espinha do Cinema, tema
  diferente, com a reviravolta da regra de **altura** (`idade >= 12 and altura >= 1.40`) pra
  montanha-russa. Padrão olhinho 👀 (concept → tip → try-first → toggler com solução + terminal)
- Encerramento com stats + ponte pro cap 04 (gancho: "atendeu 1 cliente; e se a fila tivesse 50?")

### Motion (atenção ao manter)
A "Máquina de execução" depende do engine `data-seq`/`data-seq-step`/`data-seq-frame` do
`shared/scripts.js`. O atributo `data-seq` fica no `.exec-machine` (ancestral de código E frames).
**Nº de elementos `[data-seq-step]` deve bater com o nº de `[data-seq-frame]`** (hoje 7 e 7) — o
engine usa `Math.max(steps, frames)` como total de quadros; sobra de elementos = quadros em branco.

### Quando manter atualizado
Sincronizar com: card no `index.html` do hub (CAP · 3.6), botão "próximo" do `03b` (aponta pra cá)
e o mapa rápido abaixo.

---

## 🟢 Capítulo 05 — Funções
**Pasta:** `capitulos/05-funcoes/`
**Cor temática:** verde menta + turquesa (`--accent7` + `--accent3`)
**Slides cobertos:** def, parâmetros, retorno, sistema de notas, ranking de alunos

### Tópicos
1. **Por que funções?** — evitar repetir código (analogia: receita reutilizável)
2. **def — criando funções** — `def saudacao(): print(...)`
3. **Desafio — Função de soma** (`func_soma.py`)
4. **Desafio — Saudação personalizada** (`func_saudacao.py`)
5. **Sistema de Notas** (`sistema_notas.py`) — 3 notas → média → aprovado/reprovado
6. **Sistema de Notas com função** (`sistema_notas_func.py`) — refatorando
7. **Mini Projeto — Ranking de Alunos** 🎓 (`ranking_alunos.py`) — `zip()` + `sorted()`
8. **Resumo Parte 02**

### Visual obrigatório
- Caixa "função" com seta de input (parâmetro) e output (retorno)
- Animação de "chamar a função N vezes" mostrando reaproveitamento

---

## 🏆 Capítulo 06 — Desafios Integradores
**Pasta:** `capitulos/06-desafios/`
**Cor temática:** coral + dourado (`--accent2` + `--accent5`)
**Slides cobertos:** 5 sistemas-completos para consolidação

### Os 5 desafios
1. **Sistema de Votação de Filmes** 🎬
   - https://programa-ai-desafio-sistema-de-vota.vercel.app/
2. **Lanchonete AI Burgers** 🍔
   - https://programa-ai-desafio-lanchonete-ai.vercel.app/
3. **Cinema AI** 🎟 — `cinema_ai.py`
4. **AI Arcade** 🎮 — `ai_arcade.py`
5. **Academia AI Fitness** 🏋️ — `academia_ai.py`

Cada desafio tem:
- Cenário ilustrado
- Menu mockup (terminal estilizado)
- Regras numeradas
- Dicas de quais conceitos usar (loops, listas, funções, condicionais)
- Olhinho 👀 com solução completa
- Link externo (quando aplicável)

---

## 🟦 Capítulo 07 — Dicionários
**Pasta:** `capitulos/07-dicionarios/`
**Cor temática:** roxo + lilás (`--accent` + `--accent6`)
**Slides cobertos:** Parte 03 — dict, cadastro, atualizar, lista de dicts, sistema de cadastro

### Tópicos
1. **Quiz relembrando** — for? lista?
2. **Dicionários — chave: valor** — `{"nome": "Kelson", "idade": 33}`
3. **Desafio — `cadastro_dicionario.py`** (nome, idade, curso)
4. **Desafio — `cadastro_pet.py`** (nome, espécie, idade)
5. **Desafio — `atualizar_dados_aluno.py`**
6. **Lista de dicionários** — mini-cadastros
7. **Desafio Prático — `sistema_cadastro.py`** (menu add/listar/buscar/sair)
8. **Desafio para Casa — `sistema_cadastro_pet.py`** (versão pet)
9. **Resumo Parte 03**

### Visual obrigatório
- Dicionário desenhado: caixa grande com pares "chave → valor"
- Lista de dicionários: prateleira com mini-fichas

---

## 🟡 Capítulo 08 — JSON (Persistência básica)
**Pasta:** `capitulos/08-json/`
**Cor temática:** dourado + turquesa (`--accent5` + `--accent3`)
**Slides cobertos:** "E se fecharmos o programa?", JSON, salvar_dados, ler_dados, sistema_cadastro_json

### Tópicos
1. **O problema** — fechei o programa e tudo sumiu! 😱
2. **JSON = JavaScript Object Notation** — texto que parece dicionário Python
3. **Bora Codar — `salvar_dados.py`** (`json.dump`)
4. **Bora Codar — `ler_dados.py`** (`json.load`)
5. **Desafio Prático — `sistema_cadastro_json.py`** — pega o do cap 07 e salva ao sair, lê ao iniciar
6. **Resumo / ponte para TinyDB**

### Visual obrigatório
- "Programa fecha → dados somem" → "JSON salva em arquivo"
- Estrutura de um arquivo `.json` com syntax highlight

---

## 🟧 Capítulo 09 — TinyDB (migrado da v1)
**Pasta:** `capitulos/09-tinydb/`
**Origem:** `../programacao-iniciantes/index.html` (seção TinyDB)

### Manter da v1
- Estrutura: O Problema → O que é TinyDB? → Insert → Read → Search → Update → Remove → CRUD resumo → Tabelas → Demo → Desafio → Resumo
- Demo interativa
- Link externo se houver

### Adaptar
- Novos imports do `shared/`
- Sidebar nav ajustada (link ← hub)
- Coerência com cap 08 (JSON é evolução para TinyDB)

---

## 🔴 Capítulo 10 — Streamlit (migrado da v1)
**Pasta:** `capitulos/10-streamlit/`
**Origem:** `../programacao-iniciantes/index.html` (seção Streamlit)

### Manter da v1
- O que é Streamlit? Para que serve? Componentes (text, input, button, etc)
- Exercícios e demos
- Visual do "browser" mockado

### Adaptar
- Novos imports do `shared/`
- Coerência com cap 09 (Streamlit consome dados do TinyDB)
- Encerramento épico do bootcamp 🎉

---

## 📊 Mapa rápido (TL;DR)

| # | Capítulo | Tema | Conceitos-chave |
|---|---|---|---|
| 01 | Boas-vindas | Hello world | print, input, primeira execução |
| 02 | Variáveis & Tipos | Caixinhas | str, int, float, bool, f-string |
| 03 | Condicionais | Decisões | if/elif/else, operadores |
| 3.6 | Super Desafio (Caps 1-3) | Consolidar | Cinema AI (guiado) + Parque AI (solo), só if/elif/else + and/or |
| 04 | Loops & Listas | Repetir | while, for, range, listas |
| 4.5 | 30 Desafios (Caps 1-4) | Fixar | while + for + range + listas (treinão) |
| 05 | Funções | Reutilizar | def, parâmetros, retorno |
| 06 | Desafios | Consolidar | 5 mini-sistemas |
| 07 | Dicionários | Estruturar | dict, lista de dicts |
| 08 | JSON | Salvar | json.dump/load |
| 09 | TinyDB | Banco mini | CRUD em arquivo |
| 10 | Streamlit | UI | apps web em Python |

## 🔗 Links externos do bootcamp
- Desafio 01: https://desafio-01-programacao-iniciantes-p.vercel.app/
- Sistema de Votação: https://programa-ai-desafio-sistema-de-vota.vercel.app/
- Lanchonete AI: https://programa-ai-desafio-lanchonete-ai.vercel.app/
