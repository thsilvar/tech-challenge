from flask import Flask, Blueprint
from app.route_produtos import produto_api as routes_namespace
from app.route_imp_exp import importacao_api as importacao_ns, exportacao_api as exportacao_ns
from flask_restx import Api




def create_app():
    app = Flask(__name__)
# Registrando o blueprint com as rotas        
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    
    api = Api(
        blueprint,
        title="Tech Challenge API",
        contact="Alexandre Lima - ale_and5@hotmail.com | Thiago Ramos - | Lucas Caique de Lima - | Eduardo Barbosa - ",
        description="API para acessar dados da Embrapa",
        version="1.0",
        doc='/docs'
    )

    api.add_namespace(routes_namespace, path='/produtos')
    api.add_namespace(importacao_ns, path='/dados')
    api.add_namespace(exportacao_ns, path='/dados')

    app.register_blueprint(blueprint)
    return app

