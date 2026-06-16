import requests
import pytest
import random
import string

BASE_URL = "https://compassuol.serverest.dev"

@pytest.fixture
def produto_por_id_response(produto_cadastrado):
    response, _ = produto_cadastrado

    if response.status_code == 201:
        produto_id = response.json()["_id"]

        return requests.get(
            f"{BASE_URL}/produtos/{produto_id}"
        )

    return response


def test_buscar_produto_por_id_status_code(
    produto_por_id_response
):
    assert produto_por_id_response.status_code == 200


def test_buscar_produto_por_id_retorna_json(
    produto_por_id_response
):
    assert (
        "application/json"
        in produto_por_id_response.headers["Content-Type"]
    )


def test_buscar_produto_por_id_retorna_campos_principais(
    produto_por_id_response
):
    body = produto_por_id_response.json()

    campos_obrigatorios = [
        "nome",
        "preco",
        "descricao",
        "quantidade",
        "_id"
    ]

    for campo in campos_obrigatorios:
        assert campo in body


def test_buscar_produto_por_id_tipos_campos(
    produto_por_id_response
):
    body = produto_por_id_response.json()

    assert isinstance(body["nome"], str)
    assert isinstance(body["preco"], int)
    assert isinstance(body["descricao"], str)
    assert isinstance(body["quantidade"], int)
    assert isinstance(body["_id"], str)


def test_buscar_produto_por_id_nao_encontrado():
    produto_id = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=16
        )
    )

    response = requests.get(
        f"{BASE_URL}/produtos/{produto_id}"
    )

    assert response.status_code == 400

    body = response.json()

    assert body["message"] == "Produto não encontrado"
