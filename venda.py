vendas = {
    "Daniel": [
        {'nome_do_produto': 'Maçã', 'marca': 'Algum lugar', 'price': 20.0},
        {'nome_do_produto': 'Banana', 'marca': 'Outro lugar', 'price': 15.0}
    ],
    "Ana": [
        {'nome_do_produto': 'Laranja', 'marca': 'Sul frutas', 'price': 25.0}
    ],
    "Carlos": [
        {'nome_do_produto': 'Abacaxi', 'marca': 'Tropical', 'price': 30.0}
    ],
    "Juliana": [
        {'nome_do_produto': 'Melancia', 'marca': 'Fazenda Boa', 'price': 28.0}
    ]
}

print("=== Análise de Vendas ===")
maior_venda = 0
vendedor_maior_venda = ""
produto_maior_venda = {}

# Total de vendas por vendedor
for vendedor, produtos in vendas.items():
    total = sum(p['price'] for p in produtos)
    print(f"Total de vendas de {vendedor}: R${total:.1f}\n")

    print(f"Produtos do vendedor: {vendedor}:")
    for p in produtos:
        print(f"Nome do produto: {p['nome_do_produto']}")
        print(f"Marca: {p['marca']}")
        print(f"Preço: {p['price']}\n")

        if p['price'] > maior_venda:
            maior_venda = p['price']
            vendedor_maior_venda = vendedor
            produto_maior_venda = p

# Comparação de vendas
print("Comparação de vendas:")
for vendedor, produtos in vendas.items():
    total = sum(p['price'] for p in produtos)
    print(f"- Vendedor: {vendedor}: R${total:.1f}")

print(f"\nMaior venda: R${maior_venda}")
print(f"Vendedor com maior venda: {vendedor_maior_venda}")
print([produto_maior_venda])

# Pergunta final (simulada)
resposta = input("Deseja continuar? (s/n): ")
