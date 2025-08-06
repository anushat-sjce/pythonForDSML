#import the Flask class from the flask module
from flask import Flask

#create instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

#define a route for the root URL ("/")
@app.route("/")
def home():
    #Function that handles requests to the root URL
    return "Hello, World!!"



### How to run
  """
  flask --app server --debug run 
  curl -X GET -i -w '\n'
  """
