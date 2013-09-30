from django.db import models

# Create your models here.
'''
class CarData(models.Model):
	car_id = 		models.IntegerField(unique=True, primary_key=True)
	model = 		models.CharField(max_length=100 ,db_index=True)
	make =			models.CharField(max_length=100)
	youSaveSpend =	models.IntegerField()
	comb08=			models.IntegerField()
	fuelType= 		models.CharField(max_length=100)
	fuelCost=		models.IntegerField()

	def __unicode__(self):
	    return self.model


class Data(models.Model):
    city08  =           models.IntegerField()
    co2TailpipeGpm =	models.IntegerField()
    comb08 =	        models.IntegerField()
    cylinders=	        models.IntegerField()
    drive= 		        models.CharField(max_length=50)
    feScore=	        models.IntegerField()
    fuelCost08=	        models.IntegerField()
    fuelCostA08=	    models.IntegerField()
    fuelType1= 		    models.CharField(max_length=50)
    highway08=	        models.IntegerField()
    highwayA08=	        models.IntegerField()
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True)
    model= 		        models.CharField(max_length=50 ,db_index=True)
    trany=              models.CharField(max_length=100)
    UCity=	            models.IntegerField()
    UCityA=	            models.IntegerField()
    UHighway=	        models.IntegerField()
    UHighwayA=	        models.IntegerField()
    VClass= 		    models.CharField(max_length=100)
    year=	            models.IntegerField(db_index=True)
    youSaveSpend=	    models.IntegerField()


class Source(models.Model):
    city08  =           models.FloatField()
    co2TailpipeGpm =	models.FloatField()
    comb08 =	        models.FloatField()
    cylinders=	        models.FloatField()
    drive= 		        models.CharField(max_length=50)
    feScore=	        models.FloatField()
    fuelCost08=	        models.FloatField()
    fuelCostA08=	    models.FloatField()
    fuelType1= 		    models.CharField(max_length=50)
    highway08=	        models.FloatField()
    highwayA08=	        models.FloatField()
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True)
    model= 		        models.CharField(max_length=50 ,db_index=True)
    trany=              models.CharField(max_length=100)
    UCity=	            models.FloatField()
    UCityA=	            models.FloatField()
    UHighway=	        models.FloatField()
    UHighwayA=	        models.FloatField()
    VClass= 		    models.CharField(max_length=100)
    year=	            models.IntegerField(db_index=True)
    youSaveSpend=	    models.FloatField()

    def __unicode__(self):
	    return self.model

class CarSource(models.Model):
    city08  =           models.FloatField()
    co2TailpipeGpm =	models.FloatField()
    comb08 =	        models.FloatField()
    cylinders=	        models.FloatField(blank=True)
    drive= 		        models.CharField(blank=True, max_length=50)
    feScore=	        models.FloatField()
    fuelCost08=	        models.FloatField()
    fuelCostA08=	    models.FloatField()
    fuelType1= 		    models.CharField(max_length=50)
    highway08=	        models.FloatField()
    highwayA08=	        models.FloatField()
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True)
    model= 		        models.CharField(max_length=50 ,db_index=True)
    trany=              models.CharField(blank=True, max_length=100)
    UCity=	            models.FloatField()
    UCityA=	            models.FloatField()
    UHighway=	        models.FloatField()
    UHighwayA=	        models.FloatField()
    VClass= 		    models.CharField(max_length=100)
    year=	            models.IntegerField(db_index=True)
    youSaveSpend=	    models.FloatField()

    def __unicode__(self):
	    return self.model

class CarDetails(models.Model):
    city08  =           models.FloatField()
    co2TailpipeGpm =	models.FloatField()
    comb08 =	        models.FloatField()
    cylinders=	        models.FloatField(null=True,blank=True)
    drive= 		        models.CharField(null=True,blank=True, max_length=50)
    feScore=	        models.FloatField()
    fuelCost08=	        models.FloatField()
    fuelCostA08=	    models.FloatField()
    fuelType1= 		    models.CharField(max_length=50)
    highway08=	        models.FloatField()
    highwayA08=	        models.FloatField()
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True)
    model= 		        models.CharField(max_length=50 ,db_index=True)
    trany=              models.CharField(null=True,blank=True, max_length=100)
    UCity=	            models.FloatField()
    UCityA=	            models.FloatField()
    UHighway=	        models.FloatField()
    UHighwayA=	        models.FloatField()
    VClass= 		    models.CharField(null=True,max_length=100)
    year=	            models.IntegerField(db_index=True)
    youSaveSpend=	    models.FloatField()

    def __unicode__(self):
	    return self.model,self.make,self.car_id

class Vehicle(models.Model):
    city08  =           models.FloatField()
    co2TailpipeGpm =	models.FloatField()
    comb08 =	        models.FloatField()
    cylinders=	        models.FloatField(null=True,blank=True)
    drive= 		        models.CharField(null=True,blank=True, max_length=50)
    feScore=	        models.FloatField()
    fuelCost08=	        models.FloatField()
    fuelCostA08=	    models.FloatField()
    fuelType1= 		    models.CharField(max_length=50)
    highway08=	        models.FloatField()
    highwayA08=	        models.FloatField()
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True)
    model= 		        models.CharField(max_length=50 ,db_index=True)
    trany=              models.CharField(null=True,blank=True, max_length=100)
    UCity=	            models.FloatField()
    UCityA=	            models.FloatField()
    UHighway=	        models.FloatField()
    UHighwayA=	        models.FloatField()
    VClass= 		    models.CharField(null=True,max_length=100)
    year=	            models.IntegerField(db_index=True)
    youSaveSpend=	    models.FloatField()

    def __unicode__(self):
	    return self.model
*/


'''
class Vehicle(models.Model):
    city08  =           models.FloatField()
    co2TailpipeGpm =	models.FloatField()
    comb08 =	        models.FloatField()
    cylinders=	        models.IntegerField(null=True,blank=True)
    drive= 		        models.CharField(blank=True, max_length=50)
    feScore=	        models.FloatField()
    fuelCost08=	        models.FloatField()
    fuelCostA08=	    models.FloatField()
    fuelType1= 		    models.CharField(max_length=50)
    highway08=	        models.FloatField()
    highwayA08=	        models.FloatField()
    car_id=	            models.IntegerField(unique=True)
    make= 		        models.CharField(max_length=50, db_index=True)
    model= 		        models.CharField(max_length=50 ,db_index=True)
    trany=              models.CharField(blank=True, max_length=100)
    UCity=	            models.FloatField()
    UCityA=	            models.FloatField()
    UHighway=	        models.FloatField()
    UHighwayA=	        models.FloatField()
    VClass= 		    models.CharField(max_length=100)
    year=	            models.IntegerField(db_index=True)
    youSaveSpend=	    models.FloatField()

    def __unicode__(self):
	    return self.model
