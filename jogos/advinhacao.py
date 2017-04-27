# -*- coding: UTF-8 -*-
def acertou():
        print('######################################')
        print('Parabens voce acertou!!')
        print('######################################')


def calcula_pontos(pontos, nivel, pontos_total):
    if (nivel == 3):
        pontos = (100 * 5)
    elif (nivel == 2):
        pontos = (100 * 2)
    else:
        pontos = 100
    pontos_total = pontos_total + pontos
    print('Voce ganhou %s pontos' % pontos)
    print('Voce ganhou %s pontos total' % pontos_total)
    return pontos_total, pontos

def errou():
    print('######################################')
    print('Limite de tentativas alcançado \n Infelismente Voce não acertou')
    print('######################################')
    jogar_novamente(pontos_total, pontos)


def jogar_novamente(pontos_total, pontos):
    print('######################################')
    print('Voce deseja jogar novamente? \n 1 -sim 2 - não')
    print('######################################')
    jogardenovo = int(input())
    if (jogardenovo == 1):
        jogo()
    else:
        print('pontos total: %s' % pontos_total)
        print('pontos %s' % pontos)
        print('FIM')

pontos_total = 0
def jogo():

    from random import randint
    print('##################################')
    print('#Bem vindo ao jogo da Advinhação #')
    print('#        Vamos começar           #')
    print('##################################')

    print('Escolha o nivel de dificudade:')
    print('1 - facil')
    print('2 - medio')
    print('3 - dificil')
    nivel = int(input())

    pontos = 0
    tentativas = 0
    numero = randint(0,100)
    print(numero)
    chute = 0
    while (chute != numero):

        if (nivel == 3):
            if (tentativas == 3):
                errou()
                break
        elif (nivel == 2):
            if (tentativas == 5):
                errou()
                break
        else:
            if (tentativas == 10):
                errou()
                break

        chute = int(input('Chute um numero entre 0 e 100: '))
        while (chute > 100):
            print('Digite um numero entre 0 e 100')
            chute = int(input())

        if (chute < numero):
            print('Ops! chute muito baixo')
            tentativas+=1
            print('numero de tentativas: %s' % tentativas)

        if (chute > numero):
            print('Ops! chute muito alto')
            tentativas+=1
            print('numero de tentativas: %s' % tentativas)
        if (chute == numero):
            acertou()
            calcula_pontos(pontos, nivel, pontos_total)
            jogar_novamente(pontos_total, pontos)
jogo()
