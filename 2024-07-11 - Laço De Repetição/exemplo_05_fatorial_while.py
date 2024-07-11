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
  
i = 0
while i <= numero:
  fatorial = j = 1
  while j <= i:
    fatorial *= j
    j += 1
  print(f'{i}! = {fatorial}')
  i += 1
