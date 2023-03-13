from App.models import *
from django.forms.models import model_to_dict

def model_obj_to_dict_converter(product_object):

    product_dict = model_to_dict(product_object, fields=['title', 'body_html','product_type','published_scope','status'])
    product_dict['options']=[]
    product_dict['variants']=[]
    product_dict['images']=[]
    product_dict['image']=''

    # variant_dict={}
    # option_dict={}
    # images_dict={}
    # image_dict={}


    for variant in ProductVariant.objects.filter(product=product_object):
        # for key in ['sku', 'price','inventory_quantity','inventory_management','grams','option2','option1']:
        #     variant_dict[key]=getattr(variant,key)
        # product_dict['variants'].append(variant_dict)

        variant_dict=model_to_dict(variant, fields=['sku','price','inventory_quantity','inventory_management','grams','option2','option1'])
        product_dict['variants'].append(variant_dict)
        variant_dict={}

    for option in ProductOption.objects.filter(product=product_object):
        # for key in ['name']:
        #     option_dict[key]=getattr(option, key)
        # option_dict['values']=[]


        option_dict=model_to_dict(option, fields=['name'])
        option_dict['values']=[]

        for value in ProductOptionValues.objects.filter(product=product_object,option=option):
            option_dict['values'].append(value.value)

        product_dict['options'].append(option_dict)


    for images in ProductImages.objects.filter(product=product_object):

        # for key in ['src','alt']:
        #     images_dict[key]=getattr(images, key)
        # product_dict['images'].append(images_dict)

        images_dict=model_to_dict(images, fields=['src','alt'])
        product_dict['images'].append(images_dict)

    product_dict['image']=model_to_dict(ProductImage.objects.get(product=product_object), fields=['src','alt'])
   
    # image=ProductImage.objects.get(product=product_object)
    # for key in ['src','alt']:
    #     image_dict[key]=getattr(image, key)
    #     product_dict['images'].append(image_dict)

    return {"product":product_dict}









    