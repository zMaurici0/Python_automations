from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

# carrega variáveis de ambiente

load_dotenv()

password = os.getenv('EMAIL_PASSWORD')

fromEmail = 'automacaotestepython@gmail.com'
toEmail = 'zmauriciomota@gmail.com'
subject = 'Automação com Python'
body = open('Envio-de-Emails/body.txt', 'r', encoding='utf-8').read()

# 1 - Definindo mensagem

mensagem = EmailMessage()
mensagem['From'] = fromEmail
mensagem['To'] = toEmail
mensagem['Subject'] = subject
mensagem.set_content(body)
safe = ssl.create_default_context()

# 2 - enviando o email

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(fromEmail, password)
    smtp.sendmail(
        fromEmail,
        toEmail,
        mensagem.as_string()
    )