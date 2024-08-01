lstNum = list()

while True:
    intNumero = int(input('Digite um número: '))
    if intNumero == 0: break
    lstNum.append(intNumero)

soma   = sum(lstNum)
media  = soma/len(lstNum)

lstNumOrd = sorted(lstNum) 

print(f'\nA soma dos valores é {soma}')
print(f'\nA média dos valores é {media}')
print(f'\nOS valores informados foram: {lstNum}')
print(f'\nOS valores ordenados são: {lstNumOrd}')