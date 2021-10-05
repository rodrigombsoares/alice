from django.core.mail import send_mail


def send_email(target_emails):
    send_mail(
        subject='Crie sua conta digital Alice gratuita',
        message='Clicando no link: Conta Digital',
        from_email='from@example.com',
        recipient_list=target_emails,
        html_message='Clicando no link: <a href="tepegueiotario">Conta Digital</a>',
        fail_silently=False,
    )
