'''
#Usando o match case
dia_da_semana = int(input("Digite um número: "))

match dia_da_semana:
    case 1:
        print("Segunda")
    case 2:
        print("Terça")
    case 3:
        print("Quarta")
    case 4:
        print("Quinta")
    case 5:
        print("Sexta")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")

    case _:
        print("Dia inválido")
'''      

#Usando o elif
dia_da_semana = int(input("Digite um número: "))

if dia_da_semana == 1:
    print("Segunda")
elif dia_da_semana == 2:
    print("Terça")
elif dia_da_semana == 3:
    print("Quarta")
elif dia_da_semana == 4:
    print("Quinta")
elif dia_da_semana == 5:
    print("Sexta")
elif dia_da_semana == 6:
    print("Sábado")
elif dia_da_semana == 7:
    print("Domingo")
else:
    print("Dia inválido")