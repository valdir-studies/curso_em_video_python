# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro!')
else:
    print('Tudo ok!')
