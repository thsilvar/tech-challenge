from flask import Blueprint, request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services import embrapa_service
import requests
from app.model.importacao_exportacao import importacao_exportacao

importacao_api = Namespace("Importacao", description="Rotas dados de importação da Embrapa")
exportacao_api = Namespace("Exportacao", description="Rotas dados de exportação da Embrapa")

importacao_model_exportacao = importacao_api.model('Importacao', {
    'pais': fields.String(description='Nome do país'),
    'quantidade_kg': fields.String(description='Quantidade em kg'),
    'valor_usd': fields.String(description='Valor em dólares')
})



@importacao_api.route('/importacao')
@importacao_api.doc(description='Rota para obter dados de importação e exportações')
@importacao_api.response(200, 'Success', [importacao_model_exportacao])
@importacao_api.response(404, 'Not Found')
class Importacao(Resource):
    def get(self):
        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'
        response = requests.get(url)
        response.encoding = 'utf-8' 
        html = response.text

        dados_extraidos = embrapa_service.extrair_exportacao_importacao(html)

        dados_importacao_exportacao = [importacao_exportacao(dado['pais'], dado['quantidade_kg'], dado['valor_usd']) for dado in dados_extraidos]

        return [importacao_model_exportacao.to_dict() for importacao_model_exportacao in dados_importacao_exportacao]

@exportacao_api.route('/exportacao')
@exportacao_api.response(200, 'Success', [importacao_model_exportacao])
@exportacao_api.response(404, 'Not Found')
class Exportacao(Resource):
    def get(self):
        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06'
        response = requests.get(url)
        response.encoding = 'utf-8' 
        html = response.text

        dados_extraidos = embrapa_service.extrair_exportacao_importacao(html)
        dados_importacao_exportacao = [importacao_exportacao(dado['pais'], dado['quantidade_kg'], dado['valor_usd']) for dado in dados_extraidos]

        return [importacao_model_exportacao.to_dict() for importacao_model_exportacao in dados_importacao_exportacao]