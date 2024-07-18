import sys

# --------------------------------------------------
# Informando o CPF a ser validado
cpf = input('\nInforme o CPF: ')

# --------------------------------------------------
# Validando a entrada
if not cpf.isdigit():
    sys.exit('ERRO: Informe apenas números...')
elif len(cpf) != 11:
    sys.exit('ERRO: Informe exatamente 11 dígitos...')

# --------------------------------------------------
# Validando o 1º dígito (d1)
d1 = 0
for i in range(len(cpf)-2):
    d1 += int(cpf[i]) * (10-i)

d1 = 0 if (d1*10 % 11) == 0 else (d1*10 % 11)

if str(d1) != cpf[len(cpf)-2]:
    sys.exit(f'\nERRO: O CPF {cpf} é INVÁLIDO (1º dígito)...')

# --------------------------------------------------
# Validando o 2º dígito
d2 = 0
for i in range(len(cpf)-1):
    d2 += int(cpf[i]) * (11-i)

d2 = 0 if (d2*10 % 11) == 0 else (d2*10 % 11)

if str(d2) != cpf[len(cpf)-1]:
    sys.exit(f'\nERRO: O CPF {cpf} é INVÁLIDO (2º dígito)...')

# --------------------------------------------------
# Se chegou aqui o CPF é válido
print(f'\nSUCESSO: O CPF {cpf} é VÁLIDO...\n')