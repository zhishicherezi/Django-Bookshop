from django.views.generic.base import TemplateView
from accounts.views import RegistrationView, ProfileView
from django.urls import path, include
from . import views
app_name = 'orders'

urlpatterns = [
    path('new-order/', views.CreateOrderView.as_view(), name = 'new-order'),
    path('done/', views.OrderDone.as_view(), name='order-done'),
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
    path('order-detail/<int:pk>', views.OrderDetailView.as_view(), name='order'),
    path('order-update/<int:pk>', views.OrderUpdateView.as_view(), name='order-update'),
    path('order-delete/<int:pk>', views.OrderDeleteView.as_view(), name='order-delete')


]