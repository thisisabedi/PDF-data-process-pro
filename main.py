import os
import logging

from src.utils import setup_logging
from src.extract import extract_data_from_pdf
from src.process import save_to_csv

PDF_FOLDER = "./pdfs"
OUTPUT_FOLDER = "./output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "all_pdfs_data.csv")

def process_all_pdfs():
    """
     Save all extracted data in OUTPUT_FILE.
    """
    all_data = []
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    logging.info(f"Found {len(pdf_files)} PDF files in {PDF_FOLDER}")

    for pdf_file in pdf_files:
        full_path = os.path.join(PDF_FOLDER, pdf_file)
        try:
            data = extract_data_from_pdf(full_path, pdf_name=pdf_file)
            all_data.extend(data)
        except Exception as e:
            logging.error(f"Error processing {pdf_file}: {e}")

    logging.info(f"Total extracted records: {len(all_data)}")
    save_to_csv(all_data, OUTPUT_FILE)

if __name__ == "__main__":
    setup_logging()  # Initialize logging
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    process_all_pdfs()