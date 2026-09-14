from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from Inventory.models import Product


def staff_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and user.is_staff,
        login_url='login'
    )(view_func)


@staff_required
def OrdersAdd(request):

    order_form = Orders_Form()

    if request.method == 'POST':

        order_form = Orders_Form(request.POST)

        print("POST DATA:", request.POST)
        print("FORM ERRORS:", order_form.errors)

        if order_form.is_valid():

            selected_product = Product.objects.get(
                id=request.POST['product_reference']
            )

            quantity = float(request.POST['quantity'])

            amount = float(selected_product.price) * quantity

            gst_amount = (amount * selected_product.gst) / 100

            bill_amount = amount + gst_amount

            new_order = Orders(
                customer_reference_id=request.POST['customer_reference'],
                product_reference_id=request.POST['product_reference'],
                order_number=request.POST['order_number'],
                order_date=request.POST['order_date'],
                quantity=quantity,
                amount=amount,
                gst_amount=gst_amount,
                bill_amount=bill_amount
            )

            new_order.save()

            print("ORDER SAVED:", new_order.id)

            return redirect('/orders/all/orders/')

    context = {
        'order_form': order_form
    }

    return render(request, 'orders_add.html', context)


@staff_required
def OrdersList(request):

    all_orders = Orders.objects.all()

    context = {
        'all_orders': all_orders
    }

    return render(request, 'orders.html', context)


@staff_required
def CustomerList(request):

    all_customers = Customer.objects.all()

    context = {
        'all_customers': all_customers
    }

    return render(request, 'customers.html', context)


@staff_required
def CustomerAdd(request):

    customer_form = Customer_Form()

    if request.method == 'POST':

        customer_form = Customer_Form(request.POST)

        if customer_form.is_valid():

            customer_form.save()

            return redirect('/orders/all/customers/')

    context = {
        'customer_form': customer_form
    }

    return render(request, 'customers_add.html', context)


@staff_required
def CustomerDelete(request, id):

    customer = Customer.objects.get(id=id)

    customer.delete()

    return redirect('/orders/all/customers/')


@staff_required
def CustomerUpdate(request, id):

    customer = Customer.objects.get(id=id)

    customer_form = Customer_Form(
        instance=customer
    )

    if request.method == 'POST':

        customer_form = Customer_Form(
            request.POST,
            instance=customer
        )

        if customer_form.is_valid():

            customer_form.save()

            return redirect('/orders/all/customers/')

    context = {
        'customer_form': customer_form
    }

    return render(request, 'customers_add.html', context)


@staff_required
def OrdersDelete(request, id):

    order = Orders.objects.get(id=id)

    order.delete()

    return redirect('/orders/all/orders/')