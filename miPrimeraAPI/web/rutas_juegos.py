from flask import request,session,make_response
import json
import decimal
from __main__ import app
import controlador_juegos
from funciones_auxiliares import Encoder,sanitize_input,prepare_response_extra_headers,validar_session_normal,validar_session_admin

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

response_extra_headers = prepare_response_extra_headers(True)

@app.route("/api/juegos",methods=["GET"])
def juegos():
    if (validar_session_normal()):
        ret,code= controlador_juegos.obtener_juegos()
    else:
        ret={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(ret, cls = Encoder),code)
    return response

@app.route("/api/juego/<id>",methods=["GET"])
def juego_por_id(id):
    id = sanitize_input(id)
    if (validar_session_normal()):
        ret,code = controlador_juegos.obtener_juego_por_id(id)
    else:
        ret={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(ret, cls = Encoder),code)
    return response

@app.route("/api/juegos",methods=["POST"])
def guardar_juego():
    if (validar_session_admin()):
        code = 200
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            nombre = sanitize_input(request.json["nombre"])
            descripcion = sanitize_input(request.json["descripcion"])
            precio = sanitize_input(request.json["precio"])
            foto = sanitize_input(request.json["foto"])
            tipo = sanitize_input(request.json["tipo"])
            if (len(nombre) ==0 or len(nombre) > 256):
                ret={"status":"Bad request n"}
                code=401 
            if (code == 200 and len(descripcion) > 256):
                ret={"status":"Bad request d"}
                code=401 
            if (code == 200 and len(foto) > 256):
                ret={"status":"Bad request f"}
                code=401
            if (code == 200 and not precio.replace(".", "").isdecimal()):
                ret={"status":"Bad request p"}
                code=401
            if (code == 200):
                try:
                    precio = float(precio)
                except:
                    ret={"status":"Bad request pf"}
                    code=401 
            if (code == 200):
                ret,code=controlador_juegos.insertar_juego(nombre,descripcion,precio,foto)
        else:
            ret={"status":"Bad request"}
            code=401
    else:
        ret={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(ret),code)
    return response

@app.route("/api/juegos/<id>", methods=["DELETE"])
def eliminar_juego(id):
    if (validar_session_admin()):
        ret,code=controlador_juegos.eliminar_juego(id)
    else:
        ret={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(ret),code)
    return response

@app.route("/api/juegos", methods=["PUT"])
def actualizar_juego():
    if (validar_session_admin()):
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
    else:
        ret={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(ret),code)
    return response

