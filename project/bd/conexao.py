import mysql.connector
import logging

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'frutaria'

def conectar_bd():
    try:
        conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        if conn.is_connected():
            print(f"Conectado ao banco de dados {DATABASE} com sucesso!")
            return conn
        else:
            return None
    except mysql.connector.Error as e:
        logging.error(f"Erro ao conectar ao banco de dados: {e}")
        print("Erro ao conectar ao banco de dados.")
        return None