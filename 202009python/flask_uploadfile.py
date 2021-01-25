#coding = utf-8

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flasgger import Swagger

UPLOAD_FOLDER = r'F:/upload'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

Swagger(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploadfile', methods=['POST'])
def test():
    """
    文件上傳
    ---
    tags:
        - tools
    consumes: ["multipart/form-data"]    
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      - name: fab
        description: 廠別
        in: query
        type: "array"
        required: true
        items:
            type: "string"
            enum: ["LCM1","LCM2","LCM3"]
    responses:
        500:
            description: Error !
        200:
            description: Success!

    """

    if 'file' not in request.files:
        return "<h1>Error!請選擇上傳的文件!</h1>"
    # bb = request.files.to_dict()
    fab = request.args.get("fab") #廠別
    file = request.files["file"]
    filename = file.filename
    if not allowed_file(filename): # 判斷文件後綴
        return "<h1>請上傳規定的文件(.pdf, .png, .jpg, .jpeg, .gif)</h1>"

    upload_path = os.path.join(app.config['UPLOAD_FOLDER'],fab)
    print(upload_path)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    save_path = os.path.join(upload_path,'temp.jpg')
    file.save(save_path)

    return "<h1>上傳成功</h1>"


@app.route('/upload/<fab>/<filename>/')
def uploaded_file(fab,filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'],fab),
                               filename)

if __name__ == '__main__':
    app.run(debug=False)