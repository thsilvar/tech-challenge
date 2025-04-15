from flask import Flask, jsonify
from app.services import embrapa_service
import requests

app = Flask(__name__)

@app.route('/produtos')
def produtos():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    dados = embrapa_service.extrair_dados_tabela(html)
    return jsonify(dados)

@app.route('/processamento')
def processamento():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'
    response = requests.get(url)
    response.encoding = 'utf-8' 
    html = response.text

    dados = embrapa_service.extrair_dados_tabela(html)
    return jsonify(dados)

@app.route('/comercializacao')
def comercializacaoento():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    response = requests.get(url)
    response.encoding = 'utf-8' 
    html = response.text

    dados = embrapa_service.extrair_dados_tabela(html)
    return jsonify(dados)

@app.route('/importacao')
def importacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'
    response = requests.get(url)
    response.encoding = 'utf-8' 
    html = response.text

    dados = embrapa_service.extrair_exportacao_importacao(html)
    return jsonify(dados)

@app.route('/exportacao')
def exportacao():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06'
    response = requests.get(url)
    response.encoding = 'utf-8' 
    html = response.text

    dados = embrapa_service.extrair_exportacao_importacao(html)
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
