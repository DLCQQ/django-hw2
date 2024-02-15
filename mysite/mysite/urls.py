from django.urls import path
from myapp import views
from myapp.views import AllOrdersProductsView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.product, name='product'),
    path('orders/', views.ordered_products, name='orders'),
    path('all_orders_products/<int:pk>/', AllOrdersProductsView.as_view(), name='all_orders_products'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]
