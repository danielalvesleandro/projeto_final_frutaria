from datetime import datetime
import pandas as pd
from .conexao import conectar_bd

# Função para registrar venda
def registrar_venda(cliente_id, produto_id, quantidade):
    conn = conectar_bd()
    cursor = conn.cursor()

    # Consultar o estoque do produtos para obter o nome e o preço
    cursor.execute("SELECT nome, quantidade, preco FROM produtos WHERE id = %s", (produto_id,))
    produto = cursor.fetchone()

    if produto and produto[1] >= quantidade:  # produto[1] é a quantidade em estoque
        total = produto[2] * quantidade  # produto[2] é o preço
        data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Inserir venda
        cursor.execute("INSERT INTO vendas (cliente_id, produto_id, quantidade, total, data_venda) "
                       "VALUES (%s, %s, %s, %s, %s, %s)",
                       (cliente_id, produto_id, produto[0], quantidade, total, data_venda))  # produto[0] é o nome

        # Atualizar estoque
        nova_quantidade = produto[1] - quantidade
        cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s", (nova_quantidade, produto_id))

        conn.commit()
        print("Venda registrada com sucesso!")
    else:
        print("Produto insuficiente em estoque ou produto não encontrado!")

    conn.close()


# Função para carregar dados de uma tabela do banco
def carregar_dados_tabela(tabela):
    engine = conectar_bd()
    query = f"SELECT * FROM {tabela}"
    df = pd.read_sql_query(query, engine)
    return df

# Função para carregar dados do estoque
def carregar_produtos():
    df = carregar_dados_tabela('produtos')
   
    # Exibe as colunas do DataFrame para depuração
    print("Colunas do DataFrame de produtos:", df.columns)

    # Verificar se a coluna 'id' existe
    if 'id' in df.columns and 'quantidade' in df.columns:
        return df[['id', 'quantidade', 'preco']]
    else:
        print("Erro: Colunas 'id' e/ou 'quantidade' não encontradas.")
        return pd.DataFrame()  # Retorna um DataFrame vazio caso as colunas não sejam encontradas

# Função para carregar dados de vendas
def carregar_vendas():
    return carregar_dados_tabela('vendas').groupby(['data_venda', 'produto_id'])['quantidade'].sum().reset_index()