#coding:utf-8
 
import sys
import random
import json
#reload(sys)
#sys.setdefaultencoding('utf8')
from flask import Flask,Blueprint,render_template,request,redirect,jsonify
from flasgger import Swagger,swag_from
 
app = Flask(__name__)
Swagger(app)

@app.route('/api/<string:language>/', methods=['GET'])
@swag_from('test.yml')
def index(language):
    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic", 
        "simple", "powerful", "amazing", 
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


app.run(debug=True)