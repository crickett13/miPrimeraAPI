from flask import request,session,make_response
import json
import decimal
from __main__ import app
import controlador_juegos
from funciones_auxiliares import Encoder,sanitize_input

@app.route("/api/juegos",methods=["GET"])
def juegos():
    juegos,code= controlador_juegos.obtener_juegos()
    return json.dumps(juegos, cls = Encoder),code

@app.route("/api/juego/<id>",methods=["GET"])
def juego_por_id(id):
    id = sanitize_input(id)
    juego,code = controlador_juegos.obtener_juego_por_id(id)
    return json.dumps(juego, cls = Encoder),code

@app.route("/api/juegos",methods=["POST"])
def guardar_juego():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        nombre = sanitize_input(request.json["nombre"])
        descripcion = sanitize_input(request.json["descripcion"])
        precio = sanitize_input(request.json["precio"])
        foto = sanitize_input(request.json["foto"])
        tipo = sanitize_input(request.json["tipo"])
        ret,code=controlador_juegos.insertar_juego(nombre,descripcion,precio,foto,tipo)
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
        id = sanitize_input(request.json["id"])
        nombre = sanitize_input(request.json["nombre"])
        descripcion = sanitize_input(request.json["descripcion"])
        precio = sanitize_input(request.json["precio"])
        foto = sanitize_input(request.json["foto"])
        tipo = sanitize_input(request.json["tipo"])
        ret,code=controlador_juegos.actualizar_juego(id,nombre,descripcion,precio,foto,tipo)
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code