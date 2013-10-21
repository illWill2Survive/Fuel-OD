from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import CarDataResource, MakeResource, YearResource
from rest_framework import viewsets, routers
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CarDataResource())
v1_api.register(MakeResource())
v1_api.register(YearResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),

)
