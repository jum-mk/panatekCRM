from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=155)
    img = models.ImageField(null=False, upload_to='brands/')
    desc = models.TextField(null=True, blank=True)
    brochure = models.CharField(max_length=255, null=True, blank=True)    

    def __str__(self):
        return self.name

    def get_cats(self):
        cats = Category.objects.filter(brand__id=self.id)
        return cats

    def get_absolute_url(self):
        return reverse('single_brand_view', kwargs={
            'name': self.name
        })


class Category(models.Model):
    name = models.CharField(max_length=155, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_product_count(self):
        var = Product.objects.filter(brand__id=self.brand.id, category__name=self.name).count()
        return var

    def get_absolute_url(self):
        return reverse('catalogue', kwargs={
            'name': self.name
        })


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=155)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    meta_description = models.CharField(max_length=125, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_images(self):
        images = ProductImage.objects.filter(product=self.id)
        return images

    def get_desc_images(self):
        images = DescriptionProductImage.objects.filter(product=self.id)
        return images

    def get_absolute_url(self):
        return reverse('single_product', kwargs={
            'id': self.id
        })


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.product.name


class DescriptionProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.product.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    company = models.CharField(max_length=30, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Pdf(models.Model):
    file = models.FileField(upload_to='pdfs/')
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email
