!pip install pandas numpy
!pip install lxml

import numpy as np
import pandas as pd

def warn(*args, **kwargs):
    pass
import warnings 
warnings.warn = warn
warnings.filterwarnings('ignore')

URL ="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(URL)
df = tables[3]
print("Columns are")
print(df.columns)
df.columns = range(df.shape[1])

print(df)
df1 = df[[0,2]]
#print(df1)
print(" Top 10 Countries with top economies in the world")
df1.columns = ["Country", "GDP (Million USD)"]
print(df1.iloc[:11,:])
df1.to_csv('./Largest_economies.csv')
