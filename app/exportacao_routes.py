from fastapi import APIRouter, status, Depends
from typing import List
import requests
from app.model.dados_comerciais import DadosComerciais
from app.services import embrapa_service
from app.auth.auth_bearer import JWTBearer
from app.config import formatUrl

router = APIRouter()

@router.get("/exportacao", response_model=List[DadosComerciais], dependencies=[Depends(JWTBearer())], summary="Dados de exportação da Embrapa", 
    responses={
    status.HTTP_200_OK: {"description": "Dados de produção obtidos com sucesso."},
    status.HTTP_404_NOT_FOUND: {"description": "Nenhum dado encontrado."},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Erro interno no servidor."}
})
async def get_exportacao():
    url = formatUrl('?opcao=opt_06')
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    dados_extraidos = embrapa_service.extrair_exportacao_importacao(html)
    return [DadosComerciais(**dado) for dado in dados_extraidos]
