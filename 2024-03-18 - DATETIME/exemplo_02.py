# https://docs.python.org/3/library/datetime.html
#from datetime import date
from datetime import *

dt_nasc  = datetime.strptime('10/11/1974', '%d/%m/%Y').date()

dt_atual = date.today()
print(dt_nasc , type(dt_nasc))
print(dt_atual, type(dt_atual))
idade = (dt_atual - dt_nasc).days
print(f'Você tem {idade} dias')

# Calcular em anos????????