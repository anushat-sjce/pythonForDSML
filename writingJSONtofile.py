import json
person = {
    "First Name" : "Anusha",
    "Middle Name" : "T",
    "Last Name" : "Das",
    "DOB" : "10031989",
    "City" : "Bangalore",
    "PinCode" : "560087",
    "Country" : "India"
}

with open("person.json", "w") as f:
    json.dump(person, f)


json_object = json.dumps(person, indent = 4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)
