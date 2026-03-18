#listas são criadas com o operador 'list', mas a forma mais comum é utilizando "[]".
#Possui índices para acessar seus valores, começando do zero.
'''
paises = ['Paris', 'Roma', 'Tokyo']
paises_avaliacoes= [4, 4, 5]

print(f'{paises}\n{paises_avaliacoes}')
'''
#print de um item da lista
'''
frutas = ['uva', 'maçã', 'pêra']
print(frutas[0])
'''
#alterando um item da lista
'''
paises = ['Paris', 'Roma', 'Tokyo']
paises[2] = "Berlim"

print(f'{paises}')
'''
#tamanho da lista
'''
frutas = ['uva', 'maçã', 'pêra']
print(len(frutas))
'''
#Lista = um tipo de dados
'''
meus_dados = ["Guilherme", 20, True]
print(meus_dados)
print(type(meus_dados)) #para saber o tipo de cada item da lista, é só informar o índice: "lista[índce]"
'''
#usando list
'''
frutas2 = list(("carro", "moto", "ônibus"))
print(frutas2)
'''
#Biblioteca(exercicio)
livros = ["Dom Casmurro", "o pequeno príncipe", "Memórias Póstumas de Brás Cubas"]
livros.reverse()

print(f"Livros cadastrados:\n{livros}")
print(f"\nO primeiro livro cadastrado: {livros[0]}")
print(f"Quantidade de livros: {len(livros)}")
print(type(livros))