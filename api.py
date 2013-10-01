from tastypie.resources import ModelResource
#from tastypie.constants import ALL
from fuel.models import Vehicle

class CarDataResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.all()
        resource_name = 'cardata'
        allowed_methods = ['get']


class MakeResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.distinct('make')
        resource_name = 'make'
        allowed_methods = ['get']
