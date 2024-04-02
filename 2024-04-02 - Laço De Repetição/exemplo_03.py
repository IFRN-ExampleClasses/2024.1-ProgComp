'''
    Como fazer um programa para solicitar números inteiros 
    e somar apenas os 10 primeiros números positivos?
'''

soma_positivos = 0
cont_positivos = 1
contador       = 1

while cont_positivos <= 10:
    valor = int(input(f'Informe o {contador}º valor: '))
    if valor > 0:
        soma_positivos += valor
        cont_positivos += 1
    contador += 1
    
print(f'A soma dos positivos é {soma_positivos}')