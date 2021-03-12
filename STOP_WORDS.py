import math
import nltk
#nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords


# constantes #######################
ALFABETO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
ALFABETO_LOW = [i.lower() for i in ALFABETO]
PONTUACAO = ['.', ',', ';', '(', ')', '-', '+', '[', ']', '{', '}', '/', '?', '\n', '\x97', '!']
####################################


# funções ##########################
def clean(text):
    '''
    função que transforma todos os caracteres em
    minúsculos e retira os sinais de pontuação
    :param text: str
    :return: str
    '''
    text = text.lower()
    texto = ''
    for char in text:
        if char not in PONTUACAO:
          texto += char

    text = texto
    return text


def identifica_stopword(texto):
    '''
    função que, a partir de um texto, faz um cálculo
    de frequência e identifica possíveis 'stopwords'
    :param texto: str
    :return: list
    '''
    tx = clean(texto)
    t = tx.split()
    words = {}
    milokov = {}

    for word in t:
        if word not in PONTUACAO:
            if word[-1] in PONTUACAO:
                w = word.replace(word[-1], '')
                t[t.index(word)] = w
            if word.lower() not in words:
                words[word.lower()] = 1
            else:
                words[word.lower()] += 1

    sort_words = sorted(words.items(), key=lambda x: x[1], reverse=True)

    for word, frequency in sort_words:
        milokov[word] = (math.sqrt((10 ** (-5)) / frequency))

    media = 0
    for word in milokov:
        media += milokov[word]
    media = media / len(milokov)

    stops = []

    for word in milokov:
        if milokov[word] < media / 7:
            stops.append(word)

    return stops


# leitura de um arquivo, geração de uma string
# e identificação de possíveis 'stopwords'
t = open('Frankenstein.txt', 'r', errors='ignore')
texto = t.read()
STOPWORDS = identifica_stopword(texto)


def remove(text):
    '''
    função que lê um texto, passado como parâmetro,
    e remove 'stopwords' e pontuações
    :param text: str
    :return: str
    '''
    tx = text.split()

    for word in tx:
        if word[-1] in PONTUACAO:
            w = word.replace(word[-1], '')
            tx[tx.index(word)] = w
        if word.lower() in STOPWORDS:
            tx.pop(tx.index(word))

    return tx


#########################################


# testes #################################
if __name__ == "__main__":
    '''
    as 'stopwords' do nltk foram utilizadas
    nesse trecho de código apenas para validar
    a geração com o algoritmo desenvolvido.
    '''
    print(len(stopwords.words('english')))
    print(stopwords.words('english'))

    print(len(STOPWORDS))
    print(STOPWORDS)

    for word in STOPWORDS:
        if word not in stopwords.words('english'):
            print(word)
