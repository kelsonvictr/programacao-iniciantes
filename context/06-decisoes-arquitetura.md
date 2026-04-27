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
