import bibtexparser
from pathlib import Path
import re
from pylatexenc.latex2text import LatexNodes2Text

# Função para sanitizar strings do cabeçalho YAML
def sanitize(text):
    return text.replace(":", " -") if text else ""

def latex_to_unicode(text):
    replacements = {
        r"{\'a}": "á", r"{\^a}": "â", r"{\`a}": "à", r"{\~a}": "ã",
        r"{\c c}": "ç", r"{\"o}": "ö", r"{\"u}": "ü",
        r"{\^e}": "ê", r"{\'e}": "é", r"{\`e}": "è",
        r"{\~o}": "õ", r"{\~n}": "ñ",
        r"{\'i}": "í", r"{\^i}": "î",
        r"{\^o}": "ô", r"{\'o}": "ó",
        r"{\^u}": "û", r"{\'u}": "ú",
        r"{\ss}": "ß",
        r"{\&}": "&",
    }
    for latex, char in replacements.items():
        text = text.replace(latex, char)
    return re.sub(r"[{}]", "", text)

def latex_to_text(text):
    return LatexNodes2Text().latex_to_text(text)

# Caminhos
bib_path = Path("Thesis/zotero_references.bib")
output_dir = Path("Vault/2 - Source Material")
output_dir.mkdir(parents=True, exist_ok=True)

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

for entry in bib_database.entries:
    citekey = entry.get("ID", "unknown")
    title = sanitize(entry.get("title", "").replace("{", "").replace("}", ""))
    authors = [sanitize(author.strip()) for author in entry.get("author", "").replace("\n", "").split(" and ")]
    year = sanitize(entry.get("year", ""))
    journal = sanitize(entry.get("journal", ""))
    keywords = [
        sanitize(re.sub(r"[()]", "", kw.strip().replace(" ", "_")))
        for kw in entry.get("keywords", "").split(",")
    ]
    note = entry.get("note", "").strip()

    vocab_notes, tech_notes, struct_notes, important_notes = [], [], [], []

    for line in note.split("\\par"):
        line = line.strip()
        if not line:
            continue
        if "Vocabulary:" in line:
            match = re.match(r'(.*?)Vocabulary:\s*(.*)', line)
            if match:
                quote, meaning = match.groups()
                quote = quote.replace("``", "`").replace("''", "`")
                quote = latex_to_text(quote.strip())
                meaning = latex_to_text(meaning.strip())
                vocab_notes.append(f"- {quote.strip()}\n\t{meaning.strip()}")
        elif "Technical:" in line:
            match = re.match(r'(.*?)Technical:\s*(.*)', line)
            if match:
                quote, meaning = match.groups()
                quote = quote.replace("``", "`").replace("''", "`")
                quote = latex_to_text(quote.strip())
                meaning = latex_to_text(meaning.strip())
                tech_notes.append(f"- {quote.strip()}\n\t{meaning.strip()}")
        elif "Structure:" in line:
            match = re.match(r'(.*?)Structure:\s*(.*)', line)
            if match:
                quote, meaning = match.groups()
                quote = quote.replace("``", "`").replace("''", "`")
                quote = latex_to_text(quote.strip())
                meaning = latex_to_text(meaning.strip())
                struct_notes.append(f"- {quote.strip()}\n\t{meaning.strip()}")
        elif "Important" in line:
            line = line.replace("``", "`").replace("''", "`")
            line = latex_to_text(line.strip())
            important_notes.append(f"- {line.strip()}")

    zotero_notes = f"""## 📌 Notas (Zotero)
### 📖 Vocabulário
{chr(10).join(vocab_notes)}

### 🛠️ Conceitos técnicos
{chr(10).join(tech_notes)}

### 🧱 Estruturas
{chr(10).join(struct_notes)}

### ⚠️ Importante
{chr(10).join(important_notes)}
"""

    additional_sections = {
        "## 🧠 Minhas reflexões": "- ",
        "## 🔗 Conexões": "- ",
        "## ✅ Próximos passos": "- ",
    }

    md_file = output_dir / f"{citekey}.md"

    if md_file.exists():
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Atualiza a seção Zotero
        content = re.sub(
            r"## 📌 Notas \(Zotero\)(.*?)(?=^## |\Z)",
            lambda m: zotero_notes + "\n",
            content,
            flags=re.DOTALL | re.MULTILINE
        )

        # Garante que cada seção adicional exista
        for section_title, section_default in additional_sections.items():
            if not re.search(rf"^{re.escape(section_title)}\s*", content, flags=re.MULTILINE):
                content += f"\n{section_title}\n{section_default}\n"

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(content)

    else:
        # Arquivo novo: inclui todas as seções
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(f"""---
title: {title}
authors:
{chr(10).join([f"  - {author}" for author in authors])}
year: {year}
source: {journal}
zotero-key: {citekey}
tags:
{chr(10).join([f"  - {kw}" for kw in keywords if kw])}
---

{zotero_notes}

## 🧠 Minhas reflexões
- 

## 🔗 Conexões
- 

## ✅ Próximos passos
- 
""")

