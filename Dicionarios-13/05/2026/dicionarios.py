#=================================================================
# =============Dicionários em Python==============================
#=================================================================

# - Criando um dicionário: my_dict = {"chave1": "valor1", "chave2": "valor2"}
jogo2 = {
    "Nome": "Super Mario Bros",
    "Gênero": "Ação",
    "Preço": 260.00,
    "Multiplayer": True,
    "Plataforma": "Nintendo"
}

# - Acessando itens de um dicionário
nome_jogo = jogo2['Nome'] # Super Mario bros
genero_jogo = jogo2['Gênero'] # Ação
preco_jogo = jogo2["Preço"] # 260.00
multiplayer_jogo = jogo2["Multiplayer"] # True
plataforma_jogo = jogo2["Plataforma"] # Nintendo
print(f"{nome_jogo}, um dos jogos mais famosos da {plataforma_jogo}, é um clássico do gênero {genero_jogo}, sendo Multiplayer:{multiplayer_jogo} e custando {preco_jogo} nas lojas oficiais.")
print("==" * 55)

# - Método 'get()' -> recupera o valor de uma chave em um dicionário, forma mais segura.
# Sintaxe: 'dicionario.get(chave, valor_padrao)'
print(f"Jogo: {jogo2.get('Nome')}")
print("==" * 55)

# - Método 'keys()' -> retorna uma lista com todas as chaves do dicionario
chaves_jogo2 = jogo2.keys()
print(chaves_jogo2)
print("==" * 55)

# - Método 'items() - > retorna todos os pares chave-valor do dicionario
items_dicionario = jogo2.items()
print(items_dicionario)
print("==" * 55)

# - Criando uma nova lista a partir de 'jogo2" contendo as chaves em letras maiúsculas
chaves_maiusculas_jogo2 = [chave.upper() for chave,valor in jogo2.items()]
print(chaves_maiusculas_jogo2)
print("==" * 55)

# - utilizando 'update()' para alterar e adicionar itens em um dicionário
jogo2.update({"Preço": 300.00, "Classificação": "Livre para todas as idades"})
print(jogo2)
print("==" * 55)

# -adicionando uma nova chave-valor ao dicionário
jogo2["Ano_lançamento"] = 1985
print(jogo2)
print("==" * 55)

# - Removendo itens de um dicionário usando 'pop()','del' ou 'popitem()'
jogo2.pop("Multiplayer") # Remove a chave "Multiplayer" e seu valor
print(f"jogo2 após remoção de multiplayer:{jogo2}\n")
#'popitem()" -> Remove o último item adicionado ao dicionário
jogo2.popitem() # Remove o último item adicionado 'Ano_lançamento'
print(f"jogo2 após remoção do último item adicionado:{jogo2}\n")
# 'del dict[chave]' -> Remove uma chave específica do dicionário
# 'del dict' -> remove o dicionario inteiro


# - Percorrendo um dicionário usando um loop 'for'
print("Percorrendo os itens do dicionário jogo2:")
for chave, valor in jogo2.items(): # Se o objetivo for imprimir os items(chave: valor), pode usar somente 'for item in jogo2.items()' também.
    print(f"{chave}: {valor}")
print()

print("Percorrendo as chaves do dicionário jogo2:")
for chave in jogo2.keys():
    print(chave)
print()

print("Percorrendo os valores do dicionário jogo2:")
for valor in jogo2.values():
    print(valor)
print("==" * 55)

# - método copy()
Copia_jogo2 = jogo2.copy() # Cria uma cópia rasa do dicionário jogo2
print(f"Cópia do jogo2: {Copia_jogo2}")
print("==" * 55)

# - método len() -> retorna o número de pares chave: valor em um dicionário
print(f"Número de pares chave:valor em jogo2: {len(jogo2)}")
print("==" * 55)

# - métododo fromkeys() -> cria um novo dicionário a partir de uma lista de chaves, atribuindo um valor padrão a cada chave.
chaves = ["Nome", "Gênero", "Preço", "Multiplayer", "Plataforma"]
novo_jogo = dict.fromkeys(chaves, "Valor Padrão")
print(f"Novo dicionário criado com fromkeys(): {novo_jogo}")
print("==" * 55)

# ===========Nested Dictionaries (Dicionários Aninhados)======================
print("====Nested Dictionaries (Dicionários Aninhados)=====")
# - Dicionários aninhados são dicionários que contêm outros dicionários como valores.
Jogos = {
    "jogo_1": {
        "Nome": "The Legend of Zelda: Breath of the Wild",
        "Gênero": "Ação/Aventura",
        "Preço": 350.00,
        "Multiplayer": False,
        "Plataforma": "Nintendo Switch"
    },

    "Jogo_2": {
        "Nome": "Clair Obscur: Expedition 33",
        "Gênero": "RPG de turno/Ação",
        "Preço": 200.00,
        "Multiplayer": False,
        "Plataforma": "PC"
    }
}

# - Acessando itens em um dicionário aninhado
nome_jogo1 = Jogos["jogo_1"]["Nome"] # The Legend of Zelda: Breath of the Wild
nome_jogo2 = Jogos["Jogo_2"]["Nome"] # Clair Obscur: Expedition 33
print(f"Jogo 1: {nome_jogo1}\nJogo 2: {nome_jogo2}")
print("==" * 55)
# - Percorrendo um dicionário aninhado usando loops 'for'
for jogo, valor in Jogos.items():
    print(jogo)
    for item in valor:
        if (item == "Nome" or item == "Gênero"):
            print(f"{item}:{valor[item]}")
    print()

