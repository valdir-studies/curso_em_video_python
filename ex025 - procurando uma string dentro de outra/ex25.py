# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
# Adaptação -> a pessoa pode informar a string que quiser, ao invés de só "SILVA"

nome = input('Qual seu nome? ').upper().split()

def compara_str(nome, str):
    str = str.upper()
    return str in nome

print(compara_str(nome, 'joão'))
