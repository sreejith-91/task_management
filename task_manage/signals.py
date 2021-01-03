from django.db.models.signals import post_save
from django.dispatch import receiver

from core.email import send_email
from core.models import Task


@receiver(post_save, sender=Task)
def notify_admin(sender, instance, created, **kwargs):
    subject = f"Task Updated - {instance.name} by {instance.user.name}"
    message = f"Task updated by {instance.user.name} \n"
    if created:
        subject = f"Task Created - {instance.name} by {instance.user.name}"
        message = f"New task created by {instance.user.name} \n"

    message_detail = f"{message}TasK Name: {instance.name}\n" \
                     f"Description: {instance.description}\n" \
                     f"Time Required: {instance.time_required}"
    send_email(subject=subject, message=message_detail)
