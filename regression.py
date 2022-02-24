#!/usr/bin/python

#Import the packages
import numpy as np
import pandas as pd
import sklearn.linear_model as lm

#Data
data = pd.read_csv("data.csv")

#Data duplication and chromosome ratio
x = data[["duplication"]]
y = data[["chromosome"]]

#Data duplication ratio and evolutionary time
x = data[["evol"]]
y = data[["duplication"]]

#Data chromosome ratio and fixation ratio (w)
x = data[["w"]]
y = data[["chromosome"]]

#linear regression
model = lm.LinearRegression()
model.fit(x, y)

#Coefficient of determination
r = model.score(x,y)
print(r)

#Intercet
print(model.intercept_)

#slope
print(model.coef_)

