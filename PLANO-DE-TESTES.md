# Plano de Testes - Atualizado

## Objetivo da Suíte

Garantir que os endpoints da API de Usuários, Produtos e Login funcionem corretamente, validando operações de cadastro, consulta, atualização, exclusão e autenticação com cobertura completa de cenários de sucesso e erro.

---

## Estratégia

### Tipo de Teste
- Testes de integração REST.
- Testes funcionais das regras de negócio.
- Testes de validação de entrada e tratamento de erros.
- Testes de autenticação e autorização.
- Testes de estrutura de resposta (JSON Schema).

### Camada Testada
- Endpoints da API REST (ServerRest).

### Ferramentas e Bibliotecas
- **Python 3.12**
- **Pytest 9.1.0** - Framework de testes
- **Requests 2.34.2** - Cliente HTTP
- **jsonschema 4.21.1** - Validação de JSON Schema

### Abordagem
Cada teste implementa:
1. Configuração via fixtures (conftest.py)
2. Envio de requisição para a API
3. Validação de status code
4. Validação de estrutura (JSON Schema)
5. Validação de dados retornados
6. Cleanup automático (teardown)

---

## Escopo

### ✅ Coberto
- Autenticação (POST /login)
  - Credenciais válidas
  - Credenciais inválidas
  - Campos vazios
  - Estrutura de resposta

- Operações CRUD de usuários
  - Listar, criar, ler, atualizar, deletar
  - Validação de campos
  - Tratamento de erros
  - Casos de sucesso e erro

- Operações CRUD de produtos
  - Listar, criar, ler, atualizar, deletar
  - Autenticação obrigatória
  - Autorização (apenas admin)
  - Validação de campos
  - Tratamento de erros

---

## Cenários Implementados

### Login (12 testes)

#### POST /login ✅
- [x] Login com credenciais corretas - retorna token (200)
- [x] Login com email inválido (401)
- [x] Login com senha inválida (401)
- [x] Login com ambos inválidos (401)
- [x] Login com email vazio (400)
- [x] Login com senha vazia (400)
- [x] Login com todos os campos vazios (400)
- [x] Validação de estrutura de resposta (JSON Schema)
- [x] Token válido no formato Bearer
- [x] Validação de estrutura do token JWT

---

### Usuários (23 testes)

#### GET /usuarios ✅
- [x] Listar usuários - status 200
- [x] Retorna array de usuários
- [x] Valida estrutura da resposta
- [x] Quantidade corresponde à lista
- [x] Valida tipos de dados

#### POST /usuarios ✅
- [x] Cadastrar usuário - status 201
- [x] Retorna mensagem de sucesso
- [x] Retorna ID do usuário criado
- [x] Rejeita email duplicado - status 400

#### GET /usuarios/{id} ✅
- [x] Buscar usuário existente - status 200
- [x] Retorna dados corretos do usuário
- [x] Valida tipos de dados
- [x] Usuário inexistente - status 400
- [x] ID inválido (< 16 chars) - status 400

#### PUT /usuarios/{id} ✅
- [x] Atualizar usuário - status 200
- [x] Retorna mensagem de sucesso
- [x] PUT com ID novo cria usuário - status 201
- [x] Rejeita email duplicado - status 400

#### DELETE /usuarios/{id} ✅
- [x] Deletar usuário - status 200
- [x] Retorna mensagem de sucesso
- [x] Usuário deletado não é mais consultável
- [x] Usuário inexistente - status 200 (nenhum deletado)

---

### Produtos (33 testes)

#### GET /produtos ✅
- [x] Listar produtos - status 200
- [x] Retorna array de produtos
- [x] Valida estrutura com JSON Schema
- [x] Quantidade corresponde à lista
- [x] Valida tipos de dados

#### POST /produtos ✅
- [x] Cadastrar produto com token admin - status 201
- [x] Retorna mensagem de sucesso
- [x] Retorna ID do produto criado
- [x] Valida estrutura com JSON Schema
- [x] Rejeita nome duplicado - status 400
- [x] Sem token - status 401
- [x] Usuário não admin - status 403

