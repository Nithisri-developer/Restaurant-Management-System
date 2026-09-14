from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin


class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')

        return redirect('customer_home')


from .models import Product
from .forms import Product_Form


class ProductList(StaffRequiredMixin, View):

    def get(self, request):
        all_products = Product.objects.all()

        context = {
            'all_products': all_products
        }

        return render(request, 'products.html', context)


class ProductAdd(StaffRequiredMixin, View):

    def get(self, request):
        product_form = Product_Form()

        context = {
            'product_form': product_form
        }

        return render(request, 'products_add.html', context)

    def post(self, request):
        product_form = Product_Form(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')

        context = {
            'product_form': product_form
        }

        return render(request, 'products_add.html', context)


class ProductDelete(StaffRequiredMixin, View):

    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()

        return redirect('/inventory/products/')


class ProductUpdate(StaffRequiredMixin, View):

    def get(self, request, id):
        product = Product.objects.get(id=id)

        product_form = Product_Form(instance=product)

        context = {
            'product_form': product_form
        }

        return render(request, 'products_add.html', context)

    def post(self, request, id):
        product = Product.objects.get(id=id)

        product_form = Product_Form(
            request.POST,
            request.FILES,
            instance=product
        )

        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')

        context = {
            'product_form': product_form
        }

        return render(request, 'products_add.html', context)