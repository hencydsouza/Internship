import pandas as pd
import numpy as np
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import seaborn as sns
data = pd.read_excel(r'C:\Users\hency\OneDrive\Desktop\Internship\day 7\multi_linear_Data.xlsx')
df1 = pd.DataFrame(data)
print(df1)
df2 = df1.drop(["Unnamed: 0"],axis = 1)
df2.isnull()
df3 = df2.dropna()
print(df3)
print(df3.duplicated())
df3 = df3.drop_duplicates()
print(df3)
df4=df3.duplicated(subset=['Marks obtained'])
df4 = df3.drop_duplicates(subset=['Marks obtained'],keep='last')
print(df4)
df4.reset_index(inplace=True,drop=True)
print(df4)
plt.scatter(df4['Number of student'],df4['Marks obtained'],color='red')
plt.scatter(df4['Number of subject'],df4['Marks obtained'],color='g')
plt.show()
regr = linear_model.LinearRegression()
x=df4[['Number of student','Number of subject']]
y = np.asanyarray(df4['Marks obtained'])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=0)
print("X_train:",X_train.shape)
print("X_test:",X_test.shape)
print("Y_train:",y_train.shape)
print("Y_test:",y_test.shape)
Y=regr.fit(X_train,y_train)
print(X_test)
y_pred = regr.predict(X_test)
print(y_pred)
print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
b = regr.predict([[15,9]])
print("Marks scored: {}".format(b))
plt.scatter(y_test,y_pred,color='g')
plt.xlabel('Actual')
plt.ylabel('Predicted')
Accuracy=r2_score(y_test,y_pred)*100
print(" Accuracy of the model is %.2f" %Accuracy)
sns.regplot(x=y_test,y=y_pred,ci=None,color ='red')
plt.show()