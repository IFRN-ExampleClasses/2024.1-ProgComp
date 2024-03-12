'''
Um trio de Pitágoras é formado por três números naturais positivos, 
tal que:
    a**2 + b**2 = c**2

Faça um programa que solicite os valores de a, b e c 
e informe se eles formam um Trio Pitagórico.
'''

a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

if a > 0 and b > 0 and c > 0:
    if (a**2 + b**2) == (c**2):
        print(f'Os valores {a}, {b} e {c} formam um triângulo pitagórico!!!')
    else:
        print(f'Os valores {a}, {b} e {c} não formam um triângulo pitagórico!!!')
else:
    print('Valores inválidos!!!')