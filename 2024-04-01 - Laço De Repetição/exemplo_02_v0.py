'''
    Como fazer um programa para solicitar 10 números e imprimir 
    a soma deles? E a quantidade de números pares? E a quantidade 
    de números ímpares?
'''

soma_valores = 0
qte_pares    = 0
qte_impares  = 0
contador     = 1

# Lendo 1º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 2º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 3º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 4º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 5º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 6º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 7º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 8º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 9º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Lendo 10º Valor
valor = int(input(f'Informe o {contador}º valor:'))
soma_valores += valor
if valor % 2 == 0:
    qte_pares += 1
else:
    qte_impares += 1
contador += 1

# Imprimindo os resultados
print(f'A soma dos valores foi {soma_valores}')
print(f'A quantidade de números pares foi {qte_pares}')
print(f'A quantidade de números ímpares foi {qte_impares}')