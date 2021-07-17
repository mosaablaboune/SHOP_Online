from django.urls import path

from .views import order, order_list

urlpatterns = [
    path('order/', order_list, name='order_list'),
    path('order/new/', order, name='order'),
]