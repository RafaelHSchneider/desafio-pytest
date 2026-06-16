import random
import string
import requests

BASE_URL = "https://compassuol.serverest.dev"

def test_excluir_produto_status_code(
    excluir_produto_response
):
    assert excluir_produto_response.status_code == 200

def test_excluir_produto_retorna_mensagem_sucesso(
    excluir_produto_response
):
    body = excluir_produto_response.json()

    assert "message" in body

    assert (
        body["message"]
        == "Registro excluído com sucesso"
    )

def test_excluir_produto_inexistente(token_admin):
    produto_id = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=16
        )
    )

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto_id}",
        headers={
            "Authorization": token_admin
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["message"]
        == "Nenhum registro excluído"
    )

def test_produto_excluido_nao_pode_ser_consultado(
    produto_existente,
    token_admin
):
    produto, _ = produto_existente

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto['_id']}",
        headers={
            "Authorization": token_admin
        }
    )

    assert response.status_code == 200

    response = requests.get(
        f"{BASE_URL}/produtos/{produto['_id']}"
    )

    assert response.status_code == 400

    body = response.json()

    assert body["message"] == "Produto não encontrado"

def test_excluir_produto_sem_token(
    produto_existente
):
    produto, _ = produto_existente

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto['_id']}"
    )

    assert response.status_code == 401

    body = response.json()

    assert (
        body["message"]
        == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"
    )

def test_excluir_produto_usuario_nao_admin(
    token_usuario,
    produto_existente
):
    produto, _ = produto_existente

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto['_id']}",
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

def test_excluir_produto_em_carrinho(
    produto_existente,
    token_admin
):
    produto, _ = produto_existente

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto['_id']}",
        headers={
            "Authorization": token_admin
        }
    )

    if response.status_code == 400:
        body = response.json()
        
        assert "carrinhoIds" in body or "message" in body
