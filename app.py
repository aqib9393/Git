from flask import *
from flask import Flask , request, Response
import json,time,socket
from thresh_Image import local_threah
from werkzeug.utils import secure_filename
from flask import send_file
import base64
from time import sleep
from flask_cors import CORS

app= Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "Heroku App"

@app.route('/ap', methods=['GET'])
def ap():
    return "Ap is working"

if __name__=="__main__":
    app.run()
