'''
    Como fazer um programa para solicitar um número entre 1 e 9 e 
    mostrar a sua tabuada de multiplicação?
'''
import sys

valor = int(input('Informe um valor: '))

if valor < 1 or valor > 9:
    print('ERRO: Valor Inválido...')
    print('      Informe um valor >= 1 e <= 9...')
    sys.exit()

mult = 1

print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1
print(f'{valor} * {mult} = {valor*mult}')
mult += 1