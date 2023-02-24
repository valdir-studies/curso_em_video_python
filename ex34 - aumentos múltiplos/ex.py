# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? '))

if salario > 1250:
    taxa = 10
else: 
    taxa = 15

salario = salario + (salario/100 * taxa)

print(f'O salário do funcionário com o novo aumento de {taxa}% passa a ser R${salario:.2f}')
