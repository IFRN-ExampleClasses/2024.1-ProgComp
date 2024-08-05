import random

qt_elementos = 1000000

# Gerando uma lista de QT_ELEMENTOS valores entre 1 e 10000
lista_valores = [random.randint(1, 10001) for _ in range(qt_elementos)]

# Encontre valores únicos em lista_valores
valores_unicos = set(lista_valores)

# Gerando a lista LISTA_RET usando LC (List Comprehension)
lista_ret = [ [valor, lista_valores.count(valor)] for valor in lista_valores]

# Gerando a lista LISTA_RET usando MAP() com a função LAMBDA
lista_ret = list(map(lambda x: [x, lista_valores.count(x)], valores_unicos))