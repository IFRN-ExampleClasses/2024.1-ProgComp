import os

# Obtendo o diretorio onde os arquivos estão
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

# ----------------------------------------------------------------------
# Abrindo o arquivo no modo somente leitura
arqEntrada = open(dirArquivos + '\\lista_uf_capitais_populacao.txt','r', encoding='utf-8')
lstUF = list()
cabecalhos = arqEntrada.readline()[:-1]
cabecalhos = cabecalhos.split(';')
while True:
    # Lendo o conteúdo do arquivo
    linha = arqEntrada.readline()
    if linha[-1:] == '\n': linha = linha[:-1]
    # Interrompendo a leitura quando chegar ao final do arquivo
    if not linha: break
    # Adicionando a linha lida a uma lista
    lstUF.append(linha.split(';'))
# Fechando o arquivo
arqEntrada.close()
# ----------------------------------------------------------------------

'''
Criar um arquivo (populacao_2022.txt) com os nomes das capitais, 
seguidos dos nomes dos estados e a população do ano de 2022, 
ordenando da capital mais populosa até a menos populosa. Os dados
deverão ser separados por ;
'''

'''
# Usando FOR
lstPopulacao = list()
for v in lstUF:
    lstPopulacao.append([v[1], v[0], int(v[2])])

# Usando List Comprehensions
lstPopulacao = [[v[1], v[0], int(v[2])] for v in lstUF]
'''

# Usando MAP()
lstPopulacao = list(map(lambda v: [v[1], v[0], int(v[2])], lstUF))

# Ordenar lstPopulacao
lstPopulacao.sort(key=lambda v:v[2], reverse=True)

# Escrevendo o arquivo de saída (populacao_2022.txt)
arqSaida = open(dirArquivos + '\\populacao_2022.txt','w', encoding='utf-8')
arqSaida.write(f'{cabecalhos[1]};{cabecalhos[0]};{cabecalhos[2]}\n')
for v in lstPopulacao:
    arqSaida.write(f'{v[0]};{v[1]};{v[2]}\n')
arqSaida.close()
