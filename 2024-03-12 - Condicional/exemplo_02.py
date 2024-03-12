'''
Faça um programa que leia os valores de a, b e c e 
calcule as raízes de uma equação do 2º grau. 
Lembrando que para ser uma equação do 2º grau,
o valor de a não pode ser 0 (zero);
'''
import sys

a = float(input('Informe o valor de A: '))

if a == 0:
    print('O valor de A não pode ser ZERO!!!!')
    sys.exit()

b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('A equação não possui solução real !!!')
elif delta > 0:
    x_1 = (-b + delta**0.5)/(2*a)
    x_2 = (-b - delta**0.5)/(2*a)
    print('A equação possui duas soluções reais !!!')
    print(f'X1 = {x_1} e X2 = {x_2}')
else:
    x = (-b + delta**0.5)/(2*a)
    print('A equação possui uma solução real !!!')
    print(f'X1 = X2 = {x}')
