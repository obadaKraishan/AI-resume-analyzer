from flask import render_template, flash, redirect, url_for, request
from . import main
from .forms import ResumeForm
from models.resume_parser import parse_resume, extract_text_from_docx
from models.job_description_parser import parse_job_description
from models.resume_scorer import score_resume, generate_feedback
from werkzeug.utils import secure_filename
import os
import PyPDF2

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        text += page.extract_text()
    return text

@main.route('/', methods=['GET', 'POST'])
def index():
    form = ResumeForm()
    if form.validate_on_submit():
        resume_file = form.resume.data
        job_title = form.job_title.data
        job_description = form.job_description.data
        job_responsibilities = form.job_responsibilities.data
        job_experience = form.job_experience.data
        job_skills = form.job_skills.data
        job_education = form.job_education.data

        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)
            file_extension = filename.rsplit('.', 1)[1].lower()

            if file_extension in {'doc', 'docx'}:
                resume_text = extract_text_from_docx(resume_file)
            elif file_extension == 'pdf':
                resume_text = extract_text_from_pdf(resume_file)
            else:
                resume_text = resume_file.read().decode('utf-8', errors='ignore')

            resume_data = parse_resume(resume_text)
            job_description_data = parse_job_description(
                job_description, job_responsibilities, job_experience, job_skills, job_education
            )
            scores = score_resume(resume_data, job_description_data)

            feedback = generate_feedback(resume_data, job_description_data)

            flash(f'Overall Resume Score: {scores["total_score"]}%', 'success')
            flash(f'Details:', 'info')
            flash(f'Resume Structure: {scores["entity_score"]}%', 'info')
            flash(f'Skills Match: {scores["skills_score"]}%', 'info')
            flash(f'Experience Match: {scores["experience_score"]}%', 'info')
            flash(f'Education Match: {scores["education_score"]}%', 'info')
            flash(f'Issues: {feedback}', 'warning')
            return redirect(url_for('main.index'))

    return render_template('index.html', form=form)
