from django.contrib import admin
from .models import *


admin.site.site_header = 'Panatek'
admin.site.site_title = 'Panatek'
admin.site.index_title = 'Admin'




class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'category']
    inlines = [ProductImageInline]





admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(DescriptionProductImage)
admin.site.register(Profile)

