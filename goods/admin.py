from django.contrib import admin
from goods.models import Category, Product

#admin.site.register(Category) #простая регистрация таблиц
#admin.site.register(Product)

@admin.register(Category)  #регистрация таблиц в админ с более тонкими настройками
class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug': ('name',)} # автоматически заполняется поля slug по имени

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # автоматически заполняется поля slug по имени