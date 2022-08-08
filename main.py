from dataclasses import Field
from struct import unpack
from flask import Flask
from flask_restful import Api, Resource
import zmq
import time
import os
from flask import send_from_directory
from helper.helperfunc import unpack_func, create_dict

app = Flask(__name__)
api = Api(app)

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Socket to talk to server
#print("Connecting to hello world server…")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return {"hello": "world"}

class Job(Resource):

    def get(self, order_id):
        sield = ['Reference', 'OrderStatus', 'RecievedDate']
        socket.send_string(str(order_id))
        query = socket.recv()
        query = query.decode('UTF-8')
        if query == "error occured":
            return {'error' : 'occured'}
        unpack = unpack_func(query)
        Final = create_dict(unpack)
        return Final    

api.add_resource(Job, "/<string:order_id>")

if __name__ == "__main__":
    app.run()
    