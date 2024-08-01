import random

setValores = set()

contador = 1
while contador < 10000:
    valor = random.randint(1, 100001)
    setValores.add(valor)
    contador = len(setValores)

print(len(setValores))

