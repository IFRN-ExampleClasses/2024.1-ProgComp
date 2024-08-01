import random

lstValores = list()

lstValores = [random.randint(1, 101) for _ in range(1000)]

setUnicos = set(lstValores)

print(len(lstValores))
print(len(setUnicos))