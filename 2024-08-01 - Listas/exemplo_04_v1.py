import random

lstValores = list()

lstValores = [random.randint(1, 101) for _ in range(1000)]

setUnicos = set(lstValores)

lstAux = list()
for i in setUnicos:
    lstAux.append([i, lstValores.count(i)])

print(lstAux)