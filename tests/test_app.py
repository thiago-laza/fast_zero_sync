from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange(organizacao)

    response = client.get('/')  # Act(acao)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {'message': 'Ola mundo3'}
