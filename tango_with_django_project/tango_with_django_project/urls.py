from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/$', include('rango.urls')),
    url(r'^about/', include('rango.urls')),
)
