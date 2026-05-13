while True:
    nota_1 = float(input("Digite a 1º nota(0.0 a 10.0): ")) 
    nota_2 = float(input("Digite a 2º nota(0.0 a 10.0): ")) 
    
    if (nota_1 or nota_2) > 10.0: print("Inválido. Digite uma nota entre 0.0 e 10.0")
    elif (nota_1 or nota_2) < 0.0: print("Inválido. Digite uma nota entre 0.0 e 10.0")
    else: break
    
    

media = (nota_1 + nota_2) / 2


print(media)



