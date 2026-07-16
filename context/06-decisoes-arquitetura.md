# 6. Decisões de Arquitetura

> Registro cronológico das decisões importantes. **Sempre** adicionar uma entrada quando algo estrutural mudar. Não apague decisões antigas — marque como "superseded".

---

## 📅 2026-04-27 — Setup inicial da v2

### Contexto
A v1 (`programacao-iniciantes/index.html`) cobria apenas TinyDB e Streamlit em um único HTML de 2.851 linhas. O professor quer levar **o bootcamp inteiro** para HTML didático, com o suprassumo da didática, fluxos animados com autoplay, e padrão olhinho 👀 (inspirado no desafio Petshop do `backend-fullstack/`).

### Decisões tomadas

#### 1. Arquitetura modular (uma pasta por capítulo)
- **Decidido:** cada capítulo vive em `capitulos/<NN-slug>/index.html`, com seu próprio HTML.
- **Alternativa rejeitada:** um único HTML gigante (que não escala) ou SPA com rotas (over-engineering, exige build).
- **Trade-off:** alguma duplicação no `<head>` por arquivo, mas autonomia total e tempo de carga rápido.

#### 2. CSS/JS compartilhados em `shared/`
- **Decidido:** três arquivos CSS (`styles.css`, `components.css`, `animations.css`) e um JS (`scripts.js`).
- **Importação:** path relativo `../../shared/` a partir de cada capítulo.
- **Por quê 3 CSS?** separação clara: tokens base / componentes / animações. Deixa claro onde mexer.
- **Alternativa rejeitada:** CSS em `<style>` inline em cada HTML (duplicação massiva).

#### 3. Hub via `index.html` raiz
- **Decidido:** o `index.html` raiz é uma landing visual com 10 cards de capítulo, mostrando progresso (futuramente via `localStorage`), professor, instituição.
- **Alternativa rejeitada:** redirecionar direto pro capítulo 01 (perde overview).

#### 4. Sem build, sem npm, sem framework
- **Decidido:** HTML5 + CSS3 + JS vanilla. Cada arquivo abre direto no navegador.
- **Por quê:** o usuário (professor) precisa editar de forma simples. Build adiciona ritual sem benefício real para conteúdo estático.
- **Reavaliar quando:** se conteúdo passar de 30 capítulos OU precisar de busca full-text OU múltiplos professores editando simultaneamente.

#### 5. Pasta `context/` com .MD versionados
- **Decidido:** documentação persistente em markdown, indexada por `context/README.md`. CLAUDE.md raiz aponta para essa pasta.
- **Por quê:** prompt-engineering moderno — IAs (e humanos) chegam ao projeto e em 5min têm o panorama completo.
- **Padrão de boas práticas:** seguir o estilo do `AGENTS.md` raiz, mas mais granular (um arquivo por tema).

#### 6. Padrão "olhinho 👀" obrigatório em exercícios
- **Decidido:** todo exercício individual ou para casa segue o padrão de `dica → 🚨 try-first → 👀 toggler com solução`. Documentado em `05-padrao-olhinho.md`.
- **Inspiração:** desafio Petshop em `backend-fullstack/index.html`.

#### 7. Ordem dos capítulos = ordem do PDF
- **Decidido:** seguir literalmente a ordem dos slides oficiais. TinyDB e Streamlit (que existiam na v1) viram capítulos 09 e 10.
- **Liberdade didática:** podemos melhorar a apresentação dentro de cada capítulo, mas NÃO mover tópicos entre capítulos.

#### 8. Animações com autoplay (não exigem clique)
- **Decidido:** todo fluxo importante anima automaticamente quando entra no viewport (via `IntersectionObserver`).
- **Por quê:** público iniciante não descobre que pode interagir. Um GIF/animação rodando atrai a atenção e ensina sozinho.
- **Detalhe:** não criar animações infinitas que distraem — preferem rodar 1-2 vezes e parar em estado estável.

#### 9. Idioma e tom
- **Decidido:** português brasileiro 100%. Tom leve, frases curtas, "você" (não "o aluno"), emojis pontuais.
- **Estrangeirismos** só quando inevitável (`input`, `print`, `for`, `while`).

