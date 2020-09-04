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


arqLink = open('links.txt', 'r')
links = arqLink.readlines()

x = 0
y = 0
z = 0


while x < len(links):
    if links[x] == "\n":
        local = links.index(links[x])
        links.pop(local)
    else:
        links[x] = links[x].split(',')
        x += 1


for y in range(len(links)):
    url = links[y][0].replace('\n', "")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.get_text()
    data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
    data = data.translate(string.maketrans('', ''), string.punctuation)
    data = re.sub('[0-9]', '', data)
    data = re.sub('\n', '', data)
    data = data.replace('\r', '')
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

    nomeArq = 'url_'
    arquivo = open('sites/' + nomeArq + str(y + 1) + '.txt', 'w')
    for i in range(len(filtered_sentence)):
        arquivo.write(filtered_sentence[i] + ",")
        arquivo.write("\n")
# --------------------------------------------------------------------------
