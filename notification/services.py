import notification
from .models import Notification
from django.core.mail import send_mail

def create_notification(user):
    notification = Notification.objects.create(

        wallet=user.wallet.wallet_number,
        message=f"""
            Hi {user.first_name}!
            Welcome to OlaPay!
            Your wallet number is {user.wallet.account_number}
        """,

    )


    send_mail(
        subject="Welcome to OlaPay!",
        message= notification.message,
        from_email='',
        recipient_list=[user.email],
        fail_silently=True,
    )

    notification.is_read = True
    notification.save()