from nltk.corpus import stopwords
import pandas as pd
import requests
from bs4 import BeautifulSoup
import unicodedata
import re
import string
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import numpy as np
import math
import time

init = time.time()

arqLink = open('links.txt', 'r')
links = arqLink.readlines()

x = 0
y = 0
z = 0
termos = []
documentos = []

while x < len(links):
    if links[x] == "\n":
        local = links.index(links[x])
        links.pop(local)
    else:
        links[x] = links[x].split(',')
        x += 1


for y in range(len(links)):
    # for y in range(15):
    url = links[y][0].replace('\n', "")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.get_text()
    data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
    data = data.translate(string.maketrans('', ''), string.punctuation)
    data = re.sub('[0-9]', '', data)
    data = re.sub('\n', '', data)
    data = data.replace('\r', '')
    data = data.replace('\t', '')
    data = data.lower()
    data = data.split()

    stop_words = set(stopwords.words('portuguese'))

    stemmer = SnowballStemmer('portuguese')
    word_tokens = [stemmer.stem(data) for data in data]

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    while z < len(filtered_sentence):
        filtered_sentence[y].encode('ascii')
        z = z + 1

    nomeArq = 'sites/' + 'url_' + str(y + 1) + '.txt'
    documentos.append(nomeArq)
    arquivo = open(nomeArq, 'w')
    for i in range(len(filtered_sentence)):
        termos.append(filtered_sentence[i])
        arquivo.write(filtered_sentence[i] + "\n")
    arquivo.close()


chave = list(dict.fromkeys(termos))
chave.sort()
termos.sort()

g = 0
h = 0
j = 0
k = 0
freq = 0
n = len(documentos)

td = pd.DataFrame(data=None, index=documentos,
                  columns=chave, dtype=float, copy=False)

df = pd.DataFrame(data=None, index=documentos,
                  columns=chave, dtype=float, copy=False)


for g in range(len(documentos)):
    doc = open(documentos[g], 'r')
    docs = doc.readlines()
    for h in range(len(chave)):
        freq = docs.count(chave[h] + '\n')
        if freq > 0:
            td.ix[g, h] = 1 + math.log10(freq)
            df.ix[g, h] = float(1)
        else:
            td.ix[g, h] = float(0)
            df.ix[g, h] = float(0)
    doc.close()

df = df.sum(axis=0)

for k in range(len(df)):
    df[k] = float(math.log10(n/df[k]))

for g in range(len(documentos)):
    for h in range(len(chave)):
        td.ix[g, h] = td.ix[g, h] * df[h]

print(td)
fim = time.time()
tempo_total = fim - init
print(str(tempo_total) + ' Segundos')
