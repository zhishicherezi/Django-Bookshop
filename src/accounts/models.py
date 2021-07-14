from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.urls import reverse

class CustomUser(AbstractUser):
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=15,
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length = 50,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name='Город',
        max_length = 50,
        blank=True,
        null=True
    )
    index = models.IntegerField(
        verbose_name='Индекс',
        blank=True,
        null=True
    )
    adress1 = models.CharField(
        verbose_name='Адрес 1',
        max_length = 170,
        blank=True,
        null=True
    )
    adress2 = models.CharField(
        verbose_name='Адрес 2',
        max_length = 170,
        blank=True,
        null=True
    )
    extra = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
    )
    def get_absolute_url(self):
        return reverse('books:book-view', args = [self.pk])

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'

class UserProfile(models.Model):  
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=15,
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length = 50,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name='Город',
        max_length = 50,
        blank=True,
        null=True
    )
    index = models.IntegerField(
        verbose_name='Индекс',
        blank=True,
        null=True
    )
    adress1 = models.CharField(
        verbose_name='Адрес 1',
        max_length = 170,
        blank=True,
        null=True
    )
    adress2 = models.CharField(
        verbose_name='Адрес 2',
        max_length = 170,
        blank=True,
        null=True
    )
    extra = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
    )
    
    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username