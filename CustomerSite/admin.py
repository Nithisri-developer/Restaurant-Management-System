from django.contrib import admin
from .models import ContactMessage, TableBooking


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')


@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'customer',
    'phone',
    'date',
    'time',
    'guests',
    'status',
    'created_at',
)
    list_filter = (
        'status',
        'date',
    )

    search_fields = (
        'name',
        'phone',
    )