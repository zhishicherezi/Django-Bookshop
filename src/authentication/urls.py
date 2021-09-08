from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

from .views import LoginAPIView, RegistrationAPIView
from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

from .views import ProfileUpdateView, ProfileView, RegistrationView

app_name = 'authentication'
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view(), name='api-user'),
    path('users/', RegistrationAPIView.as_view(), name = 'api-register'),
    path('users/login/', LoginAPIView.as_view(),name = 'api-login'),

    path('registration/', RegistrationView.as_view(template_name='authentication/registration.html'), name = 'register'),
    path('login/', views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', views.LoginView.as_view(template_name='authentication/logout.html'), name='logout'),

    path('profile/<int:pk>/',ProfileView.as_view(template_name='authentication/profile.html'),name = 'profile'),
    path('profile-update/<int:pk>/',ProfileUpdateView.as_view(template_name='authentication/profile-upd.html'),name = 'profile-upd'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name ='pwrdchange'),


    


    
]