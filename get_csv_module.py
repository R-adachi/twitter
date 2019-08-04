import csv
from pprint import pprint

def get():
    csv_file=open("../c96_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[2]!=""):
            clist.append(str(row[2]))
    #pprint(clist)

    return(clist)

def getname():
    csv_file=open("../c96_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[1]!=""):
            clist.append(str(row[1]))
    #pprint(clist)

    return(clist)
