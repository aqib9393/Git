from flask import *
from flask import Flask , request, Response
import json,time
import base64

app= Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "Heroku App"

@app.route('/ap', methods=['GET'])
def ap():
    return "Ap is working"

@app.route('/upload', methods=[ 'POST'])
def upload():
    
    return "hello"
    

if __name__=="__main__":
    app.run()
