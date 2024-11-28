from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(summary_content, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Set width and height for text wrapping
    width, height = letter

    # Split the text into lines to fit within the page width
    text_lines = summary_content.split("\n")

    # Write text to the PDF
    y_position = height - 50
    for line in text_lines:
        # Calculate the width of the text
        text_width = c.stringWidth(line)

        # Check if the text exceeds the page width
        if text_width > (width - 100):
            # If it exceeds, calculate the number of lines needed
            num_lines = int(text_width / (width - 100)) + 1
            # Split the line into multiple lines
            split_line = [line[i:i+(int(len(line)/num_lines)+1)] for i in range(0, len(line), int(len(line)/num_lines)+1)]
            # Write each line separately
            for sub_line in split_line:
                c.drawString(50, y_position, sub_line.strip())
                y_position -= 20  # Adjust vertical position for the next line
        else:
            c.drawString(50, y_position, line.strip())
            y_position -= 20  # Adjust vertical position for the next line

    # Start a new page
    c.showPage()

    # Save the PDF document
    c.save()

    print("PDF created successfully at:", pdf_path)

# Example usage:
summary_content = """Sometimes there were heavy showers of rain, but Aaliya didn’t mind that. ‘Aaliya.’ Aaliya could still hear her mother’s voice clearly inside her head, as the black pencil hovered over the white paper. And in her mind, she could see her mother’s pink shalwar kameez, her older sister Sara’s orange T-shirt, her father’s green shirt. ‘We’re going to the market. Do you want to come?’ No, Aaliya didn’t want to go, They went to the market every Sunday morning to buy tuna-fish and vegetables - it was nothing special. ‘We'll have breakfast when we get back,’ her mother told her. ‘Be good!’ The classroom was cool, the fan purring softly overhead. Aaliya put her finger on the paper, a third of the way down from the top."""
pdf_path = "text_document.pdf"
generate_pdf(summary_content, pdf_path)
