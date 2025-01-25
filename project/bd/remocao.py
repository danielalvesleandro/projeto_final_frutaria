import logging
import random
import string
from .conexao import conectar_bd, DATABASE
from diversos.validacao import validar_id

# Função para remover cliente
def remover_cliente():
    try:
        # Coleta do ID do cliente
        while True:
            cliente_id = input("Informe o ID do cliente para remover (ou digite 'sair' para voltar): ").strip()

            if cliente_id.lower() == "sair":
                print("Retornando ao menu principal...")
                return

            if not cliente_id:
                print("O ID não pode ser vazio. Por favor, insira um valor válido.")
                continue

            valido, mensagem_erro = validar_id(cliente_id)
            if not valido:
                print(mensagem_erro)
            else:
                cliente_id = int(cliente_id)
                break

        # Remover cliente no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM clientes WHERE id = %s
        """, (cliente_id,))
        
        conn.commit()
        conn.close()

        print(f"Cliente com ID {cliente_id} removido com sucesso!")

    except Exception as e:
        # Verificar erro específico de chave estrangeira
        if "foreign key constraint fails" in str(e):
            print(f"Erro: O cliente com ID {cliente_id} não pode ser removido, pois há registros dependentes em outras tabelas.")
        else:
            logging.error(f"Erro ao remover cliente: {e}")
            print("Erro ao remover cliente.")

# Função para remover fornecedor
def remover_fornecedor():
    try:
        # Coleta do ID do fornecedor
        while True:
            fornecedor_id = input("Informe o ID do fornecedor para remover (ou digite 'sair' para voltar): ").strip()

            if fornecedor_id.lower() == "sair":
                print("Retornando ao menu principal...")
                return

            if not fornecedor_id:
                print("O ID não pode ser vazio. Por favor, insira um valor válido.")
                continue

            valido, mensagem_erro = validar_id(fornecedor_id)
            if not valido:
                print(mensagem_erro)
            else:
                fornecedor_id = int(fornecedor_id)
                break

        # Remover fornecedor no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM fornecedores WHERE id = %s
        """, (fornecedor_id,))
        
        conn.commit()
        conn.close()

        print(f"Fornecedor com ID {fornecedor_id} removido com sucesso!")

    except Exception as e:
        # Verificar erro específico de chave estrangeira
        if "foreign key constraint fails" in str(e):
            print(f"Erro: O fornecedor com ID {fornecedor_id} não pode ser removido, pois há registros dependentes em outras tabelas.")
        else:
            logging.error(f"Erro ao remover fornecedor: {e}")
            print("Erro ao remover fornecedor.")

# Função para remover produto
def remover_produto():
    try:
        # Coleta do ID do produto
        while True:
            produto_id = input("Informe o ID do produto para remover (ou digite 'sair' para voltar): ").strip()

            if produto_id.lower() == "sair":
                print("Retornando ao menu principal...")
                return

            if not produto_id:
                print("O ID não pode ser vazio. Por favor, insira um valor válido.")
                continue

            valido, mensagem_erro = validar_id(produto_id)
            if not valido:
                print(mensagem_erro)
            else:
                produto_id = int(produto_id)
                break

        # Remover produto no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM produtos WHERE id = %s
        """, (produto_id,))
        
        conn.commit()
        conn.close()

        print(f"Produto com ID {produto_id} removido com sucesso!")

    except Exception as e:
        # Verificar erro específico de chave estrangeira
        if "foreign key constraint fails" in str(e):
            print(f"Erro: O produto com ID {produto_id} não pode ser removido, pois há registros dependentes em outras tabelas.")
        else:
            logging.error(f"Erro ao remover produto: {e}")
            print("Erro ao remover produto.")
        
# Função para apagar base de dados
import random
import string
import logging
from bd.conexao import conectar_bd, DATABASE  # Certifique-se de que essas importações estão corretas

# Função para apagar base de dados
def apagar_bd():
    try:
        # Gerar código de confirmação aleatório
        temp_cod = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        # Solicitar confirmação ao usuário
        cod_confirma = input(f"Insira o código \"{temp_cod}\" se deseja mesmo apagar a base de dados. Os dados não poderão ser recuperados. "
                             "Digite 'cancelar' para abortar: ")
        
        # Verificar se o usuário deseja cancelar
        if cod_confirma.lower() == 'cancelar':
            print("Operação de remoção da base de dados cancelada.")
            return False  # Abortou a operação
        
        # Verificar se o código de confirmação está correto
        if cod_confirma == temp_cod:
            # Conectar ao servidor (não ao banco de dados específico)
            conn = conectar_bd(usar_base=False)  # Conectar sem especificar o banco de dados
            if conn:
                cursor = conn.cursor()
                # Executar o comando DROP DATABASE
                cursor.execute(f"DROP DATABASE {DATABASE}")
                conn.commit()
                conn.close()
                print(f"Base de Dados \"{DATABASE}\" apagada com sucesso!")
                return True
            else:
                print("Erro ao conectar ao banco de dados.")
                return False
        else:
            print("Código de confirmação incorreto. A base de dados não foi apagada.")
            return False
    except Exception as e:
        logging.error(f"Erro ao apagar base de dados: {e}")
        print("Erro ao apagar base de dados.")
        return False
