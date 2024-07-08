'''
    Fazer um programa que solicite um número e calcule o seu fatorial

    ATENÇÃO: Lembre-se das restrições para se calcular o fatorial
             de um número
'''
import sys

numero = int(input('Digite um número: '))

if numero < 0:
  sys.exit('ERRO: Número Inválido...')

fatorial = contador = 1
while contador <= numero:
  fatorial *= contador
  contador += 1

print(f'{numero}! = {fatorial}')