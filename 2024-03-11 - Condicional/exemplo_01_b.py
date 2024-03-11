'''
Fazer um programa que calcule a média do IFRN.
Considere que a disciplina seja semestral.
'''

nota_1 = int(input('Informe a 1ª Nota: '))
nota_2 = int(input('Informe a 2ª Nota: '))

media = (nota_1*2 + nota_2*3) / 5

print('-'*50)
print(f'Média Parcial (Calculada)..: {media}')
media = int(round(media, 0))
print(f'Média Parcial (Arredondada): {media}')

# Imprimir se o aluno foi aprovado, está em
# prova final ou foi reprovado
if media >= 60:
    print('O aluno foi APROVADO DIRETO...')
    print('PARABÉNS !!!!!!!')
elif media >= 20:
    print('O aluno está em PROVA FINAL...')
    print('TEM DE ESTUDAR !!!!!!!')
else:
    print('O aluno foi REPROVADO DIRETO...')
    print('VAI REPETIR A DISCIPLINA !!!!!!!')
