from flask_wtf import FlaskForm
from wtforms import FileField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    resume = FileField('Resume', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    job_responsibilities = TextAreaField('Job Responsibilities', validators=[DataRequired()])
    job_experience = TextAreaField('Required Experience', validators=[DataRequired()])
    job_skills = TextAreaField('Required Skills', validators=[DataRequired()])
    job_education = TextAreaField('Required Education', validators=[DataRequired()])
    submit = SubmitField('Submit')
