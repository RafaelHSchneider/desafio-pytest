import pytest
import requests

BASE_URL = "https://compassuol.serverest.dev"

@pytest.fixture
def usuarios_response():
    return requests.get(f"{BASE_URL}/usuarios")

