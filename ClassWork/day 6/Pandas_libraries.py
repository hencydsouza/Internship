import pandas as pd
data = {'student_number':[12,45,67,89,20],
        'marks_obtained':[89,90,45,67,95],
        'secured_class':[1,2,3,4,5]}

table_data = pd.DataFrame(data)

# print(table_data.iloc[0])

data = ['a','b','c','d','e','f','g','h']
series_data = pd.Series(data)
# print(series_data)

data_list = [['a','b','c','d'],['e',None,'g',None],['i','j','k','l']]
table_data = pd.DataFrame(data_list,index=['r1','r2','r3'],columns=['c1','c2','c3','c4'])
print(table_data)
# print(table_data.notna())
# print(table_data.isna())
# print(table_data.drop('r1'))
# print(table_data.head(2))
# print(table_data.tail(2))
# print(table_data.iloc[0])