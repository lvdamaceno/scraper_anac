import os
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
folder = os.getcwd() + "/files_by_year"
os.mkdir(folder)

for year in years:
    concat_year_df = pd.DataFrame()
    for file in files:
        if file[4:8] == year:
            tempDf = pd.read_csv(f'files/{file}', encoding='ISO-8859-1', )
            # limite de 5 primeiras linhas
            concat_year_df = pd.concat([concat_year_df, tempDf.head(5)], ignore_index=True)
        concat_year_df.to_csv(f'{folder}/{year}.csv')
    print(f'Dataset {year}.csv salvo com sucesso.')
print('Finalizado')


