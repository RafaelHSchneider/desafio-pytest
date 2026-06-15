import requests

BASE_URL = "https://compassuol.serverest.dev"

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