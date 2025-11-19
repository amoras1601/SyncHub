from django.db import models
from django.contrib.auth import get_user_model

class ProdutoCentral(models.Model):
    sku = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.title}"

class Loja(models.Model):
    MARKETPLACE_CHOICES = [
        ('ML', 'Mercado Livre'),
        ('SHOPEE', 'Shopee'),
        ('AMZ', 'Amazon'),
    ]

    name = models.CharField(max_length=255)
    marketplace = models.CharField(max_length=20, choices=MARKETPLACE_CHOICES)
    external_id = models.CharField(max_length=255, blank=True, help_text='ID da loja no marketplace')
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.marketplace})"

class Anuncio(models.Model):
    produto = models.ForeignKey(ProdutoCentral, on_delete=models.CASCADE, related_name='anuncios')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='anuncios')
    marketplace_id = models.CharField(max_length=255, blank=True, help_text='ID do anúncio no marketplace')
    listing_url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('produto', 'loja', 'marketplace_id'),)

    def __str__(self):
        return f"Anúncio {self.marketplace_id or self.id} - {self.produto.sku} @ {self.loja.name}"
