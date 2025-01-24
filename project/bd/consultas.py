import logging
from .conexao import conectar_bd
from mysql.connector import Error
from tabulate import tabulate

# Função para consultar clientes
def consultar_clientes():
    try:
        conn = conectar_bd()
        if conn is None:
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()

        if not clientes:
            print("Não há clientes cadastrados.")
            print("\n")
        else:
            # Definir os cabeçalhos das colunas
            headers = ["ID", "NIF", "Nome", "Sobrenome", "Telefone", "Email", "Endereço"]
            # Utilizar tabulate para formatar a lista de clientes em tabela
            print(tabulate(clientes, headers=headers, tablefmt="fancy_grid"))
            print("\n")
                
        return clientes
    except Error as e:
        logging.error(f"Erro de banco de dados ao consultar clientes: {e}")
        print("Erro de banco de dados ao consultar clientes.")
    except Exception as e:
        logging.error(f"Erro ao consultar clientes: {e}")
        print("Erro ao consultar clientes.")


# Função para consultar fornecedores
def consultar_fornecedores():
    try:
        conn = conectar_bd()
        if conn is None:
            return
    
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fornecedor")
        fornecedores = cursor.fetchall()
        conn.close()
        
        if not fornecedores:
            print("Não há fornecedores cadastrados.")
        else:
            # Definir os cabeçalhos das colunas
            headers = ["ID", "NIF", "Nome", "Sobrenome", "Telefone", "Email", "Endereço"]
            # Utilizar tabulate para formatar a lista de fornecedores em tabela
            print(tabulate(fornecedores, headers=headers, tablefmt="fancy_grid"))
            print("\n")
                
        return fornecedores
    except Error as e:
        logging.error(f"Erro de banco de dados ao consultar fornecedores: {e}")
        print("Erro de banco de dados ao consultar fornecedores.")
    except Exception as e:
        logging.error(f"Erro ao consultar fornecedores: {e}")
        print("Erro ao consultar fornecedores.")
        
# Função para consultar produtos
def consultar_produtos():
    try:
        conn = conectar_bd()
        if conn is None:
            return
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        conn.close()

        if not produtos:
            print("Não há produtos cadastrados.")
        else:
            # Definir os cabeçalhos das colunas
            headers = ["ID", "Nome", "Categoria", "Preço", "Quantidade"]
            # Utilizar tabulate para formatar a lista de produtos em tabela
            print(tabulate(produtos, headers=headers, tablefmt="fancy_grid"))
            print("\n")
                
        return produtos
    except Error as e:
        logging.error(f"Erro de banco de dados ao consultar produtos: {e}")
        print("Erro de banco de dados ao consultar produtos.")
    except Exception as e:
        logging.error(f"Erro ao consultar produtos: {e}")
        print("Erro ao consultar produtos.")
