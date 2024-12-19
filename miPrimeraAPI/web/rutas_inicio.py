from __future__ import print_function
from __main__ import app
from flask import request,session
from bd import obtener_conexion
import json
import sys
from funciones_auxiliares import Encoder
import controlador_usuario

@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        juego_json = request.json
        username = juego_json['username']
        password = juego_json['password']
        respuesta,code= controlador_usuario.login_usuario(username,password)
        return json.dumps(respuesta, cls = Encoder),code
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        juego_json = request.json
        username = juego_json['username']
        password = juego_json['password']
        perfil = juego_json['profile']
        respuesta,code= controlador_usuario.registro_usuario(username,password,perfil)
        return json.dumps(respuesta, cls = Encoder),code
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code


@app.route("/logout",methods=['GET'])
def logout():
    session.clear()
    return json.dumps({"status":"OK"}),200
