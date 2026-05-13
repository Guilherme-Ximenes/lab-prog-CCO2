#Treinando tuplas
#=====ETAPA 1=====
#===Questão 01===
pedidos = [("Ana", "Pizza"), 
           ("Bruno", "Hamburguer"), 
           ("Carla", "Pizza"),
           ("Diego", "Sushi"),
           ("Elisa", "Pizza")]
#=====ETAPA 2=====
#===Questão 02===
print("===Lista de Pedidos===")
print(f"{pedidos}")
print(f"Tipo da variável 'pedidos': {type(pedidos)}\n")

#===Questão 03===
print("===Primeiro e último pedidos===")
primeiro_pedido = pedidos[0]
ultimo_pedido = pedidos[-1]
#exibindo:
print(f"Primeiro pedido: {primeiro_pedido}")
print(f"Último pedido: {ultimo_pedido}\n")

#===Questão 04===
print("===Quantidade de pedidos===")
qtd_pedidos = len(pedidos)
#exibindo:
print(qtd_pedidos)
#=====ETAPA 3=====
#===Questão 05===
print("===Se tentarmos alterar o pedido na tupla===")
print("pedidos[2][1] = ('Carla', 'Sushi') #ERRO -> tupla não recebe atribuição de itens, ou seja, não há como add elementos")

#===Questão 06===
carla_pedido_lista = list(pedidos[2][1]) #transformando o pedido de carla em lista
carla_pedido_lista = ("Carla", "Sushi") #alterando a lista 
carla_pedido_tupla = tuple(carla_pedido_lista)  #transformando a nova lista alterada em uma tupla

pedidos.pop(2) #removendo a tupla antiga do pedido de Carla em pedidos

pedidos.insert(2, carla_pedido_tupla) #adicionando a nova tupla do pedido de Carla em pedidos
print(pedidos)
#=====ETAPA 4=====
#===Questão 07===
#unpacking:
print(f"\n===Exibindo os pedidos com unpacking===")
for nome, pedido in pedidos:
    print(f"Cliente: {nome} - Pedido: {pedido}")
#=====ETAPA 5=====
#===Questão 08===
#tupla com pratos pedidos
print(f"\n===Todos os pratos pedidos===")
pratos_pedidos = tuple(prato for nome, prato in pedidos)
print(f"{", ".join(pratos_pedidos)}")

#===Questão 09===
print(f"\n===Quantidade de pizzas pedidas===")
pedidos_pizza = pratos_pedidos.count("Pizza")
print(pedidos_pizza)

#===Questão 10===
print(f"\n===Primeira ocorrência de Pizza===")
print(f"Índice: {pratos_pedidos.index("Pizza")}")

#===Questão 11===
print(f"\n===Cliente que fez o primeiro pedido de pizza===")
clientes_que_pediram_pizza = tuple(cliente for cliente, pedido in pedidos if pedido.lower() == "pizza")
print(f"Cliente: {clientes_que_pediram_pizza[0]}")

#=====ETAPA 6=====
#===Questão 12===
print(f"\n===Por que está errado isso?===")
print("pratos_pedidos.index('Lasanha') #ERROR -> 'elemento (x) não foi encontrado na tupla', como não há esse pedido, o compilador identifica o erro de ñ encontrado")

#===Questão 13===
print(f"\n===Por que utilizamos tuplas nesse caso e quando usar listas?===\n")
print("Devemos usar tuplas nesse caso, pois é um dado que não deve ser alterado -> um pedido.\nA lista deve ser utilizado em dados que queremos alterar, ordenar, armazenar e organizar.\nExemplo de uso de lista: fila de processamento, carrinho de compras em um site, banco de dados, etc.")