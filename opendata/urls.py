from django.conf.urls import patterns, include, url
from api import CarDataResource
from api import ModelResource
from django.contrib import admin

admin.autodiscover()

#v1_api = Api(api_name='v1')
#v1_api.register(CarDataResource())

cardata_resource= CarDataResource()
model_resource= ModelResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opendata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(cardata_resource.urls)),
    url(r'^api/model', include(model_resource.urls)),

)
