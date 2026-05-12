Turma_A = {"Jessé", "José", "Arthur", "Caio"}
Turma_B = {"Lukinhas", "Thomaz", "Pedro", "Cezário"}
Turma_A_B = Turma_A.union(Turma_B)

print(Turma_A_B)

#Verificando se há elemento em comum entre os conjuntos
Turma_B.update(["Jessé", "Arthur"])
IntersectionAB = Turma_A.intersection(Turma_B)
print(IntersectionAB)

#Verificando apenas os elementos de A que não estão em B
DifferenceAB = Turma_A.difference(Turma_B)
print(DifferenceAB)
