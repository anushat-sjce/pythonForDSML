from flask import Flask, request, make_response

app = Flask(__name__)

data = [ 
    {
        "uuid" : 1,
        "First Name" : "Anusha",
        "Last Name ": "T "
    }, 
    {
        "uuid" : 2,
        "First Name" : "Jayathirth",
        "Last Name" : "Rao"
    }
]

@app.route("/person/<int:uuid>")

def get_person_byid(uuid):
    for person in data:
        if person["uuid"] == uuid:
            return person
    return {"Message": "Person not found"}

@app.route("/person/<int:uuid>", methods=['DELETE'])

def delete_person(uuid):
    for person in data:
        if person["uuid"] == uuid:
            data.remove(person)
            return {"message ": "enetry deleted"}, 200
    return {"message" : "Entry Not found"}, 404
#curl -X DELETE -i  '\n' localhost:5000/person/2
