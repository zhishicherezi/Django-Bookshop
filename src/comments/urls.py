from django.urls import path, include
from . import views
app_name = 'comments'

urlpatterns = [
    path('create-comment/', views.CommentCreateView.as_view(), name = 'create-comment'),
]