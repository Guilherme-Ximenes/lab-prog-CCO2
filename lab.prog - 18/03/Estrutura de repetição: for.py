#usado para percorrer uma sequência de dados
#sintaxe: for 'iterável/variável de controle' in 'dado/range(se quiser definir um tamanho)':

#Exemplo 1
'''
cidades = ["Recife", "Olinda", "Jaboatão"]

for cidade in cidades:
    print(cidade)
''' 
#Exercício 1
'''
lista_compras = ['banana', 'ovos', 'leite', 'carne']
for item in lista_compras:
    print(item)
'''    
#Exercício 2 (usando if e break no for)
'''
lista_compras = ['banana', 'ovos', 'leite', 'carne']
for item in lista_compras:
    print(item)
    
    if item == 'ovos':
        break
'''
#usando continue no for
'''
paises_copa = ["Brasil", "Argentina", "Chile", "Equador"]
for pais in paises_copa:
    if pais == "Argentina":
        continue
    
    print(pais)
'''
#Range no for
'''
for i in range(2):
     print("Tabuada")


for i in range(1, 10):
    for x in range(1, 10):
        mult = i * x
        print(f"{i} x {x} = {mult}")
'''       
#Passo no range(exercício para imprimir números pares)
for i in range(0, 11, 2):
    print(i)