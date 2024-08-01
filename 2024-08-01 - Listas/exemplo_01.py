import random

lstValores = list()

contador = 1
while contador <= 10000:
    valor = random.randint(1, 100001)
    if valor not in lstValores:
        lstValores.append(valor)
        contador += 1

print(len(lstValores))

