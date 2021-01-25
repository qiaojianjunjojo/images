#coding:utf8
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from flask import Flask,Blueprint,render_template,request,redirect,jsonify
from flasgger import Swagger,swag_from

app = Flask(__name__)

swagger = Swagger(app)

#swagger展现api接口方法集合，访问http://127.0.0.1:9001/apidocs/即可
@app.route('/api/publish/',methods=['get'])
@swag_from('color.yml')
def build():
    return jsonify({"a":[1]})


if __name__ == '__main__':
    app.run(debug=True)