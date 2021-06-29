from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.models.usuario_model import UsuarioModel
from src.controllers.factories.make_usecases import cadastrarUsuarioService

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/usuarios')
def cadastrar_usuarios(usuario: UsuarioModel):
    response = cadastrarUsuarioService.cadastrarUsuario(usuario)
    return response


