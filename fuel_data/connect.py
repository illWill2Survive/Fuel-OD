#!/usr/bin/python

import sys, traceback
import psycopg2  # make sure you have psycopg is installed -- use pip
import csv      #pretty sure this is default in Python

connection_string ="dbname='fuel' user='illwill' host='localhost' port='5432' \
                    password='1D@t@$0ur30fGr3@tn3$$4'"
def main():
    try:
        print "trap or die"
        connect()
        process()
    except KeyboardInterrupt:
         print "Shutdown requested ... exiting"

    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


def connect():
    try:
        conn= psycopg2.connect(connection_string)
        global cur
        cur = conn.cursor()
    except:
        print "I can't connect my G"
        traceback.print_exc(file=sys.stdout)

def process():
    try:
        #IO = open("vehicles_updated_NoHeader.csv")
        #with open('vehicles_updated_NoHeader.csv','rb') as csvfile:
        with open('fuel.csv','rb') as csvfile:
            data = csv.reader(csvfile, delimiter='|', quotechar ='|', \
                    quoting=csv.QUOTE_MINIMAL)
            for row in data:
                SQL= 'INSERT INTO fuel_vehicle ("city08","co2TailpipeGpm","comb08","cylinders","drive","feScore","fuelCost08", "fuelCostA08", "fuelType1","highway08", "highwayA08","car_id", "make", "model","trany", "UCity", "UCityA", "UHighway", "UHighwayA", "VClass", "year","youSaveSpend") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                #print cur.fetchall()
                #print type(tuple(row))
                temp=tuple(row)
                #print type(temp)
                #print temp
                print SQL,row
                print cur.mogrify(SQL,temp,)
                #sys.exit(0)
                print temp
                #print cur.mogrify(SQL,(temp,))
                #cur.execute(SQL,row)
                
            #conn.commit()
            #conn.close()
       
       
       
       
       #CSVIO = csv.reader(IO)
        
        #for row in CSVIO:
         #   if row[3] == ''or row[3] == 'NA':
          #      row[3] = None

    except Exception:
        traceback.print_exc(file=sys.stdout)
        
        
if __name__ == "__main__":
    main()


