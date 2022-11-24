from flask import Flask , request, Response
import json,time,socket
from thresh_Image import local_threah
from werkzeug.utils import secure_filename
from flask import send_file
import base64
from time import sleep
from flask_cors import CORS

app= Flask(__name__)
app.secret_key = "cairocoders-ednalan"
CORS(app)

ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
local_ip = socket.gethostbyname(socket.gethostbyname(socket.gethostname()))
@app.route('/', methods=['GET'])
def homepage():
    data_set={'Page': 'Home','Message':'Successfully loaded the Home page', 'Time':time.time()}
    json_dump= json.dumps(data_set)
    return json_dump
@app.route('/ml', methods=[ 'POST'])
def ml():
    if 'files[]' not in request.files:
        return json.dumps({"hello":"wrong"})
    files=request.files.getlist('files[]')
    filename=[]
    for file in files:
        if file and allowed_file(file.filename):
            return json.dumps({"hello":"why"})
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

            #testing end

    data_set={'img': base64_lst,'result': True}
    json_dump= json.dumps(data_set)

    return json_dump
if __name__=="__main__":
    app.run(port=777)
    #app.run(host=local_ip,port=777)