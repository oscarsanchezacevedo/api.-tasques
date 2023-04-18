#!/usr/bin>/python3

import flask
import app_tasques
import tasca
import json

app = flask.Flask(__name__)
core_app = app_tasques.App_tasques()
@app.route("/tasks/<id>", methods=["DELETE"])
def delete_task(id):
    resultat = core_app.esborra_tasca(id)
    return "", 204

@app.route("/tasks", methods=["POST", "GET", "PUT"])
def tasks():
    if flask.request.method == "POST":
        info_body = flask.request.get_data()   #info_body = '{"title": "hola"}' -> str
        tasca_nova = json.loads(info_body)     #tasca_nova = {"title": "hola"} -> dictionary
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"])  #Objecte.Tasca -> tasca.Tasca
        resultat = core_app.afegeix_tasca(objecte_tasca)
        return "", 201
    elif flask.request.method == "PUT":
        info_body = flask.request.get_data()   #info_body = '{"title": "hola"}' -> str
        tasca_nova = json.loads(info_body)     #tasca_nova = {"title": "hola"} -> dictionary
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"], tasca_nova["done"], tasca_nova["id"])  #Objecte.Tasca -> tasca.Tasca
        resultat = core_app.modifica_tasca(objecte_tasca)
        return "", 204

    elif flask.request.method == "GET":
        llista_jsons = []
        llista_tasques = core_app.llegir_tasques()
        for t in llista_tasques:
            tasca_json = str (t)                 #tasca_json ->str 
            tasca_diccionary = json.loads(tasca_json)  #tasca_diccionay ->diccionary
            llista_jsons.append(tasca_diccionary)   #array de diccionaries
        return flask.jsonify(llista_jsons), 200   #retorna a json + content-type: application/json


app.run(host="0.0.0.0")