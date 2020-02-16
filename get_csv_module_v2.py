import csv
from pprint import pprint

def get_pre_grade(c):
    csv_file=open("../"+c+"_grade.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[2]!=""):
            clist.append(row)

    return(clist)
