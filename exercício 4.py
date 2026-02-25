numero = int(input("Digite um número de 1 a 3: "))
bebidas = ["Café", "Chá", "Suco"]

match numero:
    case 1:
        print(f"Você escolheu {bebidas[0]}")
    case 2:
        print(f"Você escolheu {bebidas[1]}")
    case 3:
        print(f"Você escolheu {bebidas[2]}")
    case _:
        print("Bebida não disponível")