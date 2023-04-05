# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: Informa se o processo do cálcula deve ser mostrado ou não
    :return: O resultado do fatorial do número num
    """
    res = 1
    while num >= 1:
        if show:
            print(num, end='')
            print(f' x ' if num > 1 else ' = ', end='')
        res *= num
        num -= 1
    return res

print(fatorial(5, True))
print(fatorial(7))
