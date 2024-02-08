from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('save_client_data/', views.save_client_data, name='save_client_data')
]
