vendedores = []

while True:
    print("\n=== Adicionar Vendedor ===")
    nome = input("Nome do vendedor: ")
    empresa = input("Empresa do vendedor: ")

    vendedor = {'Nome': nome, 'Empresa': empresa}
    vendedores.append(vendedor)

    print(vendedor)
    print("Vendedor adicionado com sucesso!")

    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break

print("\n=== Lista de Vendedores ===")
for v in vendedores:
    print(f"Nome: {v['Nome']}, Empresa: {v['Empresa']}")
