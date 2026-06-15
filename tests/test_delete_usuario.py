import random
import string
import requests

BASE_URL = "https://compassuol.serverest.dev"

def test_excluir_usuario_status_code(
    excluir_usuario_response
):
    assert excluir_usuario_response.status_code == 200

def test_excluir_usuario_retorna_mensagem_sucesso(
    excluir_usuario_response
):
    body = excluir_usuario_response.json()

    assert "message" in body

    assert (
        body["message"]
        == "Registro excluído com sucesso"
    )

def test_excluir_usuario_inexistente():
    usuario_id = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=16
        )
    )

    response = requests.delete(
        f"{BASE_URL}/usuarios/{usuario_id}"
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["message"]
        == "Nenhum registro excluído"
    )

def test_usuario_excluido_nao_pode_ser_consultado(
    usuario_existente
):
    usuario, _ = usuario_existente

    response = requests.delete(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )

    assert response.status_code == 200

    response = requests.get(
        f"{BASE_URL}/usuarios/{usuario['_id']}"
    )

    assert response.status_code == 400

    body = response.json()

    assert body["message"] == "Usuário não encontrado"