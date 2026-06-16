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


@pytest.fixture
def admin_payload():
    return {
        "nome": "Administrador Teste",
        "email": f"admin_{uuid.uuid4().hex[:8]}@qa.com.br",
        "password": "123456",
        "administrador": "true"
    }


@pytest.fixture
def admin_usuario(admin_payload):
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
def produto_payload():
    return {
        "nome": f"Produto {uuid.uuid4().hex[:8]}",
        "preco": 100,
        "descricao": "Produto para testes",
        "quantidade": 10
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
def token_usuario(usuario_comum):
    _, payload = usuario_comum

    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )

    return response.json()["authorization"]

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

@pytest.fixture
def produto_update_payload():
    return {
        "nome": f"Produto Atualizado {uuid.uuid4().hex[:8]}",
        "preco": 250,
        "descricao": "Produto atualizado para testes",
        "quantidade": 20
    }

@pytest.fixture
def login_payload(usuario_comum_payload):
    return {
        "email": usuario_comum_payload["email"],
        "password": usuario_comum_payload["password"]
    }

@pytest.fixture
def login_response(usuario_comum, login_payload):
    _, payload = usuario_comum
    
    return requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )