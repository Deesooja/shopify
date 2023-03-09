from django.shortcuts import render
from django.views import View
from .module.insert_data_in_db import insert_data
from ajax_datatable.views import AjaxDatatableView
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
    

class ProductsAjaxDatatableView(AjaxDatatableView):
    print('ok')
    model = Product
    title = 'Product'
    columns = ['pk','product_id', 'title', 'body_html','vendor','product_type','created_at','handle','updated_at','published_at','template_suffix','status','published_scope',]
    order_columns = ['id','product_id', 'title', 'body_html','vendor','product_type','created_at','handle','updated_at','published_at','template_suffix','status','published_scope',]
    initial_order = [["pk", "asc"],["title", "asc"],["body_html", "asc"],["vendor", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'pk', 'visible': True, },
        {'name': 'product_id', 'visible': True, },
        {'name': 'title', 'visible': True, },
        {'name': 'body_html', 'visible': True, },
        {'name': 'vendor', 'visible': True, },
        {'name': 'product_type', 'visible': True, },
        {'name': 'created_at', 'visible': True, },
        {'name': 'created_at', 'visible': True, },
        {'name': 'template_suffix', 'visible': True, },
        {'name': 'status', 'visible': True, },
       
    ]
