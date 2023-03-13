from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .module.insert_data_in_db import insert_data
from .module.model_to_dict import model_obj_to_dict_converter
from .module.DatabaseServises import *
from django.core.serializers.json import DjangoJSONEncoder
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from .module.shopify import *
from .models import *
import json
# Create your views here.

# <----------------------------------------Shopify Get Data--------------------------->
class IndexView(View):

    def get(self,request,*args, **kwargs):
        context={}

        product_obj=Product.objects.get(id=66)

        product_dict=model_obj_to_dict_converter(product_obj)
      
        product_dict=json.dumps(product_dict,cls=DjangoJSONEncoder)

        shopify_data=get_shopify_data()

        for product_dict in shopify_data.get('products'):

            if not Product.objects.filter(product_id=product_dict.get('id')).exists():
                
                createProduct(product_dict)

        return render(request,'app/index.html',context)

# <----------------------------------------Shopify Create Data--------------------------->
class CreateDataView(View):

    def get(self,request,*args, **kwargs):
        
        context={}

        product_obj=Product.objects.get(id=66)

        product_dict=model_obj_to_dict_converter(product_obj)

        product_json=json.dumps(product_dict,cls=DjangoJSONEncoder)

        shopify_data=create_shopify_data(product_json,False)
        
        createProduct(shopify_data.get('product'))

        return render(request,'app/create_data.html',context)
    
# <----------------------------------------Shopify Update Data--------------------------->

class UpdateDataView(View):

    def get(self,request,*args, **kwargs):
        context={}

        product_obj=Product.objects.get(id=66)

        product_dict=model_obj_to_dict_converter(product_obj,update=True)

        product_json=json.dumps(product_dict,cls=DjangoJSONEncoder)

        shopify_data=update_shopify_data(product_obj.product_id, product_json, file=False)

        # updateProduct(shopify_data.get('product'))

        return render(request,'app/update_data.html',context)


# <----------------------------------------Shopify Delete Data--------------------------->

class DeteteDataView(View):

    def get(self,request,*args, **kwargs):
        context={}
        delete_shopify_data('products',7461053628608)
        return HttpResponse("Data deleted")
    




class ProductsTableView(View):

    def get(self,request,*args, **kwargs):
        context={}
        return render(request,'app/product_table.html',context)
    

class ProductDetailsTableView(View):

    def get(self,request,*args, **kwargs):
        context={'id':request.GET.get('id')}
        # print(request.GET.get('id'))
        return render(request,'app/product_details.html',context)
  
    




