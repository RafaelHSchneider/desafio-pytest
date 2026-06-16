# Guia Rápido: Calcular Cobertura de Testes

## ⚡ 3 Passos

### Passo 1: Rodar com cobertura
```bash
pytest --cov=tests --cov-report=term tests/
```

### Passo 2: Ver resultado no terminal
```
Name                        Stmts   Miss  Cover
─────────────────────────────────────────────
tests/login/test_login.py      57      0   100%
tests/produtos/test_*.py      200     15    92%
─────────────────────────────────────────────
TOTAL                         350     35    90%
```

### Passo 3: Gerar relatório visual (opcional)
```bash
pytest --cov=tests --cov-report=html tests/
start htmlcov/index.html
```

---

## 📊 Entender Resultado

```
Name                  Stmts   Miss  Cover
──────────────────────────────────────────
arquivo.py             100    10   90%
```

- **Stmts** = 100 linhas de código
- **Miss** = 10 linhas não testadas
- **Cover** = 90% coberto

**Fórmula:** `(Stmts - Miss) / Stmts * 100 = Cover`

---

## 🎯 Comandos Úteis

| Comando | Resultado |
|---|---|
| `pytest --cov=tests --cov-report=term` | Terminal simples |
| `pytest --cov=tests --cov-report=term-missing` | Mostra linhas não cobertas |
| `pytest --cov=tests --cov-report=html` | Relatório visual HTML |
| `pytest --cov=tests --cov-fail-under=80` | Falha se < 80% |

---

## 🚀 Rodar Agora

```bash
# Seu projeto
cd c:\Users\rafae\Desktop\Desafio 1

# Cobertura de todos os testes
pytest --cov=tests --cov-report=term-missing tests/

# Apenas login
pytest --cov=tests/login --cov-report=term tests/login/

# Gerar HTML
pytest --cov=tests --cov-report=html tests/
```

---

## 💡 Dicas

✅ Term-missing = Mostra exatamente quais linhas faltam
✅ HTML = Abra no navegador para análise visual
✅ Fail-under = Configure no CI/CD para rejeitar PRs

---

## 📚 Mais Info

Ver: `COBERTURA-TESTES.md` para guia completo
