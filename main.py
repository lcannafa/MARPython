from flask import Flask
from flask_restful import Resource, Api
import info_procesor

app = Flask(__name__)
api = Api(app)


""" FLASK PART
- Crea un servidor, de manera local.
- Tiene la clase getLink, que es es que obtiene el link para el archivo de Dropbox.
- Se deja como ejemplo HelloWorld2 de como se establecerian mas funciones.

En la actualidad esta corriendo en el DCA en la dirección http://machinear.dis.eafit.edu.co

COMO LANZAR: 
    python main.py
 """

# getLink
# Requiere:
# - tipo: es un entero que maneja si se va imprimir el documento con tablas o sin tablas.
#        ( 0 manda sin tablas, 1 manda con tablas)

class getLink(Resource):
    def get(self, tipo):
        json = info_procesor.get_doc(tipo)
        link = str(json).partition("link='")[2][:-2]
        return {'link' : link}


#Ejemplo de un get.
class HelloWorld2(Resource):
    def get(self):
        return{'about':'Hello World'}

# ------------------------------------------------- AGREGAR RECURSOS DEL API -----------------------------------------------
api.add_resource(getLink, '/<int:tipo>')
api.add_resource(HelloWorld2, '/')
# --------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # Para definir un puerto en particular, (host='0.0.0.0', port = xxxx)
    app.run(debug=True)
