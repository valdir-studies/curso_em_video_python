# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia():
    lista_num = []
    for i in range(0, 5):
        lista_num.append(randint(1, 100))
    return lista_num

def soma_pares(lista): 
    soma = 0
    for i in lista: 
        if i % 2 == 0: soma += i
    return soma

lista_aleatoria = sorteia()
print(lista_aleatoria)

soma_pares = soma_pares(lista_aleatoria)
print(soma_pares)
