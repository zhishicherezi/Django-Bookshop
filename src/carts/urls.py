from accounts.views import RegistrationView, ProfileView
from django.urls import path, include
from . import views
app_name = 'carts'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart-edit'),
    path('delete-good-in-cart/<int:pk>', views.DeleteGoodInCartView.as_view(), name='book-delete-in-cart'),
    path('update-cart/', views.CartUpdate.as_view(), name='update-cart')
]