from django.urls import reverse
from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    keywords = models.CharField(max_length=200, default='Ключевые слова')
    art = models.CharField(max_length=20, null=True, blank=True, verbose_name='Артикул')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.CharField(max_length = 30, verbose_name='Количество')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товарный каталог'
        verbose_name = 'Товар'

    def __str__(self):
        return self.art
    

    def get_absolute_url(self):
        return reverse('spelsberg:spelsberg_detail', args=[self.id, self.slug])
    

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('spelsberg:spelsberg_lists', args={self.slug})
    


