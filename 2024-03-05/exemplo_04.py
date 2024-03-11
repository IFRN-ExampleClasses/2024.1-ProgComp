'''
Como obter separadamente quociente e o resto de uma divisão??????
'''

dividendo = int(input('Informe o DIVIDENDO: '))
divisor   = int(input('Informe o DIVISOR..: '))

quociente = dividendo // divisor
print(f'Quociente: {quociente}')

resto = dividendo % divisor
print(f'Resto....: {resto}')