from django.shortcuts import render
from django.views import View
from .module.insert_data_in_db import insert_data
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from .module.shopify import get_shopify_data
from .models import *
import json
# Create your views here.

class IndexView(View):

    def get(self,request,*args, **kwargs):
        context={}
        shopify_data=get_shopify_data()
        # print(shopify_data)
        for product_dict in shopify_data.get('products'):

            if not Product.objects.filter(product_id=product_dict.get('product_id')).exists():

                product_obj=insert_data(Product,product_dict,None,None,'product_id')

                if len(product_dict.get('variants')) >0:

                    for variant_dict in product_dict.get('variants'):

                        insert_data(ProductVariant,variant_dict,product_obj,None,'variant_id')
                
                if len(product_dict.get('options')) > 0:

                    for option_dict in product_dict.get('options'):

                        option_obj=insert_data(ProductOption,option_dict,product_obj,None,'option_id')

                        for value in option_dict.get('values'):

                            ProductOptionValues.objects.create(product=product_obj,option=option_obj,value=value)

                if len(product_dict.get('images')) > 0:

                    for images_dict in product_dict.get('images'):

                        insert_data(ProductImages,images_dict,product_obj,None,'image_id')

                image_dict=product_dict.get('image')
                if image_dict:
                    if len(image_dict) >0:

                        insert_data(ProductImage,image_dict,product_obj,None,'image_id')

        return render(request,'app/index.html',context)




class ProductsTableView(View):

    def get(self,request,*args, **kwargs):
        context={}
        return render(request,'app/product_table.html',context)
    

    

    


