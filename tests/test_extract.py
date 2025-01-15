import unittest
import os
from src.extract import extract_data_from_pdf

class TestExtractData(unittest.TestCase):
    def setUp(self):
       
        self.test_pdf = "./pdfs/1.pdf"
        self.test_pdf = "./pdfs/2.pdf"
        self.test_pdf = "./pdfs/3.pdf"
    
    def test_valid_pdf(self):
        if not os.path.exists(self.test_pdf):
            self.skipTest(f"Test PDF not found: {self.test_pdf}")
        data = extract_data_from_pdf(self.test_pdf, pdf_name="sample.pdf")
        self.assertGreater(len(data), 0, )

    def test_invalid_pdf(self):
        with self.assertRaises(Exception):
            extract_data_from_pdf("./pdfs/invalid.pdf")

if __name__ == "__main__":
    unittest.main()