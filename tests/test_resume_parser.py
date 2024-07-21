import unittest
from models.resume_parser import parse_resume

class TestResumeParser(unittest.TestCase):
    def test_parse_resume(self):
        resume_text = "John Doe\nSoftware Engineer\nSkills: Python, Java"
        doc = parse_resume(resume_text)
        self.assertIsNotNone(doc)

if __name__ == '__main__':
    unittest.main()
