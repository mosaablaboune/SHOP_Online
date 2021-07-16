from django.forms import ModelForm
from django.forms import fields
from .models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'title', 'description', 'price', 'image')