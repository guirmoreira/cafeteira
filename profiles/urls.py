from django.conf.urls import url
from profiles import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^order/(?P<product>[0-9]+)$', views.order, name='order'),
               url(r'^rasp_orders$', views.rasp_orders, name='rasp_orders'),
               url(r'^rasp_remove_order$', views.rasp_remove_order, name='rasp_remove_order'),
               url(r'^manutencao$', views.manutencao, name='manutencao'), ]
