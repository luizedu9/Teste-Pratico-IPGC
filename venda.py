# -*- coding: utf-8 -*-

# Teste Backend IPGC
# venda.py
# Luiz Eduardo Pereira

class Venda:
  
  def __init__(self, codigo, data, cliente, produtos):
    self.codigo = codigo
    self.data = data
    self.cliente = cliente
    self.produtos = produtos

    # Getters e Setters

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

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