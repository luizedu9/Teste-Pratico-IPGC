# -*- coding: utf-8 -*-

# Teste Backend IPGC
# venda.py
# Luiz Eduardo Pereira

class Venda:
  def __init__(self, data, cliente, produtos, codigo=None):
    self.data = data
    self.cliente = self.cliente
    self.produtos = self.produtos
    self.codigo = codigo

    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente
        
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def produtos(self):
        return self.__produtos
        
    @produtos.setter
    def produtos(self, produtos):
        self.__produtos = produtos

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo