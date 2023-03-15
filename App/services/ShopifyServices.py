from App.models import *
from django.core.serializers.json import DjangoJSONEncoder
from App.module.shopify import *
from App.module.model_to_dict import *
from App.module.DatabaseServises import *
import json

def creating_shopify_product_by_create_dbtable(shop , product_object):

    product_dict=model_obj_to_dict_converter_for_create_table(product_object)

    product_json=json.dumps(product_dict,cls=DjangoJSONEncoder)

    # my_json = json.loads(product_json)
    # print(my_json)
    # created=createProduct(my_json.get('product'))  # OK

    # print(product_json)

    response=create_shopify_data(shop,product_json,False)

    print('response.status_code',response.status_code)

    if response.status_code ==201:

        created=createProduct(shop , response.body.get('product'))  # OK

        if created:

            product_object.shopify_created_status=True

            product_object.save()

            return True
    
    return False


def updating_shopify_product_by_dbtable(product_object):

    # for product_object in Product.objects.filter(shopify_updated_status=False):

    # product_object=Product.objects.get(id=66)

    product_dict=model_obj_to_dict_converter(product_object,update=True)

    product_json=json.dumps(product_dict,cls=DjangoJSONEncoder)

    response=update_shopify_data(shop=product_object.shop , product_id=product_object.product_id , product=product_json, file=False)
    # print('response.body',response.body)

    if response.isSuccess:

        product_object.shopify_updated_status=True
        product_object.save()

        return True
    return False
    
    
    

