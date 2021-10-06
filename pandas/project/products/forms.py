from django import forms
from django.forms import fields
from .models import Product, Purchase

class PurchaseForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all() , 
                                     label="Product",
                                     widget = forms.Select(attrs={'class' : 'ui selection dropdown'}))      
    class Meta:
        model = Purchase
        fields =  ['product' , 'price' , 'quantity']
