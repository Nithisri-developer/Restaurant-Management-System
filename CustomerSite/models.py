from django.db import models
from django.conf import settings

class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TableBooking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
    )
    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    date = models.DateField()

    time = models.TimeField()

    guests = models.PositiveIntegerField()

    special_request = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time}"