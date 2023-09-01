import requests

def realizar_analise_de_credito(dados_proposta):
    url_base = 'https://loan-processor.digitalsys.com.br/api/v1'
    endpoint = '/loan/'

    url = f'{url_base}{endpoint}'
    
    response = requests.post(url, json=dados_proposta)
    data = response.json()
    status = data['approved']

    if status == 'True':

        status2 = 'Aprovada'
    else:
        status2 = 'Negada'

    return status2

    

def avaliar_proposta_automaticamente(dados_proposta):
    resposta_analise = realizar_analise_de_credito(dados_proposta)
    return resposta_analise
