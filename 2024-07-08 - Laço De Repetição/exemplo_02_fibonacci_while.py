'''
    Faça um programa que exiba a Sequência de Fibonacci. 
    O programa deverá solicitar um número que será a quantidade
    de elementos da Sequência de Fibonacci.

    ATENÇÃO: Considere que a Sequência de Fibonacci irá iniciar em 1 
'''
import sys

print('\nSequência de Fibonacci\n')
numero = int(input('Digite a quantidade de elementos: '))

if numero <= 0:
  sys.exit('ERRO: Informe um número positivo...')

anterior = 0
atual    = 1
contador = 0

while contador < numero:
  print(atual, end = ', ')
  anterior, atual = atual, anterior + atual
  contador += 1