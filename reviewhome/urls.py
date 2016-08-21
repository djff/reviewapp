__author__ = 'djff'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
]