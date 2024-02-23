from django.shortcuts import render, redirect
from .models import Client, Product, Order
from django.views.generic import ListView
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def clients(request):
    all_clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': all_clients})

# def products(request):
#     all_products = Product.objects.all()
#     return render(request, 'products.html', {'products': all_products})




# def product(request):
#     # Здесь ты можешь получить список заказов из базы данных или другого источника данных
#     orders = ['Заказ 1', 'Заказ 2', 'Заказ 3']

#     return render(request, 'product.html', {'orders': orders})


def product(request):
    # Заглушки данных о заказах
    orders = [
        {'id': 1, 'name': 'Заказ 1'},
        {'id': 2, 'name': 'Заказ 2'},
        {'id': 3, 'name': 'Заказ 3'}
    ]

    return render(request, 'product.html', {'orders': orders})






# def orders(request):
#     all_orders = Order.objects.all()
#     return render(request, 'orders.html', {'orders': all_orders})

# def save_client_data(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         address = request.POST.get('address')
#         # Create an instance of the Client model and save the data
#         client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
#         # Additional actions, such as redirecting to another page
#         return redirect('home')
#     else:
#         return render(request, 'client_data_form.html')


def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')

        # Вернуть JSON-ответ с обновленными данными о корзине
        cart_items = [{'name': 'Товар 1', 'price': 100}, {'name': 'Товар 2', 'price': 200}]
        return JsonResponse({'success': True, 'cart_items': cart_items})

    return JsonResponse({'success': False})
    

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


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product-id')
        product_name = request.POST.get('product-name')

        # Получение или создание корзины из сессии
        cart = request.session.get('cart', [])

        # Добавление выбранного товара в корзину
        cart.append({'product_id': product_id, 'product_name': product_name})

        # Сохранение обновленной корзины в сессии
        request.session['cart'] = cart

        # Вернуть JSON-ответ с обновленным списком выбранных товаров
        return render(request, 'add_to_cart.html')
        return JsonResponse({'success': True, 'cart_items': cart})

    return JsonResponse({'success': False})




# def orders(request):
#     # В этой функции ты можешь получить список заказов из базы данных или другого источника данных
#     orders = ['Заказ 1', 'Заказ 2', 'Заказ 3']

    return render(request, 'orders.html', {'orders': orders})

@csrf_protect
def my_view(request):
    if request.method == 'POST':
        # Получение данных из запроса
        data = request.POST.get('data')
        
        # Вывод данных в консоль
        print(data)
        
        return HttpResponse('Success')  # Возвращаем ответ
        
    else:
        return HttpResponse('Invalid request method')  # Возвращаем ошибку, если метод запроса не POST
    
    
    
def ordered_products(request):
    # Получаем текущую дату и вычисляем даты для фильтрации
    current_date = timezone.now().date()
    week_ago = current_date - timedelta(days=7)
    month_ago = current_date - timedelta(days=30)
    year_ago = current_date - timedelta(days=365)
    
    # Фильтруем заказы по заданным периодам и сортируем их по времени
    week_orders = Order.objects.filter(date__range=[week_ago, current_date]).order_by('-date')
    month_orders = Order.objects.filter(date__range=[month_ago, current_date]).order_by('-date')
    year_orders = Order.objects.filter(date__range=[year_ago, current_date]).order_by('-date')
    
    # Создаем множество для хранения уникальных товаров
    unique_products = set()
    
    # Получаем список уникальных товаров из заказов
    for order in week_orders | month_orders | year_orders:
        unique_products.update(order.products.all())
    
    context = {
        'week_orders': week_orders,
        'month_orders': month_orders,
        'year_orders': year_orders,
        'unique_products': unique_products
    }
    
    return render(request, 'ordered_products.html', context)


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверные учетные данные'})

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def add_new_client(request):
    # Создаем нового клиента
    client = Client(name='Имя клиента', email='email@example.com', phone_number='1234567890', address='Адрес клиента')
    client.save()

    return render(request, 'client_added.html', {'client': client})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})