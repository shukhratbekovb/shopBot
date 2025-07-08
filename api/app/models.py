from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название Категории")
    description = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Описание Категории")
    image = models.ImageField(upload_to="/categories", null=True, blank=True, verbose_name="Изображение")
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название Продукта")
    description = models.CharField(max_length=1024, null=True, blank=True, verbose_name="Описание Продукта")
    image = models.ImageField(upload_to="/products", null=True, blank=True, verbose_name="Изображение")
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Продукты"


class Customer(models.Model):
    chat_id = models.IntegerField(unique=True, verbose_name="Ид Чат")
    full_name = models.CharField(max_length=512, verbose_name="ФИО")
    phone = models.CharField(max_length=30, verbose_name="Номер Телефона")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата Создания")
    last_interaction = models.DateTimeField(auto_now=True, verbose_name="Дата Последнего Входа")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Клиенты"


class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="items", verbose_name="Клиент")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(verbose_name="Кол-во")


class Order(models.Model):
    STATUS = (
        ("C", "COMPLETED"),
        ("P", "PROCCESS"),
        ("D", "CANCELLED")
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name="Клиент")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Продукт")
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата Создания")
    status = models.CharField(max_length=2, choices=STATUS, verbose_name="Статус")

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="Клиент")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(verbose_name="Кол-во")
