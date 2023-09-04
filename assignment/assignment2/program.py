import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/hency/OneDrive/Desktop/Internship/assignment/assignment2/insurance.csv')
# print(data.head)

# data.hist(bins=10)

data.dropna()

print(data)