# Relatório de Cobertura de Testes de API (Swagger / ServeRest)

Este documento apresenta os resultados da cobertura de testes com base nos endpoints mapeados da API (Login, Usuários, Produtos e Carrinhos).

## 📊 Resumo Executivo

- **Método de Cálculo Utilizado:** *Status Code Coverage (Output)*
- **Status Codes Testados:** 28 de 38
- **Cobertura Total Atingida:** **73.68%**

---

## 🛠️ Método de Cálculo da Cobertura

O cálculo de cobertura foi realizado utilizando a abordagem de **Status Code Coverage (Output)**. Este método avalia a eficácia dos testes com base nas respostas (HTTP Status Codes) possíveis que a API pode retornar para cada endpoint mapeado, em vez de avaliar apenas as rotas isoladamente.

### Fórmula Utilizada:
Cobertura (%) = (Status Codes Testados / Total de Status Codes Possíveis) * 100


Esta abordagem garante que cenários de sucesso (ex: `200 OK`, `201 Created`), erros de validação do cliente (ex: `400 Bad Request`, `401 Unauthorized`) e erros de negócio tenham sido validados conforme a especificação da API.

---

## 🔍 Mapeamento de Escopo por Módulo

Com base na especificação visual da API, os seguintes módulos e operações compõem o escopo de validação:

1. **Login**
   - `POST /login` - Realizar login
2. **Usuários**
   - `GET /usuarios` - Listar usuários cadastrados
   - `POST /usuarios` - Cadastrar usuário
   - `GET /usuarios/{_id}` - Buscar usuário por ID
   - `DELETE /usuarios/{_id}` - Excluir usuário
   - `PUT /usuarios/{_id}` - Editar usuário
3. **Produtos**
   - `GET /produtos` - Listar produtos cadastrados
   - `POST /produtos` - Cadastrar produto *(Requer Autenticação)*
   - `GET /produtos/{_id}` - Buscar produto por ID
   - `DELETE /produtos/{_id}` - Excluir produto *(Requer Autenticação)*
   - `PUT /produtos/{_id}` - Editar produto *(Requer Autenticação)*

---

## 🚫 Cenários Fora de Escopo (Não Testados)

### 🛒 Módulo: Carrinhos
Os endpoints listados abaixo pertencentes ao módulo de **Carrinhos** não foram incluídos na bateria de testes automatizados:

- `GET /carrinhos` - Listar carrinhos cadastrados
- `POST /carrinhos` - Cadastrar carrinho
- `GET /carrinhos/{_id}` - Buscar carrinho por ID
- `DELETE /carrinhos/concluir-compra` - Excluir carrinho / Concluir compra
- `DELETE /carrinhos/cancelar-compra` - Excluir carrinho e retornar produtos para estoque

### 💡 Justificativa:
Estes cenários e endpoints específicos ficaram fora do escopo de validação técnica pois não foram especificados no descritivo do desafio.