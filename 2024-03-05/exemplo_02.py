'''
Fazer um programa que calcule a média do IFRN.
Considere que a disciplina seja semestral.
'''

nota_1 = int(input('Informe a 1ª Nota: '))
nota_2 = int(input('Informe a 2ª Nota: '))

media = (nota_1*2 + nota_2*3) / 5

print(f'Média Parcial: {media}')
print(f'Média Parcial: {media:.0f}')

print('-'*50)
print(f'Média Parcial: {media}')
media = int(round(media, 0))
print(f'Média Parcial: {media}')
