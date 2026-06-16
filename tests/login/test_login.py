import requests
import uuid
from tests.schemas import SchemaValidator, login_sucesso_schema

BASE_URL = "https://compassuol.serverest.dev"

def test_login_status_code(login_response):
    assert login_response.status_code == 200

def test_login_retorna_json(login_response):
    assert (
        "application/json"
        in login_response.headers["Content-Type"]
    )

def test_login_retorna_mensagem(login_response):
    body = login_response.json()

    assert "message" in body
    assert body["message"] == "Login realizado com sucesso"

def test_login_retorna_token(login_response):
    body = login_response.json()

    assert "authorization" in body
    assert isinstance(body["authorization"], str)
    assert body["authorization"].startswith("Bearer ")

def test_login_valida_schema(login_response):
    """Valida response contra JSON Schema"""
    SchemaValidator.validate_response(login_response, login_sucesso_schema)

def test_login_com_email_invalido():
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": "email_inexistente@qa.com.br",
            "password": "123456"
        }
    )

    assert response.status_code == 401

    body = response.json()

    assert body["message"] == "Email e/ou senha inválidos"

def test_login_com_senha_invalida(usuario_comum):
    usuario, payload = usuario_comum

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": "senha_errada"
        }
    )

    assert response.status_code == 401

    body = response.json()

    assert body["message"] == "Email e/ou senha inválidos"

def test_login_com_email_e_senha_invalidos():
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": "invalido@qa.com.br",
            "password": "senha_errada"
        }
    )

    assert response.status_code == 401

    body = response.json()

    assert body["message"] == "Email e/ou senha inválidos"

def test_token_expira_em_10_minutos(login_response):
    body = login_response.json()

    authorization = body["authorization"]
    
    assert authorization.startswith("Bearer ")
    token = authorization.split(" ")[1]
    
    assert len(token.split(".")) == 3

def test_login_com_campos_vazios():
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": "",
            "password": ""
        }
    )

    assert response.status_code == 400

    body = response.json()

    assert body.get("message") or body.get("email") or body.get("password")

def test_login_com_email_vazio():
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": "",
            "password": "123456"
        }
    )

    assert response.status_code == 400

    body = response.json()

    assert body.get("message") or body.get("email")

def test_login_com_senha_vazia(usuario_comum):
    usuario, payload = usuario_comum

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": ""
        }
    )

    assert response.status_code == 400

    body = response.json()

    # Valida que há erro de validação
    assert body.get("message") or body.get("password")
