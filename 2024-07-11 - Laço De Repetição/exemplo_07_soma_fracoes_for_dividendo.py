'''
    Escreva um programa que calcule a seguinte soma :  

    soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
'''
soma    = 0
divisor = 1

for dividendo in range(1,100,2):
  termo = dividendo/divisor
  soma += termo
  print(f'Termo {dividendo}/{divisor} = {termo:.5f}')
  divisor += 1

print(f'\nSoma final: {soma:.5f}')