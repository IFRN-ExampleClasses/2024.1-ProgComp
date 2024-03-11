'''
Fazer um programa que solicite ao usuário um número inteiro
e diga ao usuário se o número é par positivo, par negativo,
ímpar positivo, ímpar negativo ou se é nulo
'''
numero = int(input('Informe um valor inteiro: '))

if numero > 0 and numero % 2 == 0:
    print('O Número informado é POSITIVO...')
    print('O Número informado é PAR...')
elif numero > 0 and numero % 2 == 1:
    print('O Número informado é POSITIVO...')    
    print('O Número informado é ÍMPAR...')
elif numero < 0 and numero % 2 == 0:
    print('O Número informado é NEGATIVO...')
    print('O Número informado é PAR...')
elif numero < 0 and numero % 2 == 1:
    print('O Número informado é NEGATIVO...')
    print('O Número informado é ÍMPAR...')
else:
    print('O Número informado é NULO...')
