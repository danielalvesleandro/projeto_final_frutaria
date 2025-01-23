import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def conectar_bd():
    engine = create_engine('mysql+mysqlconnector://root:@localhost/frutaria')
    return engine

# Função para carregar dados de uma tabela do banco
def carregar_dados_tabela(tabela):
    engine = conectar_bd()
    query = f"SELECT * FROM {tabela}"
    df = pd.read_sql_query(query, engine)
    return df

# Função para carregar dados do estoque
def carregar_estoque():
    df = carregar_dados_tabela('estoque')
   
    # Exibe as colunas do DataFrame para depuração
    print("Colunas do DataFrame de estoque:", df.columns)

    # Verificar se a coluna 'id_produto' existe
    if 'id_produto' in df.columns and 'quantidade' in df.columns:
        return df[['id_produto', 'quantidade', 'preco']]
    else:
        print("Erro: Colunas 'id_produto' e/ou 'quantidade' não encontradas.")
        return pd.DataFrame()  # Retorna um DataFrame vazio caso as colunas não sejam encontradas

# Função para carregar dados de vendas
def carregar_vendas():
    return carregar_dados_tabela('vendas').groupby(['data_venda', 'produto_nome'])['quantidade'].sum().reset_index()

# Visualizações
df_estoque = carregar_estoque()

# Verifique se o DataFrame foi carregado corretamente
if not df_estoque.empty:
    fig_estoque = px.bar(df_estoque, x='id_produto', y='quantidade', title="Quantidade de Produtos no Estoque")
else:
    fig_estoque = {}

df_vendas = carregar_vendas()
fig_vendas = px.line(df_vendas, x='data_venda', y='quantidade', title="Vendas ao Longo do Tempo")

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do Dash
app.layout = html.Div([
    html.H1("Dashboard Frutaria"),
    dcc.Dropdown(
        id='dropdown_produtos',
        options=[{'label': produto, 'value': produto} for produto in df_estoque['id_produto'].unique()],
        multi=True,
        placeholder="Selecione os produtos"
    ),
    dcc.Graph(id='grafico_estoque'),
    dcc.Graph(id='grafico_vendas'),
])

# Função para atualizar o gráfico de estoque com base nos produtos selecionados
@app.callback(
    Output('grafico_estoque', 'figure'),
    [Input('dropdown_produtos', 'value')]
)
def update_estoque(produtos_selecionados):
    if produtos_selecionados:
        df_estoque_filtrado = df_estoque[df_estoque['id_produto'].isin(produtos_selecionados)]
        fig_estoque = px.bar(df_estoque_filtrado, x='id_produto', y='quantidade', color='preco',
                             title="Quantidade de Produtos no Estoque")
    else:
        fig_estoque = px.bar(df_estoque, x='id_produto', y='quantidade', color='preco',
                             title="Quantidade de Produtos no Estoque")
    return fig_estoque

# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)

