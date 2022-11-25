from flask import *
from flask import Flask , request, Response
import json
import base64
from thresh_Image import local_threah
from werkzeug.utils import secure_filename
#from flask_cors import CORS
import cv2
import imutils
import numpy as np


app= Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "Heroku App"

@app.route('/ap', methods=['GET'])
def ap():
    return "Ap is working"

@app.route('/upload', methods=[ 'POST'])
def upload():
    if request.method=="POST":
        if request.files['image']:
            imagefile=request.files['image']
            imagefile.save("hello.jpg")
            try:
                local_threah("hello.jpg")
                with open("final.jpg", "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
                base64_message = my_string.decode('utf-8')
                data_set={'img': base64_message,'result': True}
                json_dump= json.dumps(data_set)
                return json_dump
            except:
                data_set={'img': "Please choose a valid image", 'result':False}
                json_dump= json.dumps(data_set)
                return json_dump

    

if __name__=="__main__":
    app.run()
