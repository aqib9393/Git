from flask import *
from flask import Flask , request, Response
import json
import base64
from thresh_Image import local_threah
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin


app= Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app)


ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
@cross_origin()
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

@app.route('/test', methods=['POST'])
def upload_image():
    files = request.files.getlist('image')
    file_names = []
    base64_lst=[]

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_names.append(filename)
            file.save(filename)
            #testing start
            try:
                local_threah(filename)
                with open("final.jpg", "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
                base64_lst.append(my_string.decode('utf-8'))
            except:
                data_set={'img': "Please choose a valid image "+filename, 'result':False}
                json_dump= json.dumps(data_set)
                return json_dump


    data_set={'img': base64_lst,'result': True}
    json_dump= json.dumps(data_set)
    return json_dump

@app.route('/check', methods=['POST'])
@cross_origin()
def upload_i():
    files = request.files.getlist('image')
    file_names = []
    base64_lst=[]

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_names.append(filename)
            file.save(filename)
            #testing start
            try:
                local_threah(filename)
                with open("final.jpg", "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
                base64_lst.append(my_string.decode('utf-8'))
            except:
                data_set={'img': "Please choose a valid image "+filename, 'result':False}
                json_dump= json.dumps(data_set)
                return json_dump


    data_set={'img': base64_lst,'result': True}
    json_dump= json.dumps(data_set)
    return json_dump
    

if __name__=="__main__":
    app.run()
