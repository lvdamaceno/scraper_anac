from os import listdir
from os.path import isfile, join
import pandas as pd


def files_list(path):
    files_names = [file_name for file_name in listdir(path) if isfile(join(path, file_name))]
    files_names.sort()
    return files_names


def year_list(path):
    files_names = [file_name for file_name in listdir(path) if isfile(join(path, file_name))]
    all_names = [item[4:8] for item in files_names]
    filtered_years = list(set(all_names))
    filtered_years.sort()
    return filtered_years


files = files_list('files')
years = year_list('files')

concat_year_df = pd.DataFrame(columns=['ICAO Empresa Aérea', 'Número Voo', 'Código Autorização (DI)', 'Código Tipo Linha',
                                     'ICAO Aeródromo Origem', 'ICAO Aeródromoo Destino', 'Partida Prevista',
                                     'Partida Real', 'Chegada Prevista', 'Chegada Real', 'Situação Voo',
                                     'Código Justificativa'])
for file in files:
    if file[4:8] == years[0]:
        tempDf = pd.read_csv(f'files/{file}', encoding='ISO-8859-1')
        # limite de 100 primeiras linhas
        concat_year_df = pd.concat([concat_year_df, tempDf.head(10)], ignore_index=True)
    concat_year_df.to_csv(f'{years[0]}.csv')

print(concat_year_df)
