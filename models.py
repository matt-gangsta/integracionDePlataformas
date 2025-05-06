from pydantic import BaseModel
from typing import List, Dict

class Usuario(BaseModel):
    nombre: str
    rol: str
    contrasena: str

class OrquestarRequest(BaseModel):
    servicio_destino: str
    parametros_adicionales: Dict

class ServicioRegistro(BaseModel):
    nombre: str
    descripcion: str
    endpoints: List[str]

class ReglasOrquestacion(BaseModel):
    reglas: Dict

class AutenticacionRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

class AutorizacionRequest(BaseModel):
    recursos: List[str]
    rol_usuario: str