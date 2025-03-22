from django.urls import path
from .views import create_order, checkout, fake_payment, user_orders, buy_now, order_detail

app_name = "orders"

urlpatterns = [
    path("create/", create_order, name="create_order"),
    path("checkout/<int:order_id>/", checkout, name="pay_order"),
    path("payment/<int:order_id>/", fake_payment, name="fake_payment"),
    path("my-orders/", user_orders, name="user_orders"),
    path("buy-now/", buy_now, name="buy_now"),
    path("order/<int:order_id>/", order_detail, name="order_detail"),

]
