# Plano de Testes

## Objetivo da Suíte

Garantir que os endpoints da API de Usuários e Produtos funcionem corretamente, validando operações de cadastro, consulta, atualização e exclusão de registros.

---

## Estratégia

### Tipo de Teste
- Testes de integração.
- Testes funcionais das regras de negócio expostas pelos endpoints.
- Testes de validação de entrada e tratamento de erros.

### Camada Testada
- Endpoints da API REST.

### Ferramentas
- Python
- Pytest
- Requests

### Abordagem
Cada teste deverá:
1. Enviar uma requisição para a API.
2. Validar o código de resposta (status code).
3. Verificar os dados retornados pela API.

---

## Escopo

### Coberto
- Cadastro de usuários.
- Consulta de usuários.
- Atualização de usuários.
- Exclusão de usuários.
- Cadastro de produtos.
- Consulta de produtos.
- Atualização de produtos.
- Exclusão de produtos.
- Tratamento de registros inexistentes.



---

## Cenários a Implementar

### Usuários

#### GET /usuarios
- Listar usuários cadastrados.

#### POST /usuarios
- Cadastrar usuário com dados válidos.
- Tentar cadastrar usuário com dados inválidos.

#### GET /usuarios/{id}
- Buscar usuário existente.
- Buscar usuário inexistente.

#### PUT /usuarios/{id}
- Atualizar usuário existente.
- Tentar atualizar usuário inexistente.

#### DELETE /usuarios/{id}
- Excluir usuário existente.
- Tentar excluir usuário inexistente.

---

### Produtos

#### GET /produtos
- Listar produtos cadastrados.

#### POST /produtos
- Cadastrar produto com dados válidos.
- Tentar cadastrar produto com dados inválidos.

#### GET /produtos/{id}
- Buscar produto existente.
- Buscar produto inexistente.

#### PUT /produtos/{id}
- Atualizar produto existente.
- Tentar atualizar produto inexistente.

#### DELETE /produtos/{id}
- Excluir produto existente.
- Tentar excluir produto inexistente.

---

## Critérios de Qualidade

Um teste será considerado pronto quando:

- Possuir nome descritivo.
- Executar de forma independente.
- Validar o status code da resposta.
- Validar os dados retornados pela API.
- Executar sem falhas.

A suíte será considerada concluída quando:

- Todos os cenários planejados estiverem implementados.
- Todos os testes estiverem passando.
- Não houver testes duplicados.
- Os principais fluxos de sucesso e erro estiverem cobertos.