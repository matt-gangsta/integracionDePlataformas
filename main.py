from fastapi import FastAPI, Depends, HTTPException, status
from auth import get_current_user, check_role
from models import OrquestarRequest, ServicioRegistro, Usuario, ReglasOrquestacion, AutenticacionRequest, AutorizacionRequest
from services import orquestar_servicio, obtener_info_servicio, registrar_servicio, actualizar_reglas, autenticar_usuario, autorizar_acceso

app = FastAPI()

usuarios_db = {
    "admin": Usuario(nombre="admin", rol="Administrador", contrasena="adminpass")
}

@app.on_event("startup")
async def crear_usuario_predeterminado():
    if "nuevo_usuario" not in usuarios_db:
        usuarios_db["nuevo_usuario"] = Usuario(nombre="nuevo_usuario", rol="Orquestador", contrasena="secreta")

@app.get("/usuarios")
def obtener_usuarios():
    return usuarios_db

@app.post("/orquestar")
def orquestar(req: OrquestarRequest, user: Usuario = Depends(get_current_user)):
    check_role(user, ["Orquestador", "Administrador"])
    return orquestar_servicio(req.servicio_destino, req.parametros_adicionales)

@app.get("/informacion-servicio/{id}")
def informacion_servicio(id: str, user: Usuario = Depends(get_current_user)):
    return obtener_info_servicio(id)

@app.post("/registrar-servicio")
def registrar(req: ServicioRegistro, user: Usuario = Depends(get_current_user)):
    check_role(user, ["Administrador"])
    return registrar_servicio(req)

@app.put("/actualizar-reglas-orquestacion")
def actualizar_reglas_endpoint(req: ReglasOrquestacion, user: Usuario = Depends(get_current_user)):
    check_role(user, ["Orquestador"])
    return actualizar_reglas(req)

@app.post("/autenticar-usuario")
def autenticar(req: AutenticacionRequest):
    return autenticar_usuario(req)

@app.post("/autorizar-acceso")
def autorizar(req: AutorizacionRequest, user: Usuario = Depends(get_current_user)):
    return autorizar_acceso(req, user)