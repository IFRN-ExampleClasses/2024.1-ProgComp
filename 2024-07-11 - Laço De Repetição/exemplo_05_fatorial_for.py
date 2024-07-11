'''
    Fazer um programa que solicite um número calcule o fatorial 
    de cada número entre 0 e o número informado

    ATENÇÃO: Lembre-se das restrições para se calcular o fatorial
             de um número
'''
import sys

numero = int(input('Digite um número inteiro não-negativo: '))

if numero <= 0:
  sys.exit('ERRO: Informe um número positivo...')
  
for i in range(numero + 1):
  fatorial = 1
  for j in range(1, i + 1):
    fatorial *= j
  print(f"{i}! = {fatorial}")

