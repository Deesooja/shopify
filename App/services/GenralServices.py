from django.conf import settings
from App.models import *

def api_and_header(shop ,product_id=None ,update_url=False,):
    
    url=settings.GET_POST_URL %(shop.domain_name)
    if update_url:
        url=settings.UPDATE_DELETE %(shop.domain_name,product_id)
   
    headers=settings.HEADER['X-Shopify-Access-Token']=shop.access_token
    # print('settings.HEADER',settings.HEADER)
    

    return url , settings.HEADER
    
