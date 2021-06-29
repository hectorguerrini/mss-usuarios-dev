import pytest
from pydantic import ValidationError
from src.models.usuario_model import UsuarioModel

class Test_UsuarioModel():
    
    def test_create_instance_model(self):
        usuario = UsuarioModel(nome='Vitonha maroca',nascimento='1960-05-24')
        assert usuario.nome == "Vitonha Maroca"
        assert usuario.nascimento.year == 1960

    def test_validator_nome_error(self):
        with pytest.raises(ValidationError) as error_info:
            usuario = UsuarioModel(nome='')        
