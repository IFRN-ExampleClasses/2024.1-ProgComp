lstAlunos = list()

while True:
    strMatricula = input('\nInforme a matrícula do aluno: ')
    strNome      = input('Informe o nome do aluno.....: ')
    intIdade     = int(input('Informe a idade do aluno....: '))

    lstAlunos.append([strMatricula, strNome, intIdade])

    strContinua = ' '
    while strContinua not in 'sn':
        strContinua  = input('\nDeseja informa novo aluno? ').lower()
    if strContinua == 'n': break
    
lstAlunos.sort(key=lambda x:x[1])

print(lstAlunos)