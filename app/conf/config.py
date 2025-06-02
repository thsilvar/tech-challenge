import os
from dotenv import load_dotenv
from secrets import token_urlsafe

# Carrega variáveis de ambiente se existirem
load_dotenv()

# Se já existir SECRET_KEY no ambiente, usa ela, senão gera automático
SECRET_KEY = os.getenv("SECRET_KEY", token_urlsafe(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./techdb.db")

URL_EMBRAPA = "http://vitibrasil.cnpuv.embrapa.br/index.php"


def formatUrl(parm):
    return URL_EMBRAPA + parm;
