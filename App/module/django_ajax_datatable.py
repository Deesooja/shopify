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

#<!------------------------------------- product class ------------------>
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
        
        return
    
#<!------------------------------------- product variants class ------------------>
class VariantsAjaxDatatableView(AjaxDatatableView):

    model = ProductVariant
    title = 'Product-Variant'
    columns = ['id','variant_id', 'title', 'price','position','inventory_policy','grams','weight','weight_unit',]
    order_columns = ['id','variant_id', 'title', 'price','position','inventory_policy','grams','weight','weight_unit',]
    # initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'variant_id', 'visible': True, },
        {'name': 'title', 'visible': True, },
        {'name': 'price', 'visible': True, },
        {'name': 'position', 'visible': True, },
        {'name': 'inventory_policy', 'visible': True, },
        {'name': 'grams', 'visible': True, },
        {'name': 'weight', 'visible': True, },
        {'name': 'weight_unit', 'visible': True, },
    ]

    def get_initial_queryset(self, request=None):

        queryset = self.model.objects.all()

        if 'id' in request.REQUEST:
            id = int(request.REQUEST.get('id'))
            queryset = queryset.filter(product=id)

        return queryset
    
#<!------------------------------------- product options class ------------------> 
class OptionsAjaxDatatableView(AjaxDatatableView):

    model = ProductOption
    title = 'Product-Option'
    columns = ['id','option_id', 'name','position']
    order_columns = ['id','option_id', 'name','position']
    # initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'option_id', 'visible': True, },
        {'name': 'name', 'visible': True, },
        {'name': 'position', 'visible': True, },
        
    ]
    def customize_row(self, row, obj):
    # 'row' is a dictionary representing the current row, and 'obj' is the current object.
        row['pk'] = '<a  href="%s?id=%s">%s</a>' % ('/option-value/', obj.id, obj.id)
        
        return 


    def get_initial_queryset(self, request=None):

        queryset = self.model.objects.all()

        if 'id' in request.REQUEST:
            id = int(request.REQUEST.get('id'))
            queryset = queryset.filter(product=id)

        return queryset
    

#<!------------------------------------- product images class ------------------> 
class ImagesAjaxDatatableView(AjaxDatatableView):

    model = ProductImages
    title = 'Product-Images'
    columns = ['id','image_id', 'position','alt','width', 'height','src']
    order_columns = ['id','image_id', 'position','alt','width', 'height','src']
    # initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'image_id', 'visible': True, },
        {'name': 'position', 'visible': True, },
        {'name': 'alt', 'visible': True, },
        {'name': 'width', 'visible': True, },
        {'name': 'height', 'visible': True, },
        {'name': 'src', 'visible': True, },
        
    ]
    def get_initial_queryset(self, request=None):

        queryset = self.model.objects.all()

        if 'id' in request.REQUEST:
            id = int(request.REQUEST.get('id'))
            queryset = queryset.filter(product=id)

        return queryset
    

#<!------------------------------------- product image class ------------------> 
class ImageAjaxDatatableView(AjaxDatatableView):

    model = ProductImage
    title = 'Product-Image'
    columns = ['id','image_id', 'position','alt','width', 'height','src']
    order_columns = ['id','image_id', 'position','alt','width', 'height','src']
    # initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'image_id', 'visible': True, },
        {'name': 'position', 'visible': True, },
        {'name': 'alt', 'visible': True, },
        {'name': 'width', 'visible': True, },
        {'name': 'height', 'visible': True, },
        {'name': 'src', 'visible': True, },
        
    ]
    def get_initial_queryset(self, request=None):

        queryset = self.model.objects.all()

        if 'id' in request.REQUEST:
            id = int(request.REQUEST.get('id'))
            queryset = queryset.filter(product=id)

        return queryset