import os
from bd.inicializacao import criar_bd, criar_tabelas
from bd.insercao import inserir_cliente, inserir_fornecedor, inserir_produto
from bd.consultas import consultar_clientes, consultar_fornecedores, consultar_produtos
from bd.atualizacao import atualizar_produto #atualizar_cliente, atualizar_fornecedor
from bd.remocao import remover_cliente, remover_fornecedor, remover_produto
from bd.vendas import registrar_venda#, atualizar_venda, consultar_vendas, cancelar_venda

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o menu principal
def exibir_menu_principal():
    #limpar_tela()
    print("\nMENU PRINCIPAL")
    print("1. Operações")
    print("2. Gráficos")
    print("3. Manutenção")
    print("4. Sair")

# Função para exibir o submenu de Operações
def exibir_submenu_operacoes():
    #limpar_tela()
    print("\nSUBMENU - OPERAÇÕES")
    print("1. Cliente")
    print("2. Fornecedores")
    print("3. Estoque")
    print("4. Vendas")
    print("5. Voltar")

# Função para exibir o submenu de Cliente
def exibir_submenu_cliente():
    #limpar_tela()
    print("\nSUBMENU - CLIENTE")
    print("1. Inserir Cliente")
    print("2. Atualizar Cliente")
    print("3. Consultar Clientes")
    print("4. Remover Cliente")
    print("5. Voltar")

# Função para exibir o submenu de Fornecedores
def exibir_submenu_fornecedores():
    #limpar_tela()
    print("\nSUBMENU - FORNECEDORES")
    print("1. Inserir Fornecedor")
    print("2. Atualizar Fornecedor")
    print("3. Consultar Fornecedores")
    print("4. Remover Fornecedor")
    print("5. Voltar")

# Função para exibir o submenu de Estoque
def exibir_submenu_estoque():
    #limpar_tela()
    print("\nSUBMENU - ESTOQUE")
    print("1. Inserir Produto")
    print("2. Atualizar Produto")
    print("3. Consultar Produtos")
    print("4. Remover Produto")
    print("5. Voltar")

# Função para exibir o submenu de Vendas
def exibir_submenu_vendas():
    #limpar_tela()
    print("\nSUBMENU - VENDAS")
    print("1. Inserir Venda")
    print("2. Atualizar Venda")
    print("3. Consultar Vendas")
    print("4. Cancelar Venda")
    print("5. Voltar")

# Função para exibir o submenu de Gráficos
def exibir_submenu_graficos():
    #limpar_tela()
    print("\nSUBMENU - GRÁFICOS")
    print("1. Visualizar Clientes")
    print("2. Visualizar Fornecedores")
    print("3. Visualizar Estoque")
    print("4. Visualizar Vendas")
    print("5. Voltar")

# Função para exibir o submenu de Manutenção
def exibir_submenu_manutencao():
    #limpar_tela()
    print("\nSUBMENU - MANUTENÇÃO")
    print("1. Limpar e Otimizar Tabelas")
    print("2. Carregar Amostra de Dados")
    print("3. Remover Base de Dados")
    print("4. Voltar")

# Função para processar entradas com possibilidade de sair
def entrada_com_saida(prompt):
    entrada = input(prompt + " (ou digite 'sair' para voltar): ").strip().lower()
    if entrada == 'sair':
        return None
    return entrada

# Função para processar o submenu Cliente
def processar_submenu_cliente(opcao):
    if opcao == 1:
        while True:
            inserir_cliente()
    elif opcao == 2:
        while True:
            cliente_id = entrada_com_saida("Informe o ID do cliente para atualizar")
            if cliente_id is None:
                break
            nome = entrada_com_saida("Informe o novo nome do cliente")
            if nome is None:
                break
            #atualizar_cliente(cliente_id, nome)
    elif opcao == 3:
        consultar_clientes()
        input("Pressione Enter para continuar...")
    elif opcao == 4:
        while True:
            cliente_id = entrada_com_saida("Informe o ID do cliente para remover")
            if cliente_id is None:
                break
            remover_cliente(cliente_id)
    elif opcao == 5:
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para processar o submenu Fornecedores
def processar_submenu_fornecedores(opcao):
    if opcao == 1:
        while True:
            inserir_fornecedor()
    elif opcao == 2:
        while True:
            fornecedor_id = entrada_com_saida("Informe o ID do fornecedor para atualizar")
            if fornecedor_id is None:
                break
            nome = entrada_com_saida("Informe o novo nome do fornecedor")
            if nome is None:
                break
            #atualizar_fornecedor(fornecedor_id, nome)
    elif opcao == 3:
        consultar_fornecedores()
        input("Pressione Enter para continuar...")
    elif opcao == 4:
        while True:
            fornecedor_id = entrada_com_saida("Informe o ID do fornecedor para remover")
            if fornecedor_id is None:
                break
            remover_fornecedor(fornecedor_id)
    elif opcao == 5:
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para processar o submenu Estoque
def processar_submenu_estoque(opcao):
    if opcao == 1:
        inserir_produto()
    elif opcao == 2:
        while True:
            produto_id = entrada_com_saida("Informe o ID do produto para atualizar")
            if produto_id is None:
                break
            nome = entrada_com_saida("Informe o novo nome do produto")
            if nome is None:
                break
            atualizar_produto(produto_id, nome)
    elif opcao == 3:
        consultar_produtos()
        input("Pressione Enter para continuar...")
    elif opcao == 4:
        remover_produto(produto_id)
    elif opcao == 5:
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para processar o submenu Vendas
def processar_submenu_vendas(opcao):
    if opcao == 1:
        while True:
            consultar_clientes()
            cliente_id = int(input("Informe o ID do cliente: "))
            consultar_produtos()
            produto_id = input("Informe o ID do produto: ")
            quantidade = int(input("Informe a quantidade: "))
            registrar_venda(cliente_id, produto_id, quantidade)
    elif opcao == 2:
        while True:
            venda_id = entrada_com_saida("Informe o ID da venda para atualizar")
            if venda_id is None:
                break
            nome = entrada_com_saida("Informe o novo nome da venda")
            if nome is None:
                break
            #atualizar_venda(venda_id, nome)
    elif opcao == 3:
        print("Função não implementada")
        #consultar_vendas()
    elif opcao == 4:
        while True:
            venda_id = entrada_com_saida("Informe o ID da venda para cancelar")
            if venda_id is None:
                break
            #cancelar_venda(venda_id)
    elif opcao == 5:
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para processar o submenu Gráficos
def processar_submenu_graficos(opcao):
    if opcao == 1:
        print("Visualizar gráficos de clientes...")
        # Chamar função de visualização de gráficos de clientes
    elif opcao == 2:
        print("Visualizar gráficos de fornecedores...")
        # Chamar função de visualização de gráficos de fornecedores
    elif opcao == 3:
        print("Visualizar gráficos de estoque...")
        # Chamar função de visualização de gráficos de estoque
    elif opcao == 4:
        print("Visualizar gráficos de vendas...")
        # Chamar função de visualização de gráficos de vendas
    elif opcao == 5:
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para processar o submenu Manutenção
def processar_submenu_manutencao(opcao):
    if opcao == 1:
        print("Limpar e otimizar tabelas...")
        # Chamar função de limpeza e otimização de tabelas
    elif opcao == 2:
        print("Carregar amostra de dados...")
        # Chamar função de carregar amostra de dados
    elif opcao == 3:
        print("Remover base de dados...")
        # Chamar função para remover base de dados
    elif opcao == 4:
        return False
    else:
        print("Opção inválida! Tente novamente.")
    return True

# Função para processar o menu principal
def processar_menu_principal():
    while True:
        exibir_menu_principal()
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                while True:
                    exibir_submenu_operacoes()
                    sub_opcao = int(input("Escolha uma opção: "))
                    
                    if sub_opcao == 1:
                        while True:
                            exibir_submenu_cliente()
                            if not processar_submenu_cliente(int(input("Escolha uma opção: "))):
                                break
                    elif sub_opcao == 2:
                        while True:
                            exibir_submenu_fornecedores()
                            if not processar_submenu_fornecedores(int(input("Escolha uma opção: "))):
                                break
                    elif sub_opcao == 3:
                        while True:
                            exibir_submenu_estoque()
                            if not processar_submenu_estoque(int(input("Escolha uma opção: "))):
                                break
                    elif sub_opcao == 4:
                        while True:
                            exibir_submenu_vendas()
                            if not processar_submenu_vendas(int(input("Escolha uma opção: "))):
                                break
                    elif sub_opcao == 5:
                        break
                    else:
                        print("Opção inválida! Tente novamente.")

            elif opcao == 2:
                while True:
                    exibir_submenu_graficos()
                    sub_opcao = int(input("Escolha uma opção: "))
                    if not processar_submenu_graficos(sub_opcao):
                        break

            elif opcao == 3:
                while True:
                    exibir_submenu_manutencao()
                    sub_opcao = int(input("Escolha uma opção: "))
                    if not processar_submenu_manutencao(sub_opcao):
                        break

            elif opcao == 4:
                print("Saindo...")
                break

            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Função principal para inicializar o sistema
def main():
    # Cria o banco de dados (se necessário)
    conn = criar_bd()  
    if conn is None:
        print("Erro ao criar o banco de dados, sistema não pode continuar.")
        return
    
    # Criação das tabelas
    criar_tabelas()

    # Chama o menu principal para iniciar o sistema
    processar_menu_principal()

if __name__ == "__main__":
    main()

