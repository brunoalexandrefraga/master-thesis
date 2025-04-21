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
template_path = Path("Vault/2 - Source Material/Templates/article_notes_template.md")
zotero_template_path = Path("Vault/2 - Source Material/Templates/zotero_notes_template.md")
chapter_template_path = Path("Vault/2 - Source Material/Templates/chapter_notes_template.md")
section_template_path = Path("Vault/2 - Source Material/Templates/section_notes_template.md")
subsection_template_path = Path("Vault/2 - Source Material/Templates/subsection_notes_template.md")
book_template_path = Path("Vault/2 - Source Material/Templates/book_notes_template.md")

output_dir.mkdir(parents=True, exist_ok=True)

# Lê os templates
zotero_template_text = zotero_template_path.read_text(encoding="utf-8")
chapter_template_text = chapter_template_path.read_text(encoding="utf-8")
section_template_text = section_template_path.read_text(encoding="utf-8")
subsection_template_text = subsection_template_path.read_text(encoding="utf-8")
book_template_text = book_template_path.read_text(encoding="utf-8")

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

additional_sections = {
    "## 📝 My reflections": "- ",
    "## 🌐 Connections": "- ",
    "## 🧭 Next steps": "- ",
}





# ... (importações e funções utilitárias continuam iguais)

for entry in bib_database.entries:
    if entry.get("ENTRYTYPE") != "book":
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


    author_summary = summarize_authors(authors)
    book_title = f"{title} ({author_summary})"
    book_folder = output_dir / book_title
    book_folder.mkdir(parents=True, exist_ok=True)

    current_chapter_folder = None
    current_section_folder = None
    current_subsection_folder = None
    current_chapter = None
    current_section = None
    current_subsection = None
    chapter_links = []
    chapter_titles = []
    sections_by_chapter = {}
    subsections_by_section = {}

    # Inicializa listas para as anotações do Zotero
    vocab_notes = {}
    tech_notes = {}
    translate_notes = {}
    important_notes = {}
    explanation_notes = {}

    for line in note.split("\\par"):
        line = line.strip()
        if not line or "Annotations" in line:
            continue

        clean_line = latex_to_text(line).replace("``", "`").replace("''", "`").strip()

        if line.endswith("Chapter"):
            chapter_title = extract_clean_title(line)
            current_chapter = chapter_title
            current_chapter_folder = book_folder / chapter_title
            current_chapter_folder.mkdir(parents=True, exist_ok=True)
            chapter_titles.append(chapter_title)
            sections_by_chapter[chapter_title] = []
            chapter_links.append(f"- [[{chapter_title}/{chapter_title}|{chapter_title}]]")
            current_section_folder = current_subsection_folder = None
            current_section = current_subsection = None

        elif line.endswith("Section"):
            section_title = extract_clean_title(line)
            if current_chapter_folder is None:
                continue
            current_section = section_title
            current_section_folder = current_chapter_folder / section_title
            current_section_folder.mkdir(parents=True, exist_ok=True)
            parent_chapter = current_chapter_folder.name
            sections_by_chapter[parent_chapter].append(section_title)
            subsections_by_section[section_title] = []
            current_subsection_folder = None
            current_subsection = None

        elif line.endswith("Subsection"):
            subsection_title = extract_clean_title(line)
            if current_section_folder is None:
                continue
            current_subsection = subsection_title
            current_subsection_folder = current_section_folder / subsection_title
            current_subsection_folder.mkdir(parents=True, exist_ok=True)
            subsections_by_section[current_section_folder.name].append(subsection_title)

        else:
            current_note_target = current_subsection or current_section or current_chapter or book_title
            if "Vocabulary:" in line:
                match = re.match(r'(.*?)Vocabulary:\s*(.*)', line)
                if match:
                    quote, meaning = match.groups()
                    quote = latex_to_text(quote.strip().replace("``", "`").replace("''", "`"))
                    meaning = latex_to_text(meaning.strip())
                    # Inicializa a lista se necessário
                    if current_note_target not in vocab_notes:
                        vocab_notes[current_note_target] = []

                    vocab_notes[current_note_target].append(f"- {quote}\n\t{meaning}")

            elif "Technical:" in line:
                match = re.match(r'(.*?)Technical:\s*(.*)', line)
                if match:
                    quote, meaning = match.groups()
                    quote = latex_to_text(quote.strip().replace("``", "`").replace("''", "`"))
                    meaning = latex_to_text(meaning.strip())
                    # Inicializa a lista se necessário
                    if current_note_target not in tech_notes:
                        tech_notes[current_note_target] = []

                    tech_notes[current_note_target].append(f"- {quote}\n\t{meaning}")

            elif "Translate:" in line:
                match = re.match(r'(.*?)Translate:\s*(.*)', line)
                if match:
                    quote, meaning = match.groups()
                    quote = latex_to_text(quote.strip().replace("``", "`").replace("''", "`"))
                    meaning = latex_to_text(meaning.strip())
                    # Inicializa a lista se necessário
                    if current_note_target not in translate_notes:
                        translate_notes[current_note_target] = []

                    translate_notes[current_note_target].append(f"- {quote}\n\t{meaning}")

            elif "Important" in line:
                match = re.match(r'(.*?)Important:\s*(.*)', line)
                if match:
                    quote, meaning = match.groups()
                    quote = latex_to_text(quote.strip().replace("``", "`").replace("''", "`"))
                    meaning = latex_to_text(meaning.strip())
                    # Inicializa a lista se necessário
                    if current_note_target not in important_notes:
                        important_notes[current_note_target] = []

                    important_notes[current_note_target].append(f"- {quote}\n\t{meaning}")
                else:
                    clean = latex_to_text(line.replace("``", "`").replace("''", "`")).strip()
                    # Inicializa a lista se necessário
                    if current_note_target not in important_notes:
                        important_notes[current_note_target] = []

                    important_notes[current_note_target].append(f"- {clean}")

            elif "Explanation:" in line:
                match = re.match(r'(.*?)Explanation:\s*(.*)', line)
                if match:
                    quote, meaning = match.groups()
                    quote = latex_to_text(quote.strip().replace("``", "`").replace("''", "`"))
                    meaning = latex_to_text(meaning.strip())
                    # Inicializa a lista se necessário
                    if current_note_target not in explanation_notes:
                        explanation_notes[current_note_target] = []

                    explanation_notes[current_note_target].append(f"- {quote}\n\t{meaning}")



    # Renderiza o template de notas Zotero com os conteúdos
    zotero_notes_book = zotero_template_text
    zotero_notes_book = zotero_notes_book.replace("{{vocab_notes}}", "\n".join(vocab_notes.get(book_title, [])))
    zotero_notes_book = zotero_notes_book.replace("{{tech_notes}}", "\n".join(tech_notes.get(book_title, [])))
    zotero_notes_book = zotero_notes_book.replace("{{translate_notes}}", "\n".join(translate_notes.get(book_title, [])))
    zotero_notes_book = zotero_notes_book.replace("{{important_notes}}", "\n".join(important_notes.get(book_title, [])))
    zotero_notes_book = zotero_notes_book.replace("{{explanation_notes}}", "\n".join(explanation_notes.get(book_title, [])))




    # Cria arquivos principais de capítulo, seção e subseção com os templates e índices
    for chapter_title in chapter_titles:
        chapter_path = book_folder / chapter_title / f"{chapter_title}.md"
        sections_index = "\n".join(
            [f"- [[{chapter_title}/{sec}/{sec}|{sec}]]" for sec in sections_by_chapter[chapter_title]]
        )

        # Renderiza o template de notas Zotero com os conteúdos
        zotero_notes_chapter = zotero_template_text
        zotero_notes_chapter = zotero_notes_chapter.replace("{{vocab_notes}}", "\n".join(vocab_notes.get(chapter_title, [])))
        zotero_notes_chapter = zotero_notes_chapter.replace("{{tech_notes}}", "\n".join(tech_notes.get(chapter_title, [])))
        zotero_notes_chapter = zotero_notes_chapter.replace("{{translate_notes}}", "\n".join(translate_notes.get(chapter_title, [])))
        zotero_notes_chapter = zotero_notes_chapter.replace("{{important_notes}}", "\n".join(important_notes.get(chapter_title, [])))
        zotero_notes_chapter = zotero_notes_chapter.replace("{{explanation_notes}}", "\n".join(explanation_notes.get(chapter_title, [])))


        if not chapter_path.exists():
            chapter_content = render_template(chapter_template_text, {
                "chapter_title": chapter_title,
                "tags": "",
                "sections_index": sections_index,
                "zotero_notes": zotero_notes_chapter
            })
            chapter_path.write_text(chapter_content, encoding="utf-8")
        else:
            with open(chapter_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Atualiza a seção Zotero
            content = re.sub(
                r"## 🔗 Notes \(Zotero\)(.*?)(?=^## |\Z)",
                lambda m: zotero_notes_chapter + "\n",
                content,
                flags=re.DOTALL | re.MULTILINE
            )

            # Atualiza a seção Chapter index
            content = re.sub(
                r"## 📂 Sections index(.*?)(?=^## |\Z)",
                lambda m: "## 📂 Sections index\n" + sections_index + "\n\n",
                content,
                flags=re.DOTALL | re.MULTILINE
            )

            # Garante que cada seção adicional exista
            for template_section_title, section_default in additional_sections.items():
                if not re.search(rf"^{re.escape(template_section_title)}\s*", content, flags=re.MULTILINE):
                    content += f"\n{template_section_title}\n{section_default}\n"

            with open(chapter_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[✎] Updated: {chapter_path.name}")



        for section_title in sections_by_chapter[chapter_title]:
            section_path = book_folder / chapter_title / section_title / f"{section_title}.md"
            subsections_index = "\n".join(
                [f"- [[{chapter_title}/{section_title}/{sub}/{sub}|{sub}]]" for sub in subsections_by_section[section_title]]
            )

            # Renderiza o template de notas Zotero com os conteúdos
            zotero_notes_section = zotero_template_text
            zotero_notes_section = zotero_notes_section.replace("{{vocab_notes}}", "\n".join(vocab_notes.get(section_title, [])))
            zotero_notes_section = zotero_notes_section.replace("{{tech_notes}}", "\n".join(tech_notes.get(section_title, [])))
            zotero_notes_section = zotero_notes_section.replace("{{translate_notes}}", "\n".join(translate_notes.get(section_title, [])))
            zotero_notes_section = zotero_notes_section.replace("{{important_notes}}", "\n".join(important_notes.get(section_title, [])))
            zotero_notes_section = zotero_notes_section.replace("{{explanation_notes}}", "\n".join(explanation_notes.get(section_title, [])))



            if not section_path.exists():
                section_content = render_template(section_template_text, {
                    "section_title": section_title,
                    "tags": "",
                    "subsections_index": subsections_index,
                    "zotero_notes": zotero_notes_section
                })
                section_path.write_text(section_content, encoding="utf-8")
            else:
                with open(section_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Atualiza a seção Zotero
                content = re.sub(
                    r"## 🔗 Notes \(Zotero\)(.*?)(?=^## |\Z)",
                    lambda m: zotero_notes_section + "\n",
                    content,
                    flags=re.DOTALL | re.MULTILINE
                )

                # Atualiza a seção Chapter index
                content = re.sub(
                    r"## 📄 Subsections index(.*?)(?=^## |\Z)",
                    lambda m: "## 📄 Subsections index\n" + subsections_index + "\n\n",
                    content,
                    flags=re.DOTALL | re.MULTILINE
                )

                # Garante que cada seção adicional exista
                for template_section_title, section_default in additional_sections.items():
                    if not re.search(rf"^{re.escape(template_section_title)}\s*", content, flags=re.MULTILINE):
                        content += f"\n{template_section_title}\n{section_default}\n"

                with open(section_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[✎] Updated: {section_path.name}")





            for subsection_title in subsections_by_section[section_title]:
                subsection_path = book_folder / chapter_title / section_title / subsection_title / f"{subsection_title}.md"


                # Renderiza o template de notas Zotero com os conteúdos
                zotero_notes_subsection = zotero_template_text
                zotero_notes_subsection = zotero_notes_subsection.replace("{{vocab_notes}}", "\n".join(vocab_notes.get(subsection_title, [])))
                zotero_notes_subsection = zotero_notes_subsection.replace("{{tech_notes}}", "\n".join(tech_notes.get(subsection_title, [])))
                zotero_notes_subsection = zotero_notes_subsection.replace("{{translate_notes}}", "\n".join(translate_notes.get(subsection_title, [])))
                zotero_notes_subsection = zotero_notes_subsection.replace("{{important_notes}}", "\n".join(important_notes.get(subsection_title, [])))
                zotero_notes_subsection = zotero_notes_subsection.replace("{{explanation_notes}}", "\n".join(explanation_notes.get(subsection_title, [])))




                if not subsection_path.exists():
                    subsection_content = render_template(subsection_template_text, {
                        "subsection_title": subsection_title,
                        "tags": "",
                        "zotero_notes": zotero_notes_subsection
                    })
                    subsection_path.write_text(subsection_content, encoding="utf-8")
                else:
                    with open(subsection_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Atualiza a seção Zotero
                    content = re.sub(
                        r"## 🔗 Notes \(Zotero\)(.*?)(?=^## |\Z)",
                        lambda m: zotero_notes_subsection + "\n",
                        content,
                        flags=re.DOTALL | re.MULTILINE
                    )

                    # Garante que cada seção adicional exista
                    for template_section_title, section_default in additional_sections.items():
                        if not re.search(rf"^{re.escape(template_section_title)}\s*", content, flags=re.MULTILINE):
                            content += f"\n{template_section_title}\n{section_default}\n"

                    with open(subsection_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"[✎] Updated: {subsection_path.name}")




    # Cria o arquivo principal do livro
    book_path = book_folder / f"{title}.md"

    if not book_path.exists():
        book_content = render_template(book_template_text, {
            "title": title,
            "authors": "\n".join([f"  - {author}" for author in authors]),
            "year": year,
            "journal": journal,
            "citekey": citekey,
            "tags": "\n".join(keywords),
            "chapters_index": "\n".join(chapter_links),
            "zotero_notes": zotero_notes_book
        })
        book_path.write_text(book_content, encoding="utf-8")
        print(f"[✓] Structure created for: {title}")
    else:
        with open(book_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Atualiza a seção Zotero
        content = re.sub(
            r"## 🔗 Notes \(Zotero\)(.*?)(?=^## |\Z)",
            lambda m: zotero_notes_book + "\n",
            content,
            flags=re.DOTALL | re.MULTILINE
        )

        # Atualiza a seção Chapter index
        content = re.sub(
            r"## 📘 Chapters index(.*?)(?=^## |\Z)",
            lambda m: "## 📘 Chapters index\n" + "\n".join(chapter_links) + "\n\n",
            content,
            flags=re.DOTALL | re.MULTILINE
        )

        # Garante que cada seção adicional exista
        for template_section_title, section_default in additional_sections.items():
            if not re.search(rf"^{re.escape(template_section_title)}\s*", content, flags=re.MULTILINE):
                content += f"\n{template_section_title}\n{section_default}\n"

        with open(book_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[✎] Updated: {book_path.name}")



