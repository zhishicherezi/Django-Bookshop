from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView
from django.views.generic.edit import DeleteView, UpdateView
from django.views import View
from django.http import HttpResponseRedirect
from . import models, forms
from books import models as books_models
from django.urls import reverse_lazy

class CartView(UpdateView):
    template_name = 'carts/cart-edit.html'
    model = models.BooksInCart
    form_class = forms.CreateCartForm
    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.update_or_create(
            pk=cart_id,
            defaults={},
            
        )
        if created:
            self.request.session['cart_id'] = cart.pk

        book_id = self.request.GET.get('book_id')
        if book_id:
            book = books_models.Book.objects.get(pk=int(book_id))
            book_in_cart, book_created = models.BooksInCart.objects.update_or_create(
                cart=cart,
                book=book,
                defaults={
                    'unit_price': book.book_price
                },
            )
            if not book_created:
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
            else:
                book_in_cart.unit_price = book.book_price
            
            book_in_cart.save()
        return cart



class DeleteGoodInCartView(RedirectView):
    model = models.BooksInCart
    success_url = reverse_lazy('carts:cart-edit')

    def get_redirect_url(self, *args, **kwargs):
        xs = super().get_redirect_url(*args, **kwargs)
        print(self.kwargs)
        xs = self.model.objects.get(pk=self.kwargs.get('pk').delete())
        return xs

class CartUpdate(View):
    def post(self, request):
        action = request.POST.get('submit')
        if action == 'save_cart':
            cart_id = self.request.session.get('cart_id')
            cart, created = models.Cart.objects.update_or_create(
                pk=cart_id,
                defaults={},
            )
            if created:
                self.request.session['cart_id'] = cart.pk
            
            goods = cart.goods.all()
            for key, value in request.POST.items():
                if 'quantitygood_' in key:
                    pk = int(key.split('_')[1])
                    good = goods.get(pk=pk)
                    good.quantity = int(value)
                    good.save()
            return HttpResponseRedirect(reverse_lazy('carts:cart-edit'))
        
        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('orders:new-order'))

