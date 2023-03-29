# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

ano_atual = datetime.today().year

trabalhador = {}
trabalhador['nome'] = str(input('Nome: ')).capitalize()
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('CTPS: '))
trabalhador['idade'] = ano_atual - trabalhador['nascimento']

if trabalhador['ctps'] != 0: 
    trabalhador['ano_contrato'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['contribuicao'] = ano_atual - trabalhador['ano_contrato']
    trabalhador['aposentadoria'] = trabalhador['ano_contrato'] + 35
    trabalhador['idade_aposentadoria'] = trabalhador['idade'] + 35

print()
for k, v in trabalhador.items():
    print(f'{k.capitalize()} tem o valor {v}')

