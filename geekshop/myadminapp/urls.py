from django.urls import path, re_path
import myadminapp.views as myadminapp

app_name = 'myadminapp'

urlpatterns = [
    # re_path(r'^$', myadminapp.index, name='index'),
    re_path(r'^$', myadminapp.UsersListView.as_view(), name='index'),

    re_path(r'^shopuser/create/$', myadminapp.shopuser_create, name='shopuser_create'),
    re_path(r'^shopuser/update/(?P<pk>\d+)/$', myadminapp.shopuser_update, name='shopuser_update'),
    re_path(r'^shopuser/delete/(?P<pk>\d+)/$', myadminapp.shopuser_delete, name='shopuser_delete'),

    re_path(r'^productcategories/$', myadminapp.categories, name='categories'),
    # re_path(r'^productcategory/create/$', myadminapp.productcategory_create, name='productcategory_create'),
    re_path(r'^productcategory/create/$', myadminapp.ProductCategoryCreateView.as_view(), name='productcategory_create'),

    # re_path(r'^productcategory/update/(?P<pk>\d+)/$', myadminapp.productcategory_update, name='productcategory_update'),
    re_path(r'^productcategory/update/(?P<pk>\d+)/$', myadminapp.ProductCategoryUpdateView.as_view(), name='productcategory_update'),

    # re_path(r'^productcategory/delete/(?P<pk>\d+)/$', myadminapp.productcategory_delete, name='productcategory_delete'),
    re_path(r'^productcategory/delete/(?P<pk>\d+)/$', myadminapp.ProductCategoryDeleteView.as_view(), name='productcategory_delete'),

    re_path(r'^products/(?P<pk>\d+)/$', myadminapp.products, name='products'),
    re_path(r'^product/create/(?P<pk>\d+)/$', myadminapp.product_create, name='product_create'),

    # re_path(r'^product/read/(?P<pk>\d+)/$', myadminapp.product_read, name='product_read'),
    re_path(r'^product/read/(?P<pk>\d+)/$', myadminapp.ProductDetailView.as_view(), name='product_read'),

    re_path(r'^product/update/(?P<pk>\d+)/$', myadminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', myadminapp.product_delete, name='product_delete'),
]
