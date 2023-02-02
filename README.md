# Crypto Finance API
![check-code-coverage](https://img.shields.io/badge/code--coverage-100%25-brightgreen)

API para cadastrar usuários e suas criptomoeadas escolhidas em um banco SQLite. Guardando as seguintes informações:

    - USER_ID
    - NAME
    - CRIPTO
    - SYMBOL
    - VALOR MIN DIA ANTERIOR
    - VALOR MAX DIA ANTERIOR
    - DATA

API utilizada: https://www.mercadobitcoin.com.br/api-doc/

# Endpoints

## Register

- Create
- Update
- Delete

## Fetch

- Pega informações do banco de dados (Read)

## Get coin

- Pega informações únicas sobre uma criptomoeada específica.

em `rest_api/src/infra/coins.yml` você encontra as abreviações de cada cripto aceita.

# ESTRUTURA

```
.
├── coverage
│   └── coverage.json
├── cov_html
│   ├── coverage_html.js
│   ├── d_a44f0ac069e85531___init___py.html
│   ├── d_a44f0ac069e85531_test_consumer_py.html
│   ├── favicon_32.png
│   ├── index.html
│   ├── keybd_closed.png
│   ├── keybd_open.png
│   ├── status.json
│   └── style.css
├── db.sqlite
├── get_coverage.sh
├── install.sh
├── README.md
├── src
│   ├── api
│   │   ├── endpoints
│   │   │   ├── fetch.py
│   │   │   ├── get_coin.py
│   │   │   ├── __init__.py
│   │   │   └── register.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── get_response_model.py
│   │   │   ├── __init__.py
│   │   │   ├── resgister_response_model.py
│   │   │   └── user.py
│   │   └── routers.py
│   ├── domain
│   │   ├── __init__.py
│   │   └── interfaces
│   │       ├── consumer.py
│   │       ├── db.py
│   │       └── __init__.py
│   ├── infra
│   │   ├── coins.yml
│   │   ├── consumer.py
│   │   ├── __init__.py
│   │   └── sqlitedb.py
│   ├── __init__.py
│   └── main.py
├── tests
│   ├── __init__.py
│   └── test_consumer.py
└── utils
    ├── get_coverage.py
    └── __init__.py
```