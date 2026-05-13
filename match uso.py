dia_da_semana = int(input("Digite um dia da semana de 1 a 7: "))
mes = 4

match dia_da_semana:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("Dia de semna em abril")
    case 6 | 7 if mes == 4:
        print("Final de semana em abril")
    case _:
        print("Dia inválido")