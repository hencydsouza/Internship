import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'C:\Users\hency\OneDrive\Desktop\Internship\day 6\insurance.csv')
df1 = pd.DataFrame(data)

# print(df1)
# df1.info()
# df1.describe()

#linear plotting
# plt.scatter(df1['age'],df1['charges'],color='red')
# plt.show()

regr = linear_model.LinearRegression()
x = np.asanyarray(df1['age'],df1['bmi'])
y = np.asanyarray(df1['charges'])

print(x)
print(y)

X = x.reshape(-1,1)

out = regr.fit(X,y)
plt.plot(x,regr.predict(X),color="g")
# print("Please enter your age")
plt.show()
# d=int(input("Enter the value: "))

# b=regr.predict([[d]])[0]
# print("Your predict insurance charges according to the age: {}".format(b))