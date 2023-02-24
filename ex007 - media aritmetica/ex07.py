# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# Adaptação -> O programa permite que várias notas sejam lançadas, não só 2
def media(*args):
    soma = float()
    for n in args:
        soma += n
    
    return soma / len(args)

print(media(10, 20)) # 15.0

