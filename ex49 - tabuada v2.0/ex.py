#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#nota: ex09 duplicado, pq eu já tinha feito assim

def tabuada(n):
    for i in range(11):
        print(f'{n} x {i} = {i*n}')

tabuada(9)