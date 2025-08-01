# pd.read.csv() function to be called once the file is downlaoded into local file .csv 



import piplite
await piplite.install(['seaborn','lxml','openpyxl'])

import pandas as pd

from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)
df
df.columns= ["First Name", "Last Name", "Location", "City", "Code", "Area Code"]
df

df["First Name"]

df2 = df[["First Name", "Last Name", "City"]]
df2
df.loc[2]

df.loc[[0,1,2], "First Name"]

df.iloc[[0,1,2], 0]
