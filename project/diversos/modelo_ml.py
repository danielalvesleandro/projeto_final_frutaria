import pandas as pd
from bd.conexao import conectar_bd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Para evitar problemas no WSL
import matplotlib.pyplot as plt
import uuid

# Função para carregar dados do banco de dados
def carregar_dados():
    conexao = conectar_bd()
    cursor = conexao.cursor(dictionary=True)

    # Consultar as tabelas de vendas, clientes e produtos
    query = """
        SELECT 
            v.id AS venda_id,
            c.nif AS cliente_nif,
            p.categoria AS produto_categoria,
            v.quantidade,
            v.total
        FROM vendas v
        INNER JOIN clientes c ON v.cliente_id = c.id
        INNER JOIN produtos p ON v.produto_id = p.id;
    """
    cursor.execute(query)
    dados = cursor.fetchall()

    # Fechar conexão
    cursor.close()
    conexao.close()

    # Converter para DataFrame
    df = pd.DataFrame(dados)
    return df

# Função para treinar e avaliar modelos de aprendizado de máquina
def carregar_modelo_ml():
    # Carregar os dados do banco
    data = carregar_dados()
    print("Dados carregados do banco de dados:\n", data.head())

    # Variáveis independentes (X) e dependente (y)
    X = data[['cliente_nif', 'produto_categoria', 'quantidade']]
    y = data['total']

    # Converter variáveis categóricas para numéricas
    X = pd.get_dummies(X, columns=['cliente_nif', 'produto_categoria'], drop_first=True)

    print(f"Forma dos dados (X, y): {data.shape}")
    print(f"Dados de entrada (X):\n{X.head()}")

    # Dividir em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    print(f"Tamanho dos conjuntos de treino e teste: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Modelos a serem treinados (modelos de regressão)
    modelos = {
        "Linear Regression": LinearRegression(),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=42),
        "KNN Regressor": KNeighborsRegressor(n_neighbors=5)
    }

    resultados = []

    # Treinar e avaliar cada modelo
    for nome, modelo in modelos.items():
        try:
            print(f"Treinando o modelo: {nome}")
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)

            # Avaliar o modelo
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            print(f"Mean Squared Error - {nome}: {mse}")
            print(f"R2 Score - {nome}: {r2}")
            resultados.append((nome, r2))
        except Exception as e:
            print(f"Erro ao treinar o modelo {nome}: {e}")

    # Visualizar resultados
    if resultados:
        modelos_nome = [r[0] for r in resultados]
        r2_scores = [r[1] for r in resultados]

        sns.barplot(x=modelos_nome, y=r2_scores)

        plt.title('Comparação de R2 dos Modelos')
        plt.ylabel('R2 Score')
        plt.xlabel('Modelos')
        random_suffix = uuid.uuid4().hex[:8]  # You can adjust the length
        plt.savefig(f"png/comparacao_modelos_{random_suffix}.png", format="png")
    else:
        print("Nenhum modelo treinado com sucesso.")

if __name__ == "__main__":
    carregar_modelo_ml()
