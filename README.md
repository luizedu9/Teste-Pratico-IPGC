# teste-backend-ipgc

Teste para Backend Developer - IPGC

# Requerimentos:

Python 3.6.8

MySQL

Pip: 
sudo apt-get install python3-pip

Virtual Enviroment:
sudo pip install virtualenv

Criação da Virtual Enviroment:
python3 -m venv venv

Abrir venv:
source venv/bin/activate

Importar dependências para venv:
pip install -r requirements.txt

# Executação:

Iniciar servidor MySQL

Inserir usuário e senha do MySQL em bd_request.py - init

Abrir venv:
source venv/bin/activate

Executar o Backend:
python3 backend.py

# Acesso API:

##Acesso ao servidor:
	http://127.0.0.1:5000/

##Cliente:  
	http://127.0.0.1:5000/cliente

	POST: Insere cliente. Json com [nome, email e telefone].
	curl -X POST http://127.0.0.1:5000/cliente -H 'Content-Type: application/json' -d '{"nome": "Adalberto", "email": "adalberto.andrade@gmail.com", "telefone": "3799977-8877"}'

	GET: Retorna todos os clientes cadastrados.
	curl -X GET http://127.0.0.1:5000/cliente

	GET /<id>: Retorna o cliente cadastrado.
	curl -X GET http://127.0.0.1:5000/cliente/1

	DELETE /<id>: Deleta o cliente alvo.
	curl -X DELETE http://127.0.0.1:5000/cliente/1

	PUT /<id>: Atualiza o cliente alvo. Json com [Cliente]
	curl -X PUT http://127.0.0.1:5000/cliente/1 -H 'Content-Type: application/json' -d '{"codigo": 1, "nome": "Adalberto Andrade", "email": "adalberto.andrade@gmail.com", "telefone": "3799977-8877"}'

##Produto:  
	http://127.0.0.1:5000/produto

	POST: Insere produto. Json com [nome, preco e descricao].
	curl -X POST http://127.0.0.1:5000/produto -H 'Content-Type: application/json' -d '{"nome": "Guarda-chuva", "preco": 49.99, "descricao": "Tamanho familia"}'

	GET: Retorna todos os produtos cadastrados.
	curl -X GET http://127.0.0.1:5000/produto

	GET /<id>: Retorna o produto cadastrado.
	curl -X GET http://127.0.0.1:5000/produto/1

	DELETE /<id>: Deleta o produto alvo.
	curl -X DELETE http://127.0.0.1:5000/produto/1

	PUT /<id>: Atualiza o produto alvo. Json com [Produto]
	curl -X PUT http://127.0.0.1:5000/produto/1 -H 'Content-Type: application/json' -d {"codigo": 1, "nome": "Guarda-chuva", "preco": 39.99, "descricao": "Tamanho pequeno"}'

##Venda:
	http://127.0.0.1:5000/venda

	POST: Insere venda. Json com [codigo_cliente, lista[codigo_produto]].
	curl -X POST http://127.0.0.1:5000/venda -H 'Content-Type: application/json' -d '{"codigo_cliente": 1, "codigo_produtos": [1, 2, 3]}'

	GET: Retorna todas as vendas cadastradas.
	curl -X GET http://127.0.0.1:5000/venda

	GET /<id>: Retorna a venda cadastrada.
	curl -X GET http://127.0.0.1:5000/venda/1

	GET /<data(dd-mm-aaaa)>: Retorna as vendas cadastradas na data especificada.
	curl -X GET http://127.0.0.1:5000/venda/01-01-2020

	DELETE /<id>: Deleta a venda alvo.
	curl -X DELETE http://127.0.0.1:5000/venda/1

	PUT /<id>: Atualiza a venda alvo. Json com [Venda]
	curl -X PUT http://127.0.0.1:5000/venda/1 -H 'Content-Type: application/json' -d '{"codigo": 1, "data": "15-02-2020", "codigo_cliente": 1, "codigo_produtos": [1, 2, 4]}'