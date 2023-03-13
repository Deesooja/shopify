from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    body_html = models.TextField()
    vendor = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    handle = models.SlugField(max_length=255)
    updated_at = models.DateTimeField()
    published_at = models.DateTimeField()
    template_suffix = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255)
    published_scope = models.CharField(max_length=255)
    tags = models.TextField(blank=True)
    admin_graphql_api_id = models.CharField(max_length=255)

    # def __init__(self, *args, **kwargs):
    #     return str( self.id)
    def __str__(self):
        return str(self.product_id)
    



class ProductVariant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variant_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=255)
    position = models.IntegerField()
    inventory_policy = models.CharField(max_length=255)
    compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fulfillment_service = models.CharField(max_length=255)
    inventory_management = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255, null=True)
    option2 = models.CharField(max_length=255, null=True)
    option3 = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    taxable = models.BooleanField()
    barcode = models.CharField(max_length=255, null=True)
    grams = models.IntegerField()
    image_id = models.BigIntegerField(null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5)
    weight_unit = models.CharField(max_length=255)
    inventory_item_id = models.BigIntegerField()
    inventory_quantity = models.IntegerField()
    old_inventory_quantity = models.IntegerField()
    requires_shipping = models.BooleanField()
    admin_graphql_api_id = models.CharField(max_length=255)

class ProductOption(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    option_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    position=models.IntegerField()

class ProductOptionValues(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    option = models.ForeignKey(ProductOption,on_delete=models.CASCADE,null=True)
    value= models.CharField(max_length=100)


class ProductImages(models.Model):
    image_id = models.BigIntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    position = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    alt = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    src = models.URLField()
    variant_ids = models.JSONField()
    admin_graphql_api_id = models.CharField(max_length=255)

class ProductImage(models.Model):
    image_id = models.BigIntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    position = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    alt = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    src = models.URLField()
    variant_ids = models.JSONField()
    admin_graphql_api_id = models.CharField(max_length=255)