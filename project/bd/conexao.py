import mysql.connector
import logging
from sqlalchemy import create_engine

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'frutaria'

# Função para conectar ao banco de dados (sem especificar uma base específica)
def conectar_bd(usar_base=True):
    try:
        # Conectar ao servidor MySQL (sem base de dados especificada)
        conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        
        if conn.is_connected():
            if usar_base:
                cursor = conn.cursor()
                cursor.execute(f"USE {DATABASE}")
            return conn
        else:
            return None
    except mysql.connector.Error as e:
        logging.error(f"Erro ao conectar à base de dados: {e}")
        print("Erro ao conectar à base de dados.")
        return None

    
# Função para conectar ao banco de dados via sqlalchemy
def conectar_bd_sqlalchemy(DATABASE):
    engine = create_engine('mysql+mysqlconnector://root:@localhost/{DATABASE}')
    return engine