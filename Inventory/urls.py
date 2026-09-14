from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/add/', ProductAdd.as_view(), name='ProductAdd'),
    path('products/update/<int:id>/', ProductUpdate.as_view(), name='product_update'),
    path('products/delete/<int:id>/', ProductDelete.as_view(), name='product_delete'),
]