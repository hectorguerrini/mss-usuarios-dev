from fastapi import APIRouter
from src.models.usuario_model import UsuarioModel
from src.controllers.factories.make_usecases import cadastrarUsuarioService


router = APIRouter(
    prefix='/usuarios',
    tags=['Usuario'],
    responses={404: {"description": "Not found"}},
)




@router.post('/')
def cadastrar_usuarios(usuario: UsuarioModel):
    response = cadastrarUsuarioService.cadastrarUsuario(usuario)
    return response


