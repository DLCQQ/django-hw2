# Импортируем модуль models из django.db
from django.db import models

# Создаем модель «Клиент»
class Client(models.Model):
    # Поля модели «Клиент»
    name = models.CharField(max_length=100) # Имя клиента
    email = models.EmailField() # Электронная почта клиента
    phone = models.CharField(max_length=20) # Номер телефона клиента
    address = models.TextField() # Адрес клиента
    date_registered = models.DateTimeField(auto_now_add=True) # Дата регистрации клиента

    # Метод для возвращения строкового представления объекта модели
    def __str__(self):
        return self.name

# Создаем модель «Товар»
class Product(models.Model):
    # Поля модели «Товар»
    name = models.CharField(max_length=100) # Название товара
    description = models.TextField() # Описание товара
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена товара
    quantity = models.IntegerField() # Количество товара
    date_added = models.DateTimeField(auto_now_add=True) # Дата добавления товара

    # Метод для возвращения строкового представления объекта модели
    def __str__(self):
        return self.name

# Создаем модель «Заказ»
class Order(models.Model):
    # Поля модели «Заказ»
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # Связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    products = models.ManyToManyField(Product) # Связь с моделью «Товар», указывает на товары, входящие в заказ
    total = models.DecimalField(max_digits=10, decimal_places=2) # Общая сумма заказа
    date_ordered = models.DateTimeField(auto_now_add=True) # Дата оформления заказа

    # Метод для возвращения строкового представления объекта модели
    def __str__(self):
        return f"Заказ №{self.id} от {self.client.name}"

# Допишем несколько функций CRUD для работы с моделями по желанию

# Функция для создания нового клиента
def create_client(name, email, phone, address):
    # Создаем объект модели «Клиент» с заданными параметрами
    client = Client(name=name, email=email, phone=phone, address=address)
    # Сохраняем объект в базе данных
    client.save()
    # Возвращаем объект
    return client

# Функция для получения списка всех клиентов
def get_all_clients():
    # Получаем QuerySet всех объектов модели «Клиент»
    clients = Client.objects.all()
    # Возвращаем QuerySet
    return clients

# Функция для обновления данных клиента по его идентификатору
def update_client(client_id, name=None, email=None, phone=None, address=None):
    # Получаем объект модели «Клиент» по его идентификатору
    client = Client.objects.get(id=client_id)
    # Если передан параметр name, обновляем поле name объекта
    if name is not None:
        client.name = name
    # Если передан параметр email, обновляем поле email объекта
    if email is not None:
        client.email = email
    # Если передан параметр phone, обновляем поле phone объекта
    if phone is not None:
        client.phone = phone
    # Если передан параметр address, обновляем поле address объекта
    if address is not None:
        client.address = address
    # Сохраняем изменения в базе данных
    client.save()
    # Возвращаем объект
    return client

# Функция для удаления клиента по его идентификатору
def delete_client(client_id):
    # Получаем объект модели «Клиент» по его идентификатору
    client = Client.objects.get(id=client_id)
    # Удаляем объект из базы данных
    client.delete()
    # Возвращаем сообщение об успешном удалении
    return f"Клиент {client.name} удален"

# Функция для создания нового товара
def create_product(name, description, price, quantity):
    # Создаем объект модели «Товар» с заданными параметрами
    product = Product(name=name, description=description, price=price, quantity=quantity)
    # Сохраняем объект в базе данных
    product.save()
    # Возвращаем объект
    return product

# Функция для получения списка всех товаров
def get_all_products():
    # Получаем QuerySet всех объектов модели «Товар»
    products = Product.objects.all()
    # Возвращаем QuerySet
    return products

# Функция для обновления данных товара по его идентификатору
def update_product(product_id, name=None, description=None, price=None, quantity=None):
    # Получаем объект модели «Товар» по его идентификатору
    product = Product.objects.get(id=product_id)
    # Если передан параметр name, обновляем поле name объекта
    if name is not None:
        product.name = name
    # Если передан параметр description, обновляем поле description объекта
    if description is not None:
        product.description = description
    # Если передан параметр price, обновляем поле price объекта
    if price is not None:
        product.price = price
    # Если передан параметр quantity, обновляем поле quantity объекта
    if quantity is not None:
        product.quantity = quantity
    # Сохраняем изменения в базе данных
    product.save()
    # Возвращаем объект
    return product

# Функция для удаления товара по его идентификатору
def delete_product(product_id):
    # Получаем объект модели «Товар» по его идентификатору
    product = Product.objects.get(id=product_id)
    # Удаляем объект из базы данных
    product.delete()
    # Возвращаем сообщение об успешном удалении
    return f"Товар {product.name} удален"

# Функция для создания нового заказа
def create_order(client, products, total):
    # Создаем объект модели «Заказ» с заданными параметрами
    order = Order(client=client, total=total)
    # Сохраняем объект в базе данных
    order.save()
    # Добавляем товары в заказ
    order.products.add(*products)
    # Возвращаем объект
    return order

# Функция для получения списка всех заказов
def get_all_orders():
    # Получаем QuerySet всех объектов модели «Заказ»
    orders = Order.objects.all()
    # Возвращаем QuerySet
    return orders

# Функция для обновления данных заказа по его идентификатору
def update_order(order_id, client=None, products=None, total=None):
    # Получаем объект модели «Заказ» по его идентификатору
    order = Order.objects.get(id=order_id)
    # Если передан параметр client, обновляем поле client объекта
    if client is not None:
        order.client = client
    # Если передан параметр products, обновляем поле products объекта
    if products is not None:
        # Удаляем все товары из заказа
        order.products.clear()
        # Добавляем новые товары в заказ
        order.products.add(*products)
    # Если передан параметр total, обновляем поле total объекта
    if total is not None:
        order.total = total
    # Сохраняем изменения в базе данных
    order.save()
    # Возвращаем объект
    return order

# Функция для удаления заказа по его идентификатору
def delete_order(order_id):
    # Получаем объект модели «Заказ» по его идентификатору
    order = Order.objects.get(id=order_id)
    # Удаляем объект из базы данных
    order.delete()
    # Возвращаем сообщение об успешном удалении
    return f"Заказ №{order.id} удален"