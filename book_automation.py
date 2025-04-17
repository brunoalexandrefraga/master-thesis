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

# Carrega os templates
template_dir = Path("Vault/6 - Templates")
chapter_template = (template_dir / "chapter_notes_template.md").read_text(encoding="utf-8")
section_template = (template_dir / "section_notes_template.md").read_text(encoding="utf-8")
subsection_template = (template_dir / "subsection_notes_template.md").read_text(encoding="utf-8")

# Caminhos
bib_path = Path("Thesis/zotero_references.bib")
output_dir = Path("Vault/2 - Source Material/Books")
output_dir.mkdir(parents=True, exist_ok=True)

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

for entry in bib_database.entries:
    if entry.get("ENTRYTYPE") != "book":
        continue

    citekey = entry.get("ID", "unknown")
    title = sanitize(entry.get("title", "").replace("{", "").replace("}", ""))
    authors = [sanitize(author.strip()) for author in entry.get("author", "").replace("\n", "").split(" and ")]
    year = sanitize(entry.get("year", ""))
    author_summary = summarize_authors(authors)
    book_folder = output_dir / f"{title} ({author_summary})"
    book_folder.mkdir(parents=True, exist_ok=True)

    note = entry.get("note", "").strip()
    keywords = [
        sanitize(re.sub(r"[()]", "", kw.strip().replace(" ", "_")))
        for kw in entry.get("keywords", "").split(",")
    ]
    tags_block = "\n".join([f"- {kw}" for kw in keywords if kw])

    # Novo: cria arquivo principal do livro
    book_main = book_folder / f"{title}.md"
    if not book_main.exists():
        book_main.write_text(f"# {title}\n\n", encoding="utf-8")

    current_chapter = None
    current_section = None
    chapter_sections = {}
    section_subsections = {}

    for line in note.split("\\par"):
        line = line.strip()
        if not line or "Annotations" in line:
            continue

        clean_line = latex_to_text(line).replace("``", "").replace("''", "").strip()

        if line.endswith("Chapter"):
            chapter_title = extract_clean_title(line)
            current_chapter = book_folder / chapter_title
            current_chapter.mkdir(parents=True, exist_ok=True)
            chapter_sections[chapter_title] = []
            current_section = None

        elif line.endswith("Section"):
            section_title = extract_clean_title(line)
            if current_chapter is None:
                continue
            current_section = current_chapter / section_title
            current_section.mkdir(parents=True, exist_ok=True)
            chapter_sections[chapter_title].append(section_title)
            section_subsections[section_title] = []

        elif line.endswith("Subsection"):
            subsection_title = extract_clean_title(line)
            if current_section is None:
                continue
            subsection_folder = current_section / subsection_title
            subsection_folder.mkdir(parents=True, exist_ok=True)
            section_subsections[current_section.name].append(subsection_title)

        else:
            destination = current_section or current_chapter or book_folder
            if destination is not None:
                index_path = destination / "Index.md"
                with index_path.open("a", encoding="utf-8") as f:
                    f.write(f"- {clean_line}\n")

    # Agora cria os arquivos principais com os templates e índices
    for chapter, sections in chapter_sections.items():
        chapter_path = book_folder / chapter
        sections_index = "\n".join([f"- [[{section}/{section}]]" for section in sections])
        content = chapter_template.replace("{{chapter_title}}", chapter)\
                                  .replace("{{tags}}", tags_block)\
                                  .replace("{{sections_index}}", sections_index)\
                                  .replace("{{zotero_notes}}", "")
        (chapter_path / f"{chapter}.md").write_text(content, encoding="utf-8")

        for section in sections:
            section_path = chapter_path / section
            subsections = section_subsections.get(section, [])
            subsections_index = "\n".join([f"- [[{subsection}/{subsection}]]" for subsection in subsections])
            content = section_template.replace("{{section_title}}", section)\
                                      .replace("{{tags}}", tags_block)\
                                      .replace("{{subsections_index}}", subsections_index)\
                                      .replace("{{zotero_notes}}", "")
            (section_path / f"{section}.md").write_text(content, encoding="utf-8")

            for subsection in subsections:
                subsection_path = section_path / subsection
                content = subsection_template.replace("{{subsection_title}}", subsection)\
                                             .replace("{{tags}}", tags_block)\
                                             .replace("{{zotero_notes}}", "")
                (subsection_path / f"{subsection}.md").write_text(content, encoding="utf-8")

    print(f"[✓] Estrutura criada com templates para: {title}")

