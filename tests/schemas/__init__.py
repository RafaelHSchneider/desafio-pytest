"""Schemas para validação JSON"""

from .usuario_schema import (
    usuarios_list_schema,
    usuario_schema,
    usuario_criado_schema,
    mensagem_schema,
    erro_schema
)

from .produto_schema import (
    produtos_list_schema,
    produto_schema,
    produto_criado_schema
)

from .login_schema import (
    login_sucesso_schema,
    login_erro_schema,
    erro_validacao_schema
)

from .schema_validator import SchemaValidator

__all__ = [
    "usuarios_list_schema",
    "usuario_schema",
    "usuario_criado_schema",
    "mensagem_schema",
    "erro_schema",
    "produtos_list_schema",
    "produto_schema",
    "produto_criado_schema",
    "login_sucesso_schema",
    "login_erro_schema",
    "erro_validacao_schema",
    "SchemaValidator"
]
