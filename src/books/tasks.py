import random, string
from celery import shared_task
from . import models
from authentication.models import User
from .utils.book_parser import books as parsed_book_list
from django.db.models.signals import post_save
from django.dispatch import receiver

from proj import settings
from django.core.mail import send_mass_mail

@shared_task
def author_add():
    for author in parsed_book_list:
            new_author = models.Author.objects.get_or_create(
                author = author.get('author')
            )
    return new_author

# Pet-task создающий книгу, со случайным именем и рандомным автором
@shared_task
def random_book_add():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range (10)])
    small_random_num = random.randint(1, 4)
    large_random_num = random.randint(128, 1024)
    new_book = models.Book.objects.create(
        book_name = parsed_book_list[random.randint(0, 20)].get('title'),
        book_price = small_random_num,
        author = models.Author.objects.get(pk=small_random_num),
        series = models.Series.objects.get(pk=small_random_num),
        genre = models.Genre.objects.get(pk=small_random_num),
        published = 2021,
        pages = large_random_num,
        pereplet = True,
        ISBN = "test",
        weight = large_random_num,
        age_protect = "test"
    )
    return new_book

@shared_task
@receiver(post_save, sender=models.Book)
def send_mail_book_created(sender, **kwargs):
    book = kwargs.get('instance')
    users = User.objects.all().filter(email_notifications=True)       
    email_list = []
        
    for user in users:
        email_list.append(user.email)
        subject = f'Новая книга уже на сайте!'
        message = f'{book} появилась в магазине'
        from_email = settings.DEFAULT_FROM_EMAIL

        # цикл для скрытия списка получателей
        messages = [(subject, message, from_email, [recipient]) for recipient in email_list]
        send_mass_mail(messages)

