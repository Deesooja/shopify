from App.module.insert_data_in_db import *
from App.models import *

def createProduct(shop , product_dict):

    print('product_dict',product_dict.get('id'))

    product_obj=insert_data(Product,product_dict,None,None,'product_id',False, shop)

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
    return True


def createProductOnCreateTable(product_dict):
    print('product_dict',product_dict.get('id'))
    
    product_obj=insert_data(CreateProduct,product_dict,None,None,None)

    if len(product_dict.get('variants')) >0:

        for variant_dict in product_dict.get('variants'):

            insert_data(CreateProductVariant,variant_dict,product_obj,None,'variant_id')
    
    if len(product_dict.get('options')) > 0:

        for option_dict in product_dict.get('options'):

            option_obj=insert_data(CreateProductOption,option_dict,product_obj,None,'option_id')

            for value in option_dict.get('values'):

                CreateProductOptionValues.objects.create(product=product_obj,option=option_obj,value=value)

    if len(product_dict.get('images')) > 0:

        for images_dict in product_dict.get('images'):

            insert_data(CreateProductImages,images_dict,product_obj,None,'image_id')

    image_dict=product_dict.get('image')
    if image_dict:
        if len(image_dict) >0:

            insert_data(CreateProductImage,image_dict,product_obj,None,'image_id')
            
    return True



def updateProduct(product_dict):
    
    product_obj=insert_data(Product,product_dict,None,None,'product_id',True)

    if len(product_dict.get('variants')) >0:

        for variant_dict in product_dict.get('variants'):

            insert_data(ProductVariant,variant_dict,product_obj,None,'variant_id',True)
    
    if len(product_dict.get('options')) > 0:

        for option_dict in product_dict.get('options'):

            option_obj=insert_data(ProductOption,option_dict,product_obj,None,'option_id',True)

            for value in option_dict.get('values'):

                ProductOptionValues.objects.filter(option=option_obj).update(product=product_obj,option=option_obj,value=value)

    if len(product_dict.get('images')) > 0:

        for images_dict in product_dict.get('images'):

            insert_data(ProductImages,images_dict,product_obj,None,'image_id',True)

    image_dict=product_dict.get('image')
    if image_dict:
        if len(image_dict) >0:

            insert_data(ProductImage,image_dict,product_obj,None,'image_id',True)
    return True