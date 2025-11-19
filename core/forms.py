from django import forms
from .models import ProdutoCentral


class ProdutoCentralForm(forms.ModelForm):
    class Meta:
        model = ProdutoCentral
        fields = ['sku', 'title', 'description', 'price']

from .models import Loja, Anuncio

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['name', 'marketplace', 'external_id', 'owner']

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['produto', 'loja', 'marketplace_id', 'listing_url', 'price', 'stock', 'active']
