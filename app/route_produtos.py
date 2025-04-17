from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services import embrapa_service
import requests
from app.model.produto import Produto

produto_api = Namespace("Produtos", description="Rotas para acessar dados dos produtos da Embrapa")
produto_model = produto_api.model('Produto', {
    'tipo_produto': fields.String(description='Nome do país'),
    'categoria': fields.String(description='Quantidade de produtos'),
    'quantidade': fields.String(description='Valor em dólares')
})



@produto_api.route('/producao')
@produto_api.doc(description='Rota para obter dados de produção')
@produto_api.response(200, 'Success', [produto_model])
@produto_api.response(404, 'Not Found') 
class ProdutoList(Resource):
    def get(self):
        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text

        dados_extraidos = embrapa_service.extrair_dados_tabela(html)
        print("Teste de dados: ", dados_extraidos)
        produtos = [Produto(dado['categoria'], dado['tipo_produto'], dado['quantidade']) for dado in dados_extraidos]

        return [produto.to_dict() for produto in produtos]

@produto_api.route('/processamento')
@produto_api.doc(description='Rota para obter dados de processamento')
@produto_api.response(200, 'Success', [produto_model])
@produto_api.response(404, 'Not Found') 
class Processamento(Resource):
    def get(self):
        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'
        response = requests.get(url)
        response.encoding = 'utf-8' 
        html = response.text

        dados = embrapa_service.extrair_dados_tabela(html)
        return jsonify(dados)

@produto_api.route('/comercializacao')
@produto_api.doc(description='Rota para obter dados de comercializacao')
@produto_api.response(200, 'Success', [produto_model])
@produto_api.response(404, 'Not Found') 
class Comercializacao(Resource):
    def get(self):
        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
        response = requests.get(url)
        response.encoding = 'utf-8' 
        html = response.text

        dados = embrapa_service.extrair_dados_tabela(html)
        return jsonify(dados)
