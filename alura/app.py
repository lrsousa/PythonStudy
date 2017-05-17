# -*- coding: UTF-8 -*-
import re

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()
    if nome_a_procurar in nomes:
        print 'O nome existe na lista'
        return True
    print 'O nome nao existe na lista'
    return False

def procurar_regex(nomes):
    print 'Digite nome a expressao regular:'
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome = raw_input()
    if nome in nomes:
        print 'Digite um novo nome:'
        nomes[nomes.index(nome)] = raw_input()

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nomes.remove(raw_input())

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print 'Digite o nome: '
    nomes.append(raw_input())

def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print 'Digite:'
        print '1 para cadastrar'
        print '2 para listar'
        print '3 para alterar'
        print '4 para procurar'
        print '5 para procurar com regex'
        print '6 para remover'
        print '0 para terminar'
        escolha = raw_input()
        if (escolha == '1'):
            cadastrar(nomes)
        if (escolha == '2'):
            listar(nomes)
        if (escolha == '3'):
            alterar(nomes)
        if (escolha == '4'):
            procurar(nomes)
        if (escolha == '5'):
            procurar_regex(nomes)
        if(escolha == '6'):
            remover(nomes)


menu()
