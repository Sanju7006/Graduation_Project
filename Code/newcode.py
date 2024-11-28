from PyPDF2 import PdfReader
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the PDF file
with open('IRJET.pdf', 'rb') as file:
    pdf_reader = PdfReader(file)
    num_pages = len(pdf_reader.pages)

    # Extract the text from the PDF file
    text = ''
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

# Encode the text using the T5 tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-base')
encoded_text = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)

# Generate the summary using the T5ForConditionalGeneration model
model = T5ForConditionalGeneration.from_pretrained('t5-base')
summary_ids = model.generate(encoded_text, max_length=150, num_beams=2, length_penalty=2.0, early_stopping=True)

# Decode the summary into a human-readable format
decoded_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print(decoded_summary)
