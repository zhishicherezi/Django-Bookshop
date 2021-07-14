from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from carts import models as carts_models
from accounts import models as acc_models
from django.contrib.auth import get_user_model

User = get_user_model()
DEFAULT_STATUS_ID = 1

class OrderStatus(models.Model):
    status = models.CharField(
        verbose_name='Статус',
        max_length=35,
        default='new',
    )
    def __str__(self):
        return f"{self.status}"

class Order(models.Model):

    cart = ForeignKey(
        carts_models.Cart,
        on_delete=models.PROTECT,
        verbose_name='Order',
        related_name='orders'
    )
    books = ForeignKey(
        carts_models.BooksInCart,
        on_delete=models.CASCADE,
        verbose_name='Книги',
        default=1,
        related_name='order_books'
    )
    customer = ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='orders'
    )
    contact_info = models.TextField(
        verbose_name="Contact info"
    )
    phone = models.TextField(
        verbose_name="Телефон"
    )
    country = models.TextField(
        verbose_name="Страна"
    )
    city = models.TextField(
        verbose_name="Город"
    )
    index = models.TextField(
        verbose_name="Индекс"
    )
    adress = models.TextField(
        verbose_name="Адрес"
    )
    extra = models.TextField(
        verbose_name="Дополнительная информация",
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now=True,
        auto_now_add=False
    )
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
