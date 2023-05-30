from http import client
from urllib import response
from flask import Flask, Response, jsonify, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId, json_util

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
@app.route('/pacientes',methods=['GET'])
def get_pacientes():
    pacientes = client["pacientes-db"]["pacientes"].find()
    response = json_util.dumps(pacientes)
    
    return Response(response, mimetype='application/json')
@app.route('/pacientes/<id>',methods=['GET']) 
def get_paciente(id):
    paciente =client["pacientes-db"]["pacientes"].find_one({'_id':ObjectId(id)})
    response= json_util.dumps(paciente)
    return Response(response, mimetype='application/json')
@app.route('/pacientes/<id>',methods=['DELETE'])
def delete_paciente(id):
    paciente =client["pacientes-db"]["pacientes"].delete_one({'_id':ObjectId(id)})
    response = jsonify({'message': 'El paciente con el id: '+ id +' fue eliminado exitosamente'})
    return response
if __name__ == "__main__":
    app.run(debug=True)