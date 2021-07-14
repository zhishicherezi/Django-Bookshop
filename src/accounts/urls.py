from accounts.views import ProfileUpdateView, RegistrationView, ProfileView
from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='books/home.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name ='pwrdchange'),
    path('profile/<int:pk>/',ProfileView.as_view(template_name='accounts/profile.html'),name = 'profile'),
    path('profile-update/<int:pk>/',ProfileUpdateView.as_view(template_name='accounts/profile-upd.html'),name = 'profile-upd')


]