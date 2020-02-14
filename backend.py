# -*- coding: utf-8 -*-

# Teste Backend IPGC
# backend.py
# Luiz Eduardo Pereira

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests
import pymysql

from cliente import Cliente
from produto import Produto
from venda import Venda

#######################################################################################################
#                                                                                                     #
#                                                 INIT                                                #
#                                                                                                     #
#######################################################################################################

# Configuração Flask
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

# Configuração PyMySQL
#db = pymysql.connect("localhost", "USER", "PASSWORD", "teste-backend-ipgc-master")
db = pymysql.connect("localhost", "admin", "admin7576", "teste-backend-ipgc")
cursor = db.cursor()

#######################################################################################################
#                                                                                                     #
#                                                 ROUTER                                              #
#                                                                                                     #
#######################################################################################################

@app.route('/pip', methods=['GET'])
@app.route('/pip/<pop>', methods=['POST'])
def pip(pop=None):
    if request.method == 'GET':
        return 'pop', 200
    if request.method == 'POST':
        return pop, 200




## LEMBRAR DO TRY EXCEPTION ***********************************************************************



# API Cliente
@app.route('/cliente', methods=['POST', 'GET', 'DELETE', 'PUT'])
def cliente():

    data = request.get_json()

    if request.method == 'POST':
        insert_cliente(Cliente(None, data['nome'], data['email'], data['telefone']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

    if request.method == 'GET': # Retorna clientes
        clientes = find_all_clientes() # "clientes" é do typo object, é necessario converter para dict para ser serializado para json 
        return jsonify({'message': '', 'clientes': objetos_to_dicionarios(clientes)}), 200
    
    if request.method == 'DELETE':
        delete_cliente(Cliente(data['codigo'], data['nome'], data['email'], data['telefone']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

    if request.method == 'PUT':
        update_cliente(Cliente(data['codigo'], data['nome'], data['email'], data['telefone']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200



@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'Erro 404 - Pagina nao existe'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'message': 'Erro 405 - Metodo nao permitido'}), 405

#######################################################################################################
#                                                                                                     #
#                                           FUNCTIONS                                                 #
#                                                                                                     #
#######################################################################################################

# Converte uma lista de objetos para uma lista de dicionarios
def objetos_to_dicionarios(objetos):
    lista = []
    for objeto in objetos:
        lista.append(objeto.__dict__)
    return(lista)

# Converte um objeto para dicionario 
def objeto_to_dicionario(objeto):
    return(objeto.__dict__)
       
#######################################################################################################
#                                                                                                     #
#                                               BD                                                    #
#                                                                                                     #
#######################################################################################################

# Insere cliente
def insert_cliente(cliente):
    cursor.execute("INSERT INTO Cliente VALUES(null, '" + cliente.nome + "', '" + cliente.email + "', '" + cliente.telefone + "')")

# Retorna clientes cadastrados. Tipo do retorno: list of cliente.
def find_all_clientes():
    cursor.execute("SELECT * FROM Cliente;")
    resultados = cursor.fetchall()
    clientes = []
    for result in resultados: # Transforma o resultado em lista de cliente
        clientes.append(Cliente(result[0], result[1], result[2], result[3]))
    return(clientes)

# Remove cliente
def delete_cliente(cliente):
    cursor.execute("DELETE FROM Cliente WHERE cli_codigo = " + str(cliente.codigo))

# Atualiza cliente
def update_cliente(cliente):
    cursor.execute("UPDATE Cliente SET cli_nome = '" + cliente.nome + "', cli_email = '" + cliente.email + "', cli_telefone = '" + cliente.telefone +"' WHERE cli_codigo = " + str(cliente.codigo))


def db_commit():
    db.commit()

def db_rollback():
    db.rollback()

#######################################################################################################
#                                                                                                     #
#                                               INIT                                                  #
#                                                                                                     #
#######################################################################################################

# Inicia servidor
if __name__ == "__main__":
    app.run()