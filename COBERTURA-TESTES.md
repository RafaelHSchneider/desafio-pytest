# Cobertura de Testes - Guia Completo

## O Que é Cobertura de Testes?

**Cobertura de testes** mede a porcentagem do código que é executada durante os testes.

- **0%** = Nenhuma linha é testada
- **50%** = Metade do código é testada
- **100%** = Todo o código é testado

---

## Por Que é Importante?

✅ **Identifica código não testado**
✅ **Detecta pontos fracos**
✅ **Garante qualidade**
✅ **Facilita manutenção**

---

## Ferramentas para Medir Cobertura

### 1. pytest-cov (Recomendado)
**Já está instalado** no seu projeto!

```bash
pytest --cov=<caminho> --cov-report=html
```

---

## Como Calcular Cobertura no Seu Projeto

### Passo 1: Verificar dependência

```bash
pip list | grep pytest-cov
```

**Você deve ver:**
```
pytest-cov                 7.1.0
```

### Passo 2: Rodar testes com cobertura

```bash
# Cobertura de um arquivo específico
pytest --cov=seu_arquivo tests/

# Cobertura de toda a pasta
pytest --cov=src tests/

# Cobertura em terminal
pytest --cov tests/ --cov-report=term
```

### Passo 3: Visualizar resultado

---

## Exemplos de Uso

### Exemplo 1: Cobertura de um módulo

```bash
cd c:\Users\rafae\Desktop\Desafio 1
pytest --cov=tests --cov-report=term tests/
```

**Resultado esperado:**
```
Name                                Stmts   Miss  Cover
────────────────────────────────────────────────────
tests/__init__.py                       0      0   100%
tests/conftest.py                      45     10    78%
tests/login/__init__.py                 0      0   100%
tests/login/conftest.py               15      3    80%
tests/login/test_login.py             50      5    90%
────────────────────────────────────────────────────
TOTAL                                 110     18    84%
```

### Exemplo 2: Gerar relatório HTML

```bash
pytest --cov=tests --cov-report=html tests/
```

**Cria pasta:** `htmlcov/index.html`

Abra no navegador para ver visualmente!

### Exemplo 3: Apenas testes de sucesso

```bash
pytest --cov=tests --cov-report=term-missing tests/
```

Mostra quais linhas NÃO foram executadas.

---

## Tipos de Cobertura

### 1. Line Coverage (Cobertura de Linhas)
**% de linhas de código executadas**

```python
def calcular_preco(quantidade, preco_unitario):
    total = quantidade * preco_unitario  # Linha 1
    if total > 100:                      # Linha 2
        total *= 0.9  # 10% desconto     # Linha 3
    return total                         # Linha 4
```

- 3 testes cobrindo tudo = 100% (4/4 linhas)
- 1 teste com total < 100 = 75% (3/4 linhas, linha 3 não executada)

### 2. Branch Coverage (Cobertura de Ramificações)
**% de caminhos diferentes testados**

```python
if quantidade > 10:      # Branch 1
    desconto = 0.2
else:                    # Branch 2
    desconto = 0.1
```

- Testar AMBOS os casos = 100% branch coverage
- Testar APENAS um caso = 50% branch coverage

### 3. Function Coverage (Cobertura de Funções)
**% de funções que foram testadas**

```python
def funcao_a():     # Função 1
    return 1

def funcao_b():     # Função 2
    return 2
```

- 1 teste para funcao_a = 50% (1/2 funções)
- 2 testes (um para cada) = 100% (2/2 funções)

---

## Interpretar Relatório

### Tabela de Cobertura

```
Name                 Stmts   Miss  Cover
─────────────────────────────────────────
arquivo.py             100    20   80%
```

| Coluna | Significado |
|---|---|
| **Stmts** | Total de linhas de código |
| **Miss** | Linhas NÃO testadas |
| **Cover** | Porcentagem coberta |

**Cálculo:** `Cover = (Stmts - Miss) / Stmts * 100`

**Exemplo:** `(100 - 20) / 100 * 100 = 80%`

---

## Seu Projeto - Como Medir?

### Opção 1: Cobertura por módulo

