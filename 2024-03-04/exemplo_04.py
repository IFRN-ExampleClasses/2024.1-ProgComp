'''
Calcular a distância entre dois pontos no plano cartesiano
'''

x1 = float(input('Informe a coordenada X de P1: '))
y1 = float(input('Informe a coordenada Y de P1: '))

x2 = float(input('Informe a coordenada X de P2: '))
y2 = float(input('Informe a coordenada Y de P2: '))

d = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)

print(f'A distância entre os pontos ({x1},{y1}) e ({x2},{y2}) é igual a {d:.3f}')