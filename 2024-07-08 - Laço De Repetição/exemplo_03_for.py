'''
    Faça um programa que solicite um número inteiro e 
    exiba a seguinte saída (no exemplo o valor informado foi 4):

    0
    0 1
    0 1 2
    0 1 2 3
    0 1 2 3 4

    ATENÇÃO: A saída vai sempre iniciar em 0 
'''
import sys

numero = int(input('Digite um número inteiro: '))

if numero <= 0:
  sys.exit('ERRO: Informe um número positivo...')

for linha in range(numero + 1):
  for coluna in range(linha + 1):
    print(coluna, end=' ')
  print()