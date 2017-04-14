# -*- coding: UTF-8 -*-
class Perfil(object):
    """Classe padrão para perfilde usuário."""
    def __init__(self, nome, telefone, empresa):
        #super(, self).__init__()
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)

class Data(object):
    """data"""
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
        print'%s/%s/%s'% (self.dia, self.mes, self.ano)

class Pessoa(object):
    """docstring for Pessoa."""
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def imprimir_imc(self):
        pesoint = (int(self.peso))
        alturaint = (float(self.altura))
        #altura2 = self.altura * self.altura
        #imc = self.peso / altura2
        calculo = pesoint / (alturaint * alturaint)
        print ' IMC de %s é: %s' % (self.nome, calculo)

# resposta alura
#class Pessoa(object):
#    def __init__(self, nome, peso, altura):
#        self.nome = nome
#        self.peso = float(peso)
#        self.altura = float(altura)
#
#    def imprime(self):
#        imc = self.peso / (self.altura **2)
#        print 'O IMC de %s é: %s ' %(self.nome, imc)
#
