import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import MinMaxScaler
from tabulate import tabulate

def conectar_bd():
    engine = create_engine('mysql+mysqlconnector://root:@localhost/frutaria')
    return engine

# Função para carregar dados de uma tabela do banco
def carregar_dados_tabela(tabela):
    engine = conectar_bd()
    query = f"SELECT * FROM {tabela}"
    df = pd.read_sql_query(query, engine)
    return df

# Função para tratar valores ausentes
def tratar_valores_ausentes(df):
    # Verificar se há valores ausentes em cada coluna
    for coluna in df.columns:
        if df[coluna].isnull().sum() > 0:
            print(f"Valores ausentes na coluna {coluna} antes da limpeza: {df[coluna].isnull().sum()}")

            # Verificar se a coluna tem valores válidos para calcular a moda
            if not df[coluna].mode().empty:
                # Substituir valores ausentes pela moda da coluna
                moda = df[coluna].mode().iloc[0]  # Pegando a moda (valor mais frequente)
                df[coluna].fillna(moda, inplace=True)
            else:
                # Caso não haja moda (por exemplo, todos os valores são diferentes ou a coluna tem apenas NaNs)
                print(f"A coluna {coluna} não possui moda. Substituindo valores ausentes por 'Desconhecido'.")
                df[coluna].fillna("Desconhecido", inplace=True)  # Valor padrão de fallback
    return df

# Função para remover duplicatas
def remover_duplicatas(df, tabela):
    # Definir colunas relevantes para verificar duplicatas baseado no tipo de tabela
    colunas_relevantes = {
        'clientes': ['nome', 'sobrenome', 'email'],
        'fornecedores': ['nif'],
        'produtos': ['nome'],
        'vendas': ['cliente_id', 'produto_id', 'quantidade', 'total', 'data_venda'],
    }

    # Verificar se a tabela tem colunas definidas
    if tabela not in colunas_relevantes:
        raise ValueError(f"Colunas para a tabela '{tabela}' não estão configuradas.")

    # Obter colunas para o tipo de tabela
    subset_cols = colunas_relevantes[tabela]

    # Verificar se as colunas existem no DataFrame
    missing_cols = [col for col in subset_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f"As colunas {missing_cols} estão ausentes no DataFrame da tabela '{tabela}'.")

    # Verificar duplicatas
    print(f"Colunas disponíveis no DataFrame: {list(df.columns)}")
    print(f"Quantidade de duplicatas antes: {df.duplicated(subset=subset_cols).sum()}")

    # Remover duplicatas com base nas colunas definidas
    df = df.drop_duplicates(subset=subset_cols, keep='first')  # Mantenha a primeira ocorrência

    # Verificar duplicatas após a remoção
    print(f"Quantidade de duplicatas após: {df.duplicated(subset=subset_cols).sum()}")

    return df


# Função para tratar dados inconsistentes
def tratar_dados_inconsistentes(df):
    # Exemplo: Verificar se as colunas numéricas não possuem valores negativos
    if 'preco' in df.columns:
        df = df[df['preco'] >= 0]  # Remover registros com preços negativos

    if 'quantidade' in df.columns:
        df = df[df['quantidade'] >= 0]  # Remover registros com quantidades negativas

    # Exemplo: Verificar se as colunas de data estão no formato correto
    if 'data_venda' in df.columns:
        df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')  # Converte para datetime, com erro em caso de dados inválidos

    return df

# Função para normalizar os dados (exemplo de normalização Min-Max)
def normalizar_dados(df):
    # Verifique se as colunas 'preco' e 'quantidade' existem e têm dados
    if 'preco' in df.columns and df['preco'].notnull().any():
        scaler = MinMaxScaler()
        df['preco'] = scaler.fit_transform(df[['preco']])

    if 'quantidade' in df.columns and df['quantidade'].notnull().any():
        scaler = MinMaxScaler()
        df['quantidade'] = scaler.fit_transform(df[['quantidade']])

    return df

# Função para carregar e limpar os dados do banco de dados
def carregar_e_limpar_dados(tabela):
    # Conectar ao banco de dados e carregar os dados
    df = carregar_dados_tabela(tabela)

    # Tratamento de valores ausentes
    df = tratar_valores_ausentes(df)

    # Remover duplicatas
    try:
        df = remover_duplicatas(df, tabela)
    except (KeyError, ValueError) as e:
        print(f"Erro ao remover duplicatas na tabela '{tabela}': {e}")

    # Tratar dados inconsistentes
    df = tratar_dados_inconsistentes(df)

    return df

def rotina_de_limpeza():
    # Carregar e limpar os dados de clientes
    dados_clientes_limpo = carregar_e_limpar_dados('clientes')

    # Visualizar os dados limpos
    print("Dados de Clientes Limpos:")
    headers = ["ID", "NIF", "Nome", "Sobrenome", "Telefone", "Email", "Endereço"]
    print(tabulate(dados_clientes_limpo.head(), headers=headers, tablefmt="fancy_grid"))
    print("\n")

    # Carregar e limpar os dados de fornecedores
    dados_fornecedores_limpo = carregar_e_limpar_dados('fornecedores')

    # Visualizar os dados limpos
    print("Dados de Fornecedores Limpos:")
    headers = ["ID", "NIF", "Nome", "Telefone", "Email", "Endereço"]
    print(tabulate(dados_fornecedores_limpo.head(), headers=headers, tablefmt="fancy_grid"))
    print("\n")
    
    # Carregar e limpar os dados de produtos
    dados_produtos_limpo = carregar_e_limpar_dados('produtos')

    # Visualizar os dados limpos
    print("Dados de Produtos Limpos:")
    headers = ["ID", "Nome", "Categoria", "Preço", "Quantidade"]
    print(tabulate(dados_produtos_limpo.head(), headers=headers, tablefmt="fancy_grid"))
    print("\n")
      
    # Carregar e limpar os dados de vendas
    dados_vendas_limpo = carregar_e_limpar_dados('vendas')

    # Visualizar os dados limpos
    print("Dados de Vendas Limpos:")
    headers = ["ID", "Nome", "Categoria", "Preço", "Quantidade"]
    print(tabulate(dados_vendas_limpo.head(), headers=headers, tablefmt="fancy_grid"))
    print("\n")