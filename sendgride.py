# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid.helpers.mail import *
import sendgrid
from django.core.mail import send_mail
import os
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from os import getenv, path
 
def email():
    message = Mail(
        from_email='from_email@example.com',
        to_emails='lawcubegsm@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
       
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    return (sg)

print(settings.SENDGRID_API_KEY)
sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
from_email = Email("noreply@example.com")
to_email = To("lawcubegsm@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

subject = 'Subject of Your Email'
message = 'Your email content here.'
from_email = settings.DEFAULT_FROM_EMAIL
to_email = ['lawcubegsm@gmail.com']

send_mail(subject, message, from_email, to_email, fail_silently=True)


# print(email(), getenv('SENDGRID_API_KEY'), 'fffff')