#### 10. BugZilla como personagem recorrente
- **Decidido:** manter o "vilão amigável" do PDF. Aparece em todos os capítulos com erros canônicos. Cor: `--bug: #ff4757`.

### Pendências reconhecidas
- Não temos sistema de progresso (quanto o aluno já viu) — pode entrar via `localStorage` em iteração futura
- Não temos busca full-text — não é prioridade dado o volume atual
- Não temos imagens próprias — usaremos emojis e SVG inline; quando necessárias, virão em `assets/images/`
- Os capítulos 09 (TinyDB) e 10 (Streamlit) precisam ser **migrados**, não recriados — preservar conteúdo e demos da v1

---

## 📅 2026-05-18 — Arena de Treino Solo + motor de auto-flow genérico

### Contexto
Os capítulos 05, 06 e 07 tinham poucos exercícios "faça sozinho" (3, 5 e 4
respectivamente) — pouco volume de prática individual. O professor pediu mais
exercícios solo e mais didática (fluxos animados, playgrounds, "fator UAU").

### Decisão
1. **Motor de auto-flow declarativo em `shared/scripts.js`** — `initSeqLoops()`.
   Qualquer elemento com `data-seq="<ms>"` vira um fluxo automático: filhos com
   `data-seq-step` recebem `.active` um por vez; filhos com `data-seq-frame="N"`
   recebem `.on` quando é a vez deles. Dispara via `IntersectionObserver`
   (autoplay, decisão nº8). Substitui o padrão antigo de escrever um
   `setInterval` à mão por capítulo (`reuseGrid`, `skeletonFlow`).
2. **Componentes de "Arena" em `shared/components.css`** — `.arena-banner`,
   `.arena-track`/`.at-dot`, `.drill-level` (selo de dificuldade ★☆☆/★★☆/★★★,
   classes `lv1/lv2/lv3`) e `.drill-tag`. Reutilizáveis por qualquer capítulo
   que tenha um banco de treinos solo.
3. **Seção "Arena de Treino Solo"** padrão no fim de cada capítulo (antes do
   projeto final / BugZilla): banner + trilha de dificuldade + 1 componente
   auto-flow "UAU" + 6 treinos solo graduados, cada um no padrão olhinho.
   Aplicado aos caps 05 (Cinema da Função), 06 (Ciclo do while True) e
   07 (For percorrendo as fichas). Caps 05/06/07 foram de 3/5/4 → 9/11/10
   exercícios solo.

### Trade-offs
- O auto-flow do componente fica em CSS local do capítulo (visual específico),
  só o motor JS é compartilhado — aceitável: o comportamento é genérico, a
  estética não.
- Cap 06 ganhou treinos mais curtos (15-25 linhas) em vez de mais "desafios
  grandes": mais repetições do mesmo esqueleto fixam melhor que poucos sistemas
  longos.

### Status: ativo

---

## 📅 2026-06-06 — Caps 09 e 10 elevados ao padrão dos caps 07/08

### Contexto
Os caps 09 (TinyDB) e 10 (Streamlit) foram migrados da v1 e estavam uma
geração atrás: pouquíssimo "olhinho" (3 try-first vs 21 no cap 08), sem Arena
Solo, sem fluxo animado, e sem a desativação de ligatures obrigatória.

### Decisão
- **Arena Solo** em ambos: banner + trilha + 5 treinos progressivos
  (`treino-1`..`treino-5`, lv1→lv2) com dica + `try-first` + `toggler`,
  antes do desafio-boss que já existia.
- **Fluxo animado** (`flow-container autoplay`): ciclo CRUD no cap 09 e ciclo
  de reatividade no cap 10.
- **Forja de Tela** (cap 10): engine `shared/tag-forge.js` reaproveitado do
  material Fullstack — funções `st.*` "voam" do editor e viram a tela real
  (Motion via CDN, com fallback estático + `prefers-reduced-motion`). CSS no
  fim de `shared/components.css`. Alvo de pintura = qualquer `[data-paint]`
  dentro de um `.browser-mockup`.
