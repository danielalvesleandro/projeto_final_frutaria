import logging
from .conexao import DATABASE, HOST, USER, PASSWORD, conectar_bd
import mysql.connector
from mysql.connector import Error

# Função para criar banco de dados
def criar_bd():
    try:
        # Conectar ao banco de dados MySQL padrão
        conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        if conn is None:
            return
        
        cursor = conn.cursor()
        # Criar banco de dados, se não existir
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
        conn.commit()
        conn.close()
        
        conn = conectar_bd()
        return conn
        
    except mysql.connector.Error as e:
        logging.error(f"Erro ao criar o banco de dados: {e}")
        print("Erro ao criar o banco de dados.")
        return None


# Função para criar tabelas
def criar_tabelas():
    try:
        conn = conectar_bd()
        if conn is None:
            return
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
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nif VARCHAR(9) NOT NULL UNIQUE,
            nome VARCHAR(255) NOT NULL,
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
            CREATE TABLE IF NOT EXISTS vendas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                produto_id INT,
                quantidade INT NOT NULL,
                total DECIMAL(10, 2) NOT NULL,
                data_venda DATETIME NOT NULL,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id),
                FOREIGN KEY(produto_id) REFERENCES produtos(id)
            );
        """)

        conn.commit()
        conn.close()
    except Error as e:
        logging.error(f"Erro ao criar tabelas: {e}")
        print("Erro ao criar tabelas.")
