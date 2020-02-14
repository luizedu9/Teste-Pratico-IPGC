# -*- coding: utf-8 -*-

# Teste Backend IPGC
# backend.py
# Luiz Eduardo Pereira

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests
import pymysql

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
def pip():
    if request.method == 'GET':
        return "pop", 200




@app.errorhandler(404)
def page_not_found(error):
    return 'Erro 404 - Página não existe', 404

@app.errorhandler(405)
def method_not_allowed(error):
    return 'Erro 405 - Método não permitido', 405


############################################################################################################################3

# Retorna dados necessarios para o funcionamento da venda
@app.route('/startVenda', methods=['GET'])
def startVenda():
    if request.method == 'GET':
        try:
            cod = find_numero_venda() # Coleta dados do codigo da venda, clientes e produtos
            clientes = find_all_clientes()
            produtos = find_all_produtos()
            return jsonify({'status': '0', 'codigoVenda': cod, 'clientes': clientes, 'produtos': produtos })
        except: # Se ocorrer algum erro, retorna status de erro
            return jsonify({'status': '1'})

# Insere dados da venda ao banco de dados
@app.route('/insertVenda', methods=['POST'])
def insertVenda():
    if request.method == 'POST':
        try:
            response = request.get_json()
            processa_venda(response) # Envia para uma função que processa os dados para inserir no banco
            db_commit()
            return jsonify({'status': '0'})
        except: # Se ocorrer algum erro, retorna status de erro
            db_rollback()
            return jsonify({'status': '1'})

# Retorna dados necessarios para o funcionamento da consulta
@app.route('/startConsulta', methods=['GET'])
def startConsulta():
    if request.method == 'GET':
        try:
            resultado = find_sql_consulta()
            return jsonify({'status': '0', 'consulta': resultado})
        except: # Se ocorrer algum erro, retorna status de erro
            return jsonify({'status': '1'})

#######################################################################################################
#                                                                                                     #
#                                           FUNCTIONS                                                 #
#                                                                                                     #
#######################################################################################################

# Processa os dados para serem inseridos no banco de dados
def processa_venda(dados):
    insert_venda(dados)
    for item in dados['itens']:
        insert_item(item, dados['numVenda'])    
       
#######################################################################################################
#                                                                                                     #
#                                               BD                                                    #
#                                                                                                     #
#######################################################################################################

# Retorna vendas cadastradas
def find_all_vendas():
    cursor.execute("SELECT * FROM Venda;")
    resultados = cursor.fetchall()
    vendas = []
    for result in resultados: # Transforma o resultado em lista de dicionarios
        vendas.append({"codigo": result[0], "data": result[1], "total": result[2], "cep": result[3], "logradouro": result[4], "numero": result[5], "complemento": result[6], "bairro": result[7], "localidade": result[8], "uf": result[9], "codigoCliente": result[10]})
    return(vendas)

# Retorna clientes cadastrados (Lista de dicionarios)
def find_all_clientes():
    cursor.execute("SELECT * FROM Cliente;")
    resultados = cursor.fetchall()
    clientes = []
    for result in resultados: # Transforma o resultado em lista de dicionarios
        clientes.append({"codigo": result[0], "nome": result[1], "cnpj": result[2]})
    return(clientes)

# Retorna produtos cadastrados (Lista de dicionarios)
def find_all_produtos():
    cursor.execute("SELECT * FROM Produto;")
    resultados = cursor.fetchall()
    produtos = []
    for result in resultados:
        produtos.append({"codigo": result[0], "descricao": result[1]})
    return(produtos)

def find_sql_consulta():
    cursor.execute("SELECT ven_codigo, ven_data, cli_nome, ven_total FROM Venda JOIN Cliente ON cli_codigo = ven_cli_codigo ORDER BY ven_codigo")
    resultados = cursor.fetchall()
    consultas = []
    for result in resultados:
        consultas.append({"codigo": result[0], "data": result[1], "cliente": result[2], "total": result[3]})
    return(consultas)

# Retorna o número de vendas cadastradas
def find_numero_venda():
    cursor.execute("SELECT * FROM Venda;")
    return(len(cursor.fetchall()) + 1) # Número da ultima venda + 1

def insert_venda(dados):
    sql_venda = "INSERT INTO Venda VALUES(null, '" + dados['date'] + "', " + str(dados['valorTotal']) + ", '" + dados['cep'] + "', '" + dados['logradouro'] + "', '" + dados['numero'] + "', '" + dados['complemento'] + "', '" + dados['bairro'] + "', '" + dados['localidade'] + "', '" + dados['uf'] + "', " + str(dados['cliente']['codigo']) + ")"
    cursor.execute(sql_venda) # Efetiva venda
    return

def insert_item(item, codigo_venda):
    sql_item = "INSERT INTO Item VALUES(null, " + str(item['codItem']) + ", " + str(item['preco']) + ", " + str(item['quantidade']) + ", " + str(item['total']) + ", " + str(item['produto']['codigo']) + ", " + str(codigo_venda) +  ")"
    cursor.execute(sql_item) # Efetiva item

def db_commit():
    db.commit()

def db_rollback():
    db.rollback()


############################################################################################################################3



#######################################################################################################
#                                                                                                     #
#                                               INIT                                                  #
#                                                                                                     #
#######################################################################################################

# Inicia servidor
if __name__ == "__main__":
    app.run()