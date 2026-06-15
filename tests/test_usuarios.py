import requests


BASE_URL = "https://compassuol.serverest.dev"

def test_listar_usuarios_status_code(usuarios_response):
    assert usuarios_response.status_code == 200


def test_listar_usuarios_retorna_campos_principais(usuarios_response):
    body = usuarios_response.json()

    assert "quantidade" in body
    assert "usuarios" in body

    assert isinstance(body["quantidade"], int)
    assert isinstance(body["usuarios"], list)


def test_listar_usuarios_quantidade_corresponde_lista(usuarios_response):
    body = usuarios_response.json()

    assert body["quantidade"] == len(body["usuarios"])


def test_listar_usuarios_estrutura_usuario(usuarios_response):
    body = usuarios_response.json()

    if not body["usuarios"]:
        return

    usuario = body["usuarios"][0]

    campos_obrigatorios = [
        "nome",
        "email",
        "password",
        "administrador",
        "_id",
    ]

    for campo in campos_obrigatorios:
        assert campo in usuario

def test_usuario_campos_possuem_tipo_correto(usuarios_response):
    usuario = usuarios_response.json()["usuarios"][0]

    assert isinstance(usuario["nome"], str)
    assert isinstance(usuario["email"], str)
    assert isinstance(usuario["password"], str)
    assert isinstance(usuario["administrador"], str)
    assert isinstance(usuario["_id"], str)

def test_cadastrar_usuario_com_sucesso(usuario_cadastrado):
    assert usuario_cadastrado.status_code == 201

    body = usuario_cadastrado.json()

    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body

def test_cadastrar_usuario_retorna_campos_esperados(usuario_cadastrado):
    body = usuario_cadastrado.json()

    assert "message" in body
    assert "_id" in body

    assert len(body.keys()) == 2

def test_cadastrar_usuario_retorna_json(usuario_cadastrado):
    assert "application/json" in usuario_cadastrado.headers["Content-Type"]


def test_cadastrar_usuario_com_email_ja_existente(usuario_existente):
    _, payload = usuario_existente

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    assert response.status_code == 400
    assert response.json()["message"] == "Este email já está sendo usado"