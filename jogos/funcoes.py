#importando variaveis.
fome = 0
xixi = 0
cagar = 6
fumar = 0
sono = 0
sede = 0
dinheiro = 0
estudar = 0
jogar_fut = 0
passeio = 0


def menu():
    print('Bem vindo ao the sims nerd')
    print('Oque voce deseja fazer?')
    print('1 - comer')
    print('2 - dormir')
    print('3 - fumar maconha')
    print('4 - beber')
    print('5 - ir no banheiro')
    print('6 - Estudar')
    print('7 - Trabalhar')
    print('8 - jogar futebol')
    print('9 - passear')
    atividade = int(input('Escolha uma opção: '))
    fazer_atividade(atividade)

#def status():



def fazer_atividade(atividade,):
    if (atividade == 1):
        comer()
    elif (atividade == 2):
        dormir()
    elif (atividade == 3):
        fumar()
    elif (atividade == 4):
        beber()
    elif (atividade == 5):
        banheiro()
    elif (atividade == 6):
        estudar()
    elif (atividade == 7):
        trabalhar()
    elif (atividade == 8):
        jogar()
    elif (atividade == 9):
        passear()
    else:
        print('digite um valor valido')

def comer():
    print('COMEU')
    global cagar
    cagar = cagar + 1
    global xixi
    print (xixi)
    xixi = xixi + 2
    print ('vontade de cagar: %s e dormir %s' % (cagar, xixi))
def dormir():
    print('DORMIU')

def fumar():
    print('Fumou, \n Voce esta chapado')

def beber():
    print('Bebeu, \n Voce esta bebado ')

def banheiro():
    print('cagou, e mijou')

def estudar():
    print('Estudou')

def trabalhar():
    print('trabalhou')

def jogar():
    print('jogou')

def passear():
    print('passeou')
