vendedor = {'Nome': 'Daniel', 'Empresa': 'G&P'}

print("=== Vendedores Disponíveis ===")
print(f"1. Nome: {vendedor['Nome']}, Empresa: {vendedor['Empresa']}")

# Escolha do vendedor
escolha = input("Escolha o número do vendedor para este produto: ")

if escolha == '1':
    nome_produto = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    empresa_produto = input("Empresa do produto: ")

    print(f"Produto adicionado com sucesso ao vendedor {vendedor['Nome']}!")
else:
    print("Vendedor não encontrado.")
