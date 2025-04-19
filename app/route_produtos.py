from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
import requests

from app.services import embrapa_service
from app.model.produto import Produto
from app.utils.config import get_embrapa_url

produto_api = Namespace("Produtos", description="Rotas para acessar dados dos produtos da Embrapa")

# Modelo Swagger para documentação
producao_model = produto_api.model('Produto', {
    'tipo_produto': fields.String(description='Tipo do produto', example='Branco'),
    'categoria': fields.String(description='Categoria de produtos', example='Vinho fino de mesa'),
    'quantidade': fields.String(description='Quantidade do produto', example='1000')
})


@produto_api.route('/producao')
class ProdutoList(Resource):
    @produto_api.doc(description='Rota para obter dados de produção')
    @produto_api.marshal_with(producao_model, as_list=True)
    @produto_api.response(404, 'Not Found')
    @jwt_required()
    def get(self):
        url = get_embrapa_url('opcao=opt_02')
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text

        dados_extraidos = embrapa_service.extrair_dados_tabela(html)
        produtos = [Produto(dado['categoria'], dado['tipo_produto'], dado['quantidade']) for dado in dados_extraidos]
        return [produto.to_dict() for produto in produtos]


@produto_api.route('/processamento')
class Processamento(Resource):
    @produto_api.doc(description='Rota para obter dados de processamento')
    @produto_api.marshal_with(producao_model, as_list=True)
    @produto_api.response(404, 'Not Found')
    @jwt_required()
    def get(self):
        url = get_embrapa_url('opcao=opt_03')
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text

        dados_extraidos = embrapa_service.extrair_dados_tabela(html)
        produtos = [Produto(dado['categoria'], dado['tipo_produto'], dado['quantidade']) for dado in dados_extraidos]
        return [produto.to_dict() for produto in produtos]


@produto_api.route('/comercializacao')
class Comercializacao(Resource):
    @produto_api.doc(description='Rota para obter dados de comercialização')
    @produto_api.marshal_with(producao_model, as_list=True)
    @produto_api.response(404, 'Not Found')
    @jwt_required()
    def get(self):
        url = get_embrapa_url('opcao=opt_04')
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text

        dados_extraidos = embrapa_service.extrair_dados_tabela(html)
        produtos = [Produto(dado['categoria'], dado['tipo_produto'], dado['quantidade']) for dado in dados_extraidos]
        return [produto.to_dict() for produto in produtos]
