'''
Fazer um programa que calcule a área de um trapézio
'''

bMenor = float(input('Informe a Base Menor: '))
bMaior = float(input('Informe a Base Maior: '))
altura = float(input('Informe a Altura....: '))

area = ((bMenor + bMaior) * 2) / 2

print(f'A área do trapézio é {area:.3f}')