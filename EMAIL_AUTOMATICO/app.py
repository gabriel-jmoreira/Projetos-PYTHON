import os
import smtplib
from email.message import EmailMessage

#configurar email e senha
EMAIL_ADDRESS = 'gabriel.dev.python@gmail.com'
EMAIL_PASSWORD = '454622gb'

#criar uma e-maiis mensagem
msg = EmailMessage()
msg['Subject'] = 'Carga #35 chegou ao porto'
msg['From'] = 'gabriel.dev.python@gmail.com'
msg['To'] = 'g.quadrado@outlook.com'
msg.set_content('Favor buscar a carga #35 que está na portaria')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)