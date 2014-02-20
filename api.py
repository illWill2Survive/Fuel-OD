from tastypie.resources import ModelResource
from tastypie.constants import ALL
from fuel.models import Vehicle
from django.core import serializers
from tastypie import fields, utils

#filter data but problem will change later
dataset= Vehicle.objects.filter(fuelType1 ='Regular_Gasoline').filter(cylinders__lt=7).filter(year__gt=2011).filter(year__lt=2014).exclude(fuelCost08=0).exclude(highway08 =0).exclude(UCity =0).exclude(UHighway=0).exclude(youSaveSpend=0).exclude(fuelCostA08='0')


class HighwayMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "UHighway"]
            queryset = dataset
            resource_name= 'highway'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL}
            ordering = ['make']

class CityMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "UCity"]
            queryset = dataset
            resource_name= 'city'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL}
            ordering = ['make']

class YouSaveSpendMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "youSaveSpend"]
            queryset = dataset
            resource_name= 'you-save-spend'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL}
            ordering = ['model']

class CarDataResource(ModelResource):
    class Meta:
        model = Vehicle
        fields = ('id','make')
        queryset = Vehicle.objects.all()
        resource_name = 'cardata'
        allowed_methods = ['get']
        include_resource_uri = False
        include_absolute_url = False
	ordering = ['make']

class MakeResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.filter(fuelType1
                ='Regular_Gasoline').filter(cylinders__lt=7).filter(year__gt=2011).filter(year__lt=2014).exclude(fuelCost08=0).exclude(highway08
                        =0).exclude(UCity
                                =0).exclude(UHighway=0).exclude(youSaveSpend=0).exclude(fuelCostA08='0').order_by('make')

        resource_name = 'make'
        allowed_methods = ['get']
        fields = ['make']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['make']

class YearResource(ModelResource):
    class Meta:
        queryset = Vehicle.objects.filter(fuelType1
                ='Regular_Gasoline').filter(cylinders__lt=7).filter(year__gt=2011).filter(year__lt=2014).exclude(fuelCost08=0).exclude(highway08
                        =0).exclude(UCity
                                =0).exclude(UHighway=0).exclude(youSaveSpend=0).exclude(fuelCostA08='0').order_by('year')
        resource_name = 'year'
        allowed_methods = ['get']
        fields = ['year']
        include_resource_uri = False
        include_absolute_url = False
        ordering = ['year']

