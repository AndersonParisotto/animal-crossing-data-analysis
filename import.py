import pandas as pd
#leitura de múltiplos arquivos CSV em um único DataFrame
import glob

#definindo o caminho onde os arquivos CSV estão localizados
path = './dados'
all_files = glob.glob(path + "/*.csv")

#criando um dicionário para armazenar os DataFrames
dataframe = {}
for filename in all_files:
    #extraindo o nome do arquivo sem a extensão para usar como chave no dicionário
    name - filename.split('/')[-1].split('.')[0]
    #lendo o arquivo CSV e armazenando no dicionário
    dataframe[name] = pd.read_csv(filenbame, index_col=None, header=0)

#imprimindo as chaves do dicionário para verificar os DataFrames carregados
print(dataframe.keys())

#verificando se os DataFrames foram carregados corretamente
if not dataframes:
    #caso nenhum arquivo tenha sido carregado
    print("Nenhum arquivo CSV foi carregado.")
else:
    #imprimindo o número de linhas e colunas de cada DataFrame
    for name, df in dataframe.items():
        print(f"DataFrame '{name}' carregado com {len(df)} linhas e {len(df.columns)} colunas.")