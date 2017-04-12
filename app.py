# -*- coding: UTF-8 -*-
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


def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print "Escolha"
        print " 1 para cadastrar"
        print " 2 para listar"
        print " 3 para remover"
        print " 0 para terminar"
        escolha = raw_input()

        if (escolha == '1'):
            cadastrar(nomes)

        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

menu()
