import requests
import wget
import time
import os
from bs4 import BeautifulSoup


def request_page(url):
    # captura todas as tags a href da pagina inicial
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tag_pre = soup.find_all('pre')
    tag_a = tag_pre[0].find_all('a')
    return tag_a


def get_links(data, url):
    # cria uma lista apenas com os links tratados
    data_links = []
    for item in range(len(data)):
        text = data[item].get_text()
        data_links.append(url + text)
    return data_links


def get_files(data, folder, link):
    for item in range(len(data)):
        text = data[item].get_text()
        start_timer = time.perf_counter()
        wget.download(link + '/' + text, folder)
        end_timer = time.perf_counter()
        print(f"Download de {text} em {end_timer - start_timer:0.4f} segundos")


def main():
    url_anac = 'https://sas.anac.gov.br/sas/vraarquivos/'
    data_anac = request_page(url_anac)
    data_links = get_links(data_anac, url_anac)
    # cria pasta para os arquivos .csv
    folder = os.getcwd() + "/files"
    os.mkdir(folder)
    for link in data_links[1:-1]:
        data = request_page(link)[1:]
        get_files(data, folder, link)


if __name__ == "__main__":
    main()
