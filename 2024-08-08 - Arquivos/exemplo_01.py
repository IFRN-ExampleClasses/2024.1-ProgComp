import os

# Obtendo o diretorio onde os arquivos estão
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

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

# Exibindo os dados lidos
print(lstUF)

