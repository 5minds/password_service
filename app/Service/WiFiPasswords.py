from flask import jsonify
from flask_restful import Resource, reqparse
from Repository import hsxkpasswd as pw_repo

parser = reqparse.RequestParser()
parser.add_argument('amount', type=int, help='The amount of passwords you want to generate')
parser.add_argument('config', type=str, help='The config file for the generator')

class WiFiPasswords(Resource):
    def get(self):
        args = parser.parse_args()
        amount = args["amount"]

        pws = pw_repo.get_passwords(amount, config="hsxkpasswd.config")
        return jsonify( passwords = pws )
