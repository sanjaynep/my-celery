# app/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task():
    send_mail(
        subject="Scheduled Email",
        message="This is an automated email sent every 10 seconds.",
        from_email="pooudellsanjay885@gmail.com",
        recipient_list=["powdelsanjay50@gmail.com"],
        fail_silently=False,
    )