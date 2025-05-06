from fastapi import HTTPException
from models import AutenticacionRequest
from auth import get_current_user, fake_users

def orquestar_servicio(destino, params):
    return {"estado": "ok", "destino": destino, "parametros": params}

def obtener_info_servicio(id):
    return {"id": id, "info": "Simulación de información"}

def registrar_servicio(req):
    return {"estado": "registrado", "servicio": req.nombre}

def actualizar_reglas(req):
    return {"estado": "actualizado", "reglas": req.reglas}

def autenticar_usuario(req: AutenticacionRequest):
    # Buscar un usuario en el diccionario cuyo nombre coincida
    for token, usuario in fake_users.items():
        if usuario.nombre == req.nombre_usuario:
            if usuario.contrasena == req.contrasena:
                return {"token": token}
            else:
                raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    # Simulamos token (en producción deberías usar JWT)
    token = "token_{usuario.nombre}"
    return {"token": token}

def autorizar_acceso(req, user):
    if user.rol == req.rol_usuario:
        return {"estado": "autorizado", "recursos": req.recursos}
    raise HTTPException(status_code=403, detail="No tiene acceso")