# https://docs.python.org/3/library/datetime.html
from datetime import date


ano_nasc = int(input('Informe o ano do seu nascimento: '))

ano_atual = date.today().year 
idade     = ano_atual - ano_nasc
print(f'Você tem {idade} anos')