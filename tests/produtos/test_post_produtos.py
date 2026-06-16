import requests
from tests.schemas import SchemaValidator, produto_criado_schema

BASE_URL = "https://compassuol.serverest.dev"

def test_cadastrar_produto_status_code(
    produto_cadastrado
):
    response, _ = produto_cadastrado

    assert response.status_code == 201

def test_cadastrar_produto_retorna_mensagem(
    produto_cadastrado
):
    response, _ = produto_cadastrado

    body = response.json()

    assert (
        body["message"]
        == "Cadastro realizado com sucesso"
    )

def test_cadastrar_produto_valida_schema(
    produto_cadastrado
):
    """Valida response contra JSON Schema"""
    response, _ = produto_cadastrado
    
    SchemaValidator.validate_response(response, produto_criado_schema)

def test_cadastrar_produto_retorna_id(
    produto_cadastrado
):
    response, _ = produto_cadastrado

    body = response.json()

    assert "_id" in body
    assert isinstance(body["_id"], str)

def test_cadastrar_produto_nome_duplicado(
    token_admin,
    produto_cadastrado
):
    _, payload = produto_cadastrado

    response = requests.post(
        f"{BASE_URL}/produtos",
        json=payload,
        headers={
            "Authorization": token_admin
        }
    )

    assert response.status_code == 400

    body = response.json()

    assert (
        body["message"]
        == "Já existe produto com esse nome"
    )

def test_cadastrar_produto_sem_token(
    produto_payload
):
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto_payload
    )

    assert response.status_code == 401

    body = response.json()

    assert (
        body["message"]
        == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"
    )

def test_cadastrar_produto_usuario_nao_admin(
    token_usuario,
    produto_payload
):
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto_payload,
        headers={
            "Authorization": token_usuario
        }
    )

    assert response.status_code == 403

    body = response.json()

    assert (
        body["message"]
        == "Rota exclusiva para administradores"
    )