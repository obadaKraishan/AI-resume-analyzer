import unittest
from models.job_description_parser import parse_job_description

class TestJobDescriptionParser(unittest.TestCase):
    def test_parse_job_description(self):
        job_description_text = "Looking for a Software Engineer with experience in Python and Java."
        doc = parse_job_description(job_description_text)
        self.assertIsNotNone(doc)

if __name__ == '__main__':
    unittest.main()
