import requests


def converter_moeda(reais):
    r = requests.get('https://economia.awesomeapi.com.br/json/last/USD', auth=('user', 'pass'))
    response = r.json()
    return reais / response.USDBRL.high
   
    
converter_moeda(10)