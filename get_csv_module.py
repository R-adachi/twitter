import csv
from pprint import pprint

csv_file=open("../key/key.csv","r",encoding="ms932",errors="",newline="")
f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)
