# -*- coding: utf-8 -*-

# Teste Backend IPGC
# cliente.py
# Luiz Eduardo Pereira

class Cliente:
  def __init__(self, nome, email, telefone=None, codigo=None):
    self.nome = nome
    self.email = self.email
    self.telefone = self.telefone
    self.codigo = codigo

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
        
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo