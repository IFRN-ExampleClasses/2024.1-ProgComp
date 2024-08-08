import os

# Obtendo o diretorio onde os arquivos estão
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

# ----------------------------------------------------------------------
# Abrindo o arquivo no modo somente leitura
arqEntrada = open(dirArquivos + '\\lista_uf_capitais_populacao.txt','r', encoding='utf-8')
lstUF = list()
cabecalhos = arqEntrada.readline()[:-1]
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
Criar um arquivo (populacao_crescimento.txt) com os nomes das capitais, 
seguidos dos nomes dos estados, a população de 2000, a população de 2022 e 
a taxa de crescimento da população entre o censo de 2000 e o de 2022 
(taxa de crescimento é o percentual de crescimento entre as duas populações) 
ordenando da capital que teve a maior taxa de crescimento até a que teve a 
menor taxa de crescimento. 

Os dados deverão ser separados por ;

Usar a função MAP() para gerar a lista com os dados necessários e a 
função SORT() para ordenar
'''



