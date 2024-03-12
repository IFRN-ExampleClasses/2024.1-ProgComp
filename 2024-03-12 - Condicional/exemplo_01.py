'''
Faça um programa que leia duas coordenadas (X e Y) de um ponto e informe:
    - Em qual quadrante do plano cartesiano ele está, ou;
    - Se ele está sobre um dos eixos (X ou Y) e se está no 
      lado positivo ou negativo do eixo, ou;
    - Se ele está na origem.
'''
coord_x = float(input('Informe a Coordenada X: '))
coord_y = float(input('Informe a Coordenada Y: '))

if coord_x > 0 and coord_y > 0:
    print(f'O ponto ({coord_x},{coord_y}) está no 1º Quadrante')
elif coord_x < 0 and coord_y > 0:
    print(f'O ponto ({coord_x},{coord_y}) está no 2º Quadrante')
elif coord_x < 0 and coord_y < 0:
    print(f'O ponto ({coord_x},{coord_y}) está no 3º Quadrante')
elif coord_x > 0 and coord_y < 0:
    print(f'O ponto ({coord_x},{coord_y}) está no 4º Quadrante')
elif coord_x > 0 and coord_y == 0:
    print(f'O ponto ({coord_x},{coord_y}) está no Eixo X Positivo')
elif coord_x < 0 and coord_y == 0:
    print(f'O ponto ({coord_x},{coord_y}) está no Eixo X Negativo')
elif coord_x == 0 and coord_y > 0:
    print(f'O ponto ({coord_x},{coord_y}) está no Eixo Y Positivo')
elif coord_x == 0 and coord_y < 0:
    print(f'O ponto ({coord_x},{coord_y}) está no Eixo Y Negativo')
else:
    print(f'O ponto ({coord_x},{coord_y}) está na Origem')
