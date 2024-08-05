import random

qt_elementos = 1000000

# Gerando uma lista de QT_ELEMENTOS valores entre 1 e 10000
lista_valores = [random.randint(1, 10001) for _ in range(qt_elementos)]

# Calculando a raiz quadrada de cada elemento usando LC (List Comprehension)
lista_raiz = list()
for valor in lista_valores:
    lista_raiz.append(valor ** 0.5)

# Calculando a raiz quadrada de cada elemento usando LC (List Comprehension)
lista_raiz = [valor ** 0.5 for valor in lista_valores]

# Calculando a raiz quadrada de cada elemento usando a função MAP() com uma função LAMBDA
lista_raiz = list(map(lambda valor: valor ** 0.5, lista_valores))