import random
import string
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"

def test_atualizar_produto_existente_status_code(
    produto_existente,
    token_admin,
    produto_update_payload
):
    produto, _ = produto_existente

    response = requests.put(
        f"{BASE_URL}/produtos/{produto['_id']}",
        json=produto_update_payload,
        headers={
            "Authorization": token_admin
        }
    )

    assert response.status_code == 200

def test_atualizar_produto_existente_retorna_mensagem(
    produto_existente,
    token_admin,
    produto_update_payload
):
    produto, _ = produto_existente

    response = requests.put(
        f"{BASE_URL}/produtos/{produto['_id']}",
        json=produto_update_payload,
        headers={
            "Authorization": token_admin
        }
    )

    body = response.json()

    assert body["message"] == "Registro alterado com sucesso"


def test_put_com_id_inexistente_cria_produto(
    token_admin,
    produto_update_payload
):
    produto_id = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=16
        )
    )

    response = requests.put(
        f"{BASE_URL}/produtos/{produto_id}",
        json=produto_update_payload,
        headers={
            "Authorization": token_admin
        }
    )

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body

    # Teardown
    requests.delete(
        f"{BASE_URL}/produtos/{body['_id']}",
        headers={
            "Authorization": token_admin
        }
    )

def test_atualizar_produto_com_nome_ja_cadastrado(
    produto_existente,
    token_admin
):
    produto, payload = produto_existente

    # Criar um segundo produto com nome diferente
    segundo_produto_payload = {
        "nome": f"Produto {uuid.uuid4().hex[:8]}",
        "preco": 150,
        "descricao": "Segundo produto para teste",
        "quantidade": 5
    }

    response_create = requests.post(
        f"{BASE_URL}/produtos",
        json=segundo_produto_payload,
        headers={
            "Authorization": token_admin
        }
    )

    segundo_produto = response_create.json()

    # Tentar atualizar o segundo produto com o nome do primeiro
    response = requests.put(
        f"{BASE_URL}/produtos/{segundo_produto['_id']}",
        json={
            "nome": payload["nome"],
            "preco": 200,
            "descricao": "Teste",
            "quantidade": 10
        },
        headers={
            "Authorization": token_admin
        }
    )

    assert response.status_code == 400
    assert response.json()["message"] == "Já existe produto com esse nome"

    # Teardown
    requests.delete(
        f"{BASE_URL}/produtos/{segundo_produto['_id']}",
        headers={
            "Authorization": token_admin
        }
    )

def test_atualizar_produto_sem_token(
    produto_existente,
    produto_update_payload
):
    produto, _ = produto_existente

    response = requests.put(
        f"{BASE_URL}/produtos/{produto['_id']}",
        json=produto_update_payload
    )

    assert response.status_code == 401

    body = response.json()

    assert (
        body["message"]
        == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"
    )

def test_atualizar_produto_usuario_nao_admin(
    token_usuario,
    produto_existente,
    produto_update_payload
):
    produto, _ = produto_existente

    response = requests.put(
        f"{BASE_URL}/produtos/{produto['_id']}",
        json=produto_update_payload,
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
