import logging
from .conexao import conectar_bd
from diversos.validacao import validar_nome, validar_email, validar_telefone, validar_nif, validar_categoria, validar_preco, validar_quantidade, validar_endereco
from mysql.connector import IntegrityError

# Função para inserir cliente com validações de entradas
def inserir_cliente():
    try:
        # Coleta e validação dos dados do cliente
        while True:
            nome = input("Digite o nome do cliente: ")
            valido, mensagem_erro = validar_nome(nome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            sobrenome = input("Digite o sobrenome do cliente: ")
            valido, mensagem_erro = validar_nome(sobrenome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            nif = input("Digite o NIF do cliente (9 dígitos, ex: 123456789): ")
            valido, mensagem_erro = validar_nif(nif)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            email = input("Digite o email do cliente: ")
            valido, mensagem_erro = validar_email(email)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            telefone = input("Digite o telefone do cliente (apenas números, ex: 912345678): ")
            valido, mensagem_erro = validar_telefone(telefone)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            endereco = input("Digite o endereço do cliente: ")
            valido, mensagem_erro = validar_endereco(endereco)
            if valido:
                break
            else:
                print(mensagem_erro)

        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nif, nome, sobrenome, telefone, email, endereco) VALUES (%s, %s, %s, %s, %s, %s)",
                       (nif, nome, sobrenome, telefone, email, endereco))
        conn.commit()
        conn.close()

        print("Cliente registrado com sucesso!")
    except IntegrityError:
        logging.error("Erro: NIF ou e-mail duplicado ao registrar cliente.")
        print("Erro: O NIF ou o e-mail já está registrado.")
    except Exception as e:
        logging.error(f"Erro ao registrar cliente: {e}")
        print("Erro ao registrar cliente.")

# Função para inserir produto com validações de entradas
def inserir_produto():
    try:
        # Coleta e validação dos dados do produto
        while True:
            nome = input("Digite o nome do produto: ")
            valido, mensagem_erro = validar_nome(nome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            categoria = input("Digite a categoria do produto: ")
            valido, mensagem_erro = validar_categoria(categoria)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            preco = input("Digite o preço do produto (ex: 10.50): ")
            valido, mensagem_erro = validar_preco(preco)
            if valido:
                preco = float(preco)
                break
            else:
                print(mensagem_erro)

        while True:
            quantidade = input("Digite a quantidade do produto: ")
            valido, mensagem_erro = validar_quantidade(quantidade)
            if valido:
                quantidade = int(quantidade)
                break
            else:
                print(mensagem_erro)

        # Conectando ao banco de dados e inserindo o produto
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                       (nome, categoria, preco, quantidade))
        conn.commit()
        conn.close()

        print("Produto registrado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao registrar produto: {e}")
        print("Erro ao registrar produto.")
        
# Função para inserir fornecedor com validações de entradas
def inserir_fornecedor():
    try:

        # Coleta e validação dos dados do fornecedor
        while True:
            nome = input("Digite o nome do fornecedor: ")
            valido, mensagem_erro = validar_nome(nome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            sobrenome = input("Digite o sobrenome do fornecedor: ")
            valido, mensagem_erro = validar_nome(sobrenome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            nif = input("Digite o NIF do fornecedor (9 dígitos, ex: 123456789): ")
            valido, mensagem_erro = validar_nif(nif)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            email = input("Digite o email do fornecedor: ")
            valido, mensagem_erro = validar_email(email)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            telefone = input("Digite o telefone do fornecedor (apenas números, ex: 912345678): ")
            valido, mensagem_erro = validar_telefone(telefone)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            endereco = input("Digite o endereço do fornecedor: ")
            valido, mensagem_erro = validar_endereco(endereco)
            if valido:
                break
            else:
                print(mensagem_erro)

        # Conectando ao banco de dados e inserindo o fornecedor
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO fornecedor (nif, nome, sobrenome, telefone, email, endereco) VALUES (%s, %s, %s, %s, %s, %s)",
                       (nif, nome, sobrenome, telefone, email, endereco)) 
        conn.commit()
        conn.close()

        print("Fornecedor registrado com sucesso!")
    except IntegrityError:
        logging.error("Erro: NIF ou e-mail duplicado ao registrar fornecedor.")
        print("Erro: O NIF ou o e-mail já está registrado.")
    except Exception as e:
        logging.error(f"Erro ao registrar fornecedor: {e}")
        print("Erro ao registrar fornecedor.")