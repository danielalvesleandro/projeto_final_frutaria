import logging
from .conexao import DATABASE, conectar_bd
from mysql.connector import Error

# Função para criar banco de dados
def criar_bd():
    try:
        conn = conectar_bd()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
        conn.commit()
        conn.close()
        print(f"Banco de dados {DATABASE} criado ou já existente.")
    except Error as e:
        logging.error(f"Erro ao criar o banco de dados: {e}")
        print("Erro ao criar o banco de dados.")

# Função para criar tabelas
def criar_tabelas():
    try:
        conn = conectar_bd()
        if conn is None:
            return  # Se a conexão falhar, não prosseguir
        cursor = conn.cursor()

        # Criação das tabelas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nif VARCHAR(9) NOT NULL UNIQUE,
            nome VARCHAR(255) NOT NULL,
            sobrenome VARCHAR(255) NOT NULL,
            telefone VARCHAR(15) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            endereco TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fornecedor (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nif VARCHAR(9) NOT NULL UNIQUE,
            nome VARCHAR(255) NOT NULL,
            sobrenome VARCHAR(255) NOT NULL,
            telefone VARCHAR(15) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            endereco TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            categoria VARCHAR(255) NOT NULL,
            preco DECIMAL(10, 2) NOT NULL,
            quantidade INT NOT NULL
        );
        """)

        cursor.execute("""    
        CREATE TABLE IF NOT EXISTS estoque (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_produto INT NOT NULL,
            quantidade INT NOT NULL,
            preco DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (id_produto) REFERENCES produtos(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cliente_id INT,
            produto_nome VARCHAR(255) NOT NULL,
            quantidade INT NOT NULL,
            total DECIMAL(10, 2) NOT NULL,
            data_venda DATETIME NOT NULL,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        );
        """)

        conn.commit()
        conn.close()
        print("Tabelas criadas com sucesso!")
    except Error as e:
        logging.error(f"Erro ao criar tabelas: {e}")
        print("Erro ao criar tabelas.")
