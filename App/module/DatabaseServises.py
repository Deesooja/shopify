from App.module.insert_data_in_db import *
from App.models import *

def createProduct( product_dict):
    product_obj=insert_data(Product,product_dict,None,None,'product_id')

    if len(product_dict.get('variants')) >0:

        for variant_dict in product_dict.get('variants'):

            insert_data(ProductVariant,variant_dict,product_obj,None,'variant_id')
    
    if len(product_dict.get('options')) > 0:

        for option_dict in product_dict.get('options'):

            option_obj=insert_data(ProductOption,option_dict,product_obj,None,'option_id')

            for value in option_dict.get('values'):

                ProductOptionValues.objects.filter(option=option_obj).update(product=product_obj,option=option_obj,value=value)

    if len(product_dict.get('images')) > 0:

        for images_dict in product_dict.get('images'):

            insert_data(ProductImages,images_dict,product_obj,None,'image_id')

    image_dict=product_dict.get('image')
    if image_dict:
        if len(image_dict) >0:

            insert_data(ProductImage,image_dict,product_obj,None,'image_id')
    return