from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .utils.cart import Cart
from shop.models import Product

from shop.models import Product
Product.objects.all()

@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.add(product=product, quantity=1)
    messages.success(request, 'Product added to your cart!', 'success')

    return redirect('shop:product_detail', slug=product.slug)
@login_required
def show_cart(request):
    cart = Cart(request)

    for item in cart:
        item['total_price'] = item['quantity'] * item['product'].get_final_price()

    context = {'title': 'Cart', 'cart': cart}
    return render(request, 'cart.html', context)




@login_required
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:show_cart')