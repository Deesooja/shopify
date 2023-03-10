import requests
import json

def get_shopify_data():

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products.json"
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }

    response=requests.get(url=url,headers=headers)
    return response.json()


def create_shopify_data():

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products.json"
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }
    
    with open('post_data.json', 'r') as f:
        data = json.load(f)

    response=requests.post(url=url,json=data,headers=headers)

    return response.json()


def update_shopify_data():

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products/7461016174784.json"
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }
    
    with open('update_data.json', 'r') as f:
        data = json.load(f)

    response=requests.put(url=url,json=data,headers=headers)

    return response.json()


def delete_shopify_data(type,id):

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/{type}/{id}.json".format(type=type,id=id)
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }

    response=requests.delete(url=url,headers=headers)

    return response.json()