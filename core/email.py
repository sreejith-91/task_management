from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

from core.models import User


def email_config():
    from app.email_config import EMAIL_CONFIG as config
    backend = EmailBackend(host=config.get('host'), port=config.get('port'), username=config.get('host_user'),
                           password=config.get('password'), use_tls=True
                           )
    return backend


def send_email(subject=None, message=None, attach_link=None):
    conn = email_config()
    mailing_list = User.objects.filter(is_superuser=True).values_list('email', flat=True)
    email = EmailMessage(
        subject=subject, to=mailing_list, connection=conn, body=message
    )
    if attach_link:
        email.attach_file(attach_link)
    email.send()
