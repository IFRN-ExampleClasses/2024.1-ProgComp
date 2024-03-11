'''
Como obter separadamente quociente e o resto de uma divisão??????
'''

dividendo = int(input('Informe o DIVIDENDO: '))
divisor   = int(input('Informe o DIVISOR..: '))

resultado = dividendo / divisor

print(f'Resultado: {resultado}')

quociente = int(resultado)
print(f'Quociente: {quociente}')

resto = dividendo - (divisor * quociente)
print(f'Resto....: {resto}')