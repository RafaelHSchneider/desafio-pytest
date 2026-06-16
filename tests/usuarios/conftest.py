"""Fixtures para testes de usuários"""

import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


@pytest.fixture
def usuario_payload():
    return {
        "nome": "Fulano da Silva",
        "email": f"teste_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "teste",
        "administrador": "true"
    }


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


@pytest.fixture
def usuario_por_id_response(usuario_existente):
    usuario, _ = usuario_existente

    return requests.get(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )


@pytest.fixture
def excluir_usuario_response(usuario_existente):
    usuario, _ = usuario_existente

    return requests.delete(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )


@pytest.fixture
def usuario_update_payload():
    return {
        "nome": "Usuário Atualizado",
        "email": f"update_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "123456",
        "administrador": "false"
    }


@pytest.fixture
def segundo_usuario():
    payload = {
        "nome": "Segundo Usuario",
        "email": f"segundo_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "123456",
        "administrador": "true"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    usuario = response.json()

    yield usuario

    requests.delete(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )
