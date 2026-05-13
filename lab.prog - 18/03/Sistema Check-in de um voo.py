#Início
print("=" * 5, "Sistema de Check-in", "=" * 5)

#Sistema
#Passageiros
passageiros = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
print(f"\nPassageiros do Voo:\n{'-' * 23}")
for passageiro in passageiros:
    print(passageiro)
    
#Mensagem de embarque
print(f"\n=====Embarque=====")
for passageiro in passageiros:
    if passageiro != "Carlos":
        print(f"{passageiro} realizou o check-in!")
    else:
        print(f"{passageiro} perdeu o check-in!")
        
print(f"\n=====Encerrando embarque=====")
for passageiro in passageiros:
    if passageiro != "Daniela":
        print(f"{passageiro} pode embarcar!")
    elif passageiro == "Carlos":
        print(f"{passageiro} perdeu o embarque!")
    else:
        print("Embarque encerrado!")
        break
    
#Numerando os passageiros
print(f"\n")
for i in range(len(passageiros)):
    numero_passageiro = i + 1
    nome_passageiro = passageiros[i] 
    
    print(f"Passageiro {numero_passageiro}: {nome_passageiro}")

    
    
    
        