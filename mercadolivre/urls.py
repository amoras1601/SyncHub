from django.urls import path
from . import views

app_name = 'mercadolivre'

urlpatterns = [
    path('', views.index, name='index'),
    path('oauth/callback/', views.oauth_callback, name='oauth_callback'),
    path('webhook/', views.webhook, name='webhook'),
]
