import bibtexparser
from pathlib import Path
import re
from pylatexenc.latex2text import LatexNodes2Text

# Funções utilitárias
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

def extract_clean_title(raw_title):
    cleaned = re.sub(r'\s*\(.*?\)', '', raw_title).strip()
    cleaned = re.sub(r'\b(Chapter|Section|Subsection)\b$', '', cleaned).strip()
    cleaned = cleaned.strip("`'\"")
    return cleaned

# Caminhos
bib_path = Path("Thesis/zotero_references.bib")
output_dir = Path("Vault/2 - Source Material/Books")
template_path = Path("Vault/6 - Templates/article_notes_template.md")
zotero_template_path = Path("Vault/6 - Templates/zotero_notes_template.md")
output_dir.mkdir(parents=True, exist_ok=True)

# Lê os templates
template_text = template_path.read_text(encoding="utf-8")
zotero_template_text = zotero_template_path.read_text(encoding="utf-8")

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

for entry in bib_database.entries:
    if entry.get("ENTRYTYPE") != "book":
        continue

    citekey = entry.get("ID", "unknown")
    title = sanitize(entry.get("title", "").replace("{", "").replace("}", ""))
    authors = [sanitize(author.strip()) for author in entry.get("author", "").replace("\n", "").split(" and ")]
    year = sanitize(entry.get("year", ""))
    keywords = [
        sanitize(re.sub(r"[()]", "", kw.strip().replace(" ", "_")))
        for kw in entry.get("keywords", "").split(",")
    ]
    note = entry.get("note", "").strip()

    # Pasta principal do livro
    author_summary = summarize_authors(authors)
    book_folder = output_dir / f"{title} ({author_summary})"
    book_folder.mkdir(parents=True, exist_ok=True)

    # Inicializa estrutura hierárquica
    current_chapter = None
    current_section = None

    for line in note.split("\\par"):
        line = line.strip()
        if not line or "Annotations" in line:
            continue

        clean_line = latex_to_text(line).replace("``", "").replace("''", "").strip()
        # CHAPTER
        if line.endswith("Chapter"):

            chapter_title = extract_clean_title(line)
            print(chapter_title)
            current_chapter = book_folder / chapter_title
            current_chapter.mkdir(parents=True, exist_ok=True)
            index_path = current_chapter / f"{chapter_title}.md"
            index_path.write_text(f"# {chapter_title}\n\n", encoding="utf-8")
            current_section = None  # Reseta seção
        # SECTION
        elif line.endswith("Section"):
            section_title = extract_clean_title(line)
            if current_chapter is None:
                continue  # Segurança: ignora se não houver capítulo
            current_section = current_chapter / section_title
            current_section.mkdir(parents=True, exist_ok=True)
            index_path = current_section / f"{section_title}.md"
            index_path.write_text(f"# {section_title}\n\n", encoding="utf-8")
        # SUBSECTION
        elif line.endswith("Subsection"):
            subsection_title = extract_clean_title(line)
            if current_section is None:
                continue  # Segurança: ignora se não houver seção
            subsection_folder = current_section / subsection_title
            subsection_folder.mkdir(parents=True, exist_ok=True)
            index_path = subsection_folder / f"{subsection_title}.md"
            index_path.write_text(f"# {subsection_title}\n\n", encoding="utf-8")
        else:
            # Nota normal – alocar corretamente
            destination = current_section or current_chapter or book_folder
            if destination is not None:
                index_path = destination / "Index.md"
                with index_path.open("a", encoding="utf-8") as f:
                    f.write(f"- {clean_line}\n")

    print(f"[✓] Estrutura criada para: {title}")
