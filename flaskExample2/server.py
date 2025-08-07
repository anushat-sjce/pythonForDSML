#import Flask class from flask module
from flask import Flask, request, make_response

#Creating instance of Flass class by passingn the name of the current module
app = Flask(__name__)

#Define a routr for the root URL("/")
@app.route("/")

def index():
    res = make_response("Hello world , Welcome to new era of AI ")
    res.status_code = 200 
    return res


#To run the module execute
#On terminal 1 : flask --app server --debug run
#On terminal 2 : curl -X -i -w GET '\n' localhost:5000 
