

from src.usecases.cadastrar_usuario import CadastrarUsuario
from src.repositories.usuario_repository_mock import UsuarioRepositoryMock

cadastrarUsuarioService: CadastrarUsuario = (
    lambda: CadastrarUsuario(repository=UsuarioRepositoryMock()))()
