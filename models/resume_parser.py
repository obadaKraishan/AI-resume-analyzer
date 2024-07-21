import spacy
import docx

nlp = spacy.load('en_core_web_sm')


def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


def extract_section(text, section_title):
    section = []
    in_section = False
    for line in text.split("\n"):
        if section_title.lower() in line.lower():
            in_section = True
        elif in_section and line.strip() == "":
            break
        elif in_section:
            section.append(line)
    return "\n".join(section)


def parse_resume(resume_text):
    doc = nlp(resume_text)
    skills = extract_section(resume_text, 'skills')
    experience = extract_section(resume_text, 'experience')
    education = extract_section(resume_text, 'education')

    return {
        'skills': skills.lower(),
        'experience': experience.lower(),
        'education': education.lower(),
        'entities': [ent.text for ent in doc.ents],
        'full_text': resume_text
    }
