from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name = "Наименование") #максимальная длина 150, уникальное поле, имя в админке - Наименование
    slag = models.SlugField(max_length=200, unique=True, blank = True, null = True, verbose_name = "URL") #максимальная длина 200, уникальное поле, поле может быть пустым,  имя в админке - URL

    class Meta:
        db_table = "сategory" # имя таблицы в БД
        verbose_name = "Категорию" #имя в админке в ед.числе
        verbose_name_plural = "Категории" #имя в админке в множественом.числе

class Product (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name = "Наименование") #максимальная длина 150, уникальное поле, имя в админке - Наименование
    slag = models.SlugField(max_length=200, unique=True, blank = True, null = True, verbose_name = "URL") #максимальная длина 200, уникальное поле, поле может быть пустым,  имя в админке - URL
    description = models.TextField(blank = True, null = True, verbose_name = "Описание" ) 
    image = models.ImageField(upload_to='goods_images', blank = True, null = True, verbose_name = "Изображение" ) #ссылка куда ссылаеться картинка
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name = "Цена") #значение по умолчанию, 7 - цифр перед запятой, 2 - цифры после запятой
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name =  "Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name =  "Количество")
    category = models.ForeignKey(to = Category, on_delete = models.CASCADE, verbose_name = "Категория")
    
    class Meta:
        db_table = "product" # имя таблицы в БД
        verbose_name = "Продукт" #имя в админке в ед.числе
        verbose_name_plural = "Продукты" #имя в админке в множественом.числе