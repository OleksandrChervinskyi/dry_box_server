import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class MailUtils:
    @staticmethod
    def register_mail_sender(username, address, url):
        template = get_template('../templates/register.html')
        html_content = template.render({"username": username, "url": url})
        msg = EmailMultiAlternatives('Привет', f'Чтоб активировать аккаунт перейдите по ссылке {url}',
                                     os.environ.get('EMAIL_HOST_USER'),
                                     [address])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
