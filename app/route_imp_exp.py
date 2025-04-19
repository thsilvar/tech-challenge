from flask import request
from flask_restx import Namespace, Resource, fields
from app.services import embrapa_service
from app.model.importacao_exportacao import importacao_exportacao
from flask_jwt_extended import jwt_required
from app.utils.config import get_embrapa_url
import requests

# Namespaces
importacao_api = Namespace("Importacao", description="Rotas dados de importação da Embrapa")
exportacao_api = Namespace("Exportacao", description="Rotas dados de exportação da Embrapa")

# Modelo Swagger reutilizável
importacao_model = importacao_api.model('ImportacaoExportacao', {
    'pais': fields.String(description='Nome do país'),
    'quantidade_kg': fields.String(description='Quantidade em kg'),
    'valor_usd': fields.String(description='Valor em dólares')
})

# Rota de importação
@importacao_api.route('/importacao')
@importacao_api.doc(description='Rota para obter dados de importação')
@importacao_api.response(200, 'Success', [importacao_model])
@importacao_api.response(404, 'Not Found')
class Importacao(Resource):
    @jwt_required()
    def get(self):
        url = get_embrapa_url('opcao=opt_05')
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text

        dados_extraidos = embrapa_service.extrair_exportacao_importacao(html)
        dados = [importacao_exportacao(dado['pais'], dado['quantidade_kg'], dado['valor_usd']) for dado in dados_extraidos]
        return [d.to_dict() for d in dados]

# Rota de exportação
@exportacao_api.route('/exportacao')
@exportacao_api.response(200, 'Success', [importacao_model])
@exportacao_api.response(404, 'Not Found')
class Exportacao(Resource):
    @jwt_required()
    def get(self):
        url = get_embrapa_url('opcao=opt_06')
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.text

        dados_extraidos = embrapa_service.extrair_exportacao_importacao(html)
        dados = [importacao_exportacao(dado['pais'], dado['quantidade_kg'], dado['valor_usd']) for dado in dados_extraidos]
        return [d.to_dict() for d in dados]
