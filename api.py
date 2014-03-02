from tastypie.resources import ModelResource
from tastypie.constants import ALL
from fuel.models import Vehicle
from django.core import serializers
from tastypie import fields, utils

class HighwayMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "UHighway"]
            queryset = Vehicle.objects.all()
            resource_name= 'highway'
            allowed_methods = ['get']
            include_resource_uri = False
            ordering = ['make']
            filtering ={'year': ALL, "make":ALL, "model": ALL, "UHighway": ALL}
		

class CityMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "UCity"]
            queryset = Vehicle.objects.all()
            resource_name= 'city'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            ordering = ['make']
            filtering ={'year': ALL, "make":ALL, "model": ALL, "UCity" : ALL}

class YouSaveSpendMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "youSaveSpend"]
            queryset = Vehicle.objects.all()
            resource_name= 'you-save-spend'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL, "make":ALL, "model": ALL, "youSaveSpend": ALL}
            ordering = ['model']

class CarDataResource(ModelResource):
    class Meta:
        model = Vehicle
        fields = ('model','make', 'year', 'UHighway','UCity', 'youSaveSpend')
        queryset = Vehicle.objects.all()
        resource_name = 'cardata'
        allowed_methods = ['get']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['make']
        filtering ={'year': ALL, "make":ALL, "model": ALL, "youSaveSpend": ALL}

class MakeResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.all()
        resource_name = 'make'
        allowed_methods = ['get']
        fields = ['make']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['make']
        filtering ={"make":ALL}

class YearResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.all()
        resource_name = 'year'
        allowed_methods = ['get']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['year']
        filtering ={'year': ALL}
