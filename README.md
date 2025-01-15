# PDF Data Processing (Simplified)

This project extracts text from PDF files and saves it into a single CSV file, 
all in a straightforward, linear approach (no threading).

## Features
- Extract text from each page of  PDF.
- Collect  in a CSV file (page, filename, content).
- Simple structure for clarity.

## Usage

1. **Clone or download** the project.
2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate



## Install dependencies:
pip install -r requirements.txt

## Place PDF files in the pdfs folder.

## Run the script:
python main.py

Logs will appear in logs/app.log, 
and the output CSV in output/all_pdfs_data.csv.


## Testing
python -m unittest discover -s tests

## English

During the development of this project, I created two different versions of the code:


 **First Version (Concurrent Approach)**  
   - Utilized concurrency (ThreadPoolExecutor) to process multiple PDFs in parallel.  
   - Intended to improve performance when dealing with many or large PDF files.  
   - Occasionally caused issues such as the "document closed" error in PyMuPDF for certain files.

**Second Version (Simplified Approach)**  
   - Processes PDFs **sequentially**, one by one.  
   - Avoids concurrency-related errors (no “document closed” problem).  
   - Easier to debug and maintain, though it may run slower with very large numbers of PDFs.

Overall, the **concurrent version** was more advanced in terms of speed but introduced potential stability issues, while the **simplified version** provided reliable results without concurrency complications.

