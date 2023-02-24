# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Adaptação -> O usuário pode escolher qual é a taxa

def reajuste(salario, taxa):
    salario = salario + (salario * ((taxa) / 100))
    return salario

salario = float(input('Digite o salário do funcionário: '))
taxa = int(input('Digite a taxa de aumento: '))

print(f'O funcionário que recebia R${salario:.2f}, com um aumento de {taxa}% passa a receber R${reajuste(salario, taxa):.2f}')
