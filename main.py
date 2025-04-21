from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Memoria temporal
usuarios = {}

class Usuario(BaseModel):
    nombre: str
    edad: int

@app.post("/usuarios/")
def guardar_usuario(user: Usuario):
    usuarios[user.nombre] = user
    return {"mensaje": f"Usuario {user.nombre} guardado exitosamente"}


@app.get("/usuarios/{nombre}")
def obtener_usuario(nombre: str):
    if nombre in usuarios:
        return usuarios[nombre]
    return {"error": "Usuario no encontrado"}
