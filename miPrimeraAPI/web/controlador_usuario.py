from __future__ import print_function
from bd import obtener_conexion
import sys
from __main__ import app
from funciones_auxiliares import cipher_password, compare_password,create_session,delete_session
import datetime as dt
from flask_wtf.csrf import generate_csrf

def login_usuario(username, passwordIn):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT perfil,clave,numAccesosErroneos FROM usuarios WHERE usuario = %s",(username))
            usuario = cursor.fetchone()
            if usuario is None:
                ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
            else:
                perfil=usuario[0]
                password=usuario[1]
                numAccesosErroneos=usuario[2]
                estado='activo'
                current_date = dt.date.today()
                hoy=current_date.strftime('%Y-%m-%d')
                if (compare_password(password.encode("utf-8"),passwordIn.encode("utf-8"))):
                    ret = {"status": "OK","csrf_token": generate_csrf()}
                    app.logger.info("Acceso usuario %s correcto",username)
                    create_session(username,perfil)
                    numAccesosErroneos=0
                else:
                    app.logger.info("Acceso usuario %s incorrecto",username)
                    numAccesosErroneos=numAccesosErroneos+1
                    if (numAccesosErroneos>2):
                        estado="bloqueado"
                        app.logger.info("Usuario %s bloqueado",username)
                    ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo"}
                cursor.execute("UPDATE usuarios SET numAccesosErroneos=%s, fechaUltimoAcceso=%s, estado=%s WHERE usuario = %s",(numAccesosErroneos,hoy,estado,username))
                conexion.commit()
                conexion.close()
            code=200
    except Exception as e:
        print(f"Excepcion al validar al usuario {e}")   
        ret={"status":"ERROR"}
        code=500
    return ret,code


def registro_usuario(username, password, perfil):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s",(username))
            usuario = cursor.fetchone()     
            if usuario is None:
                passwordC=cipher_password(password);
                cursor.execute("INSERT INTO usuarios(usuario,clave,perfil,estado,numAccesosErroneos) VALUES(%s,%s,'normal','activo',0)",(username,passwordC))
                if cursor.rowcount == 1:
                    conexion.commit()
                    app.logger.info("Nuevo usuario creado")
                    ret={"status": "OK" }
                    code=200
                else:
                    ret={"status": "ERROR" }
                    code=500
            else:
                ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
                code=200
        conexion.close()
    except Exception as e:
        print(f"Excepcion al registrar al usuario {e}")
        ret={"status":"ERROR"}
        code=500
    return ret,code
