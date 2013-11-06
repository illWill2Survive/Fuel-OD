from django.db import models

# Create your models here.

class Vehicle(models.Model):
    city08  =           models.FloatField(null=True,blank=True)
    co2TailpipeGpm =	models.FloatField(null=True,blank=True)
    comb08 =	        models.FloatField(null=True,blank=True)
    cylinders=	        models.IntegerField(null=True,blank=True)
    drive= 		        models.CharField(blank=True, max_length=50)
    feScore=	        models.FloatField(null=True,blank=True)
    fuelCost08=	        models.FloatField(null=True,blank=True)
    fuelCostA08=	    models.FloatField(null=True,blank=True)
    fuelType1= 		    models.CharField(max_length=50, blank=True)
    highway08=	        models.FloatField(null=True,blank=True)
    highwayA08=	        models.FloatField(null=True,blank=True)
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True,blank=True)
    model= 		        models.CharField(max_length=50 ,db_index=True, blank=True)
    trany=              models.CharField(blank=True, max_length=100)
    UCity=	            models.FloatField(null=True,blank=True)
    UCityA=	            models.FloatField(null=True,blank=True)
    UHighway=	        models.FloatField(null=True,blank=True)
    UHighwayA=	        models.FloatField(null=True,blank=True)
    VClass= 		    models.CharField(max_length=100,blank=True)
    year=	            models.IntegerField(db_index=True,blank=True)
    youSaveSpend=	    models.FloatField(null=True,blank=True)

    def __unicode__(self):
	    return self.model


