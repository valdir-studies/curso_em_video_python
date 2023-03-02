# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_alist = ano_nasc + 18

if ano_alist < ano_atual:
    print(f'ATRASADO! Você precisava ter feito o alistamento há {ano_atual - ano_alist} ano(s)')
elif ano_alist > ano_atual:
    print(f'Ainda falta {ano_alist - ano_atual} ano(s) para seu alistamento militar')
else: 
    print('Você deve se alistar esse ano!')