# -*- coding: UTF-8 -*-
# connect_db.py
# 01_create_db.py
import sqlite3

conn = sqlite3.connect('/home/henrique.westphal/Documentos/git/python/jogos/contas.db')

cursor = conn.cursor()

cursor.execute("create table if not exists contas (id integer primary key autoincrement, nome text not null, saldoinicial real not null, telefone integer not null, tipo text not null, saldo real not null);")
cursor.execute("create table if not exists registros(id integer primary key autoincrement, nome text not null, valor real not null, movimento text not null, destino text, saldo real not null);")

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
        pessoas.append(self)
        cursor.execute(" insert into contas (nome, saldoinicial, telefone, tipo, saldo) values (?,?,?,?,?)", (self.nome, self.saldo_inicial, self.telefone, self.tipo, self.saldo))
        conn.commit()
        #conn.close()


    def depositar(self):
        valor_deposito = int(input('Digite o valor que voce deseja depositar: '))
        self.saldo += valor_deposito
        print('Valor depositado foi: %s' % valor_deposito)
        print('Saldo atual: %s' % self.saldo)
        registro = ('\nDEPOSITO EFETUADO \nDeposito de %s reais na conta de %s \nSaldo atual: %s' % (valor_deposito, self.nome, self.saldo))
        #self.movimentacao(registro)
        cursor.execute("insert into registros(nome, valor, movimento, saldo) values (?,?,'Deposito',?)", (self.nome, valor_deposito, self.saldo))
        conn.commit()

    def sacar(self):
        valor_saque = int(input('Digite o valor que voce deseja sacar: '))
        if (valor_saque > self.saldo):
            print('Valos de saque desejado é maior que o saldo em conta')
            self.sacar()
        else:
            self.saldo -= valor_saque
            print('voce sacou %s reais' % valor_saque)
            print('seu saldo é %s' % self.saldo)
            registro = ('\nSAQUE EFETUADO\n Voce sacou %s \n Saldo atual ' % (valor_saque, self.saldo))
            #self.movimentacao(registro)
            cursor.execute("insert into registros(nome, valor, movimento, saldo) values (?,?,'Saque',?)", (self.nome, valor_saque, self.saldo))
            conn.commit()

    def ver_saldo(self):
        print('Seu saldo atual é %s' % self.saldo)


    def transferir(self):
        valor_transferir = int(input('Digite o valor que voce deseja transferir: '))
        if (valor_transferir > self.saldo):
            print('valor maior que o saldo atual')
            self.transferir()
        else:
            print('para quem voce deseja transferir essa quantia: ')
            destino = input()
            for pessoa in pessoas:
                if pessoa.nome == destino:
                    pessoa.saldo += valor_transferir
                    print(pessoa.saldo)
                    self.saldo -= valor_transferir
                    print('valor transferido, para %s quantia %s' % (pessoa.nome, valor_transferir))
                    registro = ('\nTransferencia de valor\n Voce transferiu a quantia de %s para a conta de %s' % (valor_transferir, pessoa.nome))
                    #self.movimentacao(registro)
                    cursor.execute("insert into registros(nome, valor, movimento, destino, saldo) values (?,?,'Transferencia',?,?)", (self.nome, valor_transferir, pessoa.nome, self.saldo))
                    conn.commit()

    #def movimentacao(self, registro):
    #    arquivo = open('movimentacao%s.txt' % self.nome, 'r')
    #    conteudo = arquivo.readlines()
    #    conteudo.append("\n------------------------------------")
    #    conteudo.append(registro)
    #    conteudo.append("\n------------------------------------")
    #    arquivo = open('movimentacao%s.txt' % self.nome, 'w')
    #    arquivo.writelines(conteudo)
    #    arquivo.close()


    def extrato(self):
        arquivo = open('movimentacao%s.txt' % self.nome, 'r')
        conteudo = arquivo.readlines()
        for linha in conteudo:
            print(linha)
        arquivo.close()


pessoas = []
