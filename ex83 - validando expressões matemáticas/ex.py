# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a expressão: '))
stack = []
for char in exp:
    if char == '(': stack.append(char)
    elif char == ')':
        if len(stack) > 0: stack.pop()
        else:
            stack.append(')')
            break

print('Sua expressão está válida' if len(stack) == 0 else 'Sua expressão está inválida')
