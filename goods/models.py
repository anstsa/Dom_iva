from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Наименование"
    )  # максимальная длина 150, уникальное поле, имя в админке - Наименование
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )  # максимальная длина 200, уникальное поле, поле может быть пустым,  имя в админке - URL

    class Meta:
        db_table = "сategory"  # имя таблицы в БД
        verbose_name = "Категорию"  # имя в админке в ед.числе
        verbose_name_plural = "Категории"  # имя в админке в множественом.числе
        ordering = ('id',) #для пагинации, сортировка по ид

    def __str__(self):  #возвращает имя, а не oblect(id/pk)
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Наименование"
    )  # максимальная длина 150, уникальное поле, имя в админке - Наименование
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )  # максимальная длина 200, уникальное поле, поле может быть пустым,  имя в админке - URL
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )  # ссылка куда ссылаеться картинка
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )  # значение по умолчанию, 4 - цифр, 2 - цифры после запятой
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"  # имя таблицы в БД
        verbose_name = "Продукт"  # имя в админке в ед.числе
        verbose_name_plural = "Продукты"  # имя в админке в множественом.числе
        ordering = ("id",) #сортировка по ид

    def __str__(self): #возвращает имя и количество, а не oblect(id/pk)
        return f'{self.name}, Количество - {self.quantity}'

    def display_id (self):    #метод, в методе должен быть self, возвращает id в формате 00005
        return f'{self.id:05}'

    def sell_price (self): #метод, вычисляющий скидку на товар если скидка есть, то считаем ее, если нет то цена остается такой же
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
