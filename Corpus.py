#import nltk
from STOP_WORDS import *


# funções ##############################
def clean_stops(text):
    '''
    função que recebe um texto e remove pontuações
    e transforma todos os caracteres em minúculos
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


def remove_stops(text):
    '''
    função que recebe um texto e retira
    suas 'stopwords'
    :param text: str
    :return: str
    '''
    t = text.split()
    tx = ""
    for word in t:
        if word not in STOPWORDS:
          tx += word + ' '
    return tx


def text_tokens():
    '''
    função que gera as sentenças que serão
    usadas para responder o usuário.
    as sentenças são geradas a partir do
    arquivo 'Computer.txt'
    :return: list
    '''
    file = open('Computer.txt', 'r', errors='ignore')
    text = file.read()
    text = text.lower()
    text = nltk.sent_tokenize(text)
    return text
###########################################


# constantes ##############################
SENTS = text_tokens()
###########################################

# testes ##################################
if __name__ == "__main__":
    print(len(SENTS))
    print(SENTS)
