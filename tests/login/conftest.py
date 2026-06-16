"""Fixtures para testes de login"""

import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


@pytest.fixture
def usuario_comum_payload():
    return {
        "nome": "Usuario Comum",
        "email": f"user_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "123456",
        "administrador": "false"
    }


@pytest.fixture
def usuario_comum(usuario_comum_payload):
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=usuario_comum_payload
    )

    usuario = response.json()

    yield usuario, usuario_comum_payload

    requests.delete(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )


@pytest.fixture
def login_response(usuario_comum):
    _, payload = usuario_comum
    
    return requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )
