from App.models import *
from django.forms.models import model_to_dict

def model_obj_to_dict_converter(product_object,update=False):

    product_dict = model_to_dict(product_object, fields=['title', 'body_html','product_type','published_scope','status'])
    
    if update:

        product_dict = model_to_dict(product_object)
        product_dict['id']=product_dict.get('product_id')
        

    product_dict['options']=[]
    product_dict['variants']=[]
    product_dict['images']=[]
    product_dict['image']=''

    for variant in ProductVariant.objects.filter(product=product_object):

        variant_dict=model_to_dict(variant, fields=['title','sku','price','inventory_quantity','inventory_management','grams','option2','option1'])
        
        if update:

            variant_dict=model_to_dict(variant)
            variant_dict['id']=variant_dict.get('variant_id')
            variant_dict['product_id']=product_dict.get('product_id')

        product_dict['variants'].append(variant_dict)

        # variant_dict={}

    for option in ProductOption.objects.filter(product=product_object):

        option_dict=model_to_dict(option, fields=['name'])

        if update:

            option_dict=model_to_dict(option)
            option_dict['id']=option_dict.get('option_id')
            option_dict['product_id']=product_dict.get('product_id')

        option_dict['values']=[]

        for value in ProductOptionValues.objects.filter(product=product_object,option=option):

            option_dict['values'].append(value.value)

        product_dict['options'].append(option_dict)


    for images in ProductImages.objects.filter(product=product_object):

        images_dict=model_to_dict(images, fields=['src','alt'])

        if update:

            images_dict=model_to_dict(images)
            images_dict['id']=images_dict.get('image_id')
            images_dict['product_id']=product_dict.get('product_id')

        product_dict['images'].append(images_dict)

    product_dict['image']=model_to_dict(ProductImage.objects.get(product=product_object), fields=['src','alt'])
    
    if update:

        product_dict['image']=model_to_dict(ProductImage.objects.get(product=product_object))
        product_dict['image']['id'] = product_dict['image'].get('image_id')
        product_dict['image']['product_id']=product_dict.get('product_id')

    return {"product":product_dict}



def model_obj_to_dict_converter_for_create_table(product_object,update=False):

    product_dict = model_to_dict(product_object, fields=['id','title', 'body_html','product_type','published_scope','status','created_at','updated_at'])
    
    if update:

        product_dict = model_to_dict(product_object)
        product_dict['id']=product_dict.get('product_id')
        

    product_dict['options']=[]
    product_dict['variants']=[]
    product_dict['images']=[]
    product_dict['image']=''

    for variant in CreateProductVariant.objects.filter(product=product_object):

        variant_dict=model_to_dict(variant, fields=['id','title','sku','price','inventory_quantity','inventory_management','grams','option2','option1','created_at','updated_at'])
        
        if update:

            variant_dict=model_to_dict(variant)
            variant_dict['id']=variant_dict.get('variant_id')
            variant_dict['product_id']=product_dict.get('product_id')

        product_dict['variants'].append(variant_dict)

        # variant_dict={}

    for option in CreateProductOption.objects.filter(product=product_object):

        option_dict=model_to_dict(option, fields=['id','name','created_at','updated_at'])

        if update:

            option_dict=model_to_dict(option)
            option_dict['id']=option_dict.get('option_id')
            option_dict['product_id']=product_dict.get('product_id')

        option_dict['values']=[]

        for value in CreateProductOptionValues.objects.filter(product=product_object,option=option):

            option_dict['values'].append(value.value)

        product_dict['options'].append(option_dict)


    for images in CreateProductImages.objects.filter(product=product_object):

        images_dict=model_to_dict(images, fields=['id','src','alt','created_at','updated_at'])

        if update:

            images_dict=model_to_dict(images)
            images_dict['id']=images_dict.get('image_id')
            images_dict['product_id']=product_dict.get('product_id')

        product_dict['images'].append(images_dict)

    product_dict['image']=model_to_dict(CreateProductImage.objects.get(product=product_object), fields=['id','src','alt','created_at','updated_at'])
    
    if update:

        product_dict['image']=model_to_dict(CreateProductImage.objects.get(product=product_object))
        product_dict['image']['id'] = product_dict['image'].get('image_id')
        product_dict['image']['product_id']=product_dict.get('product_id')

    return {"product":product_dict}





    