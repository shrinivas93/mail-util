import email
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
smtp_port = 465

subject = "MAIL FROM PYTHON CODE"
body = 'Dear <b>X</b>,<br/>This mail is sent from python code.<br/><br/><i>HTML</i><span style="background: red; color: green; font-weight: bold;font-size: 24px; font-family: Calibri;">works like magic</span><br/><br/>Also, check out the attachment.<br/><figure> <img src="cid:shivaji_img" alt="Shivaji" style="width:100%"> <figcaption>Jai Bhawani.... Jai Shivaji...</figcaption></figure>'
username = "ssshukla1993@gmail.com"
sender_email = "The Great Shrinivas Shukla <ssshukla1993@gmail.com>"
receiver_emails = ["ssshukla1993@gmail.com"]
password = ''

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message.add_header('from', sender_email)
message["To"] = " ".join(receiver_emails)
message["Subject"] = subject
# message["Bcc"] = receiver_emails  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "html"))

filename = "attachment.txt"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    "attachment; filename= {}".format(filename)
)

# Add attachment to message and convert message to string
message.attach(part)


imagename = "shivaji.jpg"

with open(imagename, 'rb') as file:
    msg_image = MIMEImage(file.read(), name=imagename)

msg_image.add_header('Content-ID', '<{}>'.format('shivaji_img'))


message.attach(msg_image)


text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host=smtp_server, port=465, context=context) as server:
    server.login(username, password)
    server.sendmail(sender_email, receiver_emails, text)
