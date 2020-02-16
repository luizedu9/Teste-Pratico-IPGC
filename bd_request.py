# -*- coding: utf-8 -*-

# Teste Backend IPGC
# bd_request.py
# Luiz Eduardo Pereira

#######################################################################################################
#                                                                                                     #
#                                                 INIT                                                #
#                                                                                                     #
#######################################################################################################

import pymysql
from cliente import Cliente
from produto import Produto
from venda import Venda

# Configuração PyMySQL

# Inserir usuario e senha do mysql ####################################################################
#db = pymysql.connect("localhost", "USER", "PASSWORD", "teste-backend-ipgc-master") 
#######################################################################################################

db = pymysql.connect("localhost", "admin", "admin7576", "teste-backend-ipgc")
cursor = db.cursor()

#######################################################################################################
#                                                                                                     #
#                                               BD                                                    #
#                                                                                                     #
#######################################################################################################

def db_commit():
    db.commit()

def db_rollback():
    db.rollback()

# Cliente

# Insere cliente
def insert_cliente(cliente):
    cursor.execute("INSERT INTO Cliente VALUES(null, '" + cliente.nome + "', '" + cliente.email + "', '" + cliente.telefone + "')")

# Retorna cliente.
def find_cliente(codigo):
    cursor.execute("SELECT * FROM Cliente WHERE cli_codigo = " + codigo + ";")
    resultado = cursor.fetchall()
    return(Cliente(resultado[0][0], resultado[0][1], resultado[0][2], resultado[0][3]))

# Retorna clientes cadastrados. Tipo do retorno: list of cliente.
def find_all_clientes():
    cursor.execute("SELECT * FROM Cliente;")
    resultados = cursor.fetchall()
    clientes = []
    for result in resultados: # Transforma o resultado em lista de cliente
        clientes.append(Cliente(result[0], result[1], result[2], result[3]))
    return(clientes)

# Remove cliente
def delete_cliente(codigo):
    cursor.execute("DELETE FROM Cliente WHERE cli_codigo = " + str(codigo))

# Atualiza cliente
def update_cliente(codigo, cliente):
    cursor.execute("UPDATE Cliente SET cli_nome = '" + cliente.nome + "', cli_email = '" + cliente.email + "', cli_telefone = '" + cliente.telefone +"' WHERE cli_codigo = " + str(codigo))

# Produto

# Insere produto
def insert_produto(produto):
    cursor.execute("INSERT INTO Produto VALUES(null, '" + produto.nome + "', '" + str(produto.preco) + "', '" + produto.descricao + "')")

# Retorna produto.
def find_produto(codigo):
    cursor.execute("SELECT * FROM Produto WHERE pro_codigo = " + codigo + ";")
    resultado = cursor.fetchall()
    return(Produto(resultado[0][0], resultado[0][1], float(resultado[0][2]), resultado[0][3]))

# Retorna produtos cadastrados. Tipo do retorno: list of produto.
def find_all_produtos():
    cursor.execute("SELECT * FROM Produto;")
    resultados = cursor.fetchall()
    produtos = []
    for result in resultados: # Transforma o resultado em lista de produto
        produtos.append(Produto(result[0], result[1], float(result[2]), result[3]))
    return(produtos)

# Remove produto
def delete_produto(codigo):
    cursor.execute("DELETE FROM Produto WHERE pro_codigo = " + str(codigo))

# Atualiza produto
def update_produto(codigo, produto):
    cursor.execute("UPDATE Produto SET pro_nome = '" + produto.nome + "', pro_preco = '" + str(produto.preco) + "', pro_descricao = '" + produto.descricao +"' WHERE pro_codigo = " + str(codigo))

# Venda

# Insere produto
def insert_venda(venda):
    cursor.execute("INSERT INTO Venda VALUES(null, %s , '" + str(venda.cliente) + "')", (venda.data))
    codigo = cursor.lastrowid
    for produto in venda.produtos:
        cursor.execute("INSERT INTO Produto_Venda VALUES(" + str(produto) + ", " + str(codigo) + ")")

# Retorna venda.
def find_venda(codigo):
    cursor.execute("SELECT * FROM Venda WHERE ven_codigo = " + codigo)
    resultado_venda = cursor.fetchall()
    cursor.execute("SELECT pv_pro_codigo FROM Produto_Venda WHERE pv_ven_codigo = " + codigo)
    resultado_produtos = cursor.fetchall()
    produtos = []
    for produto in resultado_produtos:
        produtos.append(produto[0])
    return(Venda(resultado_venda[0][0], resultado_venda[0][1], resultado_venda[0][2], produtos))

def find_venda_date(date):
    cursor.execute("SELECT * FROM Venda WHERE ven_data = '" + date + "'")
    resultados_venda = cursor.fetchall()
    vendas = []
    for venda in resultados_venda:
        cursor.execute("SELECT pv_pro_codigo FROM Produto_Venda WHERE pv_ven_codigo = " + str(venda[0]))
        resultado_produtos = cursor.fetchall()
        produtos = []
        for produto in resultado_produtos:
            produtos.append(produto[0])
        vendas.append(Venda(venda[0], venda[1], venda[2], produtos))
    return(vendas)

# Retorna vendas cadastradas. Tipo do retorno: list of vendas.
def find_all_vendas():
    cursor.execute("SELECT * FROM Venda")
    resultados_venda = cursor.fetchall()
    vendas = []
    for venda in resultados_venda:
        cursor.execute("SELECT pv_pro_codigo FROM Produto_Venda WHERE pv_ven_codigo = " + str(venda[0]))
        resultado_produtos = cursor.fetchall()
        produtos = []
        for produto in resultado_produtos:
            produtos.append(produto[0])
        vendas.append(Venda(venda[0], venda[1], venda[2], produtos))
    return(vendas)

# Remove venda
def delete_venda(codigo):
    cursor.execute("DELETE FROM Produto_Venda WHERE pv_ven_codigo = " + str(codigo))
    cursor.execute("DELETE FROM Venda WHERE ven_codigo = " + str(codigo))

# Atualiza venda
def update_venda(codigo, venda):
    cursor.execute("DELETE FROM Produto_Venda WHERE pv_ven_codigo = " + str(codigo)) # Deleta produtos para inserir a nova modificação.
    cursor.execute("UPDATE Venda SET ven_data = '" + venda.data + "', ven_cli_codigo = '" + str(venda.cliente) + "' WHERE ven_codigo = " + str(codigo))
    for produto in venda.produtos:
        print(produto)
        cursor.execute("INSERT INTO Produto_Venda VALUES(" + str(produto) + ", " + str(codigo) + ")")