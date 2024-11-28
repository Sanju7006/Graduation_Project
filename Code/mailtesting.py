import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email details
sender_email = "kacharesanju4448@gmail.com"
receiver_email = "rahulpawar9766@gmail.com"
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
