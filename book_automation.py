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

def render_template(template_str, context):
    for key, value in context.items():
        template_str = template_str.replace(f"{{{{{key}}}}}", value)
    return template_str

# Caminhos
bib_path = Path("Thesis/zotero_references.bib")
output_dir = Path("Vault/2 - Source Material/Books")
template_path = Path("Vault/6 - Templates/article_notes_template.md")
zotero_template_path = Path("Vault/6 - Templates/zotero_notes_template.md")
chapter_template_path = Path("Vault/6 - Templates/chapter_notes_template.md")
section_template_path = Path("Vault/6 - Templates/section_notes_template.md")
subsection_template_path = Path("Vault/6 - Templates/subsection_notes_template.md")
book_template_path = Path("Vault/6 - Templates/book_notes_template.md")

output_dir.mkdir(parents=True, exist_ok=True)

# Lê os templates
zotero_template_text = zotero_template_path.read_text(encoding="utf-8")
chapter_template_text = chapter_template_path.read_text(encoding="utf-8")
section_template_text = section_template_path.read_text(encoding="utf-8")
subsection_template_text = subsection_template_path.read_text(encoding="utf-8")
book_template_text = book_template_path.read_text(encoding="utf-8")

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

for entry in bib_database.entries:
    if entry.get("ENTRYTYPE") != "book":
        continue

    citekey = entry.get("ID", "unknown")
    raw_title = entry.get("title", "").replace("{", "").replace("}", "")
    title = sanitize(raw_title)
    authors = [sanitize(author.strip()) for author in entry.get("author", "").replace("\n", "").split(" and ")]
    year = sanitize(entry.get("year", ""))
    journal = sanitize(entry.get("journal", ""))
    keywords = [sanitize(re.sub(r"[()]", "", kw.strip().replace(" ", "_"))) for kw in entry.get("keywords", "").split(",")]
    note = entry.get("note", "").strip()

    author_summary = summarize_authors(authors)
    book_folder = output_dir / f"{title} ({author_summary})"
    book_folder.mkdir(parents=True, exist_ok=True)

    current_chapter = None
    current_section = None
    chapter_links = []
    chapter_titles = []
    sections_by_chapter = {}
    subsections_by_section = {}

    for line in note.split("\\par"):
        line = line.strip()
        if not line or "Annotations" in line:
            continue

        clean_line = latex_to_text(line).replace("``", "").replace("''", "").strip()

        if line.endswith("Chapter"):
            chapter_title = extract_clean_title(line)
            current_chapter = book_folder / chapter_title
            current_chapter.mkdir(parents=True, exist_ok=True)
            chapter_titles.append(chapter_title)
            sections_by_chapter[chapter_title] = []
            chapter_links.append(f"- [[{chapter_title}/{chapter_title}|{chapter_title}]]")
            current_section = None

        elif line.endswith("Section"):
            section_title = extract_clean_title(line)
            if current_chapter is None:
                continue
            current_section = current_chapter / section_title
            current_section.mkdir(parents=True, exist_ok=True)
            parent_chapter = current_chapter.name
            sections_by_chapter[parent_chapter].append(section_title)
            subsections_by_section[section_title] = []

        elif line.endswith("Subsection"):
            subsection_title = extract_clean_title(line)
            if current_section is None:
                continue
            subsection_folder = current_section / subsection_title
            subsection_folder.mkdir(parents=True, exist_ok=True)
            subsections_by_section[current_section.name].append(subsection_title)

        else:
            destination = current_section or current_chapter or book_folder
            if destination is not None:
                index_path = destination / "Index.md"
                with index_path.open("a", encoding="utf-8") as f:
                    f.write(f"- {clean_line}\n")

    # Cria arquivos principais de capítulo, seção e subseção com os templates e índices
    for chapter_title in chapter_titles:
        chapter_path = book_folder / chapter_title / f"{chapter_title}.md"
        sections_index = "\n".join(
            [f"- [[{chapter_title}/{sec}/{sec}|{sec}]]" for sec in sections_by_chapter[chapter_title]]
        )
        chapter_content = render_template(chapter_template_text, {
            "chapter_title": chapter_title,
            "tags": "",
            "sections_index": sections_index,
            "zotero_notes": zotero_template_text
        })
        chapter_path.write_text(chapter_content, encoding="utf-8")

        for section_title in sections_by_chapter[chapter_title]:
            section_path = book_folder / chapter_title / section_title / f"{section_title}.md"
            subsections_index = "\n".join(
                [f"- [[{chapter_title}/{section_title}/{sub}/{sub}|{sub}]]" for sub in subsections_by_section[section_title]]
            )
            section_content = render_template(section_template_text, {
                "section_title": section_title,
                "tags": "",
                "subsections_index": subsections_index,
                "zotero_notes": zotero_template_text
            })
            section_path.write_text(section_content, encoding="utf-8")

            for subsection_title in subsections_by_section[section_title]:
                subsection_path = book_folder / chapter_title / section_title / subsection_title / f"{subsection_title}.md"
                subsection_content = render_template(subsection_template_text, {
                    "subsection_title": subsection_title,
                    "tags": "",
                    "zotero_notes": zotero_template_text
                })
                subsection_path.write_text(subsection_content, encoding="utf-8")

    # Cria o arquivo principal do livro
    book_md_path = book_folder / f"{title}.md"
    book_content = render_template(book_template_text, {
        "title": title,
        "authors": "\n".join(authors),
        "year": year,
        "journal": journal,
        "citekey": citekey,
        "tags": "\n".join(keywords),
        "chapters_index": "\n".join(chapter_links),
        "zotero_notes": zotero_template_text
    })
    book_md_path.write_text(book_content, encoding="utf-8")

    print(f"[✓] Estrutura criada para: {title}")

