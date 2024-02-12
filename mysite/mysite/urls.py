from django.urls import path
from myapp import views
from myapp.views import AllOrdersProductsView

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('all_orders_products/<int:pk>/', AllOrdersProductsView.as_view(), name='all_orders_products'),
]
