class Pessoa(object):
    """docstring for Pessoa."""
    def __init__(self):
        self.fome = 1
        self.xixi = 0
        self.cagar = 0
        self.fumar = 0
        self.sono = 0
        self.sede = 0
        self.dinheiro = 0
        self.estudar = 0
        self.aumento = 0
        self.disposicao = 3
        self.atividade = 0

    def status(self):
        print('dinheiro: %s' % self.dinheiro)
        print('disposicao: %s' % self.disposicao)
        print('aumento: %s' % self.aumento)
        print('vontade de mijar %s' % self.xixi)
        print('vontade de cagar %s' % self.cagar)

    def comecar(self):
        print('##########################')
        print('Bem vindo ao the sims nerd')
        print('##########################')


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
        self.atividade = int(input('Escolha uma opção: '))
        self.fazer_atividade()

    def verifica_status(self):
        if (self.xixi >= 3) or (self.cagar >= 3):
            self.banheiro()
        if (self.disposicao == 0):
            self.dormir()
        if (self.fome == 0):
            self.comer()


    def fazer_atividade(self):
        if (self.atividade == 1):
            self.comer()
        elif (self.atividade == 2):
            self.dormir()
        elif (self.atividade == 3):
            self.chapar()
        elif (self.atividade == 4):
            self.beber()
        elif (self.atividade == 5):
            self.banheiro()
        elif (self.atividade == 6):
            self.aprender()
        elif (self.atividade == 7):
            self.trabalhar()
        elif (self.atividade == 8):
            self.jogar()
        elif (self.atividade == 9):
            self.passear()
        else:
            print('digite um valor valido')

    def comer(self):
        if (self.dinheiro >=  10):
            print('COMEU')
            self.cagar = self.cagar + 1
            self.dinheiro = self.dinheiro - 10
        else:
            print('Nao pode comer')
            print('Voce não pode comer pois voce tem apenas R$%s, e o lanche custa R$10' % self.dinheiro)

        self.status()
        #self.menu()


    def dormir(self):
        if (self.xixi < 2) and (self.disposicao < 5):
            self.xixi = self.xixi + 1
            self.disposicao = self.disposicao + 1
            print('DORMIU, sua disposicao foi aumentada')
        else:
            print('Você não pode dormir, ou voce ira fazer xixi na cama, ou sua disposicao esta alta para dormir')

        self.status()
        #self.menu()

    def chapar(self):
        if (self.dinheiro > 30):
            self.dinheiro = self.dinheiro - 30
            self.aumento = (self.aumento / 2)
            self.fome = self.fome + 3
            print('Fumou, \n Voce esta chapado')
        else:
            print('Voce não tem grana para comprar maconha')

        self.status()
        #self.menu()

    def beber(self):
        if (self.dinheiro > 10):
            self.xixi = self.xixi + 1
            self.dinheiro = self.dinheiro - 10
            print('Bebeu, \n Voce esta bebado ')
        else:
            print('voce não pode beber, voce nao tem dinheiro')

        self.status()
        #self.menu()

    def banheiro(self):
        if (self.xixi >= 3):
            print('Voce precisa mijar')
            print('mijando...')
            self.xixi = 0
        elif (self.cagar >= 3):
            print('voce precisa cagar')
            print('cagando...')
            self.cagar = 0
        else:
            print('voce nao precisa ir ao banheiro')

        self.status()
        #self.menu()

    def aprender(self):
        if (self.disposicao >= 1) and (self.dinheiro >= 10):
            self.aumento = self.aumento + 20
            print('Parabens, Você Estudou')
            print('Agora seu salario aumentou %s reais' % self.aumento)
            self.disposicao = self.disposicao - 1
            self.dinheiro = self.dinheiro - 10
        else:
            print('sua disposicao não é o suficiente para estudar, tente dormir um pouco')
        self.status()
        #self.menu()

    def trabalhar(self):
        if (self.disposicao >= 1):
            if (self.aumento != 0):
                self.dinheiro = self.dinheiro + self.aumento
            else:
                self.dinheiro = self.dinheiro + 10
            print('trabalhou\n E sua renda é %s' % self.dinheiro)
            self.disposicao = self.disposicao - 1
        else:
            print('voce não esta disposoto atrabalhar')

        self.status()
        #self.menu()

    def jogar(self):
        if (self.disposicao >= 1) and (self.dinheiro >=20):
            self.dinheiro = self.dinheiro - 20
            self.disposicao = self.disposicao - 1
            print('jogou')
        else:
            print('Voce não pode jogar, pois esta sem dinheiro ou disposicao')

        self.status()
        #self.menu()

    def passear(self):
        if (self.disposicao >= 1) and (self.dinheiro >=20):
            self.dinheiro = self.dinheiro - 20
            self.disposicao = self.disposicao - 1
            print('passeou')
        else:
            print('Voce não pode passear, pois esta sem dinheiro ou disposicao')

        self.status()
        #self.menu()

#pessoa = Pessoa()
#pessoa.menu()
