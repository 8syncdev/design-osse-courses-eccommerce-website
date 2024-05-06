from dev_core.settings.settings import *
from django.core.mail import send_mail

def send_email_util(subject: str, message: str, recipient_list: list):
    # print(EMAIL_ADMIN_GROUP)
    send_mail(
        subject,
        message,
        EMAIL_ADMIN_GROUP,
        recipient_list,
        fail_silently=False,
    )
    return True