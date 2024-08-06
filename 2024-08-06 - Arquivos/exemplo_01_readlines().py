import os

# Obtendo o diretorio onde os arquivos estão
dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)

# Abrindo o arquivo no modo somente leitura
arqEntrada = open(dirArquivos + '\\lista_uf_capitais.txt','r', encoding='utf-8')

# Lendo o conteúdo do arquivo
conteudo = arqEntrada.readlines()

print(conteudo)

# Fechando o arquivo
arqEntrada.close()