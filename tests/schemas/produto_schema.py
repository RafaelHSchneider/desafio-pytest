"""JSON Schemas para validação de responses de produtos"""

produtos_list_schema = {
    "type": "object",
    "properties": {
        "quantidade": {"type": "integer", "minimum": 0},
        "produtos": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "nome": {"type": "string"},
                    "preco": {"type": "integer", "minimum": 0},
                    "descricao": {"type": "string"},
                    "quantidade": {"type": "integer", "minimum": 0}
                },
                "required": ["_id", "nome", "preco", "descricao", "quantidade"]
            }
        }
    },
    "required": ["quantidade", "produtos"]
}

produto_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "nome": {"type": "string"},
        "preco": {"type": "integer", "minimum": 0},
        "descricao": {"type": "string"},
        "quantidade": {"type": "integer", "minimum": 0}
    },
    "required": ["_id", "nome", "preco", "descricao", "quantidade"]
}

produto_criado_schema = {
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
