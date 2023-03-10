from django.urls import path
from .views import *
from .module.django_ajax_datatable import ProductAjaxDatatableView


urlpatterns=[
    path('',IndexView.as_view(),name="index_view"),
    path('product-page/',ProductsTableView.as_view(),name="product_page"),
    path('ajax_datatable/products/', ProductAjaxDatatableView.as_view(), name="ajax_datatable_products"),
   
]
