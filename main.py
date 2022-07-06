from random import randint

#encurtador
CHAVES = 'abcdefghijklmnopqrstuvwxyz0123456789#+ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LISTA_CODIGOS = []

class Link:
    link = ''
    link_curto = ''
    def __init__(self, link):
        self.link = link
        self.link_curto = self.Gerar()

    def Gerar(self):
        link_curto = GerarCodigo()
        if link_curto not in LISTA_CODIGOS:
            LISTA_CODIGOS.append(self)
            return link_curto
        else:
            self.Gerar()

def GerarCodigo():
    saida = ''
    while len(saida) < 10:
        pos = randint(0,len(CHAVES)-1)
        if CHAVES[pos] not in saida:
            saida+=CHAVES[pos]
    return saida
