import bibtexparser
from pathlib import Path
import re
from pylatexenc.latex2text import LatexNodes2Text

# Função para sanitizar strings do cabeçalho YAML
def sanitize(text):
    return text.replace(":", " -") if text else ""

def latex_to_text(text):
    return LatexNodes2Text().latex_to_text(text)

def summarize_authors(authors):
    surnames = [author.split(",")[0].strip() for author in authors if author.strip()]
    if len(surnames) == 1:
        return surnames[0]
    elif len(surnames) == 2:
        return f"{surnames[0]} and {surnames[1]}"
    elif len(surnames) > 2:
        return f"{surnames[0]} et al."
    else:
        return ""

# Caminhos
bib_path = Path("Thesis/zotero_references.bib")
output_dir = Path("Vault/2 - Source Material/Articles")
template_path = Path("Vault/6 - Templates/article_notes_template.md")
zotero_template_path = Path("Vault/6 - Templates/zotero_notes_template.md")
output_dir.mkdir(parents=True, exist_ok=True)

# Lê os templates
template_text = template_path.read_text(encoding="utf-8")
zotero_template_text = zotero_template_path.read_text(encoding="utf-8")

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

for entry in bib_database.entries:
    if entry.get("ENTRYTYPE") != "article":
        continue

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

    vocab_notes, tech_notes, translate_notes, important_notes = [], [], [], []

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
        elif "Translate:" in line:
            match = re.match(r'(.*?)Translate:\s*(.*)', line)
            if match:
                quote, meaning = match.groups()
                quote = quote.replace("``", "`").replace("''", "`")
                quote = latex_to_text(quote.strip())
                meaning = latex_to_text(meaning.strip())
                translate_notes.append(f"- {quote.strip()}\n\t{meaning.strip()}")
        elif "Important" in line:
            line = line.replace("``", "`").replace("''", "`")
            line = latex_to_text(line.strip())
            important_notes.append(f"- {line.strip()}")

    # Preenche o template de notas Zotero
    zotero_notes = zotero_template_text
    zotero_notes = zotero_notes.replace("{{vocab_notes}}", "\n".join(vocab_notes))
    zotero_notes = zotero_notes.replace("{{tech_notes}}", "\n".join(tech_notes))
    zotero_notes = zotero_notes.replace("{{translate_notes}}", "\n".join(translate_notes))
    zotero_notes = zotero_notes.replace("{{important_notes}}", "\n".join(important_notes))

    additional_sections = {
        "## 🧠 My reflections": "- ",
        "## 🔗 Connections": "- ",
        "## ✅ Next steps": "- ",
    }

    author_summary = summarize_authors(authors)
    md_file = output_dir / f"{title} ({author_summary}).md"

    if md_file.exists():
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Atualiza a seção Zotero
        content = re.sub(
            r"## 📌 Notes \(Zotero\)(.*?)(?=^## |\Z)",
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
        print(f"[✎] Updated: {md_file.name}")
    else:
        # Substituições no template principal
        rendered_md = template_text
        rendered_md = rendered_md.replace("{{title}}", title)
        rendered_md = rendered_md.replace("{{authors}}", "\n".join([f"  - {author}" for author in authors]))
        rendered_md = rendered_md.replace("{{year}}", year)
        rendered_md = rendered_md.replace("{{journal}}", journal)
        rendered_md = rendered_md.replace("{{citekey}}", citekey)
        rendered_md = rendered_md.replace("{{tags}}", "\n".join([f"  - {kw}" for kw in keywords if kw]))
        rendered_md = rendered_md.replace("{{zotero_notes}}", zotero_notes)


        # Arquivo novo: inclui todas as seções
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(rendered_md)
        print(f"[✓] Created: {md_file.name}")

