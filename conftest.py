import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"

@pytest.fixture
def usuarios_response():
    return requests.get(f"{BASE_URL}/usuarios")

@pytest.fixture
def usuario_payload():
    return {
        "nome": "Fulano da Silva",
        "email": f"teste_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "teste",
        "administrador": "true"
    }


@pytest.fixture
def usuario_cadastrado(usuario_payload):
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=usuario_payload
    )

    body = response.json()

    yield response

    # Teardown
    if response.status_code == 201:
        usuario_id = body["_id"]

        requests.delete(
            f"{BASE_URL}/usuarios/{usuario_id}"
        )

@pytest.fixture
def usuario_existente(usuario_payload):
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=usuario_payload
    )

    usuario = response.json()

    yield usuario, usuario_payload

    requests.delete(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )