from operator import truediv

import nltk

def acha_remove(string, elemento):
    while elemento in string:
        string.pop(string.index(elemento))

def normalizar(texto, tokenizacao, minusculo, pontuacao, acentos, stopwords, stemming):
    texto_manip = texto

    # Essa etapa introduz um problema em que precisamos verificar se a variavel é uma lista ou uma string
    # antes de manipula-la
    # TODO: aplicar isso
    if (tokenizacao):
        tokens = nltk.wordpunct_tokenize(texto_manip)
        # TODO: validar
        ## seeee tudo estiver bem::
        texto_manip = tokens
    if (minusculo):
        ## TODO: Checar o tipo de texto_manip antes de aplicar
        texto_manip = texto_manip.lower
    if (not pontuacao):
        # TODO: adicionar mais....
        # TODO: robustez para sinais repetidos???
        p = ('.', '!', '?', ',', ';',':','"','\'', '(', ')', '[', ']', '{', '}')
        for i in len(p):
            acha_remove(texto_manip, p[i])


    return texto_manip

coiso = input("Realize uma pergunta:")
print(normalizar(coiso, True, True, True, True, True, True ))
