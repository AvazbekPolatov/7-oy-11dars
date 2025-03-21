from django.contrib import admin
from .models import Order, OrderItem, City, Delivery

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(City)
admin.site.register(Delivery)
