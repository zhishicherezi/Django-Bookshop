from django.db import models

# Create your models here.

class Mailing(models.Model):
    mail_to = models.EmailField(
        verbose_name='Получатель'
    )
    text = models.TextField(
        verbose_name='Содержание'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )