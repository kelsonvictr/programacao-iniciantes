#!/usr/bin/env python3
"""
Extrai todos os HTMLs do bootcamp programacao-iniciantes-v2 para arquivos .txt
em texto plano, preservando todo o conteudo (textos, codigos, comandos, listas).

Estrutura do projeto:
  - index.html                       -> hub com cards dos 10 capitulos
  - capitulos/<NN-slug>/index.html   -> um HTML auto-contido por capitulo (10)
  - sobre/index.html                 -> pagina "sobre"

Para cada HTML, gera um .txt correspondente nesta pasta, com prefixo numerico
para preservar a ordem.
"""
import os
import re
from bs4 import BeautifulSoup, NavigableString, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# (numero, caminho_relativo_ao_ROOT, titulo)
SOURCES = [
    ("00", "index.html",                                   "Hub - Visao Geral do Bootcamp"),
    ("01", "capitulos/01-boas-vindas/index.html",          "Capitulo 01 - Boas-vindas e Fundamentos"),
    ("02", "capitulos/02-variaveis-tipos/index.html",      "Capitulo 02 - Variaveis e Tipos"),
    ("03", "capitulos/03-condicionais/index.html",         "Capitulo 03 - Condicionais"),
    ("04", "capitulos/04-loops-listas/index.html",         "Capitulo 04 - Loops e Listas"),
    ("05", "capitulos/05-funcoes/index.html",              "Capitulo 05 - Funcoes"),
    ("06", "capitulos/06-desafios/index.html",             "Capitulo 06 - Desafios"),
    ("07", "capitulos/07-dicionarios/index.html",          "Capitulo 07 - Dicionarios"),
    ("08", "capitulos/08-json/index.html",                 "Capitulo 08 - JSON"),
    ("09", "capitulos/09-tinydb/index.html",               "Capitulo 09 - TinyDB"),
    ("10", "capitulos/10-streamlit/index.html",            "Capitulo 10 - Streamlit"),
    ("11", "sobre/index.html",                             "Sobre"),
]


def slugify(s):
    s = s.lower()
    s = re.sub(r"[áàãâä]", "a", s)
    s = re.sub(r"[éèêë]", "e", s)
    s = re.sub(r"[íìîï]", "i", s)
    s = re.sub(r"[óòõôö]", "o", s)
    s = re.sub(r"[úùûü]", "u", s)
    s = re.sub(r"[ç]", "c", s)
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


BLOCK_TAGS = {
    "p", "div", "section", "header", "footer", "nav", "article", "aside",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "ul", "ol", "li", "dl", "dt", "dd",
    "table", "thead", "tbody", "tfoot", "tr",
    "blockquote", "pre", "figure", "figcaption",
    "hr", "br",
}

# Classes de "chrome" visual ou navegacao a ignorar (nao sao conteudo didatico).
SKIP_CLASSES = {
    "bg-grid", "bg-orbs", "orb",
    "progress-track", "progress-bar",
    "menu-toggle", "sidebar-nav", "sidebar-close",
    # componentes interativos (sliders, playgrounds) — viram lixo em texto plano
    "live-playground", "lp-slider-labels", "lp-orb2",
}

# IDs equivalentes a ignorar (mesmo motivo).
SKIP_IDS = {"sidebar"}


def has_class(node, cls):
    if not isinstance(node, Tag):
        return False
    classes = node.get("class") or []
    return cls in classes


def node_should_skip(node):
    if not isinstance(node, Tag):
        return False
    classes = set(node.get("class") or [])
    if classes & SKIP_CLASSES:
        return True
    nid = node.get("id")
    if nid and nid in SKIP_IDS:
        return True
    return False


def collect_text(node):
    if node is None:
        return ""
    txt = node.get_text(separator=" ", strip=False) if isinstance(node, Tag) else str(node)
    return re.sub(r"\s+", " ", txt).strip()


def render(node, out, in_pre=False, tooltip_buffer=None):
    if isinstance(node, NavigableString):
        text = str(node)
        if in_pre:
            out.append(text)
        else:
            text = re.sub(r"[ \t\r\f\v]+", " ", text)
            text = text.replace("\n", " ")
            out.append(text)
        return

    if not isinstance(node, Tag):
        return

    name = node.name.lower() if node.name else ""

    if name in {"script", "style", "noscript", "svg", "canvas", "iframe", "meta", "link"}:
        return

    if node_should_skip(node):
        return

    if has_class(node, "line-numbers"):
        return

    if has_class(node, "anno-tooltip"):
        if tooltip_buffer is not None:
            tip_text = collect_text(node)
            if tip_text:
                tooltip_buffer.append(tip_text)
        return

    if name == "br":
        out.append("\n")
        return

    if name == "hr":
        out.append("\n----------\n")
        return

    if name == "pre":
        local_tips = []
        out.append("\n\n```\n")
        for child in node.children:
            render(child, out, in_pre=True, tooltip_buffer=local_tips)
        if out and not out[-1].endswith("\n"):
            out.append("\n")
        out.append("```\n")
        if local_tips:
            out.append("\nAnotacoes:\n")
            for t in local_tips:
                out.append(f"- {t}\n")
        out.append("\n")
        return

    if name == "code" and not in_pre:
        out.append("`")
        for child in node.children:
            render(child, out, in_pre=True, tooltip_buffer=tooltip_buffer)
        out.append("`")
        return

    if name == "li":
        out.append("\n- ")
        for child in node.children:
            render(child, out, in_pre=in_pre, tooltip_buffer=tooltip_buffer)
        return

    if name == "tr":
        cells = []
        for cell in node.find_all(["td", "th"], recursive=False):
            buf = []
            for child in cell.children:
                render(child, buf, in_pre=False, tooltip_buffer=tooltip_buffer)
            cells.append(re.sub(r"\s+", " ", "".join(buf)).strip())
        out.append("\n" + " | ".join(cells))
        return

    is_block = name in BLOCK_TAGS

    if is_block:
        out.append("\n")

    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        out.append("\n" + ("#" * level) + " ")

    for child in node.children:
        render(child, out, in_pre=in_pre, tooltip_buffer=tooltip_buffer)

    if is_block:
        out.append("\n")


def clean_output(text):
    lines = text.split("\n")
    cleaned = []
    in_code = False
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
            cleaned.append(ln.rstrip())
            continue
        if in_code:
            cleaned.append(ln)
        else:
            ln = re.sub(r"[ \t]+", " ", ln)
            ln = ln.strip()
            cleaned.append(ln)
    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def extract_one(rel_path, num, title):
    abspath = os.path.join(ROOT, rel_path)
    if not os.path.isfile(abspath):
        print(f"AVISO: arquivo nao encontrado: {rel_path}")
        return None

    with open(abspath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    body = soup.body or soup

    out = []
    out.append(f"# {title}\n")
    out.append(f"(fonte: {rel_path})\n\n")

    for child in body.children:
        buf = []
        render(child, buf, in_pre=False)
        out.append("".join(buf))

    text = clean_output("".join(out))
    fname = f"{num}_{slugify(title)}.txt"
    fpath = os.path.join(HERE, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(text)
    return fname, len(text)


def main():
    written = 0
    for num, rel_path, title in SOURCES:
        result = extract_one(rel_path, num, title)
        if result is None:
            continue
        fname, size = result
        written += 1
        print(f"OK  {fname}  ({size} chars)")

    print(f"\nTotal: {written}/{len(SOURCES)} arquivos gerados.")


if __name__ == "__main__":
    main()
