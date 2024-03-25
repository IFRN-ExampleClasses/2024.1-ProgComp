# https://docs.python.org/3/library/datetime.html
#from datetime import date
from datetime import *

#https://pypi.org/project/python-dateutil/
# pip install python-dateutil
from dateutil.relativedelta import relativedelta

dt_nasc  = datetime.strptime('10/11/1974', '%d/%m/%Y').date()
dt_atual = date.today()

dias = (dt_atual - dt_nasc).days

print(f'A data atual é: {dt_atual}')
print(f'Você nasceu em: {dt_nasc}')
print(f'Você tem {dias} dias')

# Calcular em anos, meses e dias ????????
anos = dias // 365
dias = dias % 365 

meses = dias // 30
dias  = dias % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias')


# Calcular em anos, meses e dias ???????? (versãomon 2)
dif_data = relativedelta(dt_atual, dt_nasc)
anos  = dif_data.years
meses = dif_data.months
dias  = dif_data.days
print(f'Você tem {anos} anos, {meses} meses e {dias} dias')
