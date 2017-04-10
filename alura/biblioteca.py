def gera_nome_convite(nome_convidado):
    posicao_final = len(nome_convidado)
    posicao_inicial = posicao_final -4
    parte1 = nome_convidado[0:4]
    parte2 = nome_convidado[posicao_inicial: posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(nome_convidado):
    print "Enviando convite para %s" %(nome_convidado)

def processa_convite(nome_convidado):
    envia_convite(gera_nome_convite(nome_convidado))
