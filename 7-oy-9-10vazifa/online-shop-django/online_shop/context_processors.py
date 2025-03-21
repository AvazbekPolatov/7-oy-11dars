from cart.utils.cart import Cart
from shop.models import Category


def return_cart(request):
    cart = Cart(request)
    cart_count = sum(int(item['quantity']) for item in cart)  # ✅ Xatolik tuzatildi
    return {'cart_count': cart_count}


def return_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
