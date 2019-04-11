from django.urls import path, re_path
import myadminapp.views as myadminapp

app_name = 'myadminapp'

urlpatterns = [
    re_path(r'^$', myadminapp.index, name='index'),
    re_path(r'^shopuser/create/$', myadminapp.shopuser_create, name='shopuser_create'),
    re_path(r'^shopuser/update/(?P<pk>\d+)/$', myadminapp.shopuser_update, name='shopuser_update'),
    re_path(r'^shopuser/delete/(?P<pk>\d+)/$', myadminapp.shopuser_delete, name='shopuser_delete'),

    re_path(r'^productcategories/$', myadminapp.categories, name='categories'),
    re_path(r'^productcategory/update/(?P<pk>\d+)/$', myadminapp.productcategory_update, name='productcategory_update'),

    re_path(r'^products/(?P<pk>\d+)/$', myadminapp.products, name='products'),
]
