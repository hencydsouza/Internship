import pandas as pd
import matplotlib.pyplot as plt
data = {'age':[1,2,3,4,5,6,7,8,9,10],
        "weight":[5,8,12,14,16,20,22,24,26,27]}
pd_Data = pd.DataFrame(data)
print(pd_Data)
plt.scatter(pd_Data['age'],pd_Data['weight'],color='red')
plt.show()