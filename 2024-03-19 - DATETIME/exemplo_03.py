# https://docs.python.org/3/library/datetime.html
#from datetime import date
from datetime import *


dt_nasc  = datetime.strptime('10/11/1974', '%d/%m/%Y').date()
dt_atual = date.today()

idade = (dt_atual - dt_nasc).days

print(f'A data atual é: {dt_atual}')
print(f'Você nasceu em: {dt_nasc}')
print(f'Você tem {idade} dias')

# Calcular em anos????????
idade = int(round(idade / 365, 0))
print(f'Você tem {idade} anos')
