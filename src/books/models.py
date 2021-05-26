from django.db import models

# Create your models here.
class Author(models.Model):
    author = models.CharField(
        verbose_name='Автор',
        max_length=35
    )
    def __str__(self) -> str:
        return f"{self.author}"
    class Meta:
        verbose_name = 'Автор',
        verbose_name_plural = 'Авторы'

class Series(models.Model):
    series = models.CharField(
        verbose_name='Серия',
        max_length=35
    )
    def __str__(self) -> str:
        return f"{self.series}"
    class Meta:
        verbose_name='Серия'
        verbose_name_plural ='Серия'
class Genre(models.Model):
    genre = models.CharField(
        verbose_name='Жанр',
        max_length=30
    )
    def __str__(self) -> str:
        return f"{self.genre}"
    class Meta:
        verbose_name = 'Жанр',
        verbose_name_plural = 'Жанры'

class Publisher(models.Model):
    publisher = models.CharField(
        verbose_name='Издательство',
        max_length=35
    )
    def __str__(self) -> str:
        return f"{self.publisher}"
    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
class Book(models.Model):
    book_name = models.CharField(max_length=100,
        verbose_name = 'Название книги')
    book_photo = models.ImageField(
        verbose_name = 'book img')
    book_price = models.FloatField(
        verbose_name = 'price',
        default = 100)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        default = 1
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        default = 1     
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        default = 1
    )

    created = models.DateTimeField(
        verbose_name = 'Дата внесения в БД')
    published = models.IntegerField(
        verbose_name = 'Год издания',
        blank = True)
    pages = models.IntegerField(
        verbose_name='Страниц',
        blank = True
    )
    pereplet = models.BooleanField(
        verbose_name='Твердый переплет',
        blank = True
    )
    ISBN = models.CharField(max_length=100,
        verbose_name='ISBN',
        default=None
    )
    weight = models.IntegerField(
        verbose_name='Вес',
        default=None
    )
    age_protect = models.CharField(max_length=30,
        verbose_name='Возратсные ограничения',
        default=None
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        default = 1
    )
    active = models.BooleanField(
        verbose_name='Доступен для заказа',
        default=True
    )
    entry_date = models.DateTimeField(
        verbose_name='Дата внесения в каталог',
        auto_now_add=True,
        auto_now = False,
        
    )
    change_date = models.DateTimeField(
        verbose_name='Дата правки',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) -> str:
        return f"Название : {self.book_name} Автор : {self.author}"
    class Meta:
        verbose_name = 'Книга',
        verbose_name_plural = 'Книги'



