from flask import Flask
import json
from thresh_Image import local_threah

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
    local_threah("hello.jpg")
    return "hello"
    

if __name__=="__main__":
    app.run()
