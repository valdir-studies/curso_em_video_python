# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

cont_maior = 0
cont_menor = 0
for i in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    if date.today().year - ano_nasc >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'Das pessoas informadas, {cont_maior} são maiores de idade e {cont_menor} são menores de idade')
