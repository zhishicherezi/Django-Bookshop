from django.views.generic import CreateView, FormView, ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from . import models, forms
from django.views.generic.base import TemplateView

from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from carts import models as cart_models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import AnonymousUser
# Create your views here.

class CreateOrderView(FormView):
    template_name = 'orders/new-order.html'
    form_class = forms.OrderCreateForm
    success_url = reverse_lazy('orders:order-done')
    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        phone = self.request.user.phone
        country = self.request.user.country
        city = self.request.user.city        
        index = self.request.user.index
        adress = self.request.user.adress1
        extra = self.request.user.extra

        return {'phone': phone, 'country': country, 'city':city, 'index':index, 'adress':adress, 'extra': extra}

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = cart_models.Cart.objects.update_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))
         

        ci = form.cleaned_data.get('phone')
        phone = form.cleaned_data.get('phone')
        country = form.cleaned_data.get('country')
        city = form.cleaned_data.get('city')
        index = form.cleaned_data.get('index')
        adress = form.cleaned_data.get('adress')
        extra = form.cleaned_data.get('extra')
        customer = self.request.user
        user_id = self.request.session.get('_auth_user_id')
        order = models.Order.objects.create(
            cart=cart,
            contact_info = ci,
            phone = phone,
            country=country,
            city=city,
            index=index,
            adress=adress,
            extra=extra,
            customer=customer
        )
        self.request.session.pop('cart_id')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = cart_models.Cart.objects.update_or_create(
            pk=cart_id,
            defaults={},
        )
        x['object'] = cart
        return x
        
class OrderDone(TemplateView):
    template_name = 'orders/done.html'

class OrderDetailView(DetailView):
    model = models.Order

class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy('home')

class OrderUpdateView(UpdateView):
    model = models.Order
    form_class = forms.OrderUpdateForm
    success_url = reverse_lazy('orders:order-list')

class OrderListView(ListView, PermissionRequiredMixin):
    model = models.Order
    template_name = 'orders/order_list.html'
    permission_required = 'order.view_order'
    
    def get_queryset(self):
        qs = super().get_queryset()
        filter = (self.request.GET.get('filter'))
        customer_id = self.request.user.pk        
        if self.request.user.is_staff == False: 
            if filter == 'user':
                return qs.filter(customer_id = customer_id)
            elif filter == 'entry_date':
                return qs.order_by('-created').filter(customer_id = customer_id)
            elif filter == 'status':
                return qs.order_by('-status').filter(customer_id = customer_id)
            else:
                return qs

        if filter == 'user':
            return qs.filter(customer_id = customer_id)
        elif filter == 'entry_date':
            return (qs.order_by('-created'))
        elif filter == 'status':
            return (qs.order_by('-status'))
        else:
            return qs
