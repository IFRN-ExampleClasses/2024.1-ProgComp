import os

# Obtendo o diretorio onde os arquivos estão
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

# Abrindo o arquivo no modo somente leitura
arqEntrada = open(dirArquivos + '\\lista_uf.txt','r', encoding='utf-8')

while True:
    # Lendo o conteúdo do arquivo
    linha = arqEntrada.readline()
    if linha[-1:] == '\n': linha = linha[:-1]

    # Interrompendo a leitura quando chegar ao final do arquivo
    if not linha: break
    
    print(linha)

# Fechando o arquivo
arqEntrada.close()