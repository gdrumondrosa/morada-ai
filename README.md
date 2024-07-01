# Caixa Eletrônico API

Esta API simula o funcionamento de um caixa eletrônico que recebe um valor de saque e retorna as quantidades mínimas de cédulas necessárias para compor esse valor.

## Funcionalidades

- Calcular a quantidade mínima de cédulas para um valor de saque dado.
- Endpoint `/api/saque` que recebe um valor de saque e retorna as cédulas correspondentes.

## Principais Desafios

- Implementar um algoritmo eficiente para calcular a menor quantidade de cédulas possível.
- Garantir o tratamento correto de entradas inválidas ou valores que não podem ser atendidos com as cédulas disponíveis (corner cases em que uma nota > 2 % total retorna um valor = 1 ou 3).

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado
- Flask instalado (instale com `pip install Flask`)

### Criação e ativação de um ambiente virtual
```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
```
### Passos para Executar

1. Clone o repositório:

```bash
git clone https://github.com/gdrumondrosa/morada-ai.git
```

2. Rode a aplicação:
   
```bash
python app.py
```

3. Utilize um software como Postman para realizar as requisições

### Rodar os testes

```bash
python testes.py
