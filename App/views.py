from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .module.insert_data_in_db import insert_data
from .module.model_to_dict import *
from .module.DatabaseServises import *
from django.core.serializers.json import DjangoJSONEncoder
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission
from .module.shopify import *
from .models import *
import json
from App.services.ShopifyServices import *
from App.services.RestServices import *
from App.services.GenralServices import *
from App.Response import endpointResponse
from App.Theads import createCronJob,CreateTheads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

# <----------------------------------------Shopify Get Data--------------------------->

class IndexView(View):

    def get(self,request,*args, **kwargs):
        context={}

        product_obj=Product.objects.get(id=66)

        shop=Shop.objects.get(id=1)

        product_dict=model_obj_to_dict_converter(product_obj)
      
        product_dict=json.dumps(product_dict,cls=DjangoJSONEncoder)

        shopify_data=get_shopify_data(shop)

        for product_dict in shopify_data.get('products'):

            if not Product.objects.filter(product_id=product_dict.get('id')).exists():
                
                createProduct(product_dict)

        return render(request,'app/index.html',context)

# <----------------------------------------Shopify Create Data--------------------------->
class CreateDataView(View):

    def get(self,request,*args, **kwargs):

        context={}



        with open('update_json_create_db.json', 'r') as f:
            data = json.load(f)
        # print(data.get('product'))
        updated=updateProductOnCreateTable(data.get('product'))
        print(updated)


        # with open('post_data.json', 'r') as f:
        #     data = json.load(f)
        # # print(data.get('product'))
        # created=createProductOnCreateTable(data.get('product'))
        # print(created)
        # t=CreateTheads(target_fun=createCronJob)
        # t.daemon=True
        # t.start()
        # createCronJob()
        # updateCronJob()

        # product_object=CreateProduct.objects.get(id=9)
        # shop=Shop.objects.get(id=1)
        # url,headers=api_and_header(shop)
      
        # print(url)
        # print(headers)



        # created=creating_shopify_product_by_create_dbtable(shop,product_object)

        # if created:
        #     print('views ok')
        # else:
        #     print('not  ok')



        # product_dict=model_obj_to_dict_converter_for_create_table(product_object)

        # product_json=json.dumps(product_dict,cls=DjangoJSONEncoder)

        # shopify_data=create_shopify_data(product_json,False)
        # print(shopify_data)
        # # my_json = json.loads(product_json)
        # # print(my_json)
        # created=createProduct(shopify_data.get('product'))
        # if created:
        #     product_obj.shopify_created_status=True
        # # createProductOnCreateTable(my_json.get('product'))

        return render(request,'app/create_data.html',context)
    
# <----------------------------------------Shopify Update Data--------------------------->

class UpdateDataView(View):

    def get(self,request,*args, **kwargs):
        context={}

        # def create(word):
        #     for i in range(5):
        #         print(word)

        # def update(word):
        #     for i in range(5):
        #         print(word)





        # product_object=Product.objects.get(id=66)

        # shop=Shop.objects.get(id=1)

        # updated=updating_shopify_product_by_dbtable(product_object )

        # if updated:

        #     print('updated')

        # else:

        #     print('not updated')
        



        # url,headers=api_and_header(shop , product_object.product_id , update_url=True)
        # print(url)
        # print(headers)

        # product_dict=model_obj_to_dict_converter(product_obj,update=True)

        # product_json=json.dumps(product_dict,cls=DjangoJSONEncoder)

        # shopify_data=update_shopify_data(product_obj.product_id, product_json, file=False)

        # # updateProduct(shopify_data.get('product'))

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
  
    

# <--------------------------------Creating views class for Endpoint------------------->

@method_decorator(csrf_exempt, name='dispatch')
class CreateProductEndpoint(View):

    def get(self,request,*args, **kwargs):

        product_id,start,end=kwargs.get('product_id',None),kwargs.get('start',None),kwargs.get('end',None)
        
        products={"products":[]}

        if len(kwargs)>0:

            if start and end :
                
                for product_object in CreateProduct.objects.all()[int(start):int(end)]:

                    products['products'].append(model_obj_to_dict_converter_for_create_table(product_object))

                return endpointResponse(status_code=200,massage="OK",data=products)

            if product_id:

                if CreateProduct.objects.filter(id=product_id).exists():

                    product_json=model_obj_to_dict_converter_for_create_table(CreateProduct.objects.get(id=product_id))

                    return endpointResponse(status_code=200,massage="OK",data=product_json)
                
                return endpointResponse(status_code=400,massage="Product_id Does Not exist",data=[])
           
        else:

            for product_object in CreateProduct.objects.all():

                products['products'].append(model_obj_to_dict_converter_for_create_table(product_object))

                return endpointResponse(status_code=200,massage="OK",data=products)

    
    def post(self,request,*args, **kwargs):
        response={}

        data=json.loads(request.body)

        product=data.get('product')

        json_respose=json.loads(json.dumps(data,indent = 4))

        created=createProductOnCreateTable(product)

        # created=True
        if created:

            response['status_code']=201

            response['massage']="Created"

            response['data']=json_respose

            return JsonResponse(response)

        response['status_code']=400

        response['massage']="Bad Request"

        response['data']=[]

        return JsonResponse(response)

        
    
    def put(self,request,*args, **kwargs):

        data=json.loads(request.body)

        product=data.get('product')

        json_respose=json.loads(json.dumps(data,indent = 4))

        updated=updateProductOnCreateTable(product)

        if updated:
            
            return endpointResponse(status_code=200,massage="Updated",data=json_respose)
        
        return endpointResponse(status_code=400,massage="Not Updated ",data=[])
        
    
    def delete(self,request,*args, **kwargs):

        product_id=kwargs.get('product_id',None)

        if product_id is not None:

            if CreateProduct.objects.filter(id=product_id).exists():

                delete_count=product_object=CreateProduct.objects.get(id=product_id)

                if delete_count:

                    return endpointResponse(status_code=200,massage="Product Deleted",data=[])
                
                return endpointResponse(status_code=400,massage="Product Not  Deleted",data=[])

            return endpointResponse(status_code=400,massage="Product_id Does not Exist",data=[])
        
        return endpointResponse(status_code=404,massage="Product_id required on endpoint",data=[])




