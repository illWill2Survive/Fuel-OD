from tastypie.resources import ModelResource
from tastypie.constants import ALL
from fuel.models import Vehicle
from django.core import serializers
from tastypie import fields, utils

class CarDataResource(ModelResource):
    class Meta:
        model = Vehicle
        fields = ('id','make')
        queryset = Vehicle.objects.all()
        resource_name = 'cardata'
        allowed_methods = ['get']
        include_resource_uri = False
        include_absolute_url = False



class MakeResource(ModelResource):
    make = fields.CharField(attribute='make')
   # model=Vehicle
    class Meta:
        queryset =Vehicle.objects.order_by('make').distinct('make')
        resource_name = 'make'
        allowed_methods = ['get']
        #serializer = Serializer()
        # list(queryset)
        fields = ['make']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['make']

class YearResource(ModelResource):
    class Meta:
        queryset =Vehicle.objects.order_by('year').distinct('year')
        resource_name = 'year'
        allowed_methods = ['get']
        fields = ['year']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['year']