from tastypie.resources import ModelResource
#from tastypie.constants import ALL
from fuel.models import Vehicle

class CarDataResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.all()
        resource_name = 'cardata'
        allowed_methods = ['get']


class ModelResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.vaules("model").distinct()
        resource_name = 'model'
        allowed_methods = ['get']
