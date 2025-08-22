# 📝 Projeto Flask com Session e Dicionário como Banco de Dados

Este projeto é uma aplicação web simples feita com **Flask**, utilizando a funcionalidade de **session** para controle de usuário e um **dicionário em memória** como banco de dados.  

O objetivo principal é **praticar os fundamentos do Flask** e **manipulação de dados sem depender de um banco de dados real**, focando no aprendizado.

---

## 🚀 Como Rodar Localmente

### 1️⃣ Clonar o repositório
git clone https://github.com/seuusuario/projeto_carrinho_flask.git  
cd projeto_carrinho_flask

### 2️⃣ Criar e ativar o ambiente virtual
**No Linux:**  
- python3 -m venv venv  
- source venv/bin/activate  

**No Windows:**  
- python -m venv venv  
- venv\Scripts\activate  

### 3️⃣ Instalar dependências
O projeto já possui o arquivo `requirements.txt` com todas as bibliotecas necessárias:  
- pip install -r requirements.txt  

### 4️⃣ Rodar a aplicação
- python app.py  

Por padrão, o Flask roda em:  
👉 http://127.0.0.1:5000  

---

## ⚙️ Tecnologias Utilizadas
- Python 3  
- Flask  
- Session (do Flask)  
- Dicionário em memória (simulando banco de dados)  
- HTML5 / CSS3  

---

## 📚 Estrutura do Projeto
│-- app.py # Código principal da aplicação Flask

│-- templates/ # Páginas HTML com Jinja2

│-- static/ # Arquivos CSS e recursos estáticos

│-- requirements.txt # Dependências do projeto

│-- README.md # Documentação


## 🛠️ Funcionalidades
- Registro de usuário (armazenado em dicionário Python).  
- Login e autenticação usando **session**.  
- Logout com remoção da sessão.  
- Exibição de dados do usuário logado.  

---

## 📝 Observação
Como o banco de dados é um simples **dicionário em memória**, todos os dados são apagados sempre que o servidor Flask é reiniciado.  
Este projeto foi feito **apenas para estudo** e não deve ser usado em produção.

---

✍️ Desenvolvido por **Flauber Sauan Candido Alves e Alan Pereira da Silva**