from django.urls import path
from .views import *
from .module.django_ajax_datatable import *


urlpatterns=[
    path('',IndexView.as_view(),name="get_data"),
    path('create-data/',CreateDataView.as_view(),name="create_data"),
    path('update-data/',UpdateDataView.as_view(),name="update_data"),
    path('delete-data/',UpdateDataView.as_view(),name="create_data"),
    path('product-page/',ProductsTableView.as_view(),name="product_page"),
    path('product-details/',ProductDetailsTableView.as_view(),name="product_details"),
    path('ajax_datatable/products/', ProductAjaxDatatableView.as_view(), name="ajax_datatable_products"),
    path('ajax_datatable/details/', VariantsAjaxDatatableView.as_view(), name="ajax_datatable_products_details"),
    path('ajax_datatable/options/', OptionsAjaxDatatableView.as_view(), name="ajax_datatable_products_options"),
    path('ajax_datatable/images/', ImagesAjaxDatatableView.as_view(), name="ajax_datatable_products_images"),
    path('ajax_datatable/image/', ImageAjaxDatatableView.as_view(), name="ajax_datatable_products_image"),
   
]
