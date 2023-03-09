import requests

def get_shopify_data():

    url="https://vabhas-test.myshopify.com/admin/api/2023-01/products.json"
    headers={
        "Content-Type":"application/json",
        "X-Shopify-Access-Token":"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"
    }

    response=requests.get(url=url,headers=headers)
    return response.json()
