from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from Inventory.models import Product
from OrderManagement.models import Orders, Customer
from .models import ContactMessage, TableBooking



def customer_home_view(request):
    return render(request, 'customer/home.html')


def menu_view(request):

    products = Product.objects.all()

    return render(request, 'customer/menu.html', {
        'products': products
    })


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:

        cart[product_id] = current_quantity + 1

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('menu')


def cart_view(request):

    cart = request.session.get('cart', {})

    products = Product.objects.filter(
        id__in=cart.keys()
    )

    cart_items = []

    for product in products:

        quantity = cart[str(product.id)]

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    total = sum(
        item['subtotal']
        for item in cart_items
    )

    item_count = sum(
        item['quantity']
        for item in cart_items
    )

    return render(request, 'customer/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count
    })


def increase_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        product = Product.objects.get(id=product_id)

        if cart[product_id] < product.stock:
            cart[product_id] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def decrease_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def checkout_view(request):

    cart = request.session.get('cart', {})

    products = Product.objects.filter(
        id__in=cart.keys()
    )

    cart_items = []

    for product in products:

        quantity = cart[str(product.id)]

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    total = sum(
        item['subtotal']
        for item in cart_items
    )

    return render(request, 'customer/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

def place_order(request):

    print("========== PLACE ORDER ==========")
    print("METHOD:", request.method)

    cart = request.session.get('cart', {})

    print("CART:", cart)

    if request.method != 'POST':
        print("NOT POST")
        return redirect('cart')

    if not cart:
        print("CART IS EMPTY")
        return redirect('checkout')

    customer, created = Customer.objects.get_or_create(
    user=request.user,
    defaults={
        'customer_name': request.user.username,
        'customer_since': timezone.now().date()
    }
)

    for product_id, quantity in cart.items():

        print("PRODUCT:", product_id)
        print("QUANTITY:", quantity)

        product = Product.objects.get(id=product_id)

        print("STOCK:", product.stock)

        if quantity > product.stock:
            print("NOT ENOUGH STOCK")
            return redirect('checkout')

        amount = product.price * quantity

        gst_amount = (amount * product.gst) / 100

        bill_amount = amount + gst_amount

        order_number = (
            f"WEB{timezone.now().strftime('%Y%m%d%H%M%S')}"
            f"{product.id}"
        )

        order = Orders.objects.create(
            customer_reference=customer,
            product_reference=product,
            order_number=order_number,
            order_date=timezone.now().date(),
            quantity=quantity,
            amount=amount,
            gst_amount=gst_amount,
            bill_amount=bill_amount
        )

        print("ORDER CREATED:", order.id)

        product.stock -= quantity
        product.save()

    request.session['cart'] = {}
    request.session.modified = True

    print("ORDER COMPLETE")
    print("REDIRECTING TO SUCCESS PAGE")

    return redirect('order_success')


def order_success_view(request):

    return render(
        request,
        'customer/order_success.html'
    )

def about_view(request):

    return render(
        request,
        'customer/about.html'
    )

def contact_view(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('contact')

    return render(
        request,
        'customer/contact.html'
    )

@login_required(login_url='login')
def booking_view(request):
    if request.method == 'POST':
        TableBooking.objects.create(
    customer=request.user if request.user.is_authenticated else None,
    name=request.POST.get('name'),
    phone=request.POST.get('phone'),
    date=request.POST.get('date'),
    time=request.POST.get('time'),
    guests=request.POST.get('guests'),
    special_request=request.POST.get('special_request')
)

        return redirect('booking_success')

    return render(request, 'customer/booking.html')

def booking_success_view(request):
    return render(request, 'customer/booking_success.html')

@login_required(login_url='login')
def my_bookings_view(request):
    bookings = TableBooking.objects.filter(
        customer=request.user
    ).order_by('-date', '-time')

    return render(
        request,
        'customer/my_bookings.html',
        {'bookings': bookings}
    )