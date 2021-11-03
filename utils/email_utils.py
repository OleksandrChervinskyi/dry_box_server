import os

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class MailUtils:
    @staticmethod
    def register_mail_sender(username, address):
        template = get_template('register.html')
        html_content = template.render({"username": username})
        msg = EmailMultiAlternatives('Hi', 'Вы зарегистрировались!!!', os.environ.get('EMAIL_HOST_USER'),
                                     [address])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
