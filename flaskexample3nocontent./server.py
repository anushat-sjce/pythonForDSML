#importing the request, Flask library modules
from flask import Flask, request, make_response

#instantiating the flask class
app = Flask(__name__)

#define the router for the root URL
@app.route("/no_content")

#Write code logic for GET/POST here.
def no_content():
    res = make_response("No content")
    res.status_code = 204
    return res


#To run the code 
#On terminal 1 : flask --app server --debug run
#On terminal 2 : curl -X -i -w '\n' localhost:5000\no_content


theia@theia-anushatsjce:/home/project/lab2$ curl -X GET -i -w '\n' localhost:5000/no_content
HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.2.3 Python/3.11.11
Date: Thu, 07 Aug 2025 05:39:52 GMT
Content-Type: text/html; charset=utf-8
Connection: close
