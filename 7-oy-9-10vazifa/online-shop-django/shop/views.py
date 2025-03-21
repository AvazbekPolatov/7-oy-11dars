from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import CommentForm

from shop.models import Product, Category
from cart.forms import QuantityForm


def paginat(request, queryset, per_page=6):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def home_page(request):
    max_price = request.GET.get('max_price')
    products = Product.objects.all()

    if max_price:
        try:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
        except ValueError:
            pass

    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)


def product_detail(request, slug):
    form = QuantityForm()
    comment_form = CommentForm()

    product = get_object_or_404(Product.objects.select_related('category'), slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:5]

    comments = product.comments.all()
    favorites = "favorites"
    if request.user.is_authenticated and request.user.likes.filter(id=product.id).exists():
        favorites = "remove"

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('shop:product_detail', slug=slug)

    context = {
        'title': product.title,
        'product': product,
        'form': form,
        'favorites': favorites,
        'related_products': related_products,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'product_detail.html', context)
@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.add(product)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'added'})

    return redirect('shop:product_detail', slug=product.slug)


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.remove(product)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'removed'})

    return redirect('shop:favorites')


@login_required
def favorites(request):
    products = request.user.likes.all()
    context = {'title': 'Favorites', 'products': products}
    return render(request, 'favorites.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    products = Product.objects.filter(title__icontains=query)
    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)


def filter_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    sub_categories = category.sub_categories.all() if hasattr(category, 'sub_categories') else []

    all_categories = [category] + list(sub_categories)
    products = Product.objects.filter(category__in=all_categories).select_related('category')

    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)

