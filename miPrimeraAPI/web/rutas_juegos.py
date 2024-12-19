from flask import request, session
import json
import decimal
from __main__ import app
import controlador_juegos
from funciones_auxiliares import Encoder

@app.route("/api/juegos",methods=["GET"])
def juegos():
    juegos,code= controlador_juegos.obtener_juegos()
    return json.dumps(juegos, cls = Encoder),code

@app.route("/api/juego/<id>",methods=["GET"])
def juego_por_id(id):
    juego,code = controlador_juegos.obtener_juego_por_id(id)
    return json.dumps(juego, cls = Encoder),code

@app.route("/api/juegos",methods=["POST"])
def guardar_juego():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        juego_json = request.json
        ret,code=controlador_juegos.insertar_juego(juego_json["nombre"], juego_json["descripcion"], float(juego_json["precio"]), juego_json["foto"], juego_json["tipo"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/api/juegos/<id>", methods=["DELETE"])
def eliminar_juego(id):
    ret,code=controlador_juegos.eliminar_juego(id)
    return json.dumps(ret), code

@app.route("/api/juegos", methods=["PUT"])
def actualizar_juego():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        juego_json = request.json
        ret,code=controlador_juegos.actualizar_juego(juego_json["id"],juego_json["nombre"], juego_json["descripcion"], float(juego_json["precio"]),juego_json["foto"], juego_json["tipo"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code