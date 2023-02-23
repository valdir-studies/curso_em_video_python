import requests


def converter_moeda(reais):
    r = requests.get('https://economia.awesomeapi.com.br/json/last/USD', auth=('user', 'pass'))
    response = r.json()
    return reais / response.USDBRL.high
   
real = float(input('Digite o valor em reais: R$'))
print(f'Com R${real} você pode comprar U${converter_moeda(real)}')