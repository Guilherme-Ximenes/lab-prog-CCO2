nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    diagnostico = "Abaixo do peso"
    mensagem = "Cuidado, consulte um profissional de saúde!"
#Os "elifs" só serão executados se a condição anterior for falsa
elif imc < 25:
    diagnostico = "Peso normal"
    mensagem = "Tranquilo, continue cuidando da sua saúde!"
elif imc < 30:
    diagnostico = "Sobrepeso"
    mensagem = "Um pouco preocupante, é melhor ficar em alerta!"
elif imc < 35:
    diagnostico = "Obesidade grau I"
    mensagem = "Atenção, é importante cuidar da saúde!"
elif imc < 40:
    diagnostico = "Obesidade grau II"
    mensagem = "Atenção, já tá perigoso!"
else:
    diagnostico = "Obesidade grau III (mórbida)"
    mensagem = "Atenção extrema, cuide da sua saúde urgentemente!"

print(f"\n====Cálculo do IMC====\n")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f} - {diagnostico} - {mensagem}")