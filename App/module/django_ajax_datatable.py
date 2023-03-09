from ajax_datatable.views import AjaxDatatableView
from App.models import *


class ProductsAjaxDatatableView(AjaxDatatableView):
    
    model = Product
    title = 'Product'
    initial_order = [["app_label", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'title', 'visible': True, },
        {'name': 'vendor', 'visible': True, },
        {'name': 'product_type', 'visible': True, },
        {'name': 'template_suffix', 'visible': True, },
        {'name': 'status', 'visible': True, }
        
    ]
