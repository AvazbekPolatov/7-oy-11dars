from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('faqs/', views.faqs_page, name='faqs_page'),
    path('about/', views.about_page, name='about_page'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add/favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites, name='favorites'),
    path('search/', views.search, name='search'),
    path('filter/<slug:slug>/', views.filter_by_category, name='filter_by_category'),
]
