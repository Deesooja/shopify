from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .module.insert_data_in_db import insert_data
from .module.model_to_dict import model_obj_to_dict_converter
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
        print(product_dict)

        shopify_data=get_shopify_data()
        # print(shopify_data)
        for product_dict in shopify_data.get('products'):

            if not Product.objects.filter(product_id=product_dict.get('id')).exists():

                # print('product_id',product_dict.get('id'))

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

# <----------------------------------------Shopify Create Data--------------------------->
class CreateDataView(View):

    def get(self,request,*args, **kwargs):
        context={}
        product_obj=Product.objects.get(id=66)

        product_dict=model_obj_to_dict_converter(product_obj)

        product_dict=json.dumps(product_dict,cls=DjangoJSONEncoder)

        print(product_dict)

        shopify_data=create_shopify_data(product_dict,False)

        print(shopify_data)

        # for product_dict in shopify_data.get('products'):

        #     if not Product.objects.filter(product_id=product_dict.get('id')).exists():

        product_dict=shopify_data.get('product')

        # print('product_id',product_dict.get('id'))

        product_obj=insert_data(Product,product_dict,None,None,'product_id')

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

        return render(request,'app/create_data.html',context)
    
# <----------------------------------------Shopify Update Data--------------------------->
class UpdateDataView(View):

    def get(self,request,*args, **kwargs):
        context={}
        shopify_data=update_shopify_data()

        product_dict=shopify_data.get('product')

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
  
    




