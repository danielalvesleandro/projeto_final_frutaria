import string
from .conexao import conectar_bd
from faker import Faker
import random
from datetime import timedelta

# Função para gerar um NIF com 9 caracteres
def gerar_nif():
    return ''.join(random.choices(string.digits, k=9))

# Função para gerar um telefone com 9 caracteres iniciando por 9
def gerar_telefone():
    return '9' + ''.join(random.choices(string.digits, k=8))

# Função para gerar clientes
def gerar_clientes(cursor, quantidade):
    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        telefone = gerar_telefone()
        email = fake.email()
        endereco = fake.address()
        nif = gerar_nif()

        cursor.execute("""
            INSERT INTO clientes (nif, nome, sobrenome, telefone, email, endereco) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nif, nome, sobrenome, telefone, email, endereco))

# Função para gerar fornecedores
def gerar_fornecedores(cursor, quantidade):
    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        nome = fake.company()
        telefone = gerar_telefone()
        email = fake.email()
        endereco = fake.address()
        nif = gerar_nif()

        cursor.execute("""
            INSERT INTO fornecedores (nif, nome, telefone, email, endereco) 
            VALUES (%s, %s, %s, %s, %s)
        """, (nif, nome, telefone, email, endereco))

# Listas de frutas com suas categorias
frutas = [
    # Frutas comuns
    ("maçã", "Comuns"), ("banana", "Comuns"), ("laranja", "Comuns"), ("pera", "Comuns"), ("uva", "Comuns"),
    ("morango", "Comuns"), ("mamão", "Comuns"), ("abacaxi", "Comuns"), ("melão", "Comuns"), ("melancia", "Comuns"),
    ("abacate", "Comuns"), ("pêssego", "Comuns"), ("nectarina", "Comuns"), ("ameixa", "Comuns"), ("cereja", "Comuns"),
    ("figo", "Comuns"), ("romã", "Comuns"), ("kiwi", "Comuns"),

    # Frutas cítricas
    ("limão", "Cítricas"), ("lima", "Cítricas"), ("grapefruit", "Cítricas"), ("tangerina", "Cítricas"),

    # Frutas vermelhas
    ("framboesa", "Vermelhas"), ("amora", "Vermelhas"), ("mirtilo", "Vermelhas"),

    # Frutas tropicais
    ("maracujá", "Tropicais"), ("goiaba", "Tropicais"), ("carambola", "Tropicais"), ("mangostão", "Tropicais"),
    ("mangaba", "Tropicais"), ("jabuticaba", "Tropicais"), ("cupuaçu", "Tropicais"), ("acerola", "Tropicais"),
    ("jaca", "Tropicais"), ("graviola", "Tropicais"), ("pitanga", "Tropicais"),

    # Frutas secas
    ("passa", "Secas"), ("damasco", "Secas"),

    # Frutas exóticas
    ("lichia", "Exóticas"), ("romã", "Exóticas"), ("maracujá", "Exóticas"), ("fruta-do-conde", "Exóticas"),
    ("jackfruit", "Exóticas"), ("mangostin", "Exóticas"), ("durião", "Exóticas"), ("rambutan", "Exóticas"),
    ("starfruit", "Exóticas"), ("dragon fruit", "Exóticas"),

    # Outras frutas
    ("caqui", "Diversas"), ("figo", "Diversas"), ("tâmara", "Diversas"), ("romã", "Diversas"),
    ("carambola", "Diversas"), ("jaca", "Diversas"), ("graviola", "Diversas"), ("pitanga", "Diversas"),
    ("caju", "Diversas"), ("umbu", "Diversas"), ("cajá", "Diversas"), ("bacuri", "Diversas"),
]

# Função para gerar amostra de produtos
def gerar_produtos(cursor):
    
    # A função vai garantir que todas as frutas sejam inseridas, sem alterações.
    for fruta, categoria in frutas:
        nome = fruta.capitalize()
        preco = round(random.uniform(1.5, 30.0), 2)  # Preço aleatório entre 1.5 e 30.0
        quantidade = random.randint(1, 100)  # Quantidade aleatória entre 1 e 100

        # Inserir na base de dados
        cursor.execute("""
            INSERT INTO produtos (nome, categoria, preco, quantidade)
            VALUES (%s, %s, %s, %s)
        """, (nome, categoria, preco, quantidade))

# Função para gerar amostra de vendas
def gerar_vendas(cursor, quantidade):
    fake = Faker('pt_BR')
    
    # Obter os ids de clientes válidos
    cursor.execute("SELECT id FROM clientes")
    clientes_ids = [row[0] for row in cursor.fetchall()]
    
    # Obter os ids e nomes de produtos válidos
    cursor.execute("SELECT id FROM produtos")  # Apenas o id do produto
    produtos_ids = [row[0] for row in cursor.fetchall()]
    
    for _ in range(quantidade):
        # Escolher um cliente aleatório entre os existentes
        cliente_id = random.choice(clientes_ids)
        
        # Escolher um produto aleatório
        produto_id = random.choice(produtos_ids)
        
        # Gerar outros dados da venda (data, total, etc.)
        data_venda = fake.date_this_year()  # Exemplo de data aleatória
        total = round(random.uniform(10.0, 500.0), 2)  # Valor aleatório da venda
        quantidade = random.randint(1, 10)  # Quantidade aleatória de itens vendidos
        
        # Inserir a venda com produto_id
        cursor.execute("""
            INSERT INTO vendas (cliente_id, produto_id, quantidade, data_venda, total)
            VALUES (%s, %s, %s, %s, %s)
        """, (cliente_id, produto_id, quantidade, data_venda, total))

# Função para carregar amostra de dados
def carregar_amostra_dados():
    try:
        # Usando a função conectar_bd do módulo conexao
        conn = conectar_bd()
        if conn is None:
            print("Erro ao conectar ao banco de dados. Não foi possível carregar a amostra de dados.")
            return

        cursor = conn.cursor()

        # Gerar 20 clientes, 20 fornecedores, 50 produtos e 200 vendas
        print("Gerando amostra de dados...")

        gerar_clientes(cursor, 20)
        gerar_fornecedores(cursor, 20)
        gerar_produtos(cursor)

        # Commitando as inserções
        conn.commit()

        gerar_vendas(cursor, 200)

        # Commitando as inserções restantes
        conn.commit()

        print("Amostra de dados carregada com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao carregar a amostra de dados: {e}")

    finally:
        # Fechar a conexão, independentemente de erro ou sucesso
        if cursor:
            cursor.close()
        if conn:
            conn.close()

