"""JSON Schemas para validação de responses de usuários"""

usuarios_list_schema = {
    "type": "object",
    "properties": {
        "quantidade": {"type": "integer", "minimum": 0},
        "usuarios": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "nome": {"type": "string"},
                    "email": {"type": "string", "format": "email"},
                    "password": {"type": "string"},
                    "administrador": {"type": "string"}
                },
                "required": ["_id", "nome", "email", "password", "administrador"]
            }
        }
    },
    "required": ["quantidade", "usuarios"]
}

usuario_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "nome": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string"},
        "administrador": {"type": "string"}
    },
    "required": ["_id", "nome", "email", "password", "administrador"]
}


usuario_criado_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["_id", "message"]
}

mensagem_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}

erro_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}
