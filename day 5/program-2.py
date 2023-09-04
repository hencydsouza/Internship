import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from  sklearn import linear_model

df = pd.read_csv(r'C:/Users/hency/OneDrive/Desktop/Internship/day 5/insurance.csv')

y = np.asanyarray(df['age'])
x = np.asanyarray(df['charges'])
regr = linear_model.LinearRegression()
regr.fit(x.reshape(-1,1),y)
reshape_value = x.reshape(-1,1)
print(reshape_value)

# print("ENter ur age")
# d = int(input("ENter the value"))

# b  = regr.predict([[d]])[0]
# print("Your predicted insurance charges according to age: {}".format(b))