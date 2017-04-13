# -*- coding: UTF-8 -*-
import re

def cadastrar(nomes):
    print 'Digiteo nome:'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print ' Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome voce deseja remover?'
    nome_remove = raw_input()
    nomes.remove(nome_remove)

def alterar(nomes):
    print 'Qual nome voce deseja alterar?'
    nome_alterar = raw_input()
    existe = nome_alterar in nomes
    if (existe == True):
        print 'Nome encontrado'
        posicao = nomes.index(nome_alterar)
        print 'deseja alterar para qual nome?'
        novo_nome = raw_input()
        nomes[posicao] = novo_nome
        print 'nome alterado com sucesso'

    if (existe == False):
        print 'nome não encontrado'


def procurar(nomes):
    print 'Digite o nome a procurar'
    procura_nome = raw_input()
    existe = procura_nome in nomes
    if (existe == True):
        print 'nome encontrado'

    if (existe == False):
        print 'nome não encontrado'

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)


def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print "Escolha"
        print " 1 para cadastrar"
        print " 2 para listar"
        print " 3 para remover"
        print " 4 para alterar"
        print " 5 para procurar"
        print " 6 para procurar por regex"
        print " 0 para terminar"

        escolha = raw_input()

        if (escolha == '1'):
            cadastrar(nomes)

        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

        if (escolha == '4'):
            alterar(nomes)

        if (escolha == '5'):
            procurar(nomes)

        if (escolha == '6'):
            procurar_regex(nomes)



menu()
