import pytest
from pydantic import ValidationError
from src.models.usuario_model import UsuarioModel
from src.usecases.cadastrar_usuario import CadastrarUsuario
from src.repositories.usuario_repository_interface import IUsuarioRepository
from src.repositories.usuario_repository_mock import UsuarioRepositoryMock

class Test_CadastrarUsuario():
    
    def test_cadastrar_usuario(self):
        repository = UsuarioRepositoryMock()
        service = CadastrarUsuario(repository=repository)

        usuario = UsuarioModel(nome='Vitonha maroca',nascimento='1960-05-24')

        service.cadastrarUsuario(usuario)
        assert len(repository.listaUsuarios) == 1
        
    def test_validator_repository_is_null(self):
        with pytest.raises(ValidationError) as error_info:
            usuario = CadastrarUsuario()        
