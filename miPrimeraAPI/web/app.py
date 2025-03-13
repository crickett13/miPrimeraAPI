import os
from flask import Flask

from flask_wtf.csrf import CSRFProtect    #en la parte superior

app = Flask(__name__)

csrf = CSRFProtect(app)     #tras crear la variable app

import rutas_inicio

import rutas_upload

import rutas_verfichero

import rutas_juegos

from funciones_auxiliares import prepare_response_extra_headers

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)
    
@app.before_request
def csrf_protect():
    if not request.path.startswith("/login") and not request.path.startswith("/registro"):
        csrf.protect()
        
#Configuración de la cabecera
extra_headers=prepare_response_extra_headers(True);