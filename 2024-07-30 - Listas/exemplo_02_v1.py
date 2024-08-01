lstAlunos = list()

while True:
    strMatricula = input('\nInforme a matrícula do aluno: ')
    strNome      = input('Informe o nome do aluno......: ')
    intIdade     = int(input('Informe a idade do aluno.....: '))

    lstAlunos.append([strMatricula, strNome, intIdade])

    strContinua  = input('\nDeseja informa novo aluno? ').lower()
    if strContinua == 'n': break

print(lstAlunos)