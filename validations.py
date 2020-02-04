import os
import pandas as pd

# navigate do files directory
os.chdir('files')


filename = "VRA_20001.csv"
# encoding para evitar erro ao ler o csv com utf-8
data = pd.read_csv(filename, encoding='cp1252')
# retira as linhas com colunas de data vazia
filtered_data = data[data[['Partida Prevista', 'Partida Real', 'Chegada Prevista', 'Chegada Real']].notnull().all(1)]
# volta para a pasta inicial do projeto
os.chdir('..')
# cria uma pasta para os arquivos processados
folder = os.getcwd() + "/filtered_files"
os.mkdir(folder)
# exporta do dataframe para um arquivo .csv
filtered_data.to_csv(folder + '/' + filename)