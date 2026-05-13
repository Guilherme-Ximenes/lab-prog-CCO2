# Questão 01 - Cadastro de Show
nome_artista = ""
duracao_show = 0
cache_artista = 0.0

while True:
    nome_artista = input("Informe o nome do artista: ").strip()
    try:
        duracao_show = int(input("Informe a duração do show (min): "))
        if duracao_show <= 0:
            print("Valor inválido. Por favor, tente novamente.")
            continue

        cache_artista = float(input("Informe o cachê do artista: "))
        if cache_artista < 0 or cache_artista == -0.0:
            print("Valor inválido. Por favor, tente novamente.")
            continue

    except ValueError:
        print("Entrada inválida. Por favor, insira um número para a duração do show e o cachê do artista.")
        continue
    break

custo_por_minuto = cache_artista / duracao_show

print("\n===Detalhes do Show===")
print(f"Artista: {nome_artista}\nDuração: {duracao_show} minutos\nCusto por minuto: R$ {custo_por_minuto:.1f}")

#Questão 02 - Classificação do cachê
if cache_artista <= 5000:
    classificacao = "Artista independente"
elif 5001 < cache_artista <= 20000:
    classificacao = "Artista popular"
else:
    classificacao = "headliner"

print(f"\n{classificacao}")

#Questão 03 - Lista de Artistas
lineup_festival = []

print("\nInforme os 4 artistas do lineup do festival:")

i = 1
while i <= 4:
    informar_lineup = input(f"Informe o {i}° do lineup: ").strip()
    if informar_lineup == "":
        print("Entrada inválida. Por favor, tente novamente.")
    else:
        lineup_festival.append(informar_lineup)
        i += 1  

print("\n===Lineup do Festival===")
for artista in lineup_festival:
    print(artista)
print(f"\nPrimeiro: {lineup_festival[0]}")
print(f"Último: {lineup_festival[-1]}")

#Questão 04 - Contagem de Público
while True:
    try:
        print("\n===Contagem de Público===")
        publico_qtd = int(input("Informe a quantidade de pessoas entrando no festival: "))
        for i in range(1, publico_qtd + 1):
            if i == 1:
                print(f"{i} pessoa entrou no festival.")
            else:
                print(f"{i} pessoas entraram no festival.")
    except ValueError:
        print("Por favor, insira um número válido para a quantidade de pessoas.")
        continue
    break

#Questão 05 - Avaliação dos Shows
avaliacao_shows = []

print("\n===Avaliação dos Shows===")

i = 0
while i < len(lineup_festival):
    try:
        avaliacao_individual = int(input(f"Informe uma nota de 0 a 10 para o {i+1}° artista do lineup: "))
        if 0 <= avaliacao_individual <= 10:
            avaliacao_shows.append(avaliacao_individual)
            i += 1  
        else:
            print("Avaliação inválida. Por favor, insira um número entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número para a avaliação.")

print()
for artista in lineup_festival:
    indice_artista = lineup_festival.index(artista)
    print(f"{artista} - {avaliacao_shows[indice_artista]}")

media_avaliacao = sum(avaliacao_shows) / len(avaliacao_shows)
print(f"\nMédia das avaliações: {media_avaliacao:.2f}")

#Questão 06 - controle de ingressos
ingressos_vendidos = 0
inteiras = 0
meias = 0

while True:
    print("\n===Controle de Ingressos===")
    try:
        ingressos_vendidos = int(input("Informe a quantidade de ingressos vendidos: "))
        for i in range(1, ingressos_vendidos + 1):
            tipo_ingresso = int(input(f"Ingresso {i} (1 - Inteira / 2 - Meia): "))
            if tipo_ingresso == 1:
                inteiras += 1
            elif tipo_ingresso == 2:
                meias += 1
            else:
                print("Erro! informe '1' para inteira ou '2' para meia.")
                continue
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue
    break

total_arrecadado = (inteiras * 100) + (meias * 50)

print(f"\nTotal arrecadado: R${total_arrecadado:.2f}")
print(f"Quantidade de ingressos: {ingressos_vendidos}")
print(f"Inteiras: {inteiras}")
print(f"Meias: {meias}")

#Questão 07 - Busca de Artista
print(f"\n===Busca de Artista===")
while True:
    nome_artista_busca = input("\nInforme o nome do artista para buscar no lineup: ").strip().lower()
    if nome_artista_busca in [artista.lower() for artista in lineup_festival]:
        print(f"Artista confirmado no festival.")
        continuar_busca = input("Deseja buscar outro artista? (s/n): ").strip().lower()
        if continuar_busca != 's':
            break
        else:
            continue
    else: 
        print("Artista não encontrado no lineup.")
        continue