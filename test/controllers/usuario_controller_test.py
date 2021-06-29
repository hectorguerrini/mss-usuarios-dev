from fastapi.testclient import TestClient
from src.controllers.usuario_controller import app
from src.models.usuario_model import UsuarioModel

client = TestClient(app)


def test_read_main():
    usuario = UsuarioModel(nome='Vitonha maroca',nascimento='1960-05-24')
    response = client.post("/usuarios", json={"nome": "Vitonha maroca","nascimento": '1960-05-24'})
    assert response.status_code == 200

def test_error():
    usuario = UsuarioModel(nome='Vitonha maroca',nascimento='1960-05-24')
    response = client.post("/usuarios", json={"nome": "","nascimento": '1960-05-24'})
    assert response.status_code == 422
