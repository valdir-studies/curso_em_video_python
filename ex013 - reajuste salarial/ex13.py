def reajuste(salario, taxa):
    salario = salario + (salario * ((taxa) / 100))
    return salario

salario = float(input('Digite o salário do funcionário: '))
taxa = int(input('Digite a taxa de aumento: '))

print(f'O funcionário que recebia R${salario:.2f}, com um aumento de {taxa}% passa a receber R${reajuste(salario, taxa):.2f}')
