#AND, NOT, OR
#NOT inverte
#AND faz com que todas as condições sejam verdadeiras
#OR se pleo menos uma condição for verdadeira

#NOT:
chuva = False
if not chuva:
    print("está chovendo!")
else:
    print("ñ está chovendo!")

#AND
a = "carro"
b = "moto"

if (a == "carro" and b == "moto"):
    print("candidato optou pelo exame AB")
else:
    print("o candidato não optou o exame AB")

#OR
weekend = ["sabado", "domingo"]
dia = "sabado"

if (dia == "sabado" or dia == "domingo"):
    print("é dia de semana.")