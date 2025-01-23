from bd.inicializacao import criar_bd, criar_tabelas
from bd.insercao import inserir_cliente, inserir_fornecedor, inserir_produto
from bd.consultas import consultar_clientes, consultar_fornecedores, consultar_produtos
from bd.remocao import remover_cliente, remover_fornecedor, remover_produto
#from bd.atualizacao import atualizar_produto
#from vendas import registrar_venda

# Função para exibir o menu de opções
def exibir_menu():
    print("\nMENU DE OPÇÕES")
    print("1. Inserir Cliente")
    print("2. Inserir Fornecedor")
    print("3. Inserir Produto")
    print("4. Consultar Clientes")
    print("5. Consultar Fornecedores")
    print("6. Consultar Produtos")
    print("7. Remover Cliente")
    print("8. Remover Fornecedor")
    print("9. Remover Produto")
    print("10. Atualizar Produto")
    print("11. Registrar Venda")
    print("12. Sair")

# Função para processar a opção escolhida
def processar_opcao(opcao):
    if opcao == 1:
        inserir_cliente()
    elif opcao == 2:
        inserir_fornecedor()
    elif opcao == 3:
        inserir_produto()
    elif opcao == 4:
        clientes = consultar_clientes()
        if not clientes:
            print("Não há clientes cadastrados.")
        else:
            for cliente in clientes:
                print(cliente)
    elif opcao == 5:
        fornecedores = consultar_fornecedores()
        if not fornecedores:
            print("Não há fornecedores cadastrados.")
        else:
            for fornecedor in fornecedores:
                print(fornecedor)
    elif opcao == 6:
        produtos = consultar_produtos()
        if not produtos:
            print("Não há produtos cadastrados.")
        else:
            for produto in produtos:
                print(produto)
    elif opcao == 7:
        remover_cliente()
    elif opcao == 8:
        remover_fornecedor()
    elif opcao == 9:
        remover_produto()
    elif opcao == 10:
        atualizar_produto()
    elif opcao == 11:
        cliente_id = int(input("Informe o ID do cliente: "))
        produto_nome = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade: "))
        registrar_venda(cliente_id, produto_nome, quantidade)
    elif opcao == 12:
        print("Saindo...")
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para exibir o menu
def menu():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if not processar_opcao(opcao):
                break
        except ValueError:
            print("Por favor, digite um número válido.")

# Função principal para inicializar o sistema
def main():
    # Inicializar o banco de dados
    criar_bd()
    criar_tabelas()

    # Rodar o menu
    menu()

if __name__ == "__main__":
    main()
