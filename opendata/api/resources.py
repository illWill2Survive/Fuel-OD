'''from tastypie.resources import ModelResource
from fuel.models import Vechicle
from django.core.serializers import json 
from django.utils import simplejson 


class CarDataResource(ModelResource):
    class Meta:
        queryset = Cars.objects.all()
        allowed_methods = ['get']

class ModelResource(ModelResource):
        class Meta:
        #    queryset = Cars.objects
        #   '''
