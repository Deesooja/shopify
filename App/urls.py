from django.urls import path
from .views import *
from .module.django_ajax_datatable import ProductsAjaxDatatableView


urlpatterns=[
    path('',IndexView.as_view(),name="index_view"),
    path('product-page/',ProductsTableView.as_view(),name="product_page"),
    path('ajax_datatable/product/', ProductsAjaxDatatableView.as_view(), name="ajax_datatable_product"),
]
