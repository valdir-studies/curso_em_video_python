# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Adaptação -> O valor do dólar muda automaticamente a cada 30s pela api

import requests

def converter_moeda(reais):
    r = requests.get('https://economia.awesomeapi.com.br/json/last/USD', auth=('user', 'pass'))
    response = r.json()
    return reais / float(response['USDBRL']['high'])
   
real = float(input('Digite o valor em reais: R$'))
print(f'Com R${real:.2f} você pode comprar U${converter_moeda(real):.2f}')
