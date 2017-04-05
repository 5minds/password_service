from flask import Flask, json, jsonify
from flask_restful import reqparse, abort, Api, Resource
from Repository import hsxkpasswd as pw_repo

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('amount', type=int, help='The amount of passwords you want to generate')
parser.add_argument('config', type=str, help='The config file for the generator')

#  Service Layer {{{ #
class Passwords(Resource):
    def get(self):
        args = parser.parse_args()
        amount = args["amount"]
        config = args["config"]

        pws = pw_repo.get_passwords(amount, config)

        return jsonify( passwords = pws )


class WiFiPasswords(Resource):
    def get(self):
        args = parser.parse_args()
        amount = args["amount"]
        pws = pw_repo.get_passwords(amount, config="hsxkpasswd.config")
        return jsonify( passwords = pws )
#  }}} Service Layer #


#  Router {{{ #
api.add_resource(WiFiPasswords, '/passwords/wifi')
api.add_resource(Passwords, '/passwords')
#  }}} Router #

if __name__ == '__main__':
    app.run(debug=True)
