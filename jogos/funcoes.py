class Pessoa(object):
    """docstring for Pessoa."""
    def __init__(self):
        self.fome = 0
        self.xixi = 0
        self.cagar = 6
        self.fumar = 0
        self.sono = 0
        self.sede = 0
        self.dinheiro = 0
        self.estudar = 0
        self.jogar_fut = 0
        self.passeio = 0


    def menu(self):
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
        pessoa.fazer_atividade(atividade)


    def fazer_atividade(self,atividade,):
        if (atividade == 1):
            pessoa.comer()
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

    def comer(self):
        print('COMEU')
        #global cagar
        self.cagar = self.cagar + 1
        print ('vontade de cagar: %s' % self.cagar)
        pessoa.menu()
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

pessoa = Pessoa()
print(pessoa.cagar)
pessoa.menu()
