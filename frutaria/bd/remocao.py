import logging
from .conexao import conectar_bd

# Função para remover cliente
def remover_cliente():
    try:
        cliente_id = int(input("Digite o ID do cliente que deseja remover: "))
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        conn.commit()
        conn.close()
        print(f"Cliente com ID {cliente_id} removido com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao remover cliente: {e}")
        print("Erro ao remover cliente.")

# Função para remover fornecedor
def remover_fornecedor():
    try:
        fornecedor_id = int(input("Digite o ID do fornecedor que deseja remover: "))
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM fornecedor WHERE id = %s", (fornecedor_id,))
        conn.commit()
        conn.close()
        print(f"Fornecedor com ID {fornecedor_id} removido com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao remover fornecedor: {e}")
        print("Erro ao remover fornecedor.")

# Função para remover produto
def remover_produto():
    try:
        produto_id = int(input("Digite o ID do produto que deseja remover: "))
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
        conn.commit()
        conn.close()
        print(f"Produto com ID {produto_id} removido com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao remover produto: {e}")
        print("Erro ao remover produto.")