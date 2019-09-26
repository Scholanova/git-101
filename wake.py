
from flask import Flask
from flask_restful import Resource, Api
from wakeonlan import send_magic_packet

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        send_magic_packet('')
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
