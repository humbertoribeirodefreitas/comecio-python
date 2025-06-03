vendedores = []
produtos = []
vendas = {}

def adicionar_vendedor():
    nome = input("Digite o nome do vendedor: ")
    vendedores.append(nome)
    vendas[nome] = 0
    print(f"Vendedor '{nome}' adicionado com sucesso!\n")

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos.append({"nome": nome, "preco": preco})
    print(f"Produto '{nome}' adicionado com sucesso!\n")

def mostrar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return
    print("=== Lista de Produtos ===")
    for idx, produto in enumerate(produtos, start=1):
        print(f"{idx}. {produto['nome']} - R$ {produto['preco']:.2f}")
    print()

def mostrar_vendedores():
    if not vendedores:
        print("Nenhum vendedor cadastrado.\n")
        return
    print("=== Lista de Vendedores ===")
    for idx, vendedor in enumerate(vendedores, start=1):
        print(f"{idx}. {vendedor} - Total de vendas: R$ {vendas[vendedor]:.2f}")
    print()

def registrar_venda():
    if not vendedores:
        print("Nenhum vendedor cadastrado.\n")
        return
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    mostrar_vendedores()
    vendedor_idx = int(input("Selecione o vendedor pelo número: ")) - 1
    vendedor = vendedores[vendedor_idx]

    mostrar_produtos()
    produto_idx = int(input("Selecione o produto pelo número: ")) - 1
    produto = produtos[produto_idx]

    quantidade = int(input("Digite a quantidade vendida: "))
    total_venda = produto['preco'] * quantidade
    vendas[vendedor] += total_venda
    print(f"Venda registrada! Total: R$ {total_venda:.2f} para {vendedor}\n")

def mostrar_maior_venda():
    if not vendas:
        print("Nenhuma venda realizada.\n")
        return
    maior_vendedor = max(vendas, key=vendas.get)
    print(f"Maior venda foi de {maior_vendedor} com R$ {vendas[maior_vendedor]:.2f}\n")

def menu():
    print(r"""
 
██████╗░███████╗███╗░░░███╗	██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░██╗
██╔══██╗██╔════╝████╗░████║	██║░░░██║██║████╗░██║██╔══██╗██╔══██╗██║
██████╦╝█████╗░░██╔████╔██║	╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║██║
██╔══██╗██╔══╝░░██║╚██╔╝██║	░╚████╔╝░██║██║╚████║██║░░██║██║░░██║╚═╝
██████╦╝███████╗██║░╚═╝░██║	░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝██╗
╚═════╝░╚══════╝╚═╝░░░░░╚═╝	░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝
""")
    opcao = input("Deseja continuar? (s/n): ").lower()
    if opcao != 's':
        print("Encerrando o programa.")
        exit()

    while True:
        print("""
=== Menu Principal ===
1 - Adicionar vendedor
2 - Adicionar produto
3 - Mostrar produtos
4 - Mostrar vendedores
5 - Mostrar maior venda
6 - Registrar venda
7 - Sair
""")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_vendedor()
        elif escolha == '2':
            adicionar_produto()
        elif escolha == '3':
            mostrar_produtos()
        elif escolha == '4':
            mostrar_vendedores()
        elif escolha == '5':
            mostrar_maior_venda()
        elif escolha == '6':
            registrar_venda()
        elif escolha == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
