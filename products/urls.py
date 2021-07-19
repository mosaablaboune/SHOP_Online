from django.urls import path

from .views import product_edit, product_list, product_details, product_add, product_delete

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/add', product_add, name='product_add'),
    path('products/<pk>', product_details, name='product_details'),
    path('products/edit/pk', product_edit, name='product_edit'),
    path('products/delete/pk', product_delete, name='product_delete'),
]
