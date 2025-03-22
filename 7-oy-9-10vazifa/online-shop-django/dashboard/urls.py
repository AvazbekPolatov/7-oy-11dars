from django.urls import path
from .views import products, add_product, delete_product, edit_product, add_category, orders, order_detail

app_name = "dashboard"

urlpatterns = [
    path("products/", products, name="products"),
    path("products/add/", add_product, name="add_product"),
    path("products/<int:id>/delete/", delete_product, name="delete_product"),
    path("products/<int:id>/edit/", edit_product, name="edit_product"),
    path("categories/add/", add_category, name="add_category"),
    path("orders/", orders, name="orders"),
    path("orders/<int:id>/", order_detail, name="order_detail"),
]
