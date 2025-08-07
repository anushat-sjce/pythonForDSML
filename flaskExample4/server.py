
#Get with parameters 
from flask import Flask, make_response

app = Flask(__name__)

data = [
    {
        "id": "001",
        "first_name":"Anusha",
        "Last_name":"T",
        "city":"Shimoga",
        "country":"India"
    },
    {
        "id": "002",
        "first_name":"Ishaan",
        "Last_name":"Rao",
        "city":"Shimoga",
        "country":"India"
    },
    {
        "id": "003",
        "first_name":"Jayathirth",
        "Last_name":"Rao",
        "city":"Raichur",
        "country":"India"
    }
]

@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message" : f"Data of length {len(data)} found"}
        else:
            return {"message" : "Data is empty"}, 500

    except NameError:
        return {"message": "Datat not found"}, 404


#flask --app server --debug run
#curl -X GET -i -w '\n' 
localhost:5000/data
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.11
Date: Thu, 07 Aug 2025 06:08:06 GMT
Content-Type: application/json
Content-Length: 42
Connection: close

{
  "message": "Data of length 3 found"
}
