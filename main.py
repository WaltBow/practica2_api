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
