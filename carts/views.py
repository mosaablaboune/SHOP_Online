from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart
# Create your views here.

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart = Cart.objects.get(user=request.user)

    cart.items.add(product)

    return redirect('cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart = Cart.objects.get(user=request.user)

    cart.items.remove(product)

    return redirect('cart')

def clear_all(request):

    cart = Cart.objects.get(user=request.user)

    cart.items.clear()

    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()
    total_price = user.cart.total_price()

    return render(request, 'carts/cart.html', {'products': products, 'total_price': total_price})





