import requests
url_get="http://httpbin.org/get"
payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

r.url
print(r.request.body)
print(r.status_code)
print(r.text)
r.json()
