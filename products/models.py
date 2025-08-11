from datetime import datetime

import pytz
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from pages.models import BasicModel


class ProductCategory(BasicModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'


class ProductSize(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product size'
        verbose_name_plural = 'product sizes'


class ProductColor(models.Model):
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product color'
        verbose_name_plural = 'product colors'


class ProductBrand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product brand'
        verbose_name_plural = 'product brands'


class ProductModel(BasicModel):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()

    image = models.ImageField(upload_to='products/', null=True, blank=True)
    categories = models.ManyToManyField(ProductCategory, related_name='products_categories')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name='products_brands')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    discount = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    def is_new(self):
        tashkent_tz = pytz.timezone('Asia/Tashkent')
        now = datetime.now(tashkent_tz)

        # Ensure created_at is timezone-aware
        if self.created_at.tzinfo is None:
            created_at = tashkent_tz.localize(self.created_at)
        else:
            created_at = self.created_at.astimezone(tashkent_tz)

        diff = now - created_at
        return diff.days <= 3

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ProductQuantity(BasicModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='products_quantity')
    quantity = models.PositiveSmallIntegerField()

    sizes = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='products_sizes')
    colors = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='products_colors')
    fk_name = 'product' 


class ProductImageModel(BasicModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='products/')
    fk_name = 'product'

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'



class BlogModel(BasicModel):
    image = models.ImageField(verbose_name='blog_image')
    title = models.TextField(verbose_name='blog_title')
    short_description = models.TextField(verbose_name='blog_short_des')
    long_description = models.TextField(verbose_name='blog_long_des')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'