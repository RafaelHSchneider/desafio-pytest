"""Fixtures para testes de produtos"""

import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


@pytest.fixture
def produtos_response():
    """GET /produtos - lista de todos os produtos"""
    return requests.get(f"{BASE_URL}/produtos")


@pytest.fixture
def produto_payload():
    return {
        "nome": f"Produto {uuid.uuid4().hex[:8]}",
        "preco": 100,
        "descricao": "Produto para testes",
        "quantidade": 10
    }


@pytest.fixture
def produto_update_payload():
    return {
        "nome": f"Produto Atualizado {uuid.uuid4().hex[:8]}",
        "preco": 250,
        "descricao": "Produto atualizado para testes",
        "quantidade": 20
    }


@pytest.fixture
def produto_cadastrado(
    token_admin,
    produto_payload
):
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto_payload,
        headers={
            "Authorization": token_admin
        }
    )

    body = response.json()

    yield response, produto_payload

    if response.status_code == 201:
        requests.delete(
            f"{BASE_URL}/produtos/{body['_id']}",
            headers={
                "Authorization": token_admin
            }
        )


@pytest.fixture
def produto_existente(
    token_admin,
    produto_payload
):
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto_payload,
        headers={
            "Authorization": token_admin
        }
    )

    produto = response.json()

    yield produto, produto_payload

    if response.status_code == 201:
        requests.delete(
            f"{BASE_URL}/produtos/{produto['_id']}",
            headers={
                "Authorization": token_admin
            }
        )


@pytest.fixture
def excluir_produto_response(produto_existente, token_admin):
    produto, _ = produto_existente

    return requests.delete(
        f"{BASE_URL}/produtos/{produto['_id']}",
        headers={
            "Authorization": token_admin
        }
    )
