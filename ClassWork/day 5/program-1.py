import pandas as pd

df = pd.read_csv(r'C:/Users/hency/OneDrive/Desktop/Internship/day 5/insurance.csv')
# print(df)

a = df.isnull()
# print(a)

b=df.dropna()
print(b)