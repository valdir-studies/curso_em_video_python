# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:  
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

num = []

while True:
    n = int(input('Digite um número: '))
    num.append(n)
    opt = str(input('Quer continuar? [S/N] '))
    if opt in 'Nn':
        break
    elif opt not in 'Ss':
        opt = str(input('Opção inválida! Digite [S] pra sim e [N] pra não, abestado '))

num.sort(reverse=True)
print(f'A) Você digitou {len(num)} elementos')
print(f'Os valores em ordem decrescente são {num}')
print('O valor 5 faz parte da lista!' if num.count(5) > 0 else 'O valor 5 não faz parte da lista!')
