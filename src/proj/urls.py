"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books.views import BookListView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from . import serializer_views

router = routers.DefaultRouter()
router.register(r'books-api', serializer_views.BookViewSet)

urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('books/', include('books.urls', namespace='books')),
    path('', BookListView.as_view(template_name = 'books/home.html'), name ='home'),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls', namespace='accounts')),
    path('carts/', include('carts.urls', namespace='carts')),
    path('orders/',include('orders.urls',namespace='orders')),
    path('comments/',include('comments.urls',namespace='comments')),
    path('', include(router.urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