#### GET /produtos/{id} ✅
- [x] Buscar produto existente - status 200
- [x] Retorna dados corretos
- [x] Valida estrutura com JSON Schema
- [x] Valida tipos de dados
- [x] Produto inexistente - status 400

#### PUT /produtos/{id} ✅
- [x] Atualizar produto com token admin - status 200
- [x] Retorna mensagem de sucesso
- [x] PUT com ID novo cria produto - status 201
- [x] Rejeita nome duplicado - status 400
- [x] Sem token - status 401
- [x] Usuário não admin - status 403

#### DELETE /produtos/{id} ✅
- [x] Deletar produto com token admin - status 200
- [x] Retorna mensagem de sucesso
- [x] Produto deletado não é mais consultável
- [x] Produto inexistente - status 200 (nenhum deletado)
- [x] Sem token - status 401
- [x] Usuário não admin - status 403
- [x] Produto em carrinho - valida comportamento

---

## Recursos Implementados

### ✅ Validação com JSON Schema
- Schemas definidos para todas as respostas
- Validação automática de estrutura
- 4 testes de schema implementados e passando

### ✅ Organização de Fixtures
- conftest.py global (admin, usuario_comum, tokens)
- conftest.py por módulo (login, produtos, usuarios)
- Sem duplicação
- Hierarquia clara

### ✅ Documentação Adicional
- COBERTURA-TESTES.md - Como calcular cobertura
- GUIA-RAPIDO-COBERTURA.md - Quick start
- FIXTURES-ORGANIZADAS.md - Estrutura de fixtures
- FIXTURES-CORRIGIDAS.md - Histórico de correções
- 2 Bug Reports criados
- Schemas em tests/schemas/

### ✅ CI/CD Ready
- pytest-cov integrado
- Relatórios HTML disponíveis
- Linting rules definidos
- Cleanup automático

---

## Critérios de Qualidade

### Um teste é considerado pronto quando:
✅ Possui nome descritivo e significativo
✅ Executa de forma independente
✅ Valida status code da resposta
✅ Valida estrutura via JSON Schema
✅ Valida dados retornados
✅ Executa sem falhas
✅ Possui fixtures adequadas
✅ Realiza cleanup automático (teardown)

### A suíte é considerada completa quando:
✅ 68 testes implementados ✅
✅ Todos os testes passando ✅
✅ Sem testes duplicados ✅
✅ Cenários de sucesso e erro cobertos ✅
✅ Autenticação testada ✅
✅ Autorização testada ✅
✅ JSON Schema validando respostas ✅
✅ Cobertura estimada 85%+ ✅

---

## Estatísticas Finais

| Métrica | Valor |
|---|---|
| Total de testes | 68 |
| Testes passando | 68 ✅ |
| Taxa de sucesso | 100% |
| Endpoints cobertos | 11 |
| Tipos de testes | 4 |
| Arquivos conftest | 4 |
| Schemas JSON | 13 |
| Bugs encontrados | 2 |
| Documentação | 20+ arquivos |

---

## Status Final

🟢 **COMPLETO E FUNCIONAL**

```
✅ Plano original: Implementado
✅ Extras adicionados: JSON Schema, Fixtures, Documentação
✅ Todos os testes: PASSANDO
✅ Código: Pronto para produção
```

---

## Mudanças desde o plano original

### Adições
- ✅ Testes de Login (novo endpoint)
- ✅ Validação com JSON Schema
- ✅ Autenticação e autorização testadas
- ✅ Campos vazios testados
- ✅ Bug reports criados
- ✅ Documentação completa

### Melhorias
- ✅ Fixtures organizadas por módulo
- ✅ Sem duplicação de código
- ✅ Testes mais descritivos
- ✅ Cobertura de erros completa
- ✅ Estrutura profissional