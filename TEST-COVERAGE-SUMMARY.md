# Resumo de Cobertura de Testes

## Login (11 testes)
Arquivo: `tests/login/test_login.py`

### Cenários Implementados:
- ✅ **Credenciais corretas**: Login com sucesso (status 200, retorna token)
  - `test_login_status_code`
  - `test_login_retorna_json`
  - `test_login_retorna_mensagem`
  - `test_login_retorna_token`

- ✅ **Senha errada**: Falha com status 401
  - `test_login_com_senha_invalida`

- ✅ **Email inexistente**: Falha com status 401
  - `test_login_com_email_invalido`

- ✅ **Campos vazios**: Falha com validação (status 400)
  - `test_login_com_campos_vazios`
  - `test_login_com_email_vazio`
  - `test_login_com_senha_vazia`

- ✅ **Outros**: Validação adicional
  - `test_login_com_email_e_senha_invalidos`
  - `test_token_expira_em_10_minutos`

---

## Produtos (30 testes)

### 1. **Listar Produtos** - 5 testes ✅
Arquivo: `tests/produtos/test_get_produtos.py`
- `test_listar_produtos_status_code` - Status 200
- `test_listar_produtos_retorna_json` - Content-Type
- `test_listar_produtos_retorna_campos_principais` - Campos quantidade e produtos
- `test_listar_produtos_quantidade_corresponde_lista` - Validação de contagem
- `test_listar_produtos_tipos_campos_produto` - Tipos de dados

### 2. **Cadastrar Produto** - 5 testes ✅
Arquivo: `tests/produtos/test_post_produtos.py`
- `test_cadastrar_produto_status_code` - Status 201
- `test_cadastrar_produto_retorna_mensagem` - Mensagem de sucesso
- `test_cadastrar_produto_retorna_id` - Retorna _id
- `test_cadastrar_produto_nome_duplicado` - Erro 400 com nome duplicado
- `test_cadastrar_produto_sem_token` - Erro 401 sem token (admin)
- `test_cadastrar_produto_usuario_nao_admin` - Erro 403 usuário comum

### 3. **Buscar Produto por ID** - 5 testes ✅
Arquivo: `tests/produtos/test_get_produto_por_id.py`
- `test_buscar_produto_por_id_status_code` - Status 200
- `test_buscar_produto_por_id_retorna_json` - Content-Type
- `test_buscar_produto_por_id_retorna_campos_principais` - Campos obrigatórios
- `test_buscar_produto_por_id_tipos_campos` - Tipos de dados
- `test_buscar_produto_por_id_nao_encontrado` - ID inexistente retorna 400

### 4. **Atualizar Produto (PUT)** - 7 testes ✅
Arquivo: `tests/produtos/test_put_produto.py`
- `test_atualizar_produto_existente_status_code` - Status 200
- `test_atualizar_produto_existente_retorna_mensagem` - Mensagem de sucesso
- `test_put_com_id_inexistente_cria_produto` - PUT com ID novo cria novo produto (201)
- `test_atualizar_produto_com_nome_ja_cadastrado` - Erro 400 nome duplicado
- `test_atualizar_produto_sem_token` - Erro 401 sem token (admin)
- `test_atualizar_produto_usuario_nao_admin` - Erro 403 usuário comum

### 5. **Excluir Produto (DELETE)** - 7 testes ✅
Arquivo: `tests/produtos/test_delete_produto.py`
- `test_excluir_produto_status_code` - Status 200
- `test_excluir_produto_retorna_mensagem_sucesso` - Mensagem de sucesso
- `test_excluir_produto_inexistente` - ID inexistente retorna "Nenhum registro excluído"
- `test_produto_excluido_nao_pode_ser_consultado` - Validação após delete
- `test_excluir_produto_sem_token` - Erro 401 sem token (admin)
- `test_excluir_produto_usuario_nao_admin` - Erro 403 usuário comum
- `test_excluir_produto_em_carrinho` - Validação para produto em carrinho

---

## Resumo Executivo

| Funcionalidade | Testes | Status |
|---|---|---|
| Login | 11 | ✅ Completo |
| Produtos - Listar | 5 | ✅ Completo |
| Produtos - Cadastrar | 6 | ✅ Completo |
| Produtos - Buscar por ID | 5 | ✅ Completo |
| Produtos - Atualizar | 6 | ✅ Completo |
| Produtos - Excluir | 7 | ✅ Completo |
| **TOTAL** | **41** | ✅ **Completo** |

---

## Fixtures Utilizadas (conftest.py)

- `usuarios_response` - GET /usuarios
- `usuario_payload` - Payload para criar usuário
- `usuario_cadastrado` - Cria e limpa usuário (POST)
- `usuario_existente` - Cria usuário com teardown manual
- `usuario_por_id_response` - GET /usuarios/{id}
- `excluir_usuario_response` - DELETE /usuarios/{id}
- `usuario_update_payload` - Payload para atualizar usuário
- `segundo_usuario` - Cria segundo usuário para testes
- `admin_payload` - Payload admin
- `admin_usuario` - Cria usuário admin
- `token_admin` - Token de administrador
- `produto_payload` - Payload para criar produto
- `produto_cadastrado` - Cria e limpa produto
- `produto_existente` - Cria produto com teardown manual
- `excluir_produto_response` - DELETE /produtos/{id}
- `produto_update_payload` - Payload para atualizar produto
- `usuario_comum_payload` - Payload usuário comum
- `usuario_comum` - Cria usuário comum
- `token_usuario` - Token de usuário comum
- `login_payload` - Payload para login
- `login_response` - POST /login

---

## Princípios Seguidos

1. **Padrão Consistente**: Todos os testes seguem a mesma estrutura
2. **Fixtures Reutilizáveis**: Fixtures compartilhadas em conftest.py
3. **Cleanup Automático**: Teardown implementado para limpar dados de teste
4. **Cenários Negativos**: Testes para erros (401, 403, 400)
5. **Validação Completa**: Status code, headers, payload e tipos de dados
