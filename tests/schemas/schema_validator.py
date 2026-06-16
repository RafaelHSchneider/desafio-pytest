"""Helper para validar JSON Schemas"""

import json
from jsonschema import validate, ValidationError


class SchemaValidator:
    """Classe para validar respostas contra JSON Schemas"""
    
    @staticmethod
    def validate(response_data, schema):
        """
        Valida dados contra um schema JSON
        
        Args:
            response_data: Dados a validar (dict)
            schema: Schema JSON (dict)
            
        Returns:
            bool: True se válido
            
        Raises:
            ValidationError: Se a validação falhar
        """
        try:
            validate(instance=response_data, schema=schema)
            return True
        except ValidationError as e:
            raise AssertionError(
                f"Schema validation failed:\n"
                f"Error: {e.message}\n"
                f"Path: {'.'.join(str(p) for p in e.path)}\n"
                f"Schema: {json.dumps(schema, indent=2)}"
            )
    
    @staticmethod
    def validate_response(response, schema):
        """
        Valida response JSON contra um schema
        
        Args:
            response: Response object do requests
            schema: Schema JSON (dict)
            
        Returns:
            bool: True se válido
        """
        try:
            data = response.json()
            return SchemaValidator.validate(data, schema)
        except json.JSONDecodeError as e:
            raise AssertionError(f"Response is not valid JSON: {e}")
