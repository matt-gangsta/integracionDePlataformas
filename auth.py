from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from models import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Diccionario simulado: token -> usuario
fake_users = {
    "token_admin": Usuario(nombre="admin", rol="Administrador", contrasena="adminpass"),
    "token_orq": Usuario(nombre="orq", rol="Orquestador", contrasena="orqpass"),
    "token_user": Usuario(nombre="user", rol="Usuario", contrasena="userpass")
}

def get_current_user(token: str = Depends(oauth2_scheme)) -> Usuario:
    user = fake_users.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    return user

def check_role(user: Usuario, roles_permitidos: list):
    if user.rol not in roles_permitidos:
        raise HTTPException(status_code=403, detail="No autorizado")