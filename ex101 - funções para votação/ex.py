# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nasc):
    from datetime import datetime

    idade = datetime.today().year - nasc
    str_pdr = f'Com {idade} anos: '

    if idade >= 65 or 18 > idade >= 16: return str_pdr + 'VOTO OPCIONAL'
    elif idade >= 18: return str_pdr + 'VOTO OBRIGATÓRIO'
    elif idade < 18: return str_pdr + 'VOTO NEGADO'

ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))