- **Streamlit sempre mostra a tela resultante**: todo treino e o forge têm
  `browser-mockup` com o resultado.
- **Ligatures off** adicionado ao `<style>` local dos dois caps.
- Cap 09: quiz de fixação (3 perguntas) + 4º bug no BugZilla (NameError/import).

### Trade-offs
- `tag-forge.js` puxa Motion da CDN — offline cai no fallback (revela tudo sem
  voo). Aceitável: nunca quebra a página.
- Mockups são estáticos (não é o Streamlit real). Continua sendo a melhor forma
  de mostrar o resultado sem rodar Python no navegador.

### Status: ativo

---

## 📅 2026-07-01 — Cap 04 elevado ao padrão dos caps 3.5/3.6 + engine `data-seq-step` com lista de quadros

### Contexto
O cap 04 (Loops e Listas) tinha bons playgrounds interativos, mas estava uma geração
atrás dos caps 3.5/3.6: sem Máquina de Execução (o "motion"), sem Arena de Treino Solo,
e com gaps didáticos — a "volta" do loop era invisível, o acumulador só existia em código
estático, `break` só em texto, `range()` com passo negativo ausente, nenhum exercício de
`for + append` nem de índices negativos.

### Decisão
1. **Engine `data-seq` estendido (`shared/scripts.js`)** — `data-seq-step` agora aceita
   valor opcional com lista de quadros (`data-seq-step="2,5,8,11"`): o elemento fica
   `.active` nos quadros listados. Sem valor, continua posicional (retrocompatível com
   o cap 3.6). Motivação: animar um **loop** exige que o destaque de linha **volte** a
   uma linha já visitada — impossível no esquema posicional, que serve só pra código linear.
2. **Duas Máquinas de Execução no cap 04** (mesmo CSS/estrutura do 3.6, cores lilás):
   `#maquina-while` (acumulador `soma_ate_3.py`, 13 frames, destaca a VOLTA do destaque)
   e `#maquina-break` (`lista_interativa.py` com Ana/Bia/"sair", 14 frames, lista
   crescendo no `append` e saída pelo `break`).
3. **Ciclo do while** — diagrama giratório `data-seq` de 3 nós (testa → executa →
   atualiza) na seção `#while`; a animação gira em círculo, espelhando o próprio loop.
4. **Arena de Treino Solo** (padrão dos caps 05-10): banner + trilha + 6 treinos
   graduados antes do desafio final, fechando os gaps (passo negativo, for+append,
   índices negativos, contadores paralelos).
5. Hub: card do cap 04 ganhou pills `🎥 motion` e `arena 🥷`.

### Trade-offs
- As máquinas do cap 04 têm 13-14 frames (vs 7 no 3.6) → ciclo de ~25s. Aceitável:
  mostrar só 1 volta do loop mataria a didática; o loop da animação recomeça sozinho.
- A Arena do cap 04 não tem componente auto-flow próprio (padrão dos caps 05-07):
  o capítulo já tem 3 animações data-seq — uma 4ª seria ruído.

### Status: ativo

---

## 📅 2026-07-14 — Cap 08 vira só fundamento de JSON; persistência = só TinyDB

### Contexto
O cap 08 (JSON) tinha metade fundamento de formato + metade persistência com arquivo
(`json.dump`/`json.load`/`with open`/modos `"r"`/`"w"`/`try-except`, arena de 6 treinos de
arquivo e desafio `sistema_cadastro_json.py`). Isso criava DOIS mecanismos de persistência no
bootcamp (JSON na mão no cap 08 + TinyDB no cap 09), sobrecarregando o iniciante. O prof. Kelson
decidiu ter **uma única** persistência no material (TinyDB), mas manter o embasamento de JSON
**antes** dele — porque o TinyDB salva em `.json` por baixo dos panos.

### Decisão
- Cap 08 recortado pra **"JSON: a língua dos dados"** — só o formato, sem gravar arquivo.
- **Removido:** `import json`/`json.dump`/`json.load`/`with open`, seção `#magia-fluxo` (salvar/ler),
  `#salvar-dados`, `#ler-dados`, `#with-open`, chapter-divider "Hora de Persistir", a arena de 6
  treinos de arquivo e o desafio `sistema_cadastro_json.py`. BugZilla trocado (era import/arquivo
  vazio/modo errado → agora aspas simples/`True` maiúsculo/vírgula sobrando).
