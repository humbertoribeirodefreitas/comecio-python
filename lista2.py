# Lista de vendedores
vendedores = [
    {'Nome': 'Daniel', 'Empresa': 'G&P'},
    {'Nome': 'Ana', 'Empresa': 'TechCorp'},
    {'Nome': 'Bruno', 'Empresa': 'Inova'},
    {'Nome': 'Carla', 'Empresa': 'SoftSolutions'}
]

# Exibindo a lista
print("=== Lista de Vendedores ===")
for i, vendedor in enumerate(vendedores, start=1):
    print(f"{i}. {vendedor}")

# Perguntando se deseja continuar
resposta = input("Deseja continuar? (s/n): ")
