from fastapi import APIRouter, status, Depends
from typing import List
import requests
from app.model.produto import Produto
from app.services import embrapa_service
from app.auth.auth_bearer import JWTBearer
from app.config import formatUrl

router = APIRouter()


@router.get('/producao', response_model=List[Produto], dependencies=[Depends(JWTBearer())], summary="Dados de produção da Embrapa", 
    responses={
    status.HTTP_200_OK: {"description": "Dados de produção obtidos com sucesso."},
    status.HTTP_404_NOT_FOUND: {"description": "Nenhum dado encontrado."},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Erro interno no servidor."}
})
async def get():
     url = formatUrl('?opcao=opt_02')
     response = requests.get(url)
     response.encoding = 'utf-8'
     html = response.text

     dados_extraidos = embrapa_service.extrair_dados_tabela(html) 

     return [Produto(**dado) for dado in dados_extraidos]
        
@router.get('/processamento', response_model=List[Produto], dependencies=[Depends(JWTBearer())], summary="Dados de processamento da Embrapa",
            responses={
            status.HTTP_200_OK: {"description": "Dados de produção obtidos com sucesso."},
            status.HTTP_404_NOT_FOUND: {"description": "Nenhum dado encontrado."},
            status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Erro interno no servidor."}})
async def get():
    url = formatUrl('?opcao=opt_03')
    response = requests.get(url)
    response.encoding = 'utf-8' 
    html = response.text

    dados_extraidos = embrapa_service.extrair_dados_tabela(html)

    return [Produto(**dado) for dado in dados_extraidos]

@router.get('/comercializacao', response_model=List[Produto], dependencies=[Depends(JWTBearer())], summary="Dados de comercialização da Embrapa",
            responses={
            status.HTTP_200_OK: {"description": "Dados de produção obtidos com sucesso."},
            status.HTTP_404_NOT_FOUND: {"description": "Nenhum dado encontrado."},
            status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Erro interno no servidor."}})
async def get():
    url = formatUrl('?opcao=opt_04')
    response = requests.get(url)
    response.encoding = 'utf-8' 
    html = response.text
    
    dados_extraidos = embrapa_service.extrair_dados_tabela(html)      

    return [Produto(**dado) for dado in dados_extraidos]
