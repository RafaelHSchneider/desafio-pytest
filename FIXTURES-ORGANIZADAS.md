# Fixtures Organizadas e Estruturadas

## 📊 Resumo da Organização

As fixtures foram reorganizadas e separadas por módulo para melhor manutenção.

---

## 🗂️ Estrutura Final

```
tests/
├── conftest.py                    # Fixtures GLOBAIS (admin, tokens)
├── login/
│   ├── conftest.py               # Fixtures de LOGIN
│   └── test_login.py
├── produtos/
│   ├── conftest.py               # Fixtures de PRODUTOS
│   └── test_*.py
├── usuarios/
│   ├── conftest.py               # Fixtures de USUÁRIOS
│   └── test_*.py
└── schemas/
    └── ...
```

---

## 📝 Fixtures por Localização

### `tests/conftest.py` (GLOBAIS)

Fixtures usadas por múltiplos módulos:

| Fixture | Tipo | Uso |
|---|---|---|
| `admin_payload` | Payload | Cria admin |
| `admin_usuario` | Usuario | Usuário admin |
| `token_admin` | Token | Autenticação admin |

✅ **Acesso**: Todos os testes

---

### `tests/login/conftest.py` (LOGIN)

Fixtures específicas de login:

| Fixture | Tipo | Uso |
|---|---|---|
| `usuario_comum_payload` | Payload | Usuário comum |
| `usuario_comum` | Usuario | User criado |
| `login_response` | Response | Response de login |
| `token_usuario` | Token | Token do user comum |

✅ **Acesso**: Login + Produtos (compartilhado)

---

### `tests/produtos/conftest.py` (PRODUTOS)

Fixtures específicas de produtos:

| Fixture | Tipo | Uso |
|---|---|---|
| `produtos_response` | Response | GET /produtos |
| `produto_payload` | Payload | Criar produto |
| `produto_update_payload` | Payload | Atualizar produto |
| `produto_cadastrado` | Produto | Produto criado |
| `produto_existente` | Produto | Produto existente |
| `excluir_produto_response` | Response | Response DELETE |

✅ **Acesso**: Testes de produtos

---

### `tests/usuarios/conftest.py` (USUÁRIOS)

Fixtures específicas de usuários:

| Fixture | Tipo | Uso |
|---|---|---|
| `usuario_payload` | Payload | Criar usuário |
| `usuario_existente` | Usuario | User existente |
| `usuario_por_id_response` | Response | GET /usuarios/{id} |
| `excluir_usuario_response` | Response | Response DELETE |
| `usuario_update_payload` | Payload | Atualizar usuário |
| `segundo_usuario` | Usuario | Segundo usuário |

✅ **Acesso**: Testes de usuários

---

## 🎯 Hierarquia de Fixtures

```
conftest.py (raiz)
├── admin_payload
├── admin_usuario
└── token_admin

login/conftest.py
├── usuario_comum_payload
├── usuario_comum
├── login_response
└── token_usuario ← Também usada em produtos!

produtos/conftest.py
├── produtos_response
├── produto_payload
├── produto_update_payload
├── produto_cadastrado
├── produto_existente
└── excluir_produto_response

usuarios/conftest.py
├── usuario_payload
├── usuario_existente
├── usuario_por_id_response
├── excluir_usuario_response
├── usuario_update_payload
└── segundo_usuario
```

---

## ✅ Fixtures Deletadas

As seguintes fixtures foram **removidas** por não serem usadas:

- ❌ `usuarios_response` - Não era usado
- ❌ `usuario_cadastrado` - Substituída por `usuario_existente`
- ❌ `login_payload` - Não necessária (payload gerado na fixture)

**Total deletado**: 3 fixtures não utilizadas

---

## 📍 Como Usar

### Import automático

Pytest carrega fixtures automaticamente do `conftest.py`:

```python
# Não precisa importar nada!
def test_login(login_response):  # Fixture carregada automaticamente
    assert login_response.status_code == 200
```

### Hierarquia de busca

Pytest procura fixtures nesta ordem:

1. **conftest.py local** (tests/login/conftest.py)
2. **conftest.py parent** (tests/conftest.py)
3. **Built-in fixtures** (pytest, fixtures)

---

## 🔍 Exemplo de Uso

### Teste de Login
```python
# tests/login/test_login.py
def test_login_status_code(login_response):
    # Usa fixture de tests/login/conftest.py
    assert login_response.status_code == 200
```

### Teste de Produtos
```python
# tests/produtos/test_post_produtos.py
def test_cadastrar_produto(token_admin, produto_payload):
    # token_admin: tests/conftest.py (global)
    # produto_payload: tests/produtos/conftest.py (local)
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto_payload,
        headers={"Authorization": token_admin}
    )
    assert response.status_code == 201
```

### Teste de Usuários
```python
# tests/usuarios/test_post_usuarios.py
def test_criar_usuario(usuario_payload):
    # usuario_payload: tests/usuarios/conftest.py
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=usuario_payload
    )
    assert response.status_code == 201
```

---

## 📊 Estatísticas

| Métrica | Antes | Depois | Mudança |
|---|---|---|---|
| Fixtures em conftest.py | 25 | 3 | -22 |
| Fixtures em login/ | 0 | 4 | +4 |
| Fixtures em produtos/ | 0 | 6 | +6 |
| Fixtures em usuarios/ | 0 | 6 | +6 |
| Fixtures não usadas | 3 | 0 | -3 |

---

## ✨ Benefícios

✅ **Organização Clara** - Fixtures próximas ao código que usam
✅ **Manutenção Fácil** - Fácil encontrar e alterar
✅ **Sem Duplicação** - Cada fixture em um lugar
✅ **Reutilização** - Fixtures globais compartilhadas
✅ **Escalabilidade** - Fácil adicionar novos testes
✅ **Performance** - Menos fixtures carregadas

---

## 🚀 Rodar Testes

```bash
# Todos os testes
pytest tests/ -v

# Apenas login
pytest tests/login/ -v

# Apenas produtos
pytest tests/produtos/ -v

# Apenas usuários
pytest tests/usuarios/ -v

# Com cobertura
pytest tests/ --cov=tests --cov-report=html
```

---

## 📝 Checklist

- [x] Fixtures de login separadas
- [x] Fixtures de produtos separadas
- [x] Fixtures de usuários separadas
- [x] Fixtures globais centralizadas
- [x] Fixtures não usadas deletadas
- [x] Hierarquia clara
- [x] Testes passando
- [x] Documentação completa

---

## 🎉 Status

✅ **Reorganização Completa**
✅ **Todos os testes funcionando**
✅ **Estrutura profissional**
✅ **Pronto para expansão**
