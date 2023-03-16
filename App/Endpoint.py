from django.urls import path,re_path
from .views import *



urlpatterns=[

    path('product',CreateProductEndpoint.as_view(),name="product_get_post"),
    path('product/<str:product_id>',CreateProductEndpoint.as_view(),name="product_put_detete"),
    path('product/<str:start>/<str:end>',CreateProductEndpoint.as_view(),name="product_pagination"),
    # re_path(r'^product/(?P<product_id>\w+)/$',CreateProductEndpoint.as_view(),name="product_put_detete"),

]
