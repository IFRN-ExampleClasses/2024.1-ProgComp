'''
    Como fazer um programa para solicitar números inteiros 
    e ao término ele quando terminar, o programa deverá 
    informar quantos números foram informados, quantos são 
    positivos e quantos são negativos? 

    Sim, lembrando, ele vai ficar solicitando valores até que eu 
    informe o valor 0 (zero).
'''

cont_positivos = cont_negativos = 0

valor = int(input('Informe um número: '))

while valor != 0:
    if valor > 0:
        cont_positivos += 1
    else:
        cont_negativos += 1
    valor = int(input('Informe um número: '))
    

print(cont_positivos)
print(cont_negativos)
print(cont_positivos+cont_negativos)
