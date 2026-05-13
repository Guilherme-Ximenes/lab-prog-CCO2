#Início
nome = input("Digite seu nome: ")
print(f"Bem-vindo/a ao PetVida, {nome}!")

#Idade, peso, temperatura
print(f"\n...Para continuar, informe a idade, o peso e a temperatura do seu pet...")
while True:
    idade = str(input("Idade: "))
    peso = str(input("Peso(Kg): "))
    temperatura = str(input("Temperatura(ºC): "))
    if (idade.isnumeric()) and (peso.isnumeric()) and (temperatura.isnumeric()):
            break

#análise idade
idade = int(idade)
if idade < 2:
    print(f"\nEle é um filhote!")
elif idade < 7:
    print(f"\nEle já é adulto!")
elif idade > 7:
    print(f"\nEle já é idoso!")
else:
    print(f"\nDigite números válidos, por favor!")
    
#análise peso
peso = int(peso)
print(f"\nSeu pet terá um atendimento especial." if peso >= 40 else f"\nSeu pet terá um atendimento normal.")

#análise temperatura
temperatura = int(temperatura)
print(f"\nSeu pet está com febre!" if temperatura >= 39 else f"\nEle está com a temperatura normal!")

#NÌVEL 2
#Vacinação
print("\n...Vamos continuar para a segunda ficha de análise...")
while True:
    vacinado = input(f"\nSeu pet é vacinado? s/n: ")
    if vacinado.lower() == "s" or vacinado.lower() == "n":
        break

#análise vacinação
print(f"\nSeu pet poderá usar o hotelzinho" if idade >= 1 and vacinado.lower() == "s" else f"\nSeu pet não poderá usar o hotelzinho!")

#grupo de risco
print(f"...\n")
print(f"Seu pet está no grupo de risco!" if idade > 10 or peso < 2 else f"Seu pet não está em grupo de risco!")

#Serviço
while True:
    servico = input(f"...\nDigite o serviço que deseja: ")
    if not servico:
        print(f"Erro! Serviço não identificado.") 
        continue
    else: 
        print(f"Seu serviço foi identificado.")
        break

#nome e telefone
telefone = input(f"\nDigite seu número de telefone: ")
print(f"cadastro inválido" if not nome and not telefone else f"cadastro válido"  )

#NìVEL 3
#Tipo de pet
print("\n...Vamos para a ficha 3...")
while True:
    pet = input(f"\nQual o tipo do seu pet? \n[1] cachorro\n[2] gato\n[3] ave\nDigite aqui: ")
    if (pet == "1") or (pet == "2") or (pet == "3"):
        if pet == "1":
            print("Seu pet é um cachorro!")
        elif pet == "2":
            print("Seu pet é um gato!")
        else:
            print("Seu pet é uma ave!")
        break
    
#plano do cliente
print(f"\n...Antes de continuarmos, irei lhe explicar os benefícios dos nossos planos:\n 1º básico: 'benefíco básico'\n 2º premium: 'benefício premium'\n 3º VIP: 'benefício VIP'...")
while True:
    plano = input(f"Digite qual plano você deseja: \n[1] básico\n[2] premium\n[3] VIP\nDigite aqui: ")
    if (plano == "1") or (plano == "2") or (plano == "3"):
        if plano == "1":
            print("Você escolheu o plano básico")
        elif plano == "2":
            print("Você escolheu o plano premium")
        else:
            print("Você escolheu o plano VIP")
        break
    
#nota de satisfação
while True:
    nota_satisfacao = int(input("\nPor favor, peço que nos deixe uma nota de avaliação(0-10): "))
    nota_satisfacao = str(nota_satisfacao)
    if nota_satisfacao.isnumeric():
        break
    
#Nìvel 4
#cirugia
print("\n...Vamos prosseguir para a ficha 4...")
print(f"Seu pet pode fazer cirurgia!" if idade >= 1 and peso >= 2 else f"Seu pet não pode fazer cirurgia!")

#comportamento
while True:
    comportamento = input(f"\nComo você descreveria o comportamento do seu pet(agitado/estressado): ")
    if comportamento.lower() == "agitado" or comportamento.lower() == "estressado":
        print("\n...\nSeu pet precisa de emergência!" if comportamento.lower() == "agitado" and temperatura >= 39 else "Seu pet não precisa de emergência.")
        break

#valor compra
while True:
    valor_compra = str(input(f"\nDigite o valor da compra: "))
    cliente_vip = input("\nVocê é cliente VIP?(s/n)\n")
    if valor_compra.isnumeric() and cliente_vip.isalpha():
        valor_compra = int(valor_compra)
        if valor_compra >= 200 or cliente_vip.lower() == "s":
            print(f"\n...Você terá um desconto por ser VIP.")
            break
        else:
            print(f"\n...Você não receberá um desconto!")
            break
    else:
        continue

#senha digitada e senha correta
while True:
    senha = input("\nDigite sua senha: ")
    confirmacao = input("\nConfirme sua senha: ")
    if senha != confirmacao:
        print(f"Acesso negado, senha incorreta!")
        continue
    else:
        break
    
#NìVEL 5
#avaliação pet
while True:
    nota_profissional = str(input(f"\nDigite uma nota para o profissional de atendimento(0-10): "))
    nota_servico = str(input("Digite uma nota para o serviço(0-10): "))
    if nota_profissional.isnumeric() and nota_servico.isnumeric():
        nota_profissional = int(nota_profissional)
        nota_servico = int(nota_servico)
        media = (nota_profissional + nota_servico) / 2
        print(f"\nmedia = {media}\n")
        if media > 3:
            print("Boa avaliação.")
            break
        else:
            print("Avaliação ruim.")
            break
    else:
        continue
    
#classificação atendimento
print("\n...Classificação do atendimento...")
if temperatura >= 39:
    print(f"Temperatura = {temperatura}; Emergência!")
elif peso < 2:
    print(f"Peso = {peso}; Atenção!")
elif idade > 10:
    print(f"Idade = {idade}; Monitoramento")
else:
    print("Normal")






