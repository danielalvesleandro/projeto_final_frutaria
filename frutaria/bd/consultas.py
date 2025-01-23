import logging
from .conexao import conectar_bd
from mysql.connector import Error

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
        else:
            for cliente in clientes:
                print(f"ID: {cliente[0]}, NIF: {cliente[1]}, Nome: {cliente[2]} {cliente[3]}, Telefone: {cliente[4]}, Email: {cliente[5]}, Endereço: {cliente[6]}")

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
            for fornecedor in fornecedores:
                print(f"ID: {fornecedor[0]}, NIF: {fornecedor[1]}, Nome: {fornecedor[2]} {fornecedor[3]}, Telefone: {fornecedor[4]}, Email: {fornecedor[5]}, Endereço: {fornecedor[6]}")

        return fornecedores
    except Error as e:
        logging.error(f"Erro de banco de dados ao consultar fornecedor: {e}")
        print("Erro de banco de dados ao consultar fornecedor.")
    except Exception as e:
        logging.error(f"Erro ao consultar fornecedor: {e}")
        print("Erro ao consultar fornecedor.")
        
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
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Categoria: {produto[2]}, Preço: {produto[3]}, Quantidade: {produto[4]}")

        return produtos
    except Error as e:
        logging.error(f"Erro de banco de dados ao consultar produto: {e}")
        print("Erro de banco de dados ao consultar produto.")
    except Exception as e:
        logging.error(f"Erro ao consultar produto: {e}")
        print("Erro ao consultar produto.")