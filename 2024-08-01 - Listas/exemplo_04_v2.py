import random

lstValores = list()

lstValores = [random.randint(1, 101) for _ in range(1000)]

setUnicos = set(lstValores)

lstAux = [ [i, lstValores.count(i)] for i in setUnicos]

print(lstAux)