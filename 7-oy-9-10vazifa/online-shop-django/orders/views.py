from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Order, OrderItem
from cart.utils.cart import Cart


@login_required
def create_order(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price = item['product'].get_final_price()
        )

    cart.clear()
    messages.success(request, "Your order has been created successfully!", "success")

    return redirect("orders:order_detail", order_id=order.id)

@login_required
def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'title':'Checkout' ,'order':order}
    return render(request, 'checkout.html', context)


@login_required
def fake_payment(request, order_id):
    cart = Cart(request)
    cart.clear()
    order = get_object_or_404(Order, id=order_id)
    order.status = True
    order.save()
    return redirect('orders:user_orders')


@login_required
def user_orders(request):
    orders = request.user.orders.all()
    context = {'title':'Orders', 'orders': orders}
    return render(request, 'user_orders.html', context)

@login_required
def buy_now(request):
    cart = Cart(request)
    if not cart:
        return redirect("cart:show_cart")

    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(
            order=order, product=item['product'],
            price=item['price'], quantity=item['quantity']
        )

    cart.clear()
    return redirect("orders:user_orders")

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'title': 'Order Detail', 'order': order}
    return render(request, 'order_detail.html', context)
