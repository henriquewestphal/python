class Pessoa(object):
    """docstring for Pessoa."""
    def __init__(self):
        self.fome = 0
        self.xixi = 0
        self.cagar = 0
        self.fumar = 0
        self.sono = 0
        self.sede = 0
        self.dinheiro = 0
        self.estudar = 0
        self.jogar_fut = 0
        self.passeio = 0
        self.pode = ''
        self.aumento = 0
        self.disposicao = 0

    def status(self):
        print('dinheiro: %s' % pessoa.dinheiro)
        print('disposicao: %s' % pessoa.disposicao)
        print('aumento: %s' % pessoa.aumento)


    def comecar(self):
        print('##########################')
        print('Bem vindo ao the sims nerd')
        print('##########################')
        pessoa.menu()

    def menu(self):
        print('###########################')
        print('# Oque voce deseja fazer? #')
        print('# 1 - Comer               #')
        print('# 2 - Dormir              #')
        print('# 3 - Fumar maconha       #')
        print('# 4 - Beber               #')
        print('# 5 - Ir no banheiro      #')
        print('# 6 - Estudar             #')
        print('# 7 - Trabalhar           #')
        print('# 8 - Jogar futebol       #')
        print('# 9 - Passear             #')
        print('###########################')
        atividade = int(input('Escolha uma opção: '))
        pessoa.fazer_atividade(atividade)



    def fazer_atividade(self,atividade,):
        if (atividade == 1):
            pessoa.podecomer()
            pessoa.comer()
        elif (atividade == 2):
            pessoa.dormir()
        elif (atividade == 3):
            pessoa.fumar()
        elif (atividade == 4):
            pessoa.beber()
        elif (atividade == 5):
            pessoa.banheiro()
        elif (atividade == 6):
            pessoa.aprender()
        elif (atividade == 7):
            pessoa.trabalhar()
        elif (atividade == 8):
            pessoa.jogar()
        elif (atividade == 9):
            pessoa.passear()
        else:
            print('digite um valor valido')

    def podecomer(self):
        if (pessoa.dinheiro >= 10 ):
            pessoa.pode = 'sim'
            pessoa.cagar = pessoa.cagar + 1
            pessoa.dinheiro = pessoa.dinheiro - 10
        else:
            pessoa.pode = 'nao'

    def comer(self):
        if (pessoa.pode == 'sim'):
            print('COMEU')
            pessoa.cagar = pessoa.cagar + 1
        else:
            print('Nao pode COMEr')
            print('Voce não pode comer pois voce tem apenas R$%s, e o lanche custa R$10' % pessoa.dinheiro)
        pessoa.status()
        pessoa.menu()

    def podedormir(self):
        pass

    def dormir(self):
        pessoa.xixi = pessoa.xixi + 1
        pessoa.cagar = pessoa.cagar + 1
        pessoa.disposicao = pessoa.disposicao + 1
        print('DORMIU')

        pessoa.status()
        pessoa.menu()

    def fumar(self):
        print('Fumou, \n Voce esta chapado')
        pessoa.status()
        pessoa.menu()

    def beber(self):
        print('Bebeu, \n Voce esta bebado ')
        pessoa.status()
        pessoa.menu()

    def banheiro(self):
        print('cagou, e mijou')
        pessoa.status()
        pessoa.menu()

    def aprender(self):
        if (pessoa.disposicao >= 1) and (pessoa.dinheiro >= 10):
            pessoa.aumento = pessoa.aumento + 20
            print('Parabens, Você Estudou')
            print('Agora seu salario aumentou %s' % pessoa.aumento)
            pessoa.disposicao = pessoa.disposicao - 1
            pessoa.dinheiro = pessoa.dinheiro - 10
        else:
            print('sua disposicao não é o sufuciente para estudar, tente dormir um pouco')
        pessoa.status()
        pessoa.menu()

    def trabalhar(self):
        if (pessoa.disposicao >= 1):
            if (pessoa.aumento != 0):
                pessoa.dinheiro = pessoa.dinheiro + pessoa.aumento
                print('trabalhou\n E sua renda é %s' % pessoa.dinheiro)
            else:
                pessoa.dinheiro = pessoa.dinheiro + 10
            pessoa.disposicao = pessoa.disposicao - 1
        else:
            print('voce não esta disposoto atrabalhar')
        pessoa.status()
        pessoa.menu()

    def jogar(self):
        print('jogou')
        #disposicao, dinheiro
        pessoa.status()
        pessoa.menu()

    def passear(self):
        print('passeou')
        #disposicao, dinheiro
        pessoa.status()
        pessoa.menu()

pessoa = Pessoa()
pessoa.comecar()
