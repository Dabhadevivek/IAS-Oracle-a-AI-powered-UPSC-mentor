import openai
import os
from PyPDF2 import PdfReader

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_pdf_text(pdf_file):
    """Extract text from a PDF."""
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_summary(text, style="bullet_points"):
    """Summarize extracted text using GPT."""
    prompt = f"Summarize the following text into {style}:\n{text[:1500]}"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text

# Usage
if _name_ == "_main_":
    pdf_path = "../data/newspapers/sample.pdf"
    with open(pdf_path, 'rb') as pdf_file:
        pdf_text = extract_pdf_text(pdf_file)
        summary = generate_summary(pdf_text)
        print(summary)
