from flask import Flask, json, jsonify
from flask_restful import reqparse, abort, Api, Resource
import subprocess


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('amount', type=int, help='The amount of passwords you want to generate')
parser.add_argument('config', type=str, help='The config file for the generator')


#  Repo Layer {{{ #
def get_passwords(amount=None, config=None):
    cmd = "hsxkpasswd" if amount is None else "hsxkpasswd {}".format(amount)
    cmd = cmd if config is None else "{} --config-file {}".format(cmd, config)
    cmd = "{} -w NONE".format(cmd)

    try:
        result_string = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            shell=True)

    except:
        return ""

    pw_list = result_string.split('\n')

    return pw_list[:-1]
#  }}} Repo Layer #


#  Service Layer {{{ #
class Passwords(Resource):
    def get(self):
        args = parser.parse_args()
        amount = args["amount"]
        config = args["config"]

        pws = get_passwords(amount, config)

        return jsonify( passwords = pws )


class WiFiPasswords(Resource):
    def get(self):
        args = parser.parse_args()
        amount = args["amount"]
        pws = get_passwords(amount, config="hsxkpasswd.config")
        return jsonify( passwords = pws )
#  }}} Service Layer #


#  Router {{{ #
api.add_resource(Passwords, '/passwords')
api.add_resource(WiFiPasswords, '/passwords/wifi')
#  }}} Router #

if __name__ == '__main__':
    app.run(debug=True)
