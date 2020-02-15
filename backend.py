# -*- coding: utf-8 -*-

# Teste Backend IPGC
# backend.py
# Luiz Eduardo Pereira

#######################################################################################################
#                                                                                                     #
#                                                 INIT                                                #
#                                                                                                     #
#######################################################################################################

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import requests

from bd_request import *
from cliente import Cliente
from produto import Produto
from venda import Venda

# Configuração Flask
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

#######################################################################################################
#                                                                                                     #
#                                                 ROUTER                                              #
#                                                                                                     #
#######################################################################################################



## LEMBRAR DO TRY EXCEPTION ***********************************************************************



# API Cliente
@app.route('/cliente', methods=['POST', 'GET'])
@app.route('/cliente/<id>', methods=['GET', 'DELETE', 'PUT'])
def cliente(id=None):

    data = request.get_json()

    if request.method == 'POST':
        insert_cliente(Cliente(None, data['nome'], data['email'], data['telefone']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 201

    if request.method == 'GET': # Retorna cliente(s)
        if id != None:
            cliente = find_cliente(id)
            return jsonify({'message': '', 'cliente': objeto_to_dicionario(cliente)})
        clientes = find_all_clientes() # "clientes" é do tipo object, é necessario converter para dict para ser serializado para json 
        return jsonify({'message': '', 'clientes': objetos_to_dicionarios(clientes)}), 200
    
    if request.method == 'DELETE':
        delete_cliente(id)
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

    if request.method == 'PUT':
        update_cliente(id, Cliente(data['codigo'], data['nome'], data['email'], data['telefone']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

# API Produto
@app.route('/produto', methods=['POST', 'GET'])
@app.route('/produto/<id>', methods=['GET', 'DELETE', 'PUT'])
def produto(id=None):

    data = request.get_json()

    if request.method == 'POST':
        insert_produto(Produto(None, data['nome'], float(data['preco']), data['descricao']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 201

    if request.method == 'GET': # Retorna produtos
        if id != None:
            produto = find_produto(id)
            return jsonify({'message': '', 'produto': objeto_to_dicionario(produto)})
        produtos = find_all_produtos() # "produtos" é do tipo object, é necessario converter para dict para ser serializado para json 
        return jsonify({'message': '', 'produtos': objetos_to_dicionarios(produtos)}), 200
    
    if request.method == 'DELETE':
        delete_produto(id)
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

    if request.method == 'PUT':
        update_produto(id, Produto(data['codigo'], data['nome'], float(data['preco']), data['descricao']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

# API Venda
@app.route('/venda', methods=['POST', 'GET'])
@app.route('/venda/<id>', methods=['GET', 'DELETE', 'PUT'])
def venda(id=None):

    data = request.get_json()

    if request.method == 'POST':
        date = datetime.now().strftime('%Y-%m-%d')
        insert_venda(Venda(None, date, data['codigo_cliente'], data['codigo_produtos']))
        db_commit()
        return jsonify({'message': 'Sucesso'}), 201

    if request.method == 'GET': # Retorna produtos
        if id != None:
            venda = find_venda(id)
            #print((venda.data) == datetime.strftime("2020-02-14", '%Y-%m-%d'))
            return jsonify({'message': '', 'venda': objeto_to_dicionario(venda)})
        vendas = find_all_vendas() # "produtos" é do tipo object, é necessario converter para dict para ser serializado para json 
        return jsonify({'message': '', 'vendas': objetos_to_dicionarios(vendas)}), 200
    
    if request.method == 'DELETE':
        delete_venda(id)
        db_commit()
        return jsonify({'message': 'Sucesso'}), 200

    if request.method == 'PUT':
        update_venda(id, Venda(data['codigo'], data['data'], data['codigo_cliente'], data['codigo_produtos']))
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
#                                               INIT                                                  #
#                                                                                                     #
#######################################################################################################

# Inicia servidor
if __name__ == "__main__":
    app.run()