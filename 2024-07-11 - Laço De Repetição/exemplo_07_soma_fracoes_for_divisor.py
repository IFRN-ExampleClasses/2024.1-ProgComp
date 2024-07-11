'''
    Escreva um programa que calcule a seguinte soma :  

    soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
'''
soma      = 0
dividendo = 1

for divisor in range(1,51):
  termo = dividendo/divisor
  soma += termo
  print(f'Termo {dividendo}/{divisor} = {termo:.5f}')
  dividendo += 2

print(f'\nSoma final: {soma:.5f}')