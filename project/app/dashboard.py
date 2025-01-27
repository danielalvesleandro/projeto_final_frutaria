from sqlalchemy import create_engine
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

def conectar_bd():
    engine = create_engine('mysql+mysqlconnector://root:@localhost/frutaria')
    return engine

def carregar_quantidades():
    try:
        engine = conectar_bd()
        clientes = pd.read_sql_query("SELECT COUNT(*) FROM clientes", engine).iloc[0, 0]
        fornecedores = pd.read_sql_query("SELECT COUNT(*) FROM fornecedores", engine).iloc[0, 0]
        produtos = pd.read_sql_query("SELECT COUNT(*) FROM produtos", engine).iloc[0, 0]
        return clientes, fornecedores, produtos
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return 0, 0, 0

def carregar_top_5_clientes():
    try:
        engine = conectar_bd()
        df_vendas = pd.read_sql_query("SELECT * FROM vendas", engine)
        df_vendas_cliente = df_vendas.groupby('cliente_id')['quantidade'].sum().reset_index()
        df_top_5_clientes = df_vendas_cliente.sort_values(by='quantidade', ascending=False).head(5)
        
        # Carregar os dados dos clientes (nome e sobrenome)
        df_clientes = pd.read_sql_query("SELECT id, nome, sobrenome FROM clientes", engine)
        df_top_5_clientes = df_top_5_clientes.merge(df_clientes, left_on='cliente_id', right_on='id', how='left')
        
        return df_top_5_clientes[['cliente_id', 'nome', 'sobrenome', 'quantidade']]
    except Exception as e:
        print(f"Erro ao carregar os 5 clientes que mais compraram: {e}")
        return pd.DataFrame()

def carregar_top_20_vendas():
    try:
        engine = conectar_bd()
        df_vendas = pd.read_sql_query("SELECT * FROM vendas", engine)
        df_vendas['total'] = df_vendas['quantidade'] * df_vendas['produto_id'].map(
            lambda x: pd.read_sql_query(f"SELECT preco FROM produtos WHERE id = {x}", engine).iloc[0, 0] if pd.notna(x) else 0)
        df_top_20_vendas = df_vendas.sort_values(by='total', ascending=False).head(20)
        return df_top_20_vendas[['id', 'cliente_id', 'produto_id', 'quantidade', 'total']]
    except Exception as e:
        print(f"Erro ao carregar as 20 vendas com maior valor total: {e}")
        return pd.DataFrame()

clientes_count, fornecedores_count, produtos_count = carregar_quantidades()
df_top_5_clientes = carregar_top_5_clientes()
df_top_20_vendas = carregar_top_20_vendas()

fig_quantidades = px.bar(
    x=["Clientes", "Fornecedores", "Produtos"],
    y=[clientes_count, fornecedores_count, produtos_count],
    title="Quantidade de Clientes, Fornecedores e Produtos"
)

fig_top_5_clientes = px.bar(
    df_top_5_clientes, 
    x='cliente_id', 
    y='quantidade', 
    color='quantidade', 
    text=df_top_5_clientes['nome'] + ' ' + df_top_5_clientes['sobrenome'],
    title="Top 5 Clientes que Mais Compraram"
)

fig_top_20_vendas = px.bar(
    df_top_20_vendas, 
    x='id', 
    y='total', 
    color='total', 
    title="Top 20 Vendas com Maior Valor Total"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Frutaria"),
    dcc.Graph(id='grafico_quantidades', figure=fig_quantidades),
    dcc.Graph(id='grafico_top_5_clientes', figure=fig_top_5_clientes),
    dcc.Graph(id='grafico_top_20_vendas', figure=fig_top_20_vendas),
])

def carregar_dashboard():
    app.run_server(host="0.0.0.0", port=9050, debug=True, use_reloader=False)

if __name__ == "__main__":
    carregar_dashboard()