import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('mail.html').read_text())
email = EmailMessage()
email['from'] = 'Kavan Vasani'
email['to'] = 'recipient@gmail.com'
email['subject'] = 'testing'

email.set_content(html.substitute({'name': 'Recipient'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sender@gmail.com', 'password')
	smtp.send_message(email)
	print('all good')