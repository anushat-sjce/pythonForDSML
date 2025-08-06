#import the Flask class from the flask module
from flask import Flask

#create instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

#define a route for the root URL ("/")
@app.route("/")
def home():
    #Function that handles requests to the root URL
    return "Hello, World!!"



### How to run terminals
  """
  flask --app server --debug run - 1st terminal
  curl -X GET -i -w '\n' localhost:5000 - 2nd terminal
  """


#import the Flask class from the flask module
from flask import Flask

#create instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

#define a route for the root URL ("/")
@app.route("/")
def home():
    #Function that handles requests to the root URL
    return {"Message":"Hello world", "From":"Anusha", "City":"Bangalore"}
