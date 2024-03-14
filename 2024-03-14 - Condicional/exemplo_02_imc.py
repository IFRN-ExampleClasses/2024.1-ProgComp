import sys

idade  = int(input('Informe a Idade.......: '))
if idade < 18:
    print('Idade Inválida...')
    print('A Idade tem de ser positiva e ser no mínimo 18!!!')
    sys.exit()

peso = float(input('Informe o peso (kg)...: '))
if peso <= 0:
    print('Peso Inválido...')
    print('O peso tem de ser positivo!!!')
    sys.exit()

altura = float(input('Informe sua altura (m): '))
if altura <= 0:
    print('Altura Inválida...')
    print('A altura tem de ser positiva!!!')
    sys.exit()

imc = round(peso / (altura**2), 1)
print(f'IMC = {imc}')

if imc >= 40:
    print('Obesidade Grau III (Mórbida)...')
elif imc >= 35:
    print('Obesidade Grau II ...')
elif imc >= 30:
    print('Obesidade Grau I ...')
elif imc >= 25:
    print('Sobrepeso ...')
elif imc >= 18.5:
    print('Peso Normal ...')
else:
    print('Abaixo do Peso ...')