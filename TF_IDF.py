import numpy as np
from Corpus import *


# funções #########################
def tf_idf(text):
    '''
    função que recebe um texto e
    transforma em um vetor para
    calcular o tf-idf
    :param text: str
    :return: list
    '''
    word_count = {}
    for word in text:
        if word not in word_count: word_count[word] = 1
        else: word_count[word] += 1

    numero_de_termos = 0
    for n in word_count:
        numero_de_termos += word_count[n]

    tf = [None] * len(word_count)
    cont = 0
    for word in word_count:
        tf[cont] = word_count[word] / numero_de_termos
        cont += 1

    idf = [None] * len(word_count)
    cont_idf = 0
    for word in word_count:
        idf[cont_idf] = math.log10(1/(word_count[word] + 1))
        cont_idf += 1

    tf_idf_ = [None] * len(word_count)
    cont_tf_idf = 0
    for _ in word_count:
        tf_idf_[cont_tf_idf] = tf[cont_tf_idf] * idf[cont_tf_idf]
        cont_tf_idf += 1

    return tf_idf_


def cos_similarity(a, b):
    '''
    função que recebe dois vetores gerados
    pela função tf_idf e calcula sua similaridade
    atraves da similaridade de cosenos
    :param a: list
    :param b: list
    :return: float
    '''
    if len(b) < len(a):
        for _ in range(len(a)-len(b)): b.append(0)
    elif len(b) > len(a):
        for _ in range(len(b)-len(a)): a.append(0)
    cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return cos_sim


def compare(text):
    '''
    função que recebe um texto e retorna
    o texto mais similar que encontrar no
    'corpus' disponível. a similaridade é
    calculado com a função cos_similarity
    :param text: str
    :return: str
    '''
    s = -1
    sent = ''
    for i in range(len(SENTS)):
        t = tf_idf(remove_stops(clean_stops(SENTS[i])))
        c = cos_similarity(tf_idf(remove_stops(text)), t)
        if c > s:
            s = c
            sent = SENTS[i]
    return sent
##########################################

if __name__ == "__main__":
    print(compare("increment the program counter so it points to the next instruction"))
    for sent in SENTS:
        print(sent)
