import logging
import fitz  # PyMuPDF for pdf

logger = logging.getLogger(__name__)

def extract_data_from_pdf(filepath, pdf_name=None):
    data = []
    pdf_name = pdf_name or filepath
    logger.info(f"Starting extraction from {pdf_name}")

    with fitz.open(filepath) as doc:
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            data.append({
                "filename": pdf_name,
                "page": page_num,
                "content": text
            })

    logger.info(f"Finished extraction from {pdf_name}, total pages: {len(data)}")
    return data

