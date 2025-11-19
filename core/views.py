from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

from .models import ProdutoCentral, Loja, Anuncio
from .forms import ProdutoCentralForm, LojaForm, AnuncioForm

def produto_list(request):
    q = request.GET.get('q', '').strip()
    page = request.GET.get('page', 1)
    produtos = ProdutoCentral.objects.all().order_by('-updated_at')
    if q:
        produtos = produtos.filter(models.Q(title__icontains=q) | models.Q(sku__icontains=q))
    paginator = Paginator(produtos, 10)
    try:
        produtos_page = paginator.page(page)
    except PageNotAnInteger:
        produtos_page = paginator.page(1)
    except EmptyPage:
        produtos_page = paginator.page(paginator.num_pages)
    return render(request, 'core/produto_list.html', {'produtos': produtos_page, 'q': q, 'paginator': paginator})

def produto_detail(request, pk):
    produto = get_object_or_404(ProdutoCentral, pk=pk)
    anuncios = produto.anuncios.select_related('loja').all()
    return render(request, 'core/produto_detail.html', {'produto': produto, 'anuncios': anuncios})

@login_required
def produto_create(request):
    # Support HTMX: return partial form or row fragment when requested
    is_htmx = request.headers.get('HX-Request') == 'true'
    if request.method == 'POST':
        form = ProdutoCentralForm(request.POST)
        if form.is_valid():
            produto = form.save()
            if is_htmx:
                # return the new table row fragment to be inserted by HTMX
                return render(request, 'core/partials/produto_row_partial.html', {'p': produto})
            return redirect(reverse('core:produto_detail', args=[produto.pk]))
    else:
        form = ProdutoCentralForm()

    template = 'core/produto_form.html'
    if is_htmx:
        template = 'core/partials/produto_form_partial.html'

    return render(request, template, {'form': form, 'action': 'Criar'})

@login_required
def produto_update(request, pk):
    produto = get_object_or_404(ProdutoCentral, pk=pk)
    if request.method == 'POST':
        form = ProdutoCentralForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect(reverse('core:produto_detail', args=[produto.pk]))
    else:
        form = ProdutoCentralForm(instance=produto)
    return render(request, 'core/produto_form.html', {'form': form, 'action': 'Editar'})

@login_required
def produto_delete(request, pk):
    produto = get_object_or_404(ProdutoCentral, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect(reverse('core:produto_list'))
    return render(request, 'core/produto_delete.html', {'produto': produto})

def loja_list(request):
    lojas = Loja.objects.all()
    return render(request, 'core/loja_list.html', {'lojas': lojas})

def loja_detail(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    anuncios = loja.anuncios.select_related('produto').all()
    return render(request, 'core/loja_detail.html', {'loja': loja, 'anuncios': anuncios})

@login_required
def loja_create(request):
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            loja = form.save(commit=False)
            loja.owner = request.user
            loja.save()
            return redirect(reverse('core:loja_detail', args=[loja.pk]))
    else:
        form = LojaForm()
    return render(request, 'core/loja_form.html', {'form': form, 'action': 'Criar'})

@login_required
def loja_update(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect(reverse('core:loja_detail', args=[loja.pk]))
    else:
        form = LojaForm(instance=loja)
    return render(request, 'core/loja_form.html', {'form': form, 'action': 'Editar'})

@login_required
def loja_delete(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    if request.method == 'POST':
        loja.delete()
        return redirect(reverse('core:loja_list'))
    return render(request, 'core/loja_delete.html', {'loja': loja})

def anuncio_list(request):
    q = request.GET.get('q', '').strip()
    page = request.GET.get('page', 1)
    anuncios = Anuncio.objects.select_related('produto', 'loja').all().order_by('-updated_at')
    if q:
        anuncios = anuncios.filter(models.Q(marketplace_id__icontains=q) | models.Q(produto__title__icontains=q) | models.Q(loja__name__icontains=q))
    paginator = Paginator(anuncios, 10)
    try:
        anuncios_page = paginator.page(page)
    except PageNotAnInteger:
        anuncios_page = paginator.page(1)
    except EmptyPage:
        anuncios_page = paginator.page(paginator.num_pages)
    return render(request, 'core/anuncio_list.html', {'anuncios': anuncios_page, 'q': q, 'paginator': paginator})

def anuncio_detail(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    return render(request, 'core/anuncio_detail.html', {'anuncio': anuncio})

@login_required
def anuncio_create(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            anuncio = form.save()
            return redirect(reverse('core:anuncio_detail', args=[anuncio.pk]))
    else:
        form = AnuncioForm()
    return render(request, 'core/anuncio_form.html', {'form': form, 'action': 'Criar'})

@login_required
def anuncio_update(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect(reverse('core:anuncio_detail', args=[anuncio.pk]))
    else:
        form = AnuncioForm(instance=anuncio)
    return render(request, 'core/anuncio_form.html', {'form': form, 'action': 'Editar'})

@login_required
def anuncio_delete(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == 'POST':
        anuncio.delete()
        return redirect(reverse('core:anuncio_list'))
    return render(request, 'core/anuncio_delete.html', {'anuncio': anuncio})

@login_required
def dashboard(request):
    total_produtos = ProdutoCentral.objects.count()
    total_lojas = Loja.objects.count()
    total_anuncios = Anuncio.objects.count()
    recent_produtos = ProdutoCentral.objects.order_by('-updated_at')[:5]
    return render(request, 'core/dashboard.html', {
        'total_produtos': total_produtos,
        'total_lojas': total_lojas,
        'total_anuncios': total_anuncios,
        'recent_produtos': recent_produtos,
    })
