# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

def aumentar(preco, taxa):
    return preco + (preco * taxa / 100)

def diminuir(preco, taxa):
    return preco - (preco * taxa / 100)

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco / 2

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    
