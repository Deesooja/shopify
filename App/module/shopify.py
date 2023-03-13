import requests
import json
from App.models import *

def get_shopify_data():

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products.json"
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }

    response=requests.get(url=url,headers=headers)
    print(response.status_code)
    return response.json()


def create_shopify_data(product=None,file=True):

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products.json"

    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }
    data=product
    if file:
        with open('post_data.json', 'r') as f:
            data = json.load(f)

    response=requests.post(url=url,data=data,headers=headers)

    return response.json()


def update_shopify_data(product_id,product=None,file=True):

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products/%s.json" % (product_id)
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }
    data=product
    if file:
        with open('update_data.json', 'r') as f:
            data = json.load(f)

    response=requests.put(url=url,data=data,headers=headers)

    return response.json()

def delete_shopify_data(type,id):

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/{type}/{id}.json".format(type=type,id=id)
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }

    requests.delete(url=url,headers=headers)

    if type=='products':
        product_obj=Product.objects.get(product_id=id)
        product_obj.delete()

    if type=='variants':
        product_variant_obj=ProductVariant.objects.get(product_id=id)
        product_variant_obj.delete()

    if type=='options':
        product_option_obj=ProductOption.objects.get(product_id=id)
        product_option_obj.delete()

    if type=='images':
        product_images_obj=ProductImages.objects.get(product_id=id)
        product_images_obj.delete()

    if type=='image':
        product_image_obj=ProductImage.objects.get(product_id=id)
        product_image_obj.delete()

    return 