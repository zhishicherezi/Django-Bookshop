
# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView

from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from . import models, forms
from proj import local_settings, settings
class RegistrationAPIView(APIView):

    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)

    def get(self, request, *args, **kwargs):
        # Здесь нечего валидировать или сохранять. Мы просто хотим, чтобы
        # сериализатор обрабатывал преобразования объекта User во что-то, что
        # можно привести к json и вернуть клиенту.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationView(CreateView):
    model = models.User
    success_url = reverse_lazy('authentication:login')
    form_class = forms.CreateAccountForm
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        send_mail(
            subject = f"Спасибо за регистрацию, {username}", 
            message = f'''{first_name}, Вы успешно зарегистрировались в магазине BookShop!
            Также, вы можете подключить Email рассылку в личном кабинете''',
            from_email = settings.DEFAULT_FROM_EMAIL,
            auth_password = local_settings.email_pass,
            recipient_list= [email,]
            )
        self.object = form.save()
        return super().form_valid(form)
        
class ProfileView(DetailView):
    model = models.User

class ProfileUpdateView(UpdateView):
    model = models.User
    fields = [
        'email',
        'first_name',
        'last_name',
        'phone',
        'country',
        'city',
        'index',
        'adress1',
        'email_notifications'
    ]

    def get_success_url(self):
        user_id = self.request.session.get('_auth_user_id')  #ID авторизованного пользователя
        
        return reverse_lazy('authentication:profile', kwargs={'pk': user_id})