from django.shortcuts import render, redirect
from .models import Client, Product, Order
from django.views.generic import ListView
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

def clients(request):
    all_clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': all_clients})

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

def orders(request):
    all_orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': all_orders})

def save_client_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        # Create an instance of the Client model and save the data
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        # Additional actions, such as redirecting to another page
        return redirect('home')
    else:
        return render(request, 'client_data_form.html')
    

class AllOrdersProductsView(ListView):
    model = Product
    template_name = 'all_orders_products.html' 
    context_object_name = 'order_products'  # Замените на имя контекстной переменной

    def get_queryset(self):
        # Получаем значение pk из URL-параметра
        order_id = self.kwargs['pk']
        # Запрос к модели OrderProduct для всех продуктов с указанным order_id
        return Product.objects.filter(order_id=order_id)
    

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Дополнительные действия после сохранения формы
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})