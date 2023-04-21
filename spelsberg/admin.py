from django.contrib import admin

# # Register your models here.


from .models import *

#Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['art', 'name', 'slug', 'price', 'stock', 'available', 'created', 'update']
    list_filter = ['created', 'update', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)