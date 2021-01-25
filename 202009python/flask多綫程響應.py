#!flask/bin/python
#coding = utf-8

from flask import Flask, jsonify
import time
from threading import Thread,Lock
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


def getdata1(resdic,lock):
    time.sleep(3) #模擬DB查詢
    lock.acquire()
    resdic["data1"] = "data1"
    lock.release()

def getdata2(resdic,lock):
    time.sleep(3) #模擬DB查詢
    lock.acquire()
    resdic["data2"] ="data2"
    lock.release()


@app.route('/', methods=['GET'])
def get_tasks():
    lock = Lock() #用來对临界資源操作
    resdic = {}
    t1, t2 = Thread(target=getdata1,args=(resdic,lock)), Thread(target=getdata2,args=(resdic,lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return jsonify(resdic)


if __name__ == '__main__':
    app.run()
