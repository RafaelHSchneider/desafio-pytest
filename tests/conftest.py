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

@pytest.fixture
def produtos_response():
    return requests.get(f"{BASE_URL}/produtos")

import uuid

@pytest.fixture
def produto_payload():
    return {
        "nome": f"Produto Teste {uuid.uuid4().hex[:8]}",
        "preco": 100,
        "descricao": "Produto para testes",
        "quantidade": 10
    }

@pytest.fixture
def produto_cadastrado(token_admin, produto_payload):
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto_payload,
        headers={"Authorization": token_admin}
    )

    produto = response.json()

    yield produto, produto_payload

    requests.delete(
        f"{BASE_URL}/produtos/{produto['_id']}",
        headers={"Authorization": token_admin}
    )