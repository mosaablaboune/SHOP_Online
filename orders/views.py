from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import OrderForm
from .utils import send_order_email


@login_required
def order(request):
    user = request.user

    if not user.cart.items.exists():
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            order = form.save(user)
            send_order_email(user, order)
            return render(request, 'orders/order_success.html')
    else:
        form = OrderForm()

    return render(request, 'orders/order.html', {'form': form})


def order_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.all()
        return render(request, 'orders/orders_list.html', {'orders': orders})
    else:
        return redirect('product_list')

#def order_done(request, order_id):
    #if  request.user.is_authenticated and request.user.is_superuser:
       # order = get_object_or_404(Order, pk=order_id).delete()
      #  return render(request, 'orders/order_done.html', {'order': order})
    
 #   else:
 #       return redirect('order_list')

    
