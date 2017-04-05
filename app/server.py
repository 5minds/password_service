from flask import Flask, json, jsonify
from flask_restful import reqparse, abort, Api
from Service import WiFiPasswords as Service1
from Service import Passwords as Service2

app = Flask(__name__)
api = Api(app)

#  Router {{{ #
api.add_resource(Service1.WiFiPasswords, '/passwords/wifi')
api.add_resource(Service2.Passwords, '/passwords')
#  }}} Router #

if __name__ == '__main__':
    app.run(debug=True)
