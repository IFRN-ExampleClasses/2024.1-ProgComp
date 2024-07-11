'''
    Faça um programa que solicite um número inteiro e 
    exiba a seguinte saída (no exemplo o valor informado foi 4):

    0
    0 1
    0 1 2
    0 1 2 3
    0 1 2 3 4
    0 1 2 3
    0 1 2
    0 1
    0

    ATENÇÃO: A saída vai sempre iniciar em 0 
'''
import sys

numero = int(input("Digite um número inteiro: "))

if numero <= 0:
  sys.exit('ERRO: Informe um número positivo...')

linha = 0
while linha <= numero:
  coluna = 0
  while coluna < linha + 1:
    print(coluna, end=' ')
    coluna += 1
  print()
  linha += 1

linha -= 1
while linha > 0:
  coluna = 0
  while coluna < linha:
    print(coluna, end=' ')
    coluna += 1
  print()
  linha -= 1
