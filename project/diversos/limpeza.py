import pandas as pd
from bd.conexao import conectar_bd_sqlalchemy
from sklearn.preprocessing import MinMaxScaler

# Função para carregar dados de uma tabela do banco
def carregar_dados_tabela(tabela):
    engine = conectar_bd_sqlalchemy()
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
def remover_duplicatas(df):
    # Verificando duplicatas
    print(f"Quantidade de duplicatas antes: {df.duplicated().sum()}")
    df.drop_duplicates(inplace=True)
    print(f"Quantidade de duplicatas após: {df.duplicated().sum()}")
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
    df = remover_duplicatas(df)

    # Tratar dados inconsistentes
    df = tratar_dados_inconsistentes(df)

    # Opcionalmente normalizar os dados (se necessário)
    df = normalizar_dados(df)

    return df

# Carregar e limpar os dados de estoque
df_estoque_limpo = carregar_e_limpar_dados('estoque')

# Carregar e limpar os dados de vendas
df_vendas_limpo = carregar_e_limpar_dados('vendas')

# Visualizar os dados limpos
print("Dados de Estoque Limpos:")
print(df_estoque_limpo.head())  # Verifique as primeiras linhas do DataFrame
print(df_estoque_limpo.info())  # Verifique o tipo e quantidade de dados em cada coluna

print("Dados de Vendas Limpos:")
print(df_vendas_limpo.head())  # Verifique as primeiras linhas do DataFrame
print(df_vendas_limpo.info())  # Verifique o tipo e quantidade de dados em cada coluna