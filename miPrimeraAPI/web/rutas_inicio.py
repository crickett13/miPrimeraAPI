from __future__ import print_function
from __main__ import app
from flask import request,session,make_response
from bd import obtener_conexion
import json
import sys
from funciones_auxiliares import Encoder,sanitize_input,cipher_password, compare_password
import controlador_usuarios
from funciones import cipher_password, compare_password



@app.route("/api/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        juego_json = request.json
        if "username" in juego_json and "password" in juego_json:
            username = sanitize_input(juego_json['username'])
            password = sanitize_input(juego_json['password'])
            if isinstance(username, str) and isinstance(password, str) and len(username) < 50 and len(password) < 50:
                    respuesta,code= controlador_usuarios.login_usuario(username,password)
            else:
                respuesta={"status":"Bad parameters"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        ret={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), status=code, mimetype="application/json")
    return response

@app.route("/api/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        juego_json = request.json
        if "username" in login_json and "password" in login_json:
            username = sanitize_input(juego_json['username'])
            password = sanitize_input(juego_json['password'])
            perfil = sanitize_input(juego_json['profile'])
            if isinstance(username, str) and isinstance(password, str) and len(username) < 50 and len(password) < 50:
                respuesta,code= controlador_usuarios.login_usuario(username,password,perfil)
            else:
                respuesta={"status":"Bad parameters"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        ret={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), status=code, mimetype="application/json")
    return response

@app.route("/api/logout",methods=['GET'])
def logout():
    session.clear()
    return json.dumps({"status":"OK"}),200
