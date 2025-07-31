import pandas as pd
import requests

url = "https://official-joke-api.appspot.com/jokes/ten"

r = requests.get(url)
results = json.loads(r.text)
table = pd.DataFrame(results)
table.drop(columns=["type", "id"], inplace=True)
table
