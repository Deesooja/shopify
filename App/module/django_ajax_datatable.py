from ajax_datatable.views import AjaxDatatableView
from App.models import *
from django.contrib.auth.models import Permission


# class ProductsAjaxDatatableView(AjaxDatatableView):
    
#     model = Product
#     title = 'Product'
#     initial_order = [["app_label", "asc"], ]
#     length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
#     search_values_separator = '+'

#     column_defs = [
#         AjaxDatatableView.render_row_tools_column_def(),
#         {'name': 'id', 'visible': True, },
#         {'name': 'title', 'visible': True, },
#         {'name': 'vendor', 'visible': True, },
#         {'name': 'product_type', 'visible': True, },
#         {'name': 'template_suffix', 'visible': True, },
#         {'name': 'status', 'visible': True, }
        
#     ]
class ProductAjaxDatatableView(AjaxDatatableView):

    model = Product
    title = 'Product'
    columns = ['id','product_id', 'title', 'body_html','vendor','product_type','created_at','handle','updated_at','published_at','template_suffix','status','published_scope',]
    order_columns = ['id','product_id', 'title', 'body_html','vendor','product_type','created_at','handle','updated_at','published_at','template_suffix','status','published_scope',]
    # initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'product_id', 'visible': True, },
        {'name': 'title', 'visible': True, },
        {'name': 'vendor', 'visible': True, },
        {'name': 'product_type', 'visible': True, },
        {'name': 'handle', 'visible': True, },
        {'name': 'status', 'visible': True, },
    ]

    def customize_row(self, row, obj):
    # 'row' is a dictionary representing the current row, and 'obj' is the current object.
        row['pk'] = '<a  href="%s?id=%s">%s</a>' % ('/product-details/', obj.id, obj.id)
        # row['id'] =1
        return