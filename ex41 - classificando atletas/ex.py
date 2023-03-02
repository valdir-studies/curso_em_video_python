# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_nasc

if idade > 25:
    classificacao = 'MASTER'
elif 25 > idade > 19:
    classificacao = 'SÊNIOR'
elif 19 > idade > 14:
    classificacao = 'JÚNIOR'
elif 14 > idade > 9:
    classificacao = 'INFANTIL'
elif 9 > idade > 0:
    classificacao = 'MIRIM'
else: 
    classificacao = 'Oxe, tu nem nasceu ainda'

print(f'Você tem {idade} ano(s) e sua classificação é: {classificacao}')