from django.core.mail import send_mail


def sendmail(from_email: str, to_email: str, title: str, msg: str):
    subject = title
    message = msg
    from_email = from_email
    to = [to_email]
    send_mail(subject, message, from_email, to)
