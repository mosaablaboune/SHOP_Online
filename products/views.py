from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import AddProductForm


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_details.html', {'product': product})

# CRUD Product

def product_add(request):
    if  request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return render(request, 'products/product_add_success.html')
        else:
            form = AddProductForm()
        
        return render(request, 'products/product_add.html', {'form': form})
    else:
        return redirect('product_list')



def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if  request.user.is_authenticated and request.user.is_superuser:
    
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES, instance=product)

            if form.is_valid():
                form.save()
                return render(request, 'products/product_add_success.html')
        else:
            form = AddProductForm(instance=product)
        
        return render(request, 'products/product_add.html', {'form': form})
    
    else:
        return redirect('product_list')


def product_delete(request, pk):
   
    if  request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk).delete()
        return render(request, 'products/product_delete.html', {'product': product})
    
    else:
        return redirect('product_list')


