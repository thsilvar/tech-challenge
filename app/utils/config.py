import os
from dotenv import load_dotenv
from flask import current_app
from datetime import timedelta
# Carrega .env da raiz
load_dotenv()

URL_EMBRAPA = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-inseguro')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback-jwt')
SESSION_TYPE = 'filesystem'
SESSION_FILE_DIR = '/tmp/flask_session'
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
SQLALCHEMY_DATABASE_URI = 'sqlite:///techchallenge.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SWAGGER = {
    'title': 'Tech Challenge API',
    'uiversion': 3
}

def get_embrapa_url(param: str) -> str:
    return current_app.config['URL_EMBRAPA'] + f'?{param}'