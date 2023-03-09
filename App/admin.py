from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_id', 'title', 'vendor', 'product_type', 'created_at', 'updated_at', 'published_at', 'status', 'published_scope','admin_graphql_api_id')

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'variant_id', 'product_id', 'title', 'price', 'inventory_quantity', 'requires_shipping')


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'option_id','name','position')

@admin.register(ProductOptionValues)
class ProductOptionValuesAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'option_id','value')

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'position', 'src', 'alt')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'position', 'src', 'alt')