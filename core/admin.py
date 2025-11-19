from django.contrib import admin
from .models import ProdutoCentral, Loja, Anuncio


@admin.register(ProdutoCentral)
class ProdutoCentralAdmin(admin.ModelAdmin):
    list_display = ('sku', 'title', 'price', 'created_at')
    search_fields = ('sku', 'title')


@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ('name', 'marketplace', 'external_id', 'owner')
    search_fields = ('name', 'external_id')


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('marketplace_id', 'produto', 'loja', 'price', 'stock', 'active')
    search_fields = ('marketplace_id',)
