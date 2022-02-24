## Import the packages
import numpy as np
import csv
import pandas as pd

#Data
xls = pd.ExcelFile("S1-Appendix.xls")
p = pd.read_excel(xls, "protein-data")
r = pd.read_excel(xls, "RNA-data")
c = pd.read_excel(xls, "Chromosome-info")
print(p.head())
print(r.head())
print(c.head())

#Counting
NFATs_p = p["NFATs"].value_counts()
print(NFATs_p)

NFATs_r = r["NFATs"].value_counts()
print(NFATs_r)

NFATs_c = c["NFATs"].value_counts()
print(NFATs_c)

#Total samples in the dataset per NFATc family
data = p.groupby(["taxa", "NFATs"])["organisms"].count()
data_sample = p.groupby("common name") ["organisms"].count()
print(data.head())
print(data_sample.head())

#drop the duplicate names
sp_unique_p = p.drop_duplicates(["organisms", "taxa"])

#Total number of species per NFATc family
sp_p = sp_unique_p.groupby("taxa") ["organisms"].count()
print(sp_p)

#Unique species across NFATs
p_unique = p.drop_duplicates(["organisms", "NFATs"])
NFATs_unique_p = p_unique["NFATs"].value_counts()
print(NFATs_unique_p)
