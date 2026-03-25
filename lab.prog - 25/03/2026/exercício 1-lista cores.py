cores = ['azul','verde', 'vermelho']
cor = input("Digite uma cor: ")

if cor in cores:
    print(f"{cor} está na lista")
else:
    print(f"{cor} não está na lista")

#alterando um elemento da lista
cores[0] = 'roxo'

cor = input("Digite uma cor: ")

if cor in cores:
    print(f"{cor} está na lista")
else:
    print(f"{cor} não está na lista")

#alterando vários elementos da lista
cores[0:2] = ['rosa','violeta']

print(f"lista com adição de rosa e violeta: {cores}")


