from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^categories', views.CategoryView.as_view(), name='CategoryView'),
    url(r'^subcategories', views.SubCategoryView.as_view(), name='SubCategoryView'),
    url(r'^products', views.ProductView.as_view(), name='ProductView'),
]