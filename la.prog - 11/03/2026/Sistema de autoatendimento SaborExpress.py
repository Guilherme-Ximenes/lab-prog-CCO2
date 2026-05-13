#Início
print("----" * 7)
print("Bem-vindo ao sistema de atendimento do SaborExpress")
print("----" * 7, f"\n")

#Identificador do cliente
nome = input("Informe seu nome: ")

#Início do pedido
total_pedido = 0.0
while True:
    pedido = input(f"{nome.capitalize()}, deseja regitrar um novo item no pedido? (S/N) ")
    if pedido.upper() == "S" and pedido.isalpha(): #formatando igual
        item = float(input(f"\nInforme o valor do item (Digite 0 para cancelar): ")) #valor do item
        if item < 0:
            print("Valor inválido, tente novamente!")
            continue
        else:
            if item != 0:
                if item > 50:
                    print("Item premium")
                elif item > 20:
                    print("Item normal")
                else:
                    print("Item econômico")

                valor_do_item = item
                total_pedido += valor_do_item
            else:
                print(f"Pedido de {nome} cancelado!")  #cancelamento do pedido
                break 

    elif pedido.upper() == "N":
        break  
    else:
        print("Pedido inválido, tente novamente!")
        continue

print(f"Valor total do pedido de {nome}: {total_pedido:.2f}")