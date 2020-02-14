# -*- coding: utf-8 -*-

# Teste Backend IPGC
# cliente.py
# Luiz Eduardo Pereira

class Cliente:
  
  def __init__(self, codigo, nome, email, telefone=None):
    self.codigo = codigo
    self.nome = nome
    self.email = email
    self.telefone = telefone
    
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