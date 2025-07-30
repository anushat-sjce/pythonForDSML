import requests

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"

r = requests.get(url)
print(r.headers)
print(r.content)

path = os.path.join(os.getcwd(), "textfile.txt")
print(path)
    
with open(path, "wb") as file:
    file.write(r.content)
    
with open(path, "r") as file:
    lines = file.readlines()
    print(lines)
