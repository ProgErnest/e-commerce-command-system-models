from django.urls import path
from .views import *
urlpatterns =[
    path('products/', ProductListView.as_view(),name="products_list"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('products/create/', ProductCreateView.as_view(), name="product_create"),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name="product_update"),
]