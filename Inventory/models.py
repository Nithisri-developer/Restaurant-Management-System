from django.db import models


class Product(models.Model):

    FOOD_STYLE_CHOICES = [
        ('Indian', 'Indian'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('Mexican', 'Mexican'),
        ('French', 'French'),
        ('Western', 'Western'),
        ('Beverages & Desserts', 'Beverages & Desserts'),
    ]

    FOOD_TYPE_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
    ]

    product_name = models.CharField(max_length=200, null=True)
    product_code = models.CharField(max_length=20, null=True)
    price = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=0)
    picture = models.ImageField(null=True, upload_to='images/')

    food_style = models.CharField(
        max_length=50,
        choices=FOOD_STYLE_CHOICES,
        default='Indian'
    )

    food_type = models.CharField(
        max_length=20,
        choices=FOOD_TYPE_CHOICES,
        default='Vegetarian'
    )

    menu_image = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product_name