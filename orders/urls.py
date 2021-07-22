from django.urls import path

from .views import order, order_list

urlpatterns = [
    path('', order_list, name='order_list'),
    path('new/', order, name='order'),
    #path('done/<int:pk>', order_done, name='order_done'),

]