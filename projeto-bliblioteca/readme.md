# Sistema de Biblioteca em Python 📚

Projeto desenvolvido em Python para praticar conceitos de Programação Orientada a Objetos (POO), organização de código em múltiplos arquivos e manipulação de dados.

## 📌 Sobre o projeto

O sistema simula uma biblioteca simples onde é possível cadastrar leitores, adicionar livros e realizar empréstimos.

O projeto foi dividido em diferentes classes para facilitar a organização e manutenção do código.

## 🚀 Funcionalidades

### 👤 Cadastro de leitores
Permite criar leitores com:

- Nome
- Idade

A classe `Leitor` utiliza herança da classe `Pessoa`.

### 📚 Cadastro de livros
Permite adicionar livros contendo:

- Título
- Autor
- Status de empréstimo

### 🔄 Empréstimo de livros
O sistema verifica se o livro está disponível e permite realizar o empréstimo.

Caso o livro já esteja emprestado, o sistema informa que ele não está disponível.

### ↩️ Devolução de livros
Possui uma função para devolver livros cadastrados na biblioteca.

### 💾 Salvamento dos dados
Os dados da biblioteca são convertidos para dicionários e salvos em um arquivo JSON utilizando o módulo `json`.

## 🏗️ Estrutura do projeto


biblioteca-python/
│
├── main.py
├── biblioteca.py
├── livro.py
├── pessoa.py
└── main.json


## 🧩 Classes utilizadas

### Pessoa

Classe base responsável pelos dados dos usuários.

Atributos:

- `nome`
- `idade`

---

### Leitor

Classe que herda de `Pessoa`.

Representa uma pessoa que pode utilizar a biblioteca.

---

### Livro

Representa um livro da biblioteca.

Atributos:

- `titulo`
- `autor`
- `emprestado`

---

### Biblioteca

Classe responsável pelo gerenciamento:

- Lista de livros
- Lista de leitores
- Empréstimos
- Devoluções
- Conversão dos dados para JSON

## 🛠️ Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos
- JSON
- pathlib

## 📚 Conceitos praticados

Durante o desenvolvimento foram utilizados:

- Classes e objetos
- Herança
- Métodos especiais (`__init__`, `__repr__`)
- Listas
- Dicionários
- Manipulação de arquivos
- Serialização de dados com JSON
- Organização de projetos Python

## ▶️ Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO