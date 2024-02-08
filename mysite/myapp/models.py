from django.db import models
from datetime import timedelta
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.client.name}"



def create_client(name, email, phone_number, address):
    return Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)

def create_product(name, description, price, quantity):
    return Product.objects.create(name=name, description=description, price=price, quantity=quantity)

def create_order(client, products, total_amount):
    order = Order.objects.create(client=client, total_amount=total_amount)
    order.products.set(products)
    return order


def get_recent_orders(client_instance):
    """
    Возвращает список заказанных клиентом товаров из всех его заказов с сортировкой по времени.
    :param client_instance: Экземпляр клиента.
    :return: Список товаров.
    """
    end_date = timezone.now()
    start_date_7_days = end_date - timedelta(days=7)
    start_date_30_days = end_date - timedelta(days=30)
    start_date_365_days = end_date - timedelta(days=365)

    # Получаем заказы клиента за последние 7 дней
    recent_orders_7_days = Order.objects.filter(order_date__range=(start_date_7_days, end_date), client=client_instance)

    # Получаем заказы клиента за последние 30 дней
    recent_orders_30_days = Order.objects.filter(order_date__range=(start_date_30_days, end_date), client=client_instance)

    # Получаем заказы клиента за последний год
    recent_orders_365_days = Order.objects.filter(order_date__range=(start_date_365_days, end_date), client=client_instance)

    # Объединяем товары из всех заказов
    all_items = set()
    for order in recent_orders_7_days | recent_orders_30_days | recent_orders_365_days:
        all_items.update(order.items.all())

    return list(all_items)