'''
    Escreva um programa que solicite um valor n inteiro e positivo 
    e que calcula a seguinte soma:  

    S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    O programa deve escrever cada termo gerado e o valor final 
    de S.
'''
import sys

numero = int(input('Digite um valor n inteiro e positivo: '))

if numero <= 0:
  sys.exit('ERRO: Informe um número inteiro e positivo...')

soma = 0

for i in range(1, numero + 1):
  termo = 1 / i
  soma += termo
  print(f'Termo {i} -> 1/{i} = {termo:.5f}')

print(f'\nSoma final: {soma:.5f}')