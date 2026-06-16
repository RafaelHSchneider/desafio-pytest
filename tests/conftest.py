"""Global fixtures shared across all tests"""

import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


@pytest.fixture
def admin_payload():
    """Payload para criar usuário administrador"""
    return {
        "nome": "Administrador Teste",
        "email": f"admin_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "123456",
        "administrador": "true"
    }


@pytest.fixture
def admin_usuario(admin_payload):
    """Cria usuário administrador para testes"""
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=admin_payload
    )

    usuario = response.json()

    yield usuario, admin_payload

    requests.delete(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )


@pytest.fixture
def token_admin(admin_usuario):
    """Token de autenticação para administrador"""
    _, payload = admin_usuario

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )

    return response.json()["authorization"]


@pytest.fixture
def usuario_comum_payload():
    """Payload para criar usuário comum"""
    return {
        "nome": "Usuario Comum",
        "email": f"user_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "123456",
        "administrador": "false"
    }


@pytest.fixture
def usuario_comum(usuario_comum_payload):
    """Cria usuário comum para testes"""
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
def token_usuario(usuario_comum):
    """Token de autenticação para usuário comum"""
    _, payload = usuario_comum

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )

    return response.json()["authorization"]



