from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import  ProductDetailView, ProductListView, VariationListView
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    #url(r'^$', views.post_list1, name='post_list'),
    
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    # url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
    url(r'^add/new/$', views.post_new, name='post_new'),
    url(r'^add/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^add/img/$', views.add_img, name='add_img'),
    #url(r'^add/img(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^add/(?P<pk>[0-9]+)/edit/$', views.add_imgedit, name='post_edit'),
    ################
    url(r'^list/$', views.list, name='list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.post_detail_list, name='post_detail_list'),
    url(r'^list/detail/$', views.list_detail, name='list_detail'),
    url(r'^list/(?P<pk>[0-9]+)/edit/$', views.post_edit_list, name='post_edit_list'),
    #url(r'^list/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    
    
]
