import pytest
from tests.schemas import SchemaValidator, produtos_list_schema, produto_schema

def test_listar_produtos_status_code(produtos_response):
    assert produtos_response.status_code == 200

def test_listar_produtos_retorna_json(produtos_response):
    assert (
        "application/json"
        in produtos_response.headers["Content-Type"]
    )

def test_listar_produtos_valida_schema(produtos_response):
    """Valida response contra JSON Schema"""
    SchemaValidator.validate_response(produtos_response, produtos_list_schema)

def test_listar_produtos_retorna_campos_principais(
    produtos_response
):
    body = produtos_response.json()

    assert "quantidade" in body
    assert "produtos" in body

    assert isinstance(body["quantidade"], int)
    assert isinstance(body["produtos"], list)

def test_listar_produtos_quantidade_corresponde_lista(
    produtos_response
):
    body = produtos_response.json()

    assert body["quantidade"] == len(body["produtos"])

def test_listar_produtos_estrutura_produto(
    produtos_response
):
    body = produtos_response.json()

    if not body["produtos"]:
        pytest.skip("Nenhum produto cadastrado")

    produto = body["produtos"][0]

    campos_obrigatorios = [
        "nome",
        "preco",
        "descricao",
        "quantidade",
        "_id"
    ]

    for campo in campos_obrigatorios:
        assert campo in produto

def test_listar_produtos_tipos_campos_produto(
    produtos_response
):
    body = produtos_response.json()

    if not body["produtos"]:
        pytest.skip("Nenhum produto cadastrado")

    produto = body["produtos"][0]

    assert isinstance(produto["nome"], str)
    assert isinstance(produto["preco"], int)
    assert isinstance(produto["descricao"], str)
    assert isinstance(produto["quantidade"], int)
    assert isinstance(produto["_id"], str)