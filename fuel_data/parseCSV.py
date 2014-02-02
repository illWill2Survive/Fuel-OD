#!/usr/bin/python

import csv
#import sqlite3 as lite
import sys
from fuel.models import Vehicle

IO = open("vehicles_updated_NoHeader.csv")
CSVIO = csv.reader(IO)
#firstLine = CSVIO.next()

#print firstLine

#sql = """CREATE TABLE Data2("""+",".join([("%s int " % t1) for t1 in firstLine])+")";

#create db

#con = lite.connect('pythonDB')

#dblink = con.cursor()

#dblink.execute(sql)

for row in CSVIO:
	#sql= """INSERT INTO Data Values("""+",".join([('"%s"') % str(t2) for t2 in line])+")";
	#print sql;
	#dblink.execute(sql)
    #P = Source(",".join([("%s") % t2 for t2 in line]))
    #P = Source(city08=19,co2TailpipeGpm=423.1904761905,comb08=21,cylinders=4,drive="Rear_Wheel_Drive",feScore=-1,fuelCost08=2500,fuelCostA08=0,fuelType1="Regular_Gasoline",highway08=25,highwayA08=0,car_id=2,make="Alfa_Romeo",model="Spider_Veloce_2000",trany="Manual_5-spd",UCity=23.3333,UCityA=0,UHighway=35,UHighwayA=0,VClass="Two_Seaters",year=1985,youSaveSpend=-1000)
    #P.save()
    if row[3] == ''or row[3] == 'NA':
       row[3] = None
    print row
    P = Vehicle(city08=row[0],co2TailpipeGpm=row[1],comb08=row[2],cylinders=row[3],drive=row[4],feScore=row[5],fuelCost08=row[6],fuelCostA08=row[7],fuelType1=row[8],highway08=row[9],highwayA08=row[10],car_id=row[11],make=row[12],model=row[13],trany=row[14],UCity=row[15],UCityA=row[16],UHighway=row[17],UHighwayA=row[18],VClass=row[19],year=row[20],youSaveSpend=row[21])
    P.save()
    #sys.exit()

IO.close()
#con.commit()
sys.exit()
#for row in CSVIO:
