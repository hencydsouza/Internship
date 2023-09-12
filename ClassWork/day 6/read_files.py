import pandas as pd

excel_data_df = pd.read_excel('C:/Users/hency/OneDrive/Desktop/Internship/day 6/records.xlsx', sheet_name='Sheet1')

csv_data_df = pd.read_csv('C:/Users/hency/OneDrive/Desktop/Internship/day 6/data.csv')
csv_df = pd.DataFrame(csv_data_df)

print(csv_df.head(12))