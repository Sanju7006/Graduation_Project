import streamlit as st
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import os
import nltk
import pytesseract
import re
import slate3k as slate
from pdf2image import convert_from_path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from PIL import Image
import os
import openai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv, find_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

nltk.download("stopwords")
nltk.download("punkt")
#st.set_page_config(layout="wide", page_title="Your Streamlit App", page_icon="🚀", background="https://miro.medium.com/v2/resize:fit:828/format:webp/1*gYVZCuL7dz8ALoyp7Gob_A.png")

def sanitize_input(data):
    """
    Currently just a whitespace remover. More thought will have to be given with how
    to handle sanitzation and encoding in a way that most text files can be successfully
    parsed
    """
    replace = {
        ord('\f') : ' ',
        ord('\t') : ' ',
        ord('\n') : ' ',
        ord('\r') : None
    }

    return data.translate(replace)
def tokenize_content(content):
    """
    Accept the content and produce a list of tokenized sentences,
    a list of tokenized words, and then a list of the tokenized words
    with stop words built from NLTK corpus and Python string class filtred out.
    """
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())

    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]
    ]
def score_tokens(filterd_words, sentence_tokens):
    """
    Builds a frequency map based on the filtered list of words and
    uses this to produce a map of each sentence and its total score
    """
    word_freq = FreqDist(filterd_words)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]

    return ranking
def get_transcript(youtube_url):
    video_id = youtube_url.split("v=")[-1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    # Try fetching the manual transcript
    try:
        transcript = transcript_list.find_manually_created_transcript()
        language_code = transcript.language_code  # Save the detected language
    except:
        # If no manual transcript is found, try fetching an auto-generated transcript in a supported language
        try:
            generated_transcripts = [trans for trans in transcript_list if trans.is_generated]
            transcript = generated_transcripts[0]
            language_code = transcript.language_code  # Save the detected language
        except:
            # If no auto-generated transcript is found, raise an exception
            raise Exception("No suitable transcript found.")

    full_transcript = " ".join([part['text'] for part in transcript.fetch()])
    return full_transcript, language_code  # Return both the transcript and detected language
def summarize_with_langchain_and_openai(transcript, language_code, model_name='gpt-3.5-turbo'):
    # Split the document if it's too long
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_text(transcript)
    text_to_summarize = " ".join(texts[:4]) # Adjust this as needed

    # Prepare the prompt for summarization
    system_prompt = 'I want you to act as a Life Coach that can create good summaries!'
    prompt = f'''Summarize the following text in {language_code}.
    Text: {text_to_summarize}

    Add a title to the summary in {language_code}. 
    Include an INTRODUCTION, BULLET POINTS if possible, and a CONCLUSION in {language_code}.'''

    # Start summarizing using OpenAI
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        temperature=1
    )
    
    return response['choices'][0]['message']['content']
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
def summarize1(text):
    # Process text by removing numbers and unrecognized punctuation
    processedText = re.sub("’", "'", text)
    processedText = re.sub("[^a-zA-Z' ]+", " ", processedText)
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(processedText)

    # Normalize words with Porter stemming and build word frequency table
    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        elif stemmer.stem(word) in freqTable:
            freqTable[stemmer.stem(word)] += 1
        else:
            freqTable[stemmer.stem(word)] = 1

    # Normalize every sentence in the text
    sentences = sent_tokenize(text)
    stemmedSentences = []
    sentenceValue = dict()
    for sentence in sentences:
        stemmedSentence = []
        for word in sentence.lower().split():
            stemmedSentence.append(stemmer.stem(word))
        stemmedSentences.append(stemmedSentence)

    # Calculate value of every normalized sentence based on word frequency table
    # [:12] helps to save space
    for num in range(len(stemmedSentences)):
        for wordValue in freqTable:
            if wordValue in stemmedSentences[num]:
                if sentences[num][:12] in sentenceValue:
                    sentenceValue[sentences[num][:12]] += freqTable.get(wordValue)
                else:
                    sentenceValue[sentences[num][:12]] = freqTable.get(wordValue)

    # Determine average value of a sentence in the text
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue.get(sentence)

    average = int(sumValues / len(sentenceValue))

    # Create summary of text using sentences that exceed the average value by some factor
    # This factor can be adjusted to reduce/expand the length of the summary
    summary = ""
    for sentence in sentences:
            if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (3.0 * average):
                summary += " " + " ".join(sentence.split())

    # Process the text in summary and write it to a new file
    summary = re.sub("’", "'", summary)
    summary = re.sub("[^a-zA-Z0-9'\"():;,.!?— ]+", " ", summary)
    
    return summary

def summarize(ranks, sentences, length):
    """
    Utilizes a ranking map produced by score_token to extract
    the highest ranking sentences in order after converting from
    array to string.
    """
    

    indexes = nlargest(length, ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]
    return ' '.join(final_sentences)

def extractText(file):
    pdfFileObj = open(file, "rb")
    pdfPages = slate.PDF(pdfFileObj)

    # Extract text from PDF file
    text = ""
    for page in pdfPages:
        text += page
    return text

# Create three columns
col1, col2, col3 = st.columns(3)


# Add content to each column
with col1:
    styled_summary = f'<p style="color: red; font-weight: bold; text-align: justify;">{"Image"}</p>'
    st.markdown(styled_summary, unsafe_allow_html=True)
    uploaded_file_col1 = st.file_uploader("", key="file_col1")
    button_col1 = st.button("Generate Summary")
    if button_col1:
        print("I am on button1")
        if uploaded_file_col1 is not None:
            
            file_path = uploaded_file_col1.name
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension in ('.jpg', '.jpeg', '.png'):
                st.write("Valid image file:", file_path)
                st.write("Full Path:", file_path)
                from PIL import Image
                import pytesseract
                import argparse
                import cv2
                import os
                image = cv2.imread(file_path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.threshold(gray, 0, 255,
		            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                filename = "{}.jpg".format(os.getpid())
                cv2.imwrite(filename, gray)
                pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
                text = pytesseract.image_to_string(Image.open(filename))
                os.remove(filename)
                st.write("Original Text")
                st.write(text)
                content = sanitize_input(text)
                sentence_tokens, word_tokens = tokenize_content(content)
                sentence_ranks = score_tokens(word_tokens, sentence_tokens)
                st.write("Summary Text")
                summary_content = summarize(sentence_ranks, sentence_tokens, 8)
                styled_summary = f'<p style="color: red; font-weight: bold; text-align: justify;">{summary_content}</p>'
                st.markdown(styled_summary, unsafe_allow_html=True)
                summary_content = summary_content
                pdf_path = "text_document.pdf"
                generate_pdf(summary_content, pdf_path)
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from email.mime.base import MIMEBase
                from email import encoders

# Email details
                sender_email = "kacharesanju4448@gmail.com"
                receiver_email = "kacharesanju4448@gmail.com"
                subject = "PDF Attachment"
                body = "Please find the attached PDF."

# Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject

# Add body to email
                message.attach(MIMEText(body, "plain"))

# Attach PDF file
                filename = "text_document.pdf"
                attachment = open(filename, "rb")

# Set attachment MIME type
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
                )

# Attach the attachment to the message
                message.attach(part)

# Connect to SMTP server and send email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, "bfix ttyv nccl ucnu")
                    server.sendmail(sender_email, receiver_email, message.as_string())
            else:
                st.write("Invalid file format. Please upload a JPG or PNG file.")


        
            

with col2:
    styled_summary = f'<p style="color: red; font-weight: bold; text-align: justify;">{"PDF"}</p>'
    st.markdown(styled_summary, unsafe_allow_html=True)
    uploaded_file_col2 = st.file_uploader("", key="file_col2")
    button_col2 = st.button("Generate Summary",key="col2_button")
    if button_col2:
        if uploaded_file_col2 is not None:
            file_path = uploaded_file_col2.name
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension in ('.pdf'):
                st.write("Valid pdf file:", file_path)
                st.write("Full Path:", file_path)
                text = extractText(file_path)
                print(text)
                currentsummary=summarize1(text)
                mysummary = f'<p style="color: red; font-weight: bold; text-align: justify;">{currentsummary}</p>'
                st.markdown(mysummary, unsafe_allow_html=True)
                pdf_path = "pdf_document.pdf"
                generate_pdf(currentsummary, pdf_path)
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from email.mime.base import MIMEBase
                from email import encoders

# Email details
                sender_email = "kacharesanju4448@gmail.com"
                receiver_email = "kacharesanju4448@gmail.com"
                subject = "PDF Attachment"
                body = "Please find the attached PDF."

# Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject

# Add body to email
                message.attach(MIMEText(body, "plain"))

# Attach PDF file
                filename = "pdf_document.pdf"
                attachment = open(filename, "rb")

# Set attachment MIME type
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
                )

# Attach the attachment to the message
                message.attach(part)

# Connect to SMTP server and send email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, "bfix ttyv nccl ucnu")
                    server.sendmail(sender_email, receiver_email, message.as_string())
            else:
                st.write("Invalid file format. Please upload PDF File .")

with col3:
    styled_summary = f'<p style="color: red; font-weight: bold; text-align: justify;">{"Video"}</p>'
    st.markdown(styled_summary, unsafe_allow_html=True)
    openai.api_key ="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"
    st.write('YouTube video summarizer')
    link = st.text_input('Enter the link of the YouTube video you want to summarize:')
    if st.button('Start'):
        if link:
            try:
                progress = st.progress(0)       
                status_text = st.empty()
                status_text.text('Loading the transcript...')
                progress.progress(25)
                transcript, language_code = get_transcript(link)

                status_text.text(f'Creating summary...')
                progress.progress(75)

                model_name = 'gpt-3.5-turbo'
                summary = summarize_with_langchain_and_openai(transcript, language_code, model_name)

                status_text.text('Summary:')
                st.markdown(summary)
                pdf_path = "video_document.pdf"
                generate_pdf(summary, pdf_path)
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from email.mime.base import MIMEBase
                from email import encoders

# Email details
                sender_email = "kacharesanju4448@gmail.com"
                receiver_email = "kacharesanju4448@gmail.com"
                subject = "PDF Attachment"
                body = "Please find the attached PDF."

# Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject

# Add body to email
                message.attach(MIMEText(body, "plain"))

# Attach PDF file
                filename = "video_document.pdf"
                attachment = open(filename, "rb")

# Set attachment MIME type
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
                )

# Attach the attachment to the message
                message.attach(part)

# Connect to SMTP server and send email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, "bfix ttyv nccl ucnu")
                    server.sendmail(sender_email, receiver_email, message.as_string())
                
                progress.progress(100)
            except Exception as e:
                st.write(str(e))
        else:
            st.write('Please enter a valid YouTube link.')
