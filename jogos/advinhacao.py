# -*- coding: UTF-8 -*-
print('##################################')
print('#Bem vindo ao jogo da Advinhação #')
print('#        Vamos começar           #')
print('##################################')

numero = 42
chute = 0
tentativas = 0
while (chute != numero):
    chute = int(input('Chute um numero: '))

    if (chute < numero):
        print('Ops! chute muito baixo')
        tentativas+=1
        print('numero de tentativas: %s' % tentativas)

    if (chute > numero):
        print('Ops! chute muito alto')
        tentativas+=1
        print('numero de tentativas: %s' % tentativas)

print('Parabens voce acertou na %s' % tentativas)
