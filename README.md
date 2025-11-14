# Lilian-Farina---Accenture---API

DemoQA API Automation — Python + BDD + Page Object

Este projeto automatiza o fluxo de criação de usuário, autenticação, listagem de livros e reserva de dois livros utilizando as APIs públicas do DemoQA.

A automação é construída em Python, utilizando BDD, padrão de projeto Page Object aplicado para APIs, testes automatizados contínuos via GitHub Actions e arquitetura limpa.

📚 Funcionalidades Automatizadas

Este projeto executa todo o fluxo completo em uma única execução:



Criar um usuário
Endpoint: POST /Account/v1/User

Gerar token de acesso
Endpoint: POST /Account/v1/GenerateToken

Confirmar autorização do usuário
Endpoint: POST /Account/v1/Authorized

Listar livros disponíveis
Endpoint: GET /BookStore/v1/Books

Reservar dois livros
Endpoint: POST /BookStore/v1/Books

Listar detalhes do usuário com os livros reservados
Endpoint: GET /Account/v1/User/{userID}

🏗️ Arquitetura do Projeto
demoqa-api-automation/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/ci.yml
├── features/
│   ├── create_and_reserve_books.feature
│   └── environment.py
├── steps/
│   └── steps_api.py
├── src/
│   ├── api_client.py
│   ├── services/
│   │   └── bookstore_service.py
│   └── utils/
│       └── helpers.py

📌 Tecnologias utilizadas

Python 3.11

Behave (BDD)

Requests (chamadas HTTP)

Page Object aplicado em camada Service

Python-dotenv

GitHub Actions (CI)

🧪 Como Executar Localmente


1️⃣ Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Executar o cenário BDD
behave

📄 BDD — Cenário Principal
cenario: Criar usuário, gerar token, reservar 2 livros e verificar detalhes
    Given que eu gero um username e password aleatórios
    When eu crio o usuário no sistema
    And eu gero um token para o usuário
    Then o usuário deve estar autorizado
    When eu recupero a lista de livros disponíveis
    And eu escolho 2 livros e os adiciono à conta do usuário
    Then ao recuperar os detalhes do usuário, devo ver os 2 livros reservados

🤖 Integração Contínua (CI) — GitHub Actions

Pipeline automático rodando os testes em cada push ou pull request:

.github/workflows/ci.yml

name: BDD API Tests
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install deps
        run: |
          pip install -r requirements.txt
      - name: Run BDD tests
        run: behave -f pretty

🧱 Padrões de Projeto
🔹 Page Object aplicado a APIs

Mesmo sem interface web, utilizamos o Page Object para organizar a automação:

api_client.py → Cliente HTTP genérico

services/ → “Páginas” que representam grupos de endpoints

steps_api.py → Executa as ações usando serviços

helpers → Geração de dados dinâmicos

Isso gera reutilização, fácil manutenção e desacoplamento.



Projeto desenvolvido como parte de desafio técnico envolvendo API + BDD + Python + Padrões de Projeto.

Resumo do fluxo do teste:

Criar usuário — POST /Account/v1/User. 
demoqa.com

Gerar token — POST /Account/v1/GenerateToken. 
demoqa.com

Verificar autorização — POST /Account/v1/Authorized (ou GET conforme doc). 
demoqa.com

Listar livros — GET /BookStore/v1/Books. 
demoqa.com

Reservar / adicionar livros ao usuário — POST /BookStore/v1/Books com userId + collectionOfIsbns. 
demoqa.com

Ler detalhes do usuário — GET /Account/v1/User/{userId} e confirmar livros associados. 
demoqa.com

Observação: verificar no Swagger os nomes exatos dos campos (userId / userID, isbn, formato do token, headers exigidos). O Swagger oficial: https://demoqa.com/swagger/


especificação da API do DemoQA, que está descrita no Swagger/OpenAPI, para modelar os endpoints no projeto.

Essa documentação define os recursos: /Account/v1/User, /Account/v1/GenerateToken, /Account/v1/Authorized, /BookStore/v1/Books, /Account/v1/User/{userId}....

 “Swagger UI”  disponibilizado para  API de BookStore.

Pré-requisitos

Acesso à internet (p.ex. para https://demoqa.com)

curl ou Postman para testes manuais

Python 3.11+ (recomendado) e pip para execução automatizada

Dependências (ex.: requests, behave, python-dotenv) — see requirements.txt
