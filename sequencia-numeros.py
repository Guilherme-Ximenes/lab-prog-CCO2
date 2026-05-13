#sequencia numeros
numeros = []
for i in range(1, 11):
    user = int(input(f"Digite o {i}° número: "))
    numeros.append(user)
print(f"Sequência de números digitados: {numeros}\n")

print("===Sequência ao quadrado===")
numeros_quadrados = []
for num in numeros:
    quadrado = num ** 2
    numeros_quadrados.append(quadrado)
print(numeros_quadrados)
