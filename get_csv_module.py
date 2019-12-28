import csv
from pprint import pprint

cname = 'c97'

def get():
    csv_file=open("../"+cname+"_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[2]!=""):
            clist.append(str(row[2]))
    #pprint(clist)

    return(clist)

def getdb():
    csv_file=open("../db.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[0]!=""):
            clist.append(row)

    return(clist)

def getapp():
    csv_file=open("../"+cname+"_append.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[0]!=""):
            clist.append(row)

    return(clist)

def get_name_match(list):
    csv_file=open("../"+cname+"_pre.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[0] in list):
            clist.append([str(row[0]),str(row[1])])
    #pprint(clist)

    return(clist)


def getname():
    csv_file=open("../"+cname+"_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[1]!=""):
            clist.append(str(row[1]))
    #pprint(clist)

    return(clist)

def getday():
    csv_file=open("../"+cname+"_check.csv","r",encoding="ms932",errors="",newline="")
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
    csv_file=open("../"+cname+"_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    plist=[]

    for row in f:
        if(row[3]!=""):
            plist.append(str(row[3]))

    return(plist)

def getoverA():
    csv_file=open("../"+cname+"_pre.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    plist=[]

    for row in f:
        if(row[2]!="" and (row[4]=='A' or row[4]=='S')):
            plist.append(str(row[2]))

    return(plist)

def getB():
    csv_file=open("../"+cname+"_pre.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    plist=[]

    for row in f:
        if(row[2]!="" and row[4]=='B'):
            plist.append(str(row[2]))

    return(plist)

def getUn():
    csv_file=open("../"+cname+"_pre.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    plist=[]

    for row in f:
        if(row[2]!="" and row[4]==''):
            plist.append(str(row[2]))

    return(plist)

def getC():
    csv_file=open("../"+cname+"_pre.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    plist=[]

    for row in f:
        if(row[2]!="" and row[4]=='C'):
            plist.append(str(row[2]))

    return(plist)

def getcpre():
    csv_file=open("../"+cname+"pre_p1.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)


    plist=[[]]

    for row in f:
        if(row[0]!=""):
            text=''
            for r in range(len(row)-1):
                text+=str(row[r+1])
            plist.append([row[0],text])
    del plist[0]
    return(plist)

def getcc():
    csv_file=open("../"+cname+"_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    plist=[[]]

    for row in f:
        if(row[0]!=""):
            plist.append(row)
    del plist[0]
    return(plist)

def get_c_set():
    csv_file=open("../"+cname+"_check.csv","r",encoding="ms932",errors="",newline="")
    f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

    header=next(f)

    clist=[]

    for row in f:
        if(row[2]!=""):
            clist.append(list(map(str,row[:4])))
    #pprint(clist)

    return(clist)
