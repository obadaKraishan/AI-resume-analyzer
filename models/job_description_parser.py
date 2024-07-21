import spacy

nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    doc = nlp(text)
    keywords = set([token.lemma_.lower() for token in doc if token.pos_ in {'NOUN', 'PROPN', 'ADJ'} and not token.is_stop])
    return keywords

def parse_job_description(job_description_text, job_responsibilities_text, job_experience_text, job_skills_text, job_education_text):
    combined_text = f"{job_description_text} {job_responsibilities_text} {job_experience_text} {job_skills_text} {job_education_text}"
    keywords = extract_keywords(combined_text)
    return {
        'text': job_description_text,
        'responsibilities': job_responsibilities_text,
        'experience': job_experience_text,
        'skills': job_skills_text,
        'education': job_education_text,
        'keywords': keywords
    }
