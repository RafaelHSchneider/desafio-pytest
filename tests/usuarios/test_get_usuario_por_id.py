import uuid
import requests
import random
import string

BASE_URL = "https://compassuol.serverest.dev"

def test_buscar_usuario_por_id_status_code(
    usuario_por_id_response
):
    assert usuario_por_id_response.status_code == 200

def test_buscar_usuario_por_id_retorna_campos_obrigatorios(
    usuario_por_id_response
):
    body = usuario_por_id_response.json()

    campos = [
        "nome",
        "email",
        "password",
        "administrador",
        "_id"
    ]

    for campo in campos:
        assert campo in body

def test_buscar_usuario_por_id_retorna_tipos_corretos(
    usuario_por_id_response
):
    body = usuario_por_id_response.json()

    assert isinstance(body["nome"], str)
    assert isinstance(body["email"], str)
    assert isinstance(body["password"], str)
    assert isinstance(body["administrador"], str)
    assert isinstance(body["_id"], str)

def test_buscar_usuario_por_id_retorna_usuario_correto(
    usuario_existente,
    usuario_por_id_response
):
    usuario, payload = usuario_existente

    body = usuario_por_id_response.json()

    assert body["_id"] == usuario["_id"]
    assert body["nome"] == payload["nome"]
    assert body["email"] == payload["email"]
    assert body["administrador"] == payload["administrador"]



def test_buscar_usuario_inexistente():
    usuario_id = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=16
        )
    )

    response = requests.get(
        f"{BASE_URL}/usuarios/{usuario_id}"
    )

    body = response.json()

    assert response.status_code == 400
    assert body["message"] == "Usuário não encontrado"

def test_buscar_usuario_com_id_invalido():
    response = requests.get(
        f"{BASE_URL}/usuarios/id_invalido"
    )

    assert response.status_code == 400

    body = response.json()

    assert body["id"] == (
        "id deve ter exatamente 16 caracteres alfanuméricos"
    )