# -*- coding: UTF-8 -*-
class Perfil(object):
    """Classe padrão para perfilde usuário."""
    def __init__(self, nome, telefone, empresa):
        if (len(nome) < 3):
            raise ValueError('Nome deve ter pelo menos 3 caracteres')
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print ('Nome: %s, Telefone: %s, Empresa: %s, Curtidas: %s ' % (self.nome, self.telefone, self.empresa, self.__curtidas))

    def curtir(self):
        self.__curtidas+=1

    def total_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores  = linha.split(',')
            if (len(valores) is not 3):
                raise ValueError('Cada linha do arquivo %s deve ter no minimo 3 valores' % nome_arquivo)
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis


class Perfil_Vip(Perfil):
    """docstring for Perfil_Vip."""
    def __init__(self, nome, telefone,empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def total_creditos(self):
        return super(Perfil_Vip, self).total_curtidas() * 10.0
