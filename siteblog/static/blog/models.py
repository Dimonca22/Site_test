from django.db import models
from django.urls import reverse

'''
Category
=========
title, slug

Post
=========
title, slug, author, content, created_at, photo, views, category, tags
'''


class Category(models.Model):
    """Категории, к которым относятся товары"""
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT,
                                 verbose_name='Выберите категорию'
                                 )

    class Meta:
        ordering = ['title']
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
