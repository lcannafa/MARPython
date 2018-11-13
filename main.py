from flask import Flask
from flask_restful import Resource, Api
import info_procesor

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, tipo):
        doc = info_procesor.get_doc(tipo)
        strdoc = str(doc)
        kappa = strdoc.partition("link='")[2][:-2]
        return {'link' : kappa}

class HelloWorld2(Resource):
    def get(self):
        return{'about':'Hello World'}

api.add_resource(HelloWorld, '/<int:tipo>')
api.add_resource(HelloWorld2, '/')

if __name__ == '__main__':
    app.run(debug=True)
