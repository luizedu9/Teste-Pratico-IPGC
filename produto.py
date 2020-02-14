# -*- coding: utf-8 -*-

# Teste Backend IPGC
# produto.py
# Luiz Eduardo Pereira

class Produto:
  
  def __init__(self, codigo, nome, preco, descricao=None):
    self.codigo = codigo
    self.nome = nome
    self.preco = preco
    self.descricao = descricao
    
    # Getters e Setters

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

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