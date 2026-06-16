"""Fixtures para testes de login"""

import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


@pytest.fixture
def login_response(usuario_comum):
    """Response de login com usuário comum"""
    _, payload = usuario_comum
    
    return requests.post(
        f"{BASE_URL}/login",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )


