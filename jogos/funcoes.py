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

    def status(self):
        print('dinheiro: %s' % pessoa.dinheiro)
        print('disposicao: %s' % pessoa.disposicao)
        print('aumento: %s' % pessoa.aumento)
        print('vontade de mijar %s' % pessoa.xixi)
        print('vontade de cagar %s' % pessoa.cagar)

    def comecar(self):
        print('##########################')
        print('Bem vindo ao the sims nerd')
        print('##########################')
        pessoa.menu()

    def menu(self):
        pessoa.verifica_status()
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

    def verifica_status(self):
        if (pessoa.xixi >= 3) or (pessoa.cagar >= 3):
            pessoa.banheiro()
        if (pessoa.disposicao == 0):
            pessoa.dormir()
        if (pessoa.fome == 0):
            pessoa.comer()


    def fazer_atividade(self,atividade,):
        if (atividade == 1):
            pessoa.comer()
        elif (atividade == 2):
            pessoa.dormir()
        elif (atividade == 3):
            pessoa.chapar()
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

    def comer(self):
        if (pessoa.dinheiro >=  10):
            print('COMEU')
            pessoa.cagar = pessoa.cagar + 1
            pessoa.dinheiro = pessoa.dinheiro - 10
        else:
            print('Nao pode comer')
            print('Voce não pode comer pois voce tem apenas R$%s, e o lanche custa R$10' % pessoa.dinheiro)

        pessoa.status()
        pessoa.menu()


    def dormir(self):
        if (pessoa.xixi < 2) and (pessoa.disposicao < 5):
            pessoa.xixi = pessoa.xixi + 1
            pessoa.disposicao = pessoa.disposicao + 1
            print('DORMIU, sua disposicao foi aumentada')
        else:
            print('Você não pode dormir, ou voce ira fazer xixi na cama, ou sua disposicao esta alta para dormir')

        pessoa.status()
        pessoa.menu()

    def chapar(self):
        if (pessoa.dinheiro > 30):
            pessoa.dinheiro = pessoa.dinheiro - 30
            pessoa.aumento = (pessoa.aumento / 2)
            pessoa.fome = pessoa.fome + 3
            print('Fumou, \n Voce esta chapado')
        else:
            print('Voce não tem grana para comprar maconha')

        pessoa.status()
        pessoa.menu()

    def beber(self):
        if (pessoa.dinheiro > 10):
            pessoa.xixi = pessoa.xixi + 1
            pessoa.dinheiro = pessoa.dinheiro - 10
            print('Bebeu, \n Voce esta bebado ')
        else:
            print('voce não pode beber, voce nao tem dinheiro')

        pessoa.status()
        pessoa.menu()

    def banheiro(self):
        if (pessoa.xixi >= 3):
            print('Voce precisa mijar')
            print('mijando...')
            pessoa.xixi = 0
        elif (pessoa.cagar >= 3):
            print('voce precisa cagar')
            print('cagando...')
            pessoa.cagar = 0
        else:
            print('voce nao precisa ir ao banheiro')

        pessoa.status()
        pessoa.menu()

    def aprender(self):
        if (pessoa.disposicao >= 1) and (pessoa.dinheiro >= 10):
            pessoa.aumento = pessoa.aumento + 20
            print('Parabens, Você Estudou')
            print('Agora seu salario aumentou %s reais' % pessoa.aumento)
            pessoa.disposicao = pessoa.disposicao - 1
            pessoa.dinheiro = pessoa.dinheiro - 10
        else:
            print('sua disposicao não é o suficiente para estudar, tente dormir um pouco')
        pessoa.status()
        pessoa.menu()

    def trabalhar(self):
        if (pessoa.disposicao >= 1):
            if (pessoa.aumento != 0):
                pessoa.dinheiro = pessoa.dinheiro + pessoa.aumento
            else:
                pessoa.dinheiro = pessoa.dinheiro + 10
            print('trabalhou\n E sua renda é %s' % pessoa.dinheiro)
            pessoa.disposicao = pessoa.disposicao - 1
        else:
            print('voce não esta disposoto atrabalhar')

        pessoa.status()
        pessoa.menu()

    def jogar(self):
        if (pessoa.disposicao >= 1) and (pessoa.dinheiro >=20):
            pessoa.dinheiro = pessoa.dinheiro - 20
            pessoa.disposicao = pessoa.disposicao - 1
            print('jogou')
        else:
            print('Voce não pode jogar, pois esta sem dinheiro ou disposicao')

        pessoa.status()
        pessoa.menu()

    def passear(self):
        if (pessoa.disposicao >= 1) and (pessoa.dinheiro >=20):
            pessoa.dinheiro = pessoa.dinheiro - 20
            pessoa.disposicao = pessoa.disposicao - 1
            print('passeou')
        else:
            print('Voce não pode passear, pois esta sem dinheiro ou disposicao')

        pessoa.status()
        pessoa.menu()

pessoa = Pessoa()
pessoa.comecar()
