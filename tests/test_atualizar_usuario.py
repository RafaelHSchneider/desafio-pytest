import random
import string
import requests

BASE_URL = "https://compassuol.serverest.dev"

def test_atualizar_usuario_existente_status_code(
    usuario_existente,
    usuario_update_payload
):
    usuario, _ = usuario_existente

    response = requests.put(
        f"{BASE_URL}/usuarios/{usuario['_id']}",
        json=usuario_update_payload
    )

    assert response.status_code == 200

def test_atualizar_usuario_existente_retorna_mensagem(
    usuario_existente,
    usuario_update_payload
):
    usuario, _ = usuario_existente

    response = requests.put(
        f"{BASE_URL}/usuarios/{usuario['_id']}",
        json=usuario_update_payload
    )

    body = response.json()

    assert body["message"] == "Registro alterado com sucesso"


def test_put_com_id_inexistente_cria_usuario(
    usuario_update_payload
):
    usuario_id = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=16
        )
    )

    response = requests.put(
        f"{BASE_URL}/usuarios/{usuario_id}",
        json=usuario_update_payload
    )

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body

def test_atualizar_usuario_com_email_ja_cadastrado(
    usuario_existente,
    segundo_usuario
):
    usuario_1, payload_1 = usuario_existente

    response = requests.put(
        f"{BASE_URL}/usuarios/{segundo_usuario['_id']}",
        json={
            "nome": "Teste",
            "email": payload_1["email"],
            "password": "123456",
            "administrador": "true"
        }
    )

    assert response.status_code == 400
    assert response.json()["message"] == "Este email já está sendo usado"