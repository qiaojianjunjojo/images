#!flask/bin/python
#coding = utf-8

from flask import Flask, jsonify
import time
from threading import Thread,Lock
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


def getdata1():
    time.sleep(3) #模擬DB查詢
    return "data1"

def getdata2():
    time.sleep(3) #模擬DB查詢
    return "data2"


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify(data1 = getdata1(),data2 = getdata2())


if __name__ == '__main__':
    app.run()
