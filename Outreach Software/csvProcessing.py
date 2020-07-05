import pandas as pd
import numpy as np

col_list = ['Company Name', 'Founders Email Ids']
df = pd.read_csv('companies-2.csv', delimiter = ',', usecols = col_list)
df.replace('', np.nan)
df["Company Name"].fillna("No Name", inplace = True) 
df["Founders Email Ids"].fillna("No Email", inplace = True) 
df.to_csv('relevant.csv')


