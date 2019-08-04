import csv
from pprint import pprint

csv_file=open("../c96_check.csv","r",encoding="ms932",errors="",newline="")
f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)


clist=[]

for row in f:
    clist.append(str(row[3]))

return(clist)
