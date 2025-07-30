# Import Beautiful Soup to parse the web page content
import requests
from bs4 import BeautifulSoup

#URL for GET operation.
url="https://en.wikipedia.org/wiki/IBM"

response=requests.get(url)
html_content=response.text

#Do not enable the below line of code. throws a lot of unstructured + structured data
#print(html_content)

soup=BeautifulSoup(html_content,"html.parser")
print(html_content[:500])

#find all anchor tags in the list <a>
titles = soup.find_all('title')
print(titles)


for title2 in titles:
    print(title2.text, "\n\n")

images = soup.find_all("img")
print(images)

for imgs in images:
    print(imgs,"\n\n")
