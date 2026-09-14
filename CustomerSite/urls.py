from django.urls import path

from .views import (
    customer_home_view,
    menu_view,
    add_to_cart,
    cart_view,
    increase_cart,
    decrease_cart,
    remove_from_cart,
    checkout_view,
    place_order,
    order_success_view,
    about_view,
    contact_view,
    booking_view,
    booking_success_view,
    my_bookings_view,
)


urlpatterns = [

    path(
        '',
        customer_home_view,
        name='customer_home'
    ),

    path(
        'menu/',
        menu_view,
        name='menu'
    ),

    path(
        'cart/add/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        cart_view,
        name='cart'
    ),

    path(
        'cart/increase/<int:product_id>/',
        increase_cart,
        name='increase_cart'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        decrease_cart,
        name='decrease_cart'
    ),

    path(
        'cart/remove/<int:product_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'checkout/',
        checkout_view,
        name='checkout'
    ),

    path(
        'place-order/',
        place_order,
        name='place_order'
    ),

    path(
        'order-success/',
        order_success_view,
        name='order_success'
    ),

    path(
        'about/',
        about_view,
        name='about'
    ),

    path(
        'contact/',
        contact_view,
        name='contact'
    ),

    path(
        'booking/',
        booking_view,
        name='booking'
    ),

    path(
        'booking-success/',
        booking_success_view,
        name='booking_success'
    ),

    path(
    'my-bookings/',
    my_bookings_view,
    name='my_bookings'
),
]