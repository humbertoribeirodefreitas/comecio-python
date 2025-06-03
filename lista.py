def listar_produtos_por_vendedor():
    print("=== Lista de Produtos por Vendedor ===")
    
    vendedor = input("Vendedor: ")
    produtos = []

    while True:
        print(f"\nProdutos do vendedor: {vendedor}:")
        nome = input("  Nome do produto: ")
        marca = input("  Marca: ")
        preco = float(input("  Preço: "))

        produto = {
            'nome': nome,
            'marca': marca,
            'preco': preco
        }
        produtos.append(produto)

        for p in produtos:
            print(f"- Nome: {p['nome']}, Preço: R${p['preco']}, Marca: {p['marca']}")
        
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    listar_produtos_por_vendedor()
