from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import CarDataResource, MakeResource, YearResource,HighwayMPGResource , CityMPGResource, YouSaveSpendMPGResource
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')  

#register the resources to v1 for the web services 
v1_api.register(CarDataResource())
v1_api.register(MakeResource())
v1_api.register(YearResource())
v1_api.register(HighwayMPGResource())
v1_api.register(CityMPGResource())
v1_api.register(YouSaveSpendMPGResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
