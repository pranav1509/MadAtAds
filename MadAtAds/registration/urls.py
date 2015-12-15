'''
Created on Dec 14, 2015

@author: Pranav
'''


from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))