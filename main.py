import pandas as pd
import requests
import math
from bs4 import BeautifulSoup
import unicodedata
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from interface import *
from backend import *

app = None
app = Interface()
app.run()

arqLink = open(Interface.carregar(), 'r')
print('Arquivos carregados')
links = arqLink.readlines()


while True:
    if Backend.flag == 1:
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

        # for y in range(len(links)):
        for y in range(5):
            url = links[y][0].replace('\n', "")
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            data = soup.get_text()
            data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
            data = str(data)
            data = data.replace('!', '')
            data = data.replace('"', '')
            data = data.replace('#', '')
            data = data.replace('$', '')
            data = data.replace('%', '')
            data = data.replace('&', '')
            data = data.replace("'", '')
            data = data.replace('(', '')
            data = data.replace(')', '')
            data = data.replace('*', '')
            data = data.replace('+', '')
            data = data.replace(',', '')
            data = data.replace('/', '')
            data = data.replace('-', '')
            data = data.replace('.', '')
            data = data.replace(':', '')
            data = data.replace('\\', '')
            data = data.replace(';', '')
            data = data.replace('<', '')
            data = data.replace('=', '')
            data = data.replace('>', '')
            data = data.replace('?', '')
            data = data.replace('@', '')
            data = data.replace('[', '')
            data = data.replace(']', '')
            data = data.replace('^', '')
            data = data.replace('_', '')
            data = data.replace('`', '')
            data = data.replace('{', '')
            data = data.replace('|', '')
            data = data.replace('}', '')
            data = data.replace('~', '')
            data = re.sub('[0-9]', '', data)
            data = data.replace('\\n', '')
            data = data.replace('\\r', '')
            data = data.replace('\\t', '')
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
                    td.iloc[g, h] = 1 + (math.log10(freq))
                    df.iloc[g, h] = 1
                else:
                    td.iloc[g, h] = 0
                    df.iloc[g, h] = 0
            doc.close()

        df = df.sum(axis=0)

        soma_df = 0

        for k in range(len(df)):
            soma_df = math.log10(n / df[k])
            df[k] = soma_df

        for g in range(len(documentos)):
            for h in range(len(chave)):
                td.iloc[g, h] = td.iloc[g, h] * df[h]

        chave_de_busca = Backend.chave
        print('Chave capturada')
        print(Backend.chave)
        chave_de_busca = chave_de_busca.lower()
        chave_de_busca = chave_de_busca.split()

        chave_tratada = []

        for h in range(len(chave)):
            exist = chave_de_busca.count(chave[h])
            if exist != 0:
                chave_tratada.append(1)
            else:
                chave_tratada.append(0)

        soma_q = 0
        soma_d = []
        soma = 0
        produto_escalar = []

        for h in range(len(chave_tratada)):
            soma_q = soma_q + (chave_tratada[h] * chave_tratada[h])

        soma_q = math.sqrt(soma_q)

        for g in range(len(documentos)):
            for h in range(len(chave_tratada)):
                soma = soma + (td.iloc[g, h] * td.iloc[g, h])
            soma = math.sqrt(soma)
            soma_d.append(soma)

        td.loc['CHAVE DE BUSCA'] = chave_tratada

        for h in range(len(chave)):
            td.iloc[-1, h] = td.iloc[-1, h] * df[h]

        for g in range(len(documentos)):
            for h in range(len(chave_tratada)):
                soma = soma + (td.iloc[g, h] * td.iloc[-1, h])
            produto_escalar.append(soma)

        produto_escalar.pop()
        produto_escalar.append(1)

        cos = []

        par_chave_valor = {}

        for h in range(len(produto_escalar)):
            cos.append(produto_escalar[h] / (soma_q * soma_d[h]))
            par_chave_valor[links[h][0].replace('\n', "")] = cos[h]

        cos.pop()
        cos.sort(reverse=True)

        par_chave_valor = sorted(par_chave_valor.items(),
                                 key=lambda x: x[1], reverse=True)

        Backend.lista = par_chave_valor

        print(par_chave_valor[0])
        print(par_chave_valor[1])
        print(par_chave_valor[2])
        print(par_chave_valor[3])
        print(par_chave_valor[4])
        print(Backend.lista)


