import pandas as pd
import numpy as np

df1 = pd.DataFrame([[1,2,3,4,4],[55,7,8], [2,3,1,5], [8,3,2,5]], columns=['a', 'b', 'c', 'd', 'e'])
# print(df1.head(3))
# # print(df1.tail(1))
# print(df1.iloc[2:4, 3])

#             reading csv
#df = pd.read_csv('data.csv')
#print(df.head())
#print(df['label'].dtype)

##df1.to_csv('df1.csv', index=False)