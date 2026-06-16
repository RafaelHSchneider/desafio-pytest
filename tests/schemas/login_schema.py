"""JSON Schemas para validação de responses de login"""

login_sucesso_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "authorization": {"type": "string", "pattern": "^Bearer .+$"}
    },
    "required": ["message", "authorization"]
}

login_erro_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}

erro_validacao_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}
