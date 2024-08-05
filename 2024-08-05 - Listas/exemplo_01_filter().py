import random

qt_elementos = 1000000

# Gerando uma lista de QT_ELEMENTOS valores entre 1 e 10000
'''
# O bloco a seguir pode ser substituido por uma LC (List Comprehension)
lista_valores = list()
for _ in range(qt_elementos):
    lista_valores.append(random.randint(1,10000))
'''
lista_valores = [random.randint(1, 10001) for _ in range(qt_elementos)]


# Extraindo apenas os valores pares usando LC (List Comprehension)
lista_par = [valor for valor in lista_valores if valor % 2 == 0]


# Extraindo apenas os valores pares usando a função FILTER() com LAMBDA
lista_par = list(filter(lambda valor: valor % 2 == 0, lista_valores))
