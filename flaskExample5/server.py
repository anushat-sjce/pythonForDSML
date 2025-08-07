from flask import Flask, make_response,request

app = Flask(__name__)

data = [{    
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5
        }, 
        {
            "city" : "Bangalore",
            "town" : "Bhadravathi",
            "pincode":"570013"
        }
    ]

@app.route("/count")
def count_objects():
    try:
        if data and len(data) > 0:
            return {"data count ": len(data)}, 200
        else :
            return {"No data present"}, 200
    except NameError:
        return {"message":"Error - Data not defined"}, 500
   
