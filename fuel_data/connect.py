#!/usr/bin/python

# I wrote this script to properly load data into my database
# Author: Jaren Glover @GloveDotCom
# 

import sys, traceback
import psycopg2  # make sure you have psycopg is installed -- use pip
import csv      #pretty sure this is default in Python

connection_string = ""

FILE = '' #name of the file you want to process  

def main():
    try:
        print "trap or die"
        connect()
    except KeyboardInterrupt:
         print "Shutdown requested ... exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


def connect():
    try:
        conn= psycopg2.connect(connection_string)
        global cur #made global so I can call it in the below process function
        cur = conn.cursor()
        process()
        conn.commit()
        conn.close()
    except:
        print "I can't connect my G"
        traceback.print_exc(file=sys.stdout)

def process():
    try:
        with open(FILE,'rb') as csvfile:
            data = csv.reader(csvfile, delimiter='|', \
                    quoting=csv.QUOTE_MINIMAL)
            for row in data:
                SQL= 'INSERT INTO fuel_vehicle (city08,"co2TailpipeGpm","comb08",cylinders,"drive","feScore","fuelCost08","fuelCostA08","fuelType1","highway08","highwayA08","car_id","make","model","trany", "UCity","UCityA","UHighway","UHighwayA","VClass","year","youSaveSpend") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                #print cur.mogrify(SQL,row)
                cur.execute(SQL,row)

    except Exception:
        traceback.print_exc(file=sys.stdout)
        
        
if __name__ == "__main__":
    main()
