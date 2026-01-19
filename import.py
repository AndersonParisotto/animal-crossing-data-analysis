#código para importar múltiplos arquivos CSV de uma pasta usando pandas
import pandas as pd
#biblioteca para manipulação de arquivos e diretórios
import glob
#biblioteca para operações do sistema operacional
import os

#definindo o caminho da pasta onde os arquivos CSV estão localizados
path = './dados' 
#usando glob para encontrar todos os arquivos CSV na pasta especificada
all_files = glob.glob(path + "/*.csv")

#criando um dicionário para armazenar os dataframes
dataframes = {}
#lendo cada arquivo CSV e armazenando no dicionário com o nome do arquivo como chave
for filename in all_files:
    #extraindo o nome do arquivo sem a extensão para usar como chave
    name = os.path.basename(filename).replace('.csv', '')
    #lendo o arquivo CSV e armazenando no dicionário
    dataframes[name] = pd.read_csv(filename)

#verificando os nomes dos dataframes importados
print(dataframes.keys()) 

#verificando o número de linhas e colunas de cada dataframe
if not dataframes:
    print("Erro: Nenhum arquivo CSV encontrado. Verifique o caminho da pasta!")
else:
    #iterando sobre o dicionário para imprimir o tamanho de cada dataframe
    for nome, df in dataframes.items():
        print(f"Tabela: {nome} | Linhas: {len(df)} | Colunas: {len(df.columns)}")