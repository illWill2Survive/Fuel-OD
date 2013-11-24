from tastypie.resources import ModelResource
from tastypie.constants import ALL
from fuel.models import Vehicle
from django.core import serializers
from tastypie import fields, utils
#import simplejson as json

dataset= Vehicle.objects.filter(fuelType1 ='Regular_Gasoline').filter(cylinders__lt=7).filter(year__gt=2011).filter(year__lt=2014).exclude(fuelCost08=0).exclude(highway08 =0).exclude(UCity =0).exclude(UHighway=0).exclude(youSaveSpend=0).exclude(fuelCostA08='0')


class HighwayMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "UHighway"]
            queryset = dataset
            resource_name= 'HighwayMPG'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL}

class CityMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "UHighway"]
            queryset = dataset
            resource_name= 'City'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL}

class YouSaveSpendMPGResource(ModelResource):
        class Meta:
            fields =["make", "model", "year", "youSaveSpend"]
            queryset = dataset
            resource_name= 'YouSaveSpend'
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering ={'year': ALL}

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

# this below code is me trying to dynamics give the columns names via the URL...having some trouble will come back in later :(
'''
class ColumnsResource(ModelResource):
    def apply_filters(self, request, applicable_filters):
        """
        An ORM-specific implementation of ``apply_filters``.

        The default simply applies the ``applicable_filters`` as ``**kwargs``,
        but should make it possible to do more advanced things.

        Here we override to check for a 'distinct' query string variable,
        if it's equal to True we apply distinct() to the queryset after filtering.
        """
        columns_list = request.GET.get('cname')        #, False) == 'True'
        print columns_list.decode('utf-8')
        print columns_list.decode('utf-8').split(',')
        temp = columns_list.decode('utf-8').split(',')
        #temp1= tuple(temp)
        print "----"
        print temp
        #print mike[0]
        #print mike[1]
        #arlos ="'year','make','model'"
        glover = []
        print columns_list
        for i in self.get_object_list(request).values(*temp):
            glover.append(i)


        #print columns_list
        print glover
        #print "jaren"

        distinct = request.GET.get('list', False) == 'True'
        #print applicable_filters
        if distinct:
            #jaren = self.get_object_list(request).values('make','year','pk')
            #carlos =  serializers.serialize('json', jaren)
            #print "glover"
            #return json.dumps(glover)
           return self.get_object_list(request).values(*temp)
           # return self.get_object_list(glover) #values(*temp)  #self.get_object_list(glover).filter(**applicable_filters) #.values("make") #filter(**applicable_filters) #.values('make','year','pk')  #self.get_object_list(request).values('make')
            #return jaern
        else:
            return self.get_object_list(request).filter(**applicable_filters)
    class Meta:
            resource_name="cname"
            queryset = dataset
           # fields = ["year",'make','id']
            allowed_methods = ['get']
            include_resource_uri = False
            include_absolute_url = False
            filtering = {'year': ALL}

'''
