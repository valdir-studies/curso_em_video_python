# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
tempo = int(input('Em quantos anos você vai pagar a casa? ')) * 12

if valor_casa / tempo > salario * 0.3:
    print('Seu empréstimo foi negado')
else:
    print('Seu empréstimo foi aprovado')
