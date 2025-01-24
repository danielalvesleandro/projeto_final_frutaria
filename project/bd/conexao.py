import mysql.connector
import logging
from sqlalchemy import create_engine

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'frutaria'

def conectar_bd():
    try:
        # Conectar ao banco de dados "mysql" para garantir a conexão
        conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        if conn.is_connected():
            print(f"Conectado ao MySQL com sucesso!")
            
            cursor = conn.cursor()
            cursor.execute(f"USE {DATABASE}")
            return conn
        else:
            return None
    except mysql.connector.Error as e:
        logging.error(f"Erro ao conectar ao banco de dados: {e}")
        print("Erro ao conectar ao banco de dados.")
        return None

    
# Função para conectar ao banco de dados via sqlalchemy
def conectar_bd_sqlalchemy():
    engine = create_engine('mysql+mysqlconnector://root:@localhost/{DATABASE}}')
    return engine