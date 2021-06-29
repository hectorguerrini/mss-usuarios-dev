from abc import ABC, abstractmethod
from src.models.usuario_model import UsuarioModel

class IUsuarioRepository(ABC):
    @abstractmethod
    def cadastrarUsuario(self, usuario: UsuarioModel):
        pass