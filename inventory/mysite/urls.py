from django.conf.urls import url
from mysite import views

urlpatterns = [
    url(r'^$',views.AboutView.as_view(),name='about'),
    url(r'^inventory/$',views.add_Inventory,name='add_Inventory'),
    url(r'^product/$',views.InventoryListView.as_view(),name='list'),
    url(r'^product/(?P<pk>\d+)$',views.InventoryListDetail.as_view(),name='inventory_detail'),
    url(r'^product/(?P<pk>\d+)/edit/$',views.UpdateInventoryView.as_view(),name='product_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.remove_inventory, name='product_remove'),
    # url(r'^inventory/(?P<productId>[0-9]+)/$', views.detail, name='detail'),
    ]