- **Adicionado:** `#regras-json` (4 regras + 6 tipos), `#traducao` (fluxo dict⇄JSON + "não faz na
  mão, o TinyDB faz"), `#onde-json` (APIs/config/TinyDB/IA). **Mantido** o playground tradutor
  (WOW do cap) e o quiz.
- 2115 → ~1318 linhas. Sidebar, hero, título, resumo/ponte e card do hub atualizados.
- Cap 09 (`#ponte` e `#o-problema`) reescrito pra NÃO assumir que o aluno já usou `json.dump` nem
  escreveu `sistema_cadastro_json.py` — agora contrasta TinyDB com "fazer JSON na mão".
- `context/04-conteudo-bootcamp.md` atualizado (seção cap 08 + TL;DR) com aviso de não reintroduzir.

### Trade-offs
- Cap 08 fica mais curto e "teórico" (sem exercício de codar). Aceitável: o objetivo é ser ponte
  conceitual pro cap 09, onde a prática de persistência acontece de fato.
- O playground ainda referencia a tradução `dumps`/`loads` como conceito (setas relabeladas pra
  "traduz"), sem ensinar as funções.

### Status: ativo

---

## 📅 2026-07-16 — Novo cap 7.5: 3 Desafios Chefões (entre Dicionários e JSON)

### Contexto
Depois do cap 07 o aluno domina todas as estruturas do "Python de terminal" (dict fecha o ciclo),
mas ia direto pro cap 08 (JSON, teórico, sem codar). Faltava um momento de consolidação TOTAL —
os treinões 3.5/4.5 cobrem até loops/listas e o cap 06 é anterior aos dicionários. O professor
pediu 3 desafios bem didáticos com tudo visto até então, com olhinho mas incentivando a não ver.

### Decisão
1. **Novo capítulo `capitulos/07b-desafios-caps-1-a-7/`** (CAP · 7.5), com 3 desafios em escada:
   `playlist_ai.py` (★☆☆), `mercadinho_ai.py` (★★☆, reintroduz `def`) e `banco_ai.py`
   (★★★, `def` + `return` + menu completo). Framing de "fase de chefão": nenhum golpe novo.
2. **Padrão de desafio mais rico** que o dos treinões: cenário (`boss-banner`) + terminal
   `data-typewriter` mostrando o programa-alvo + regras numeradas + dica que cita exercícios
   anteriores POR NOME (playlist ← adicionar_nomes/cadastro_dicionario; banco ← sistema_cadastro).
3. **Escada anti-spoiler em 2 degraus**: toggler 🆘 "empurrãozinho" (roteiro em palavras, zero
   código) ANTES do olhinho 👀. Mais o "Juramento do olhinho" (botão interativo) no início.
   Objetivo: dar saída pro aluno travado sem entregar a solução.
4. **`None` como único "tempero novo"**, apresentado explicitamente como bônus (retorno de
   `buscar_conta`), ancorado no `.get()` do cap 07. Fora isso, conteúdo 100% já visto.
5. **Navegação re-roteada**: ponte do cap 07 → 7.5 (JSON citado como "depois"); encerramento do
   7.5 reusa o gancho "fechou o programa, dados sumiram" → cap 08. Card novo no hub.

### Trade-offs
- São só 3 desafios (vs 30 dos treinões) — proposital: aqui o objetivo é integração em sistemas
  completos, não volume de repetição.
- O typewriter mostra a "resposta comportamental" antes do aluno codar — decisão consciente:
  ver O QUE construir não revela COMO (o código continua atrás do olhinho).

### Status: ativo

---

## 📅 [próxima entrada]

> Adicione aqui ao tomar uma nova decisão estrutural. Formato:
>
> ```
> ## 📅 YYYY-MM-DD — Resumo curto
> ### Contexto
> ### Decisão
> ### Trade-offs
> ### Status: ativo / superseded por (link)
> ```
