from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('produtos/<int:pk>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:pk>/apagar/', views.produto_delete, name='produto_delete'),

    path('lojas/', views.loja_list, name='loja_list'),
    path('lojas/novo/', views.loja_create, name='loja_create'),
    path('lojas/<int:pk>/', views.loja_detail, name='loja_detail'),
    path('lojas/<int:pk>/editar/', views.loja_update, name='loja_update'),
    path('lojas/<int:pk>/apagar/', views.loja_delete, name='loja_delete'),
    path('anuncios/', views.anuncio_list, name='anuncio_list'),
    path('anuncios/novo/', views.anuncio_create, name='anuncio_create'),
    path('anuncios/<int:pk>/', views.anuncio_detail, name='anuncio_detail'),
    path('anuncios/<int:pk>/editar/', views.anuncio_update, name='anuncio_update'),
    path('anuncios/<int:pk>/apagar/', views.anuncio_delete, name='anuncio_delete'),

    path('dashboard/', views.dashboard, name='dashboard'),
]
