from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import ProdutoCentral, Loja, Anuncio


def home(request):
    # Simple landing with quick stats and links
    total_produtos = ProdutoCentral.objects.count()
    total_lojas = Loja.objects.count()
    total_anuncios = Anuncio.objects.count()
    return render(request, 'home.html', {
        'total_produtos': total_produtos,
        'total_lojas': total_lojas,
        'total_anuncios': total_anuncios,
    })


@login_required
def profile(request):
    # Show basic user info and lojas owned by the user
    user = request.user
    lojas = Loja.objects.filter(owner=user)
    return render(request, 'registration/profile.html', {'user': user, 'lojas': lojas})
