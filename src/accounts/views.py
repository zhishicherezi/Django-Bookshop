from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# Create your views here.
#CRUD
User = get_user_model()

class RegistrationView(CreateView):
    model = models.CustomUser
    success_url = reverse_lazy('login')
    form_class = forms.CreateAccountForm

class ProfileView(DetailView):
    model = models.CustomUser

class ProfileUpdateView(UpdateView):
    model = models.CustomUser
    fields = [
        'email',
        'first_name',
        'last_name',
        'phone',
        'country',
        'city',
        'index',
        'adress1',
    ]

    def get_success_url(self):
        print(self.request.session.get('_auth_user_id'))       
        user_id = self.request.session.get('_auth_user_id')  #ID авторизованного пользователя
        
        return reverse_lazy('accounts:profile', kwargs={'pk': user_id})

    


    