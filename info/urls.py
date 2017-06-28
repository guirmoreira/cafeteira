from django.conf.urls import url
from info import views

urlpatterns = [url(r'^info$', views.info, name='info')]
