from flask import *
from flask import Flask , request, Response
import json
import base64
from werkzeug.utils import secure_filename
#from flask_cors import CORS
import cv2
import imutils


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
