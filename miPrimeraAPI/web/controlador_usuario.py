from __future__ import print_function
from bd import obtener_conexion
import sys         


def login_usuario(username, password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
                cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s",(username))
                usuario = cursor.fetchone()
        conexion.close()
        if usuario is None:
            ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
        else:
            passwordIn=usuario[1]
            if (compare_password(password.encode("utf-8"),passwordIn.encode("utf-8"))):
                ret = {"status": "OK" }
                session["usuario"]=username
                session["perfil"]=usuario[0]
            else:
                ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo"}
                code=200
    except:
        print("Excepcion al validar al usuario")   
        ret={"status":"ERROR"}
        code=500
    return ret,code


def registro_usuario(username, password, perfil):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s",(username,))
            usuario = cursor.fetchone()
            if usuario is None:
                passwordC=cipher_password(password);
                cursor.execute("INSERT INTO usuarios(usuario,clave,perfil) VALUES(%s,%s,'normal')",(username,passwordC))
                if cursor.rowcount == 1:
                    conexion.commit()
                    ret={"status": "OK" }
                    code=200
                else:
                    ret={"status": "ERROR" }
                    code=500
            else:
                ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
            code=200
        conexion.close()
    except:
        print("Excepcion al registrar al usuario")   
        ret={"status":"ERROR"}
        code=500
    return ret,code