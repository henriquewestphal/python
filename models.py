# -*- coding: UTF-8 -*-
class Perfil(object):
    """Classe padrão para perfilde usuário."""
    def __init__(self, nome, telefone, empresa):
        #super(, self).__init__()
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s, Curtidas: %s' % (self.nome, self.telefone, self.empresa, self.__curtidas)


    def curtir(self):
        self.__curtidas+=1

    def total_curtidas(self):
        return self.__curtidas
