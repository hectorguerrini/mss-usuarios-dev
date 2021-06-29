from src.repositories.usuario_repository_interface import IUsuarioRepository
from src.models.usuario_model import UsuarioModel

class UsuarioRepositoryMock(IUsuarioRepository):
    listaUsuarios: list[UsuarioModel] = []


    def cadastrarUsuario(self, usuario: UsuarioModel):
        self.listaUsuarios.append(usuario)
