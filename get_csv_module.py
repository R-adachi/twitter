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

def getday():
    csv_file=open("../c96_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[[]]
    dlist=[]

    for row in f:
        if(row[3]!=""):
            clist.append(str(row[3]).split('-'))
    del clist[0]
    #pprint(clist)
    for i in clist:
        dlist.append(i[0])

    return(dlist)

def getp():
    csv_file=open("../c96_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    plist=[]

    for row in f:
        if(row[3]!=""):
            plist.append(str(row[3]))

    return(plist)