```bash
# Cobertura dos testes
pytest --cov=tests --cov-report=term-missing

# Cobertura de login
pytest --cov=tests/login tests/login/

# Cobertura de produtos
pytest --cov=tests/produtos tests/produtos/
```

### Opção 2: Relatório visual

```bash
pytest --cov=tests --cov-report=html --cov-report=term

# Abre arquivo: htmlcov/index.html
```

### Opção 3: Com filtro

```bash
# Apenas testes de schema
pytest --cov=tests -k "valida_schema" --cov-report=term

# Apenas login
pytest --cov=tests/login tests/login/ --cov-report=term
```

---

## Comandos Úteis

### Ver ajuda
```bash
pytest --cov-help
```

### Cobertura mínima exigida
```bash
pytest --cov=tests --cov-fail-under=80
```
Falha se cobertura < 80%

### Excluir arquivos
```bash
pytest --cov=tests --cov-report=term \
  --cov-report=html \
  --cov-omit="*/migrations/*" \
  tests/
```

### Estatísticas detalhadas
```bash
pytest --cov=tests \
  --cov-report=term-missing:skip-covered \
  tests/
```

---

## Metas de Cobertura

| Nível | Cobertura | Situação |
|---|---|---|
| 🟢 Excelente | 80%+ | Produção pronta |
| 🟡 Bom | 60-80% | Aceitável |
| 🟠 Médio | 40-60% | Precisa melhorar |
| 🔴 Fraco | <40% | Arriscado |

---

## Seu Projeto Atual

### Estimativa de Cobertura

**Testes implementados:**
- ✅ 12 testes de login
- ✅ 7 testes de GET /produtos
- ✅ 7 testes de GET por ID /produtos
- ✅ 7 testes de POST /produtos
- ✅ 7 testes de DELETE /produtos
- ✅ 7 testes de PUT /produtos

**Total: ~47 testes de API**

**Estimativa:** 80-85% de cobertura (alto nível)

---

## Como Rodar Agora

```bash
cd c:\Users\rafae\Desktop\Desafio 1

# Terminal
pytest --cov=tests --cov-report=term tests/

# HTML (abrir no navegador)
pytest --cov=tests --cov-report=html tests/
start htmlcov/index.html

# Com detalhes de linhas não cobertas
pytest --cov=tests --cov-report=term-missing tests/
```

---

## Exemplo Prático

### Seu projeto

```bash
pytest --cov=tests --cov-report=term tests/

# Resultado esperado:
Name                           Stmts   Miss  Cover
──────────────────────────────────────────────
tests/__init__.py                  1      0   100%
tests/conftest.py                 30      5    83%
tests/login/__init__.py             0      0   100%
tests/login/conftest.py            12      2    83%
tests/login/test_login.py          45      3    93%
tests/produtos/__init__.py          0      0   100%
tests/produtos/conftest.py         25      4    84%
tests/produtos/test_*.py          200     15    92%
tests/usuarios/__init__.py          0      0   100%
tests/usuarios/conftest.py         18      3    83%
──────────────────────────────────────────────
TOTAL                            331     32    90%
```

---

## Dicas Importantes

✅ **Cobertura alta ≠ Código perfeito**
- 100% cobertura não significa sem bugs
- Testes ruins podem ter alta cobertura

✅ **Foco no importante**
- Priorize testes em código crítico
- Ignore código trivial (getters, setters)

✅ **Manutenha atualizado**
- Atualize testes quando código muda
- Remova testes obsoletos

✅ **CI/CD**
- Integre cobertura no pipeline
- Rejeite PRs com cobertura baixa

---

## Próximos Passos

1. **Rodar cobertura agora:**
   ```bash
   pytest --cov=tests --cov-report=html tests/
   ```

2. **Analisar resultado**

3. **Identificar gaps** (código não testado)

4. **Adicionar testes** para cobrir gaps

5. **Melhorar meta** gradualmente

---

## Referências

- [pytest-cov docs](https://pytest-cov.readthedocs.io/)
- [Coverage.py docs](https://coverage.readthedocs.io/)
- [Best practices](https://docs.pytest.org/en/latest/coverage.html)
