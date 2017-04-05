from flask import Flask
from flask_restful import Api
from Endpoint import controller as controller

app = Flask(__name__)
api = Api(app)

api = controller.get_resources(api)

if __name__ == '__main__':
    app.run(debug=True)
