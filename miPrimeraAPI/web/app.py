import os
from flask import Flask, request, make_response
import json
from logging.config import dictConfig
from flask_wtf.csrf import CSRFProtect    #en la parte superior
from funciones_auxiliares import prepare_response_extra_headers, Encoder

app = Flask(__name__)
app.config.from_pyfile('settings.py')
csrf = CSRFProtect(app)     #tras crear la variable app

#Configuracion de los logs
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
            "time-rotate": {
               "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "flask.log",
                "when": "D",
                "interval": 10,
                "backupCount": 5,
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console","time-rotate"]},
    }
)

#Configuración de las sesiones con cookies
app.config.update(PERMANENT_SESSION_LIFETIME=600)
#app.config.update( SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',)
app.config.update( SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',)

@app.errorhandler(500)
def server_error(error):
    app.logger.exception('An exception occurred during a request.')
    respuesta={"status":"Error"}
    code=500
    return make_response(json.dumps(respuesta, cls=Encoder), code)

@app.before_request
def csrf_protect():
    app.logger.info("La petición es %s", request.path)
    if not request.path.startswith("/api/login") and not request.path.startswith("/api/registro"):
        csrf.protect()

#Configuración de la cabecera
extra_headers=prepare_response_extra_headers(True);

@app.after_request
def logAfterRequest(response):
    app.logger.info(
        "path: %s | method: %s | status: %s | size: %s >>> %s",
        request.path,
        request.method,
        response.status,
        response.content_length,
        request.remote_addr,
    )
    response.headers.extend(extra_headers)
    return response

import rutas_inicio
import rutas_upload
import rutas_verfichero
import rutas_juegos

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)