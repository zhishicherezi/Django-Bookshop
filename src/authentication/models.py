from django.db import models

# Create your models here.
import jwt
from datetime import datetime, timedelta

from django.conf import settings 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


from django.db import models

class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=100
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=100
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

    email_notifications = models.BooleanField(verbose_name='Email подписка на рассылку', default=False)

    def create_user(self, username, email, first_name, last_name, password=None, phone=None, country=None, city=None, adress1=None, adress2=None, index=None, extra=None, email_notifications=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if phone is None:
            raise TypeError('Users must have a phone address.')

        user = self.model(username=username, first_name=first_name, last_name=last_name, email=self.normalize_email(email), phone = phone, country = country, city = city, index=index, adress1=adress1, adress2=adress2, extra=extra, email_notifications=email_notifications)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_notifications = models.BooleanField(verbose_name='Email подписка на рассылку', default=False)
    
    # Дополнительные данные пользователя для заказа
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=100
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=100
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
    # Дополнительный поля, необходимые Django
    # при указании кастомной модели пользователя.

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.username

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode()