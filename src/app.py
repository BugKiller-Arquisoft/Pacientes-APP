from http import client
from flask import Flask, request
from flask_pymongo import PyMongo
from pymongo import MongoClient

app= Flask(__name__)
client =MongoClient("mongodb+srv://pacientes-user:isis2503@cluster0.zga6qxp.mongodb.net/?retryWrites=true&w=majority")

@app.route('/pacientes',methods=['POST'])
def pacientes():
    nombre = request.json['nombre']
    fechanacimiento = request.json['fechanacimiento']
    rh=request.json['rh']
    tipodocumento = request.json['tipodocumento']
    documentodeidentidad = request.json['documentodeidentidad']
    eps =request.json['eps']
    ciudadresidencia=request.json['ciudadresidencia']
    
    if nombre and fechanacimiento and rh and tipodocumento and documentodeidentidad and eps and ciudadresidencia:
        id =client["pacientes-db"]["pacientes"].insert_one({'nombre':nombre, 'fechanacimiento':fechanacimiento,'rh':rh,
                                  'tipodocumento':tipodocumento,'documentodeidentidad':documentodeidentidad,'eps':eps,
                                 'ciudadresidencia':ciudadresidencia})
        response = {
            'id': str(id),
            'nombre':nombre,
            'fechanacimiento':fechanacimiento,
            'rh':rh,
            'tipodocumento':tipodocumento,
            'documentodeidentidad':documentodeidentidad,
            'eps':eps,
            'ciudadresidencia':ciudadresidencia
        }
    return response
if __name__ == "__main__":
    app.run(debug=True)