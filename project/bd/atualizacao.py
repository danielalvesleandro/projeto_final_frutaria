import logging
from .conexao import conectar_bd
from validacoes import validar_nome, validar_categoria, validar_preco, validar_quantidade

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
