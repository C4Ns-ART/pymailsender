from email import message
from email.mime.text import MIMEText
from msilib.schema import MIME
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):
    fromMail = "mailadresiniz@gmail.com" # Mail adresiniz
    server = smtplib.SMTP("smtp.gmail.com",587) # Gmail olduğu için smtp.gmail.com kullandık PORT: 587 Default
    server.starttls()
    server.login(fromMail, "sifreniz") # Mail şifreniz
    message = MIMEMultipart('alternative')
    message['Subject']= subject
    htmlContent = MIMEText(content, 'html')
    
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )

    print("Eposta başarı ile gönderildi!")
    server.quit()