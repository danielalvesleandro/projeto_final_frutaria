import pandas as pd
from bd.conexao import conectar_bd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# Função para carregar dados do banco de dados
# def carregar_dados():
#     conexao = conectar_bd()
#     cursor = conexao.cursor(dictionary=True)

#     # Consultar as tabelas de vendas, clientes e produtos
#     query = """
#         SELECT 
#             v.id AS venda_id,
#             c.nif AS cliente_nif,
#             p.categoria AS produto_categoria,
#             v.quantidade,
#             v.total
#         FROM vendas v
#         INNER JOIN clientes c ON v.cliente_id = c.id
#         INNER JOIN produtos p ON v.produto_id = p.id;
#     """
#     cursor.execute(query)
#     dados = cursor.fetchall()

#     # Fechar conexão
#     cursor.close()
#     conexao.close()

#     # Converter para DataFrame
#     df = pd.DataFrame(dados)
#     return df

# # Função para treinar e avaliar modelos de aprendizado de máquina
# def carregar_modelo_ml():
#     # Carregar os dados do banco
#     data = carregar_dados()
#     print("Dados carregados do banco de dados:\n", data.head())

#     # Variáveis independentes (X) e dependente (y)
#     X = data[['cliente_nif', 'produto_categoria', 'quantidade']]
#     y = data['total']

#     # Converter variáveis categóricas para numéricas
#     X = pd.get_dummies(X, columns=['cliente_nif', 'produto_categoria'], drop_first=True)

#     # Dividir em conjuntos de treino e teste
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#     # Modelos a serem treinados
#     modelos = {
#         "Logistic Regression": LogisticRegression(max_iter=200),
#         "Decision Tree": DecisionTreeClassifier(random_state=42),
#         "KNN": KNeighborsClassifier(n_neighbors=5)
#     }

#     resultados = []

#     # Treinar e avaliar cada modelo
#     for nome, modelo in modelos.items():
#         modelo.fit(X_train, y_train)
#         y_pred = modelo.predict(X_test)

#         # Avaliar o modelo
#         acc = accuracy_score(y_test, y_pred.round())  # Arredondar previsões para comparação com valores reais
#         print(f"Accuracy - {nome}: {acc}")
#         print(f"Classification Report - {nome}:\n", classification_report(y_test, y_pred.round()))
#         resultados.append((nome, acc))

#     # Visualizar resultados
#     modelos_nome = [r[0] for r in resultados]
#     accuracies = [r[1] for r in resultados]

#     sns.barplot(x=modelos_nome, y=accuracies)
    
#     plt.title('Comparação de Acurácia dos Modelos')
#     plt.ylabel('Acurácia')
#     plt.xlabel('Modelos')
#     plt.show()

def carregar_modelo_ml():
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Teste de Gráfico no WSL")
    plt.show()

if __name__ == "__main__":
    carregar_modelo_ml()
