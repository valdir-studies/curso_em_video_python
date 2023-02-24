# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Me informe o comprimento de uma reta A: '))
b = int(input('Agora o B: '))
c = int(input('Finalmente o C: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo com essas 3 retas')
else:
    print('Não é possível formar um triângulo com essas retas')
