'''
Fazer um programa que solicite ao usuário um número inteiro
e diga ao usuário se o número é par positivo, par negativo,
ímpar positivo, ímpar negativo ou se é nulo
'''
numero = int(input('Informe um valor inteiro: '))

if numero > 0:
    print('O Número informado é POSITIVO...')
    if numero % 2 == 0:
        print('O Número informado é PAR...')
    else:
        print('O Número informado é ÍMPAR...')
elif numero < 0:
    print('O Número informado é NEGATIVO...')
    if numero % 2 == 0:
        print('O Número informado é PAR...')
    else:
        print('O Número informado é ÍMPAR...')
else:
    print('O Número informado é NULO...')
