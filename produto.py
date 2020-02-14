# -*- coding: utf-8 -*-

# Teste Backend IPGC
# produto.py
# Luiz Eduardo Pereira

class Produto:
  def __init__(self, nome, preco, descricao=None, codigo=None):
    self.nome = nome
    self.preco = self.preco
    self.descricao = self.descricao
    self.codigo = codigo

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco
        
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao
        
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo