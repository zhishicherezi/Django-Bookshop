from django.core.mail import send_mail, send_mass_mail
from authentication.models import User



class EmailNotificationMixin:
    book_name = None
    author = None
    email = None
    userlist = []

    def __init__(self):
        for user in User.objects.all():
            return self.userlist.append(user.email)
    
    def send_email(self):
        send_mass_mail(
            f"{self.book_name} уже в нашем магазине!",
            f"{self.book_name} от автора {self.author} появилась в нашем магазине",
            "django.test.email.bookshop@gmail.com",
            self.userlist
        )
    if email == True:
        send_email()
