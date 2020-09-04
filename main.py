import pandas as pd
import requests
from bs4 import BeautifulSoup


arqLink = open('links.txt', 'r')
links = arqLink.readlines()

x = 0
y = 0

while x < len(links):
    if links[x] == "\n":
        local = links.index(links[x])
        links.pop(local)
    else:
        links[x] = links[x].split(',')
        x += 1


while y < len(links):
    site = links[y][0].replace('\n', "")
    url = site
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    data = soup.get_text()
    data_str = str(data.encode('utf-8'))
    data_str = data_str.replace("  ", ",")
    data_str = data_str.replace(" ", ",")
    data_str = data_str.replace("\n", ",")
    data_str = data_str.replace(".", ",")
    data_str = data_str.replace("?", ",")
    data_str = data_str.replace("!", ",")
    data_str = data_str.replace("@", ",")
    data_str = data_str.replace(";", ",")
    data_str = data_str.replace(":", ",")
    data_str = data_str.replace("/", ",")
    data_str = data_str.replace("\r", ",")
    data_str = data_str.replace('""', '')
    data_str = data_str.lower()
    data_list = data_str.split(',')
    data_list = list(filter(None, data_list))
    nomeArq = 'url_'
    arquivo = open('sites/' + nomeArq + str(y + 1) + '.txt', 'w')
    for i in range(len(data_list)):
        arquivo.write(data_list[i] + ",")
        arquivo.write("\n")
    y = y + 1
