
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

