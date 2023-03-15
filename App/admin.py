from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','shop','product_id','shopify_updated_status', 'title', 'vendor', 'product_type', 'created_at', 'updated_at', 'published_at', 'status', 'published_scope','admin_graphql_api_id')

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


#<-------------------------------------------For Crating shopify data db----------------> 

@admin.register(CreateProduct)
class CreateProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'body_html', 'status', 'shopify_created_status', 'created_at', 'updated_at')

@admin.register(CreateProductVariant)
class CreateProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'sku', 'title', 'price', 'inventory_quantity', 'inventory_management', 'grams','option1','option2','created_at','updated_at')


@admin.register(CreateProductOption)
class CreateProductOptionAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'name','created_at','updated_at')

@admin.register(CreateProductOptionValues)
class CreateProductOptionValuesAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'option_id','value','created_at','updated_at')

@admin.register(CreateProductImages)
class CreateProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',  'src', 'alt','created_at','updated_at')

@admin.register(CreateProductImage)
class CreateProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product',  'src', 'alt','created_at','updated_at')

# <------------------------------------------------Shop Table---------------->
@admin.register(Shop)
class CreateProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain_name',  'access_token', 'use_it', 'created_at','updated_at')
