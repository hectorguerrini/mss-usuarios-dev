from pydantic import BaseModel, validator
from src.models.usuario_model import UsuarioModel
from src.repositories.usuario_repository_interface import IUsuarioRepository


class CadastrarUsuario(BaseModel):
    repository: IUsuarioRepository


    class Config:
        arbitrary_types_allowed = True

    @validator('repository')
    def repository_is_null(cls, v):
        return v

    def cadastrarUsuario(self, usuario: UsuarioModel):
        self.repository.cadastrarUsuario(usuario)
        return usuario