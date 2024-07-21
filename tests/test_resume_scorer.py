import unittest
from models.resume_parser import parse_resume
from models.job_description_parser import parse_job_description
from models.resume_scorer import score_resume


class TestResumeScorer(unittest.TestCase):
    def test_score_resume(self):
        resume_text = "John Doe\nSoftware Engineer\nSkills: Python, Java"
        job_description_text = "Looking for a Software Engineer with experience in Python and Java."

        resume_doc = parse_resume(resume_text)
        job_description_doc = parse_job_description(job_description_text)

        score = score_resume(resume_doc, job_description_doc)
        self.assertGreater(score, 0)


if __name__ == '__main__':
    unittest.main()
