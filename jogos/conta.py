# -*- coding: UTF-8 -*-
class Conta(object):
    """docstring for Conta."""
    def __init__(self, nome, saldo_inicial, telefone, tipo):
        if (len(nome) < 3):
            raise ValueError('Nome deve ter no minimo 3 caracteres')
        self.nome = nome
        self.saldo_inicial = saldo_inicial
        self.telefone = telefone
        self.tipo = tipo
        self.saldo = self.saldo_inicial


    def depositar(self):
        valor_deposito = int(input('Digite o valor que voce deseja depositar: '))
        self.saldo = self.saldo + valor_deposito
        print('Valor depositado foi: %s' % valor_deposito)
        print('Saldo atual %s' % self.saldo)

    def sacar(self):
        valor_saque = int(input('Digite o valor que voce deseja sacar: '))
        if (valor_saque > self.saldo):
            print('Valos de saque desejado é maior que o saldo em conta')
            self.sacar()
        else:
            self.saldo = self.saldo - valor_saque
            print('voce sacou %s reais' % valor_saque)
            print('seu saldo é %s' % self.saldo)

    def ver_saldo(self):
        print('Seu saldo atual é %s' % self.saldo)

    def transferir(self):
        valor_transferir = int(input('Digite o valor que voce deseja transferir'))
        if (valor_transferir > self.saldo):
            print('valor maior que o saldo atual')
            self.transferir()
        else:
            print('para quem voce deseja transferir essa quantia: ')
            destino = input()
            self.saldo = self.saldo - valor_transferir
            #destino.saldo = destino.saldo + valor_transferir
            print('valor transferido, para %s quantia %s' % (destino.nome, valor_transferir))
