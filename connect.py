from flask import Flask
from flask_restful import Resource, Api
import info_procesor
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, tipo):
        doc = info_procesor.get_doc(tipo)
        strdoc = str(doc)
        kappa = strdoc.partition("link='")[2][:-2]
        return {'about' : kappa}

api.add_resource(HelloWorld, '/<int:tipo>')

if __name__ == '__main__':
    app.run(debug=True)
