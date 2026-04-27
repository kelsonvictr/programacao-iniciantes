# 📚 Pasta de contexto — programacao-iniciantes-v2

Esta pasta guarda **toda a documentação de contexto** do projeto que não é código. Foi pensada para que **uma IA chegando do zero** (Claude, Copilot, ChatGPT) consiga reconstruir mentalmente o projeto inteiro lendo esses arquivos.

## 🗂️ Índice

| Arquivo | Quando consultar |
|---|---|
| [`01-projeto-overview.md`](./01-projeto-overview.md) | Para entender o **propósito** do projeto, público-alvo, professor, contexto institucional |
| [`02-design-system.md`](./02-design-system.md) | Antes de escrever **CSS** ou criar novos componentes visuais |
| [`03-padroes-didaticos.md`](./03-padroes-didaticos.md) | Antes de escrever **conteúdo educacional** — analogias, ordem dos blocos, tom |
| [`04-conteudo-bootcamp.md`](./04-conteudo-bootcamp.md) | **Sempre** antes de criar/editar um capítulo — é a fonte da verdade dos tópicos |
| [`05-padrao-olhinho.md`](./05-padrao-olhinho.md) | Para criar exercícios com spoiler de resposta (dica → tente sozinho → 👀 ver código) |
| [`06-decisoes-arquitetura.md`](./06-decisoes-arquitetura.md) | Para entender **por que** as coisas estão assim — e atualizar quando mudar |

## 🔄 Como manter atualizado

- Quando uma decisão arquitetural for tomada (ex: adicionar Tailwind, mudar bundling), registre em `06-decisoes-arquitetura.md` com data
- Quando novos componentes visuais forem padronizados, registre em `02-design-system.md`
- Quando a ordem ou ementa dos capítulos mudar, atualize `04-conteudo-bootcamp.md`
- **Não duplique** informação entre arquivos — prefira referenciar (`veja 02-design-system.md#cores`)

## ⚠️ O que NÃO vai aqui

- Conteúdo dos capítulos (vai em `capitulos/<nome>/index.html`)
- Código compartilhado (vai em `shared/`)
- TODO de tarefas em andamento (use o sistema de tarefas da IA, não markdown)
