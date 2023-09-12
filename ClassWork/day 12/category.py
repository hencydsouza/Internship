import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
df = pd.read_excel("flipkart_categories.xlsx")
#print(df)
df.info()
df.isnull().sum()
from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()
df['Category_1'] = Le.fit_transform(df['Category_1'])
df
df['Category_2'] = Le.fit_transform(df['Category_2'])
df['Category_3'] = Le.fit_transform(df['Category_3'])
x = df.drop(['Category_1'],axis=1)
y= df['Category_1']
#print(x,y)
X_train,X_test,y_train,y_test = train_test_split(x,y,random_state=20,test_size=0.2)

rf =tree.DecisionTreeClassifier(criterion = 'entropy')
dt = rf .fit(X_train, y_train)
print(X_test[1:2])
y_pred = dt.predict(X_test[1:2])
print(y_pred)