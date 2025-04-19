from flask import Flask, Blueprint
from flask_restx import Api
from flasgger import Swagger
from app.utils.extensions import db, jwt, limiter
from flask_session import Session


from app.route_produtos import produto_api as routes_namespace
from app.route_imp_exp import importacao_api as importacao_ns, exportacao_api as exportacao_ns
from app.route_auth import auth_api as auth_namespace


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.utils.config')

    Session(app)

    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    Swagger(app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api = Api(
        blueprint,
        title=app.config['SWAGGER']['title'],
        version="1.0",
        description="API para acessar dados da Embrapa",
        doc='/docs',
        contact="Alexandre Lima - ale_and5@hotmail.com | Thiago Ramos - thsilvar@gmail.com | Lucas Caique de Lima - | Eduardo Barbosa - "
    )

    api.add_namespace(routes_namespace, path='/produtos')
    api.add_namespace(importacao_ns, path='/dados')
    api.add_namespace(exportacao_ns, path='/dados')
    api.add_namespace(auth_namespace, path='/auth')

    app.register_blueprint(blueprint)

    with app.app_context():
        db.create_all()
    
    return app
