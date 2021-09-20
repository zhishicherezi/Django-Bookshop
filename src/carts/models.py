from django.db import models
from django.contrib.auth import get_user_model
from authentication.models import User as CustomUser
User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        related_name='carts',
        related_query_name='mycustomer',
        verbose_name='Cart',
        on_delete=models.PROTECT
        )

    @property
    def total_price(self):
        total_price = 0
        goods = self.goods.all() 
        for good in goods:
            total_price += good.total_price
        return total_price



class BooksInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Cart',
        related_name='goods'
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        verbose_name='book'
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1
    )
    unit_price = models.DecimalField(
        verbose_name='Unit Price',
        max_digits=5,
        decimal_places=2
    ) 

    @property
    def total_price(self):
        return self.unit_price * self.quantity


class CartModel(models.Model):
    owner = models.ForeignKey( 
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Cart'
    )
    books = models.ManyToManyField(
        BooksInCart,
        related_name='book_carts'
    )
    total_books = models.IntegerField(
        default=0
    )
    final_price = models.DecimalField(
        decimal_places=2,
        max_digits=5
    )