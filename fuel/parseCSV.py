#!/usr/bin/python

import csv
import sys
from fuel.models import Data

IO = open("vehicles_updated_NoHeader.csv")
CSVIO = csv.reader(IO)
#firstLine = CSVIO.next()

#print firstLine

#sql = """CREATE TABLE Data2("""+",".join([("%s int " % t1) for t1 in firstLine])+")";

#create db

#con = lite.connect('pythonDB')

#dblink = con.cursor()

#dblink.execute(sql)

for line in CSVIO:
	#sql= """INSERT INTO Data Values("""+",".join([('"%s"') % str(t2) for t2 in line])+")";
    P ="""Data("""+",".join([('"%s"') % str(t2) for t2 in line])+"0"")"
    P.save()

	#print sql;
	#dblink.execute(sql)

#con.commit()
#sys.exit()
#for row in CSVIO:
IO.close()
sys.exit()