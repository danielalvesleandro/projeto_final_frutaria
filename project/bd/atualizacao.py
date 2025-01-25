import logging
from .conexao import conectar_bd
from diversos.validacao import validar_id, validar_nome, validar_categoria, validar_preco, validar_quantidade, validar_email, validar_endereco, validar_nif, validar_telefone

# Função para atualizar produto
def atualizar_produto():
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
       
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE produtos
        SET nome = %s, categoria = %s, preco = %s, quantidade = %s
        WHERE id = %s
        """, (nome, categoria, preco, quantidade))
        conn.commit()
        conn.close()
        print(f"Produto {nome} com ID {id} atualizado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao atualizar produto: {e}")
        print("Erro ao atualizar produto.")

# Função para atualizar cliente
def atualizar_cliente():
    try:
        # Coleta e validação do ID do cliente
        while True:
            cliente_id = input("Informe o ID do cliente para atualizar (ou digite 'sair' para voltar): ").strip()

            if not cliente_id:
                print("O ID não pode ser vazio. Por favor, insira um valor válido.")
                continue
                        
            if cliente_id.lower() == "sair":
                print("Operação cancelada pelo usuário.")
                return
            
            valido, mensagem_erro = validar_id(cliente_id)
            if not valido:
                print(mensagem_erro)
            else:
                cliente_id = int(cliente_id)
                break

        # Coleta e validação dos dados do cliente                
        while True:
            nif = input("Digite o NIF do cliente: ").strip()
            valido, mensagem_erro = validar_nif(nif)
            if valido:
                break
            else:
                print(mensagem_erro)
                
        while True:
            nome = input("Digite o nome do cliente: ").strip()
            valido, mensagem_erro = validar_nome(nome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            sobrenome = input("Digite o sobrenome do cliente: ").strip()
            valido, mensagem_erro = validar_nome(sobrenome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            telefone = input("Digite o telefone do cliente (somente números, 9 dígitos): ").strip()
            valido, mensagem_erro = validar_telefone(telefone)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            email = input("Digite o email do cliente: ").strip()
            valido, mensagem_erro = validar_email(email)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            endereco = input("Digite o endereço do cliente: ").strip()
            valido, mensagem_erro = validar_endereco(endereco)
            if valido:
                break
            else:
                print(mensagem_erro)

        # Atualização no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE clientes
        SET nome = %s, sobrenome = %s, telefone = %s, email = %s, endereco = %s
        WHERE id = %s
        """, (nome, sobrenome, telefone, email, endereco, cliente_id))
        conn.commit()
        conn.close()
        
        print(f"Cliente com ID {cliente_id} atualizado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao atualizar cliente: {e}")
        print("Erro ao atualizar cliente.")

# Função para atualizar fornecedor
def atualizar_fornecedor():
    try:
        # Coleta e validação do ID do fornecedor
        while True:
            fornecedor_id = input("Informe o ID do fornecedor para atualizar (ou digite 'sair' para voltar): ").strip()

            if not fornecedor_id:
                print("O ID não pode ser vazio. Por favor, insira um valor válido.")
                continue

            if fornecedor_id.lower() == "sair":
                print("Operação cancelada pelo usuário.")
                return
            
            valido, mensagem_erro = validar_id(fornecedor_id)
            if not valido:
                print(mensagem_erro)
            else:
                fornecedor_id = int(fornecedor_id)
                break

        # Coleta e validação dos dados do fornecedor                
        while True:
            nif = input("Digite o NIF do fornecedor: ").strip()
            valido, mensagem_erro = validar_nif(nif)
            if valido:
                break
            else:
                print(mensagem_erro)
                
        while True:
            nome = input("Digite o nome do fornecedor: ").strip()
            valido, mensagem_erro = validar_nome(nome)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            telefone = input("Digite o telefone do fornecedor (somente números, 9 dígitos): ").strip()
            valido, mensagem_erro = validar_telefone(telefone)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            email = input("Digite o email do fornecedor: ").strip()
            valido, mensagem_erro = validar_email(email)
            if valido:
                break
            else:
                print(mensagem_erro)

        while True:
            endereco = input("Digite o endereço do fornecedor: ").strip()
            valido, mensagem_erro = validar_endereco(endereco)
            if valido:
                break
            else:
                print(mensagem_erro)

        # Atualização no banco de dados
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE fornecedores
        SET nif = %s, nome = %s, telefone = %s, email = %s, endereco = %s
        WHERE id = %s
        """, (nif, nome, telefone, email, endereco, fornecedor_id))
        conn.commit()
        conn.close()
        
        print(f"Fornecedor com ID {fornecedor_id} atualizado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao atualizar fornecedor: {e}")
        print("Erro ao atualizar fornecedor.")
